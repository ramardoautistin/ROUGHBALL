"""
ROUGHBALL: AI Opponent
Smart bot logic for card selection
"""

import random
import time
from .cards import get_fresh_deck_dicts
from .teams import SYMBOLS


def smart_bot_logic(rank_val, bot_is_driving, bot_deck):
    """
    AI card selection based on situation
    
    YOUR ORIGINAL LOGIC PRESERVED:
    - Refill deck if needed
    - Draw full hand
    - Group cards by suit
    - Pick best suit for situation
    - Recycle unused cards
    
    Args:
        rank_val: Number of cards to play (1-5)
        bot_is_driving: Bool, is bot currently driving
        bot_deck: List of card dicts
    
    Returns:
        Tuple of (total_value, best_suit, max_card, display_string, special_move)
    """
    
    # 1. Safety Net - Refill if empty
    if len(bot_deck) < rank_val:
        bot_deck[:] = get_fresh_deck_dicts()
    
    # 2. Draw Hand
    hand = [bot_deck.pop() for _ in range(rank_val)]
    
    # 3. Analyze Groups
    groups = {"C": [], "H": [], "S": [], "D": [], "JKR": []}
    hand_vals = []
    
    for c in hand:
        groups[c['suit']].append(c['val'])
        hand_vals.append(c['val'])
    
    # 4. Pick Best Suit Based on Situation
    if bot_is_driving:
        priority = ["D", "H"]  # Offense first (Diamonds, Hearts)
        # Fallback if no offensive cards
        if not any(groups[s] for s in priority):
            priority = ["C", "S"]
    else:
        priority = ["C", "S"]  # Defense first (Clubs, Spades)
        # Fallback if no defensive cards
        if not any(groups[s] for s in priority):
            priority = ["D", "H"]
    
    best_suit = max(priority, key=lambda s: sum(groups[s]) if groups[s] else 0)
    
    # Fallback for completely empty hands (edge case)
    if not groups[best_suit] and 15 not in hand_vals:
        best_suit = "C"  # Default to Clubs
    
    # 5. Identify Special Moves (JKR detection)
    special = None
    has_jkr = 15 in hand_vals
    
    if has_jkr:
        if bot_is_driving:
            if groups["D"]:
                special = "JUKE"
            elif groups["H"]:
                special = "STIFF_ARM"
        else:
            if groups["S"]:
                special = "STRIP"  # This is PUNT in the spec
            elif groups["C"]:
                special = "SCRUM"  # This is RUCK in the spec
    
    # 6. Recycle Unused Cards
    # Keep cards that match best suit OR are Jokers
    # Everything else goes back to bottom of deck
    unused_cards = [c for c in hand if c['suit'] != best_suit and c['val'] != 15]
    for card in unused_cards:
        bot_deck.insert(0, card)  # Bottom of deck
    
    # 7. Format Display
    display = "".join([f"[{SYMBOLS.get(best_suit, '?')} {v}] " for v in groups[best_suit]])
    if has_jkr:
        display += "[JKR] "
    
    # 8. Return Analysis
    total_val = sum(groups[best_suit])
    max_card = max(groups[best_suit] + [0])
    
    return total_val, best_suit, max_card, display.strip(), special


def get_bot_hand_as_dicts(rank_val, best_suit, groups):
    """
    Convert bot's selected cards to list of dicts for resolver
    
    Args:
        rank_val: Number of cards being played
        best_suit: The suit bot chose
        groups: Dict of card values by suit
    
    Returns:
        List of card dicts
    """
    
    hand = []
    
    # Add all cards of best suit
    for val in groups[best_suit]:
        hand.append({"suit": best_suit, "val": val})
    
    # Add JKR if present
    for val in groups["JKR"]:
        hand.append({"suit": "JKR", "val": 15})
    
    # Pad with empty cards if needed (shouldn't happen)
    while len(hand) < rank_val:
        hand.append({"suit": "C", "val": 2})
    
    return hand[:rank_val]
