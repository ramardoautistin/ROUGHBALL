"""
ROUGHBALL: Display Module
All UI/console display functions

FIXED:
- clear() no longer uses os.system(). That call spawns a subprocess
  which BLOCKS on Termux, Neovim embedded terminals, and certain CMD
  configurations — this was the freeze you were hitting after every
  card input. The loop would resolve correctly, iterate back to the
  top, call clear(), and hang before the next frame ever rendered.
  
  Now uses direct stdout writes:
    Windows CMD/PowerShell: sends the Win32 console API sequence
    Everything else (bash, zsh, Termux, Neovim :terminal, etc):
      writes ANSI escape codes directly to stdout — no subprocess,
      no shell spawn, no blocking.

QoL v2:
- check_escape() for ESC key backdoor exit
"""

import sys
import os


class EscapeToMenu(Exception):
    """Custom exception for ESC key backdoor exit"""
    pass


def clear():
    """
    Clear the console screen — portable across ALL terminals.
    
    Windows: uses the Win32 STD_OUTPUT_HANDLE + SetConsoleTextAttribute
             to actually clear the buffer (not just scroll).
             Falls back to ANSI if the Win32 call fails (e.g. Windows
             Terminal, Mintty, or Git Bash — they all support ANSI).
    Unix/Mac/Termux/Neovim: writes ANSI escape directly to stdout.
             No subprocess. No os.system. No shell.
    """
    if os.name == 'nt':
        # Try Win32 API first (works in classic CMD and conhost)
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            # Enable virtual terminal processing (makes ANSI work in CMD too)
            STD_OUTPUT_HANDLE = -11
            ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
            handle = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
            mode = ctypes.c_ulong()
            kernel32.GetConsoleMode(handle, ctypes.byref(mode))
            kernel32.SetConsoleMode(handle, mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
        except Exception:
            pass  # Fall through to ANSI write below
    
    # Universal ANSI clear: works on bash, zsh, Termux, Neovim :terminal,
    # Windows Terminal, PowerShell, Git Bash, mintty, and CMD with VT enabled above.
    # \033[H  = cursor to home (row 1, col 1)
    # \033[2J = erase entire screen
    sys.stdout.write('\033[H\033[2J')
    sys.stdout.flush()


def print_matrix(u_team, b_team, u_score, b_score, league_name, u_driving, era_name, u_name, b_name):
    """
    Print the 8x8 field matrix with formations.
    Original ASCII mat preserved exactly.
    """
    
    board = {
        "A4": "RB", "B5": "QB", "C1": "TE", "C8": "WR",
        "D3": "DE", "D4": "OT", "D5": "DT", "D6": "OG",
        "E3": "OG", "E4": "DT", "E5": "OT", "E6": "DE",
        "G4": "SG", "H1": "CB", "H5": "SG", "H8": "LB"
    }
    
    print(f"\nSCR: [{u_name}] {u_score} | [{b_name}] {b_score} | {league_name}")
    if era_name:
        print(f"ERA: {era_name} | SELECTED TEAM: {u_name}")
    
    print("\n      1   2   3   4   5   6   7   8")
    print(f"   |----------------------------------| ({b_name.upper()} Endzone)")
    
    for r in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        line = f"{r}  | "
        
        for c in range(1, 9):
            position = board.get(f'{r}{c}', '.')
            line += f" {position.ljust(2)} "
        
        suffix = ""
        if r == 'D':
            suffix = f" < {u_name.upper()} {'DRIVING' if u_driving else 'HOLDING'} ({u_team['loc']})"
        elif r == 'E':
            suffix = f" < {b_name.upper()} {'DRIVING' if not u_driving else 'HOLDING'} ({b_team['loc']})"
        
        print(line + " |" + suffix)
        
        if r == 'D':
            print(" xxxxxxxxxxxxxxxxxxxOxxxxxxxxxxxxxxxxxxx << NEUTRAL SNAP POINT >>")
    
    print(f"   |----------------------------------| ({u_name.upper()} Endzone)")


def print_header(title, width=60):
    """Print a section header"""
    print("\n" + "=" * width)
    print(f"   {title}")
    print("=" * width)


def print_playbook_status(team):
    """Print team's playbook slots"""
    playbook = team.get('playbook', ["[EMPTY]"] * 5)
    print(f"   [PLAYBOOK SLOTS]: {playbook}")


def check_escape(user_input):
    """
    Check if user pressed ESC key (secret backdoor exit).
    
    ESC key codes:
    - '\x1b' (Unix/Mac)
    - chr(27) (cross-platform)
    
    Raises EscapeToMenu exception if detected.
    """
    if user_input in ('\x1b', chr(27), 'ESC', 'esc'):
        raise EscapeToMenu("ESC pressed - returning to main menu")
