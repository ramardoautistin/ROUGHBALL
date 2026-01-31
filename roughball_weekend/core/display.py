"""
ROUGHBALL: Display Module
All UI/console display functions
"""

import os
import time


def clear():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_matrix(u_team, b_team, u_score, b_score, league_name, u_driving, era_name, u_name, b_name):
    """
    Print the 8x8 field matrix with formations
    
    YOUR ORIGINAL ASCII MAT RESTORED
    """
    
    # The board positions (neutral formation)
    board = {
        "A4": "RB", "B5": "QB", "C1": "TE", "C8": "WR",
        "D3": "DE", "D4": "OT", "D5": "DT", "D6": "OG",
        "E3": "OG", "E4": "DT", "E5": "OT", "E6": "DE",
        "G4": "SG", "H1": "CB", "H5": "SG", "H8": "LB"
    }
    
    # Header with score and league
    print(f"\nSCR: [{u_name}] {u_score} | [{b_name}] {b_score} | {league_name}")
    if era_name:
        print(f"ERA: {era_name} | SELECTED TEAM: {u_name}")
    
    # Grid
    print("\n      1   2   3   4   5   6   7   8")
    print(f"   |----------------------------------| ({b_name.upper()} Endzone)")
    
    for r in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        line = f"{r}  | "
        
        for c in range(1, 9):
            position = board.get(f'{r}{c}', '.')
            line += f" {position.ljust(2)} "
        
        # Side annotations showing possession
        suffix = ""
        if r == 'D':
            suffix = f" < {u_name.upper()} {'DRIVING' if u_driving else 'HOLDING'} ({u_team['loc']})"
        elif r == 'E':
            suffix = f" < {b_name.upper()} {'DRIVING' if not u_driving else 'HOLDING'} ({b_team['loc']})"
        
        print(line + " |" + suffix)
        
        # Neutral snap point line
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
