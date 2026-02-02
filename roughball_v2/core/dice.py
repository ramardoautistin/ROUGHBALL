"""
ROUGHBALL: Dice Module
Handles D66, D4, and D6 rolling mechanics
"""

import random


def roll_d66():
    """
    Roll 2d6 for clash resolution
    
    Returns:
        Tuple of (die1, die2)
    """
    return (random.randint(1, 6), random.randint(1, 6))


def count_hits(dice_roll, success_window):
    """
    Count how many dice are within success window
    
    Args:
        dice_roll: Tuple of (die1, die2)
        success_window: List of success values (e.g., [1, 2, 3] for D3)
    
    Returns:
        Number of hits (0-2)
    """
    return sum(1 for die in dice_roll if die in success_window)


def roll_d4():
    """
    Roll d4 for complications
    
    Returns:
        Int from 1-4
    """
    return random.randint(1, 4)


def roll_d6():
    """
    Roll single d6
    
    Returns:
        Int from 1-6
    """
    return random.randint(1, 6)


def get_success_window(division_rank):
    """
    Get success window for division rank
    
    Args:
        division_rank: 1-5 (1=Rookies, 5=Legends)
    
    Returns:
        List of success values
    """
    windows = {
        1: [1],              # D5: Unranked Rookies
        2: [1, 2],           # D4: Backyard Amateurs
        3: [1, 2, 3],        # D3: High School Pros
        4: [1, 2, 3, 4],     # D2: College Superstars
        5: [1, 2, 3, 4, 5]   # D1: National Legends
    }
    
    return windows.get(division_rank, [1])
