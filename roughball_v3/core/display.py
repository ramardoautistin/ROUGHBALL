"""
ROUGHBALL: Display Module v10.3.1 FINAL
All UI/console display functions
"""

import sys
import os


class EscapeToMenu(Exception):
    """Custom exception for ESC key backdoor exit"""
    pass


def clear():
    """Clear the console screen - portable across ALL terminals"""
    if os.name == 'nt':
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            STD_OUTPUT_HANDLE = -11
            ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
            handle = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
            mode = ctypes.c_ulong()
            kernel32.GetConsoleMode(handle, ctypes.byref(mode))
            kernel32.SetConsoleMode(handle, mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
        except Exception:
            pass
    
    sys.stdout.write('\033[H\033[2J')
    sys.stdout.flush()


def print_matrix(u_team, b_team, u_score, b_score, league_name, u_driving, era_name, u_name, b_name, possession_state="driving"):
    """
    Print 8x8 field matrix with formations.
    
    NEUTRAL: D,C,B,A / A,B,C,D (mirrored) - 8 players each side
    STANDARD: A-H (normal) - asymmetric offense/defense
    """
    
    # NEUTRAL FORMATION - From DOC
    # Each team has: WB(1), RG(5), TB(8), QG(4), OG(3), OT(5), DT(4), DE(6)
    # Top team: rows D,C,B,A (reversed)
    # Bottom team: rows A,B,C,D (normal) with SAME positions (mirrored)
    neutral_positions = {
        'D': {1: 'WB', 5: 'RG', 8: 'TB'},  # Row D
        'C': {4: 'QG'},                     # Row C
        'B': {3: 'OG', 5: 'OT'},            # Row B  
        'A': {4: 'DT', 6: 'DE'}             # Row A
    }
    
    # STANDARD FORMATION
    standard_board = {
        "A4": "RB", "B5": "QB", "C1": "TE", "C8": "WR",
        "D3": "DE", "D4": "OT", "D5": "DT", "D6": "OG",
        "E3": "OG", "E4": "DT", "E5": "OT", "E6": "DE",
        "G4": "SG", "H1": "CB", "H5": "SG", "H8": "LB"
    }
    
    # Determine row order and formation type
    if possession_state == "neutral":
        formation_desc = "NEUTRAL FORMATION (Mirrored)"
        row_order = ['D', 'C', 'B', 'A', 'A', 'B', 'C', 'D']
        use_neutral = True
    else:
        if u_driving:
            formation_desc = f"{u_name} DRIVING"
        else:
            formation_desc = f"{b_name} DRIVING"
        row_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        use_neutral = False
    
    print(f"\nSCR: [{u_name}] {u_score} | [{b_name}] {b_score} | {league_name}")
    if era_name:
        print(f"ERA: {era_name} | FORMATION: {formation_desc}")
    
    print("\n      1   2   3   4   5   6   7   8")
    print(f"   |----------------------------------| ({b_name.upper()} Endzone)")
    
    for idx, r in enumerate(row_order):
        line = f"{r}  | "
        
        # Build row content
        for c in range(1, 9):
            if use_neutral:
                # Neutral formation - use neutral_positions
                position = neutral_positions.get(r, {}).get(c, '.')
            else:
                # Standard formation - use standard_board
                position = standard_board.get(f'{r}{c}', '.')
            line += f" {position.ljust(2)} "
        
        # Add team labels
        suffix = ""
        if possession_state == "neutral":
            if idx == 3:  # First A (top team)
                suffix = f" < {u_name.upper()} IN NEUTRAL POSITION ({u_team['loc']})"
            elif idx == 4:  # Second A (bottom team)
                suffix = f" < {b_name.upper()} IN NEUTRAL POSITION ({b_team['loc']})"
        else:
            if r == 'D':
                suffix = f" < {u_name.upper()} {'DRIVING' if u_driving else 'HOLDING'} ({u_team['loc']})"
            elif r == 'E':
                suffix = f" < {b_name.upper()} {'DRIVING' if not u_driving else 'HOLDING'} ({b_team['loc']})"
        
        print(line + " |" + suffix)
        
        # Print snap line
        if possession_state == "neutral" and idx == 3:
            print(" xxxxxxxxxxxxxxxxxxxOxxxxxxxxxxxxxxxxxxx << NEUTRAL SNAP POINT >>")
        elif possession_state != "neutral" and r == 'D':
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
    """Check if user pressed ESC"""
    if not user_input:
        return
    if user_input.strip().upper() in ('ESC', '\x1b', chr(27)):
        raise EscapeToMenu("ESC pressed - returning to main menu")


def safe_input(prompt):
    """Wrapper for input() with ESC checking"""
    try:
        user_input = input(prompt)
        check_escape(user_input)
        return user_input
    except KeyboardInterrupt:
        raise EscapeToMenu("Ctrl+C pressed - returning to main menu")
