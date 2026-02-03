"""
ROUGHBALL: AI Opponent
Smart bot logic for card selection

v10.2 FIXES:
- Bot deck properly manages 2 jokers (standard 54-card deck)
- Timeout also triggers bot deck reshuffle
- Neutral formation awareness (mixed suits allowed)
"""

import random
import time
from .cards import get_fresh_deck_dicts
from .teams import SYMBOLS


def smart_bot_logic(rank_val, bot_is_driving, bot_deck, possession_state="neutral", discard_pile=None):
    """
    AI card selection based on situation
    
    Args:
        rank_val: Number of cards to play (1-5)
        bot_is_driving: Bool, is bot currently driving
        bot_deck: List of card dicts
        possession_state: "neutral", "driving", or "holding" (for formation awareness)
        discard_pile: List of used cards (prevents JKR duplication)
    
    Returns:
        Tuple of (total_value, best_suit, max_card, display_string, special_move)
    """
    
    # 1. Safety Net - Refill if low (reshuffle discard, DON'T create new JKRs!)
    if len(bot_deck) < rank_val:
        if discard_pile and len(discard_pile) > 0:
            print(f"   [BOT DECK LOW: {len(bot_deck)} cards] Reshuffling discard pile...")
            bot_deck.extend(discard_pile)
            discard_pile.clear()
            random.shuffle(bot_deck)
            time.sleep(1)
        else:
            # Only create fresh deck if BOTH deck and discard are empty (shouldn't happen)
            print(f"   [BOT DECK EMPTY] Creating fresh deck...")
            bot_deck[:] = get_fresh_deck_dicts()
            time.sleep(1)
    
    # 2. Draw Hand
    hand = [bot_deck.pop() for _ in range(rank_val)]
    
    # 3. Analyze Groups
    groups = {"C": [], "H": [], "S": [], "D": [], "JKR": []}
    hand_vals = []
    
    for c in hand:
        groups[c['suit']].append(c['val'])
        hand_vals.append(c['val'])
    
    # 4. Pick Best Suit Based on Possession State
    # NEUTRAL: Mixed suits allowed, choose strongest
    # DRIVING: Red suits (H/D) offensive plays
    # HOLDING: Black suits (C/S) defensive covers
    
    if possession_state == "neutral":
        # Neutral formation: pick strongest suit regardless of color
        priority = ["D", "H", "C", "S"]  # Diamonds first (highest scoring potential)
        best_suit = max(priority, key=lambda s: sum(groups[s]) if groups[s] else 0)
    elif bot_is_driving:
        priority = ["D", "H"]  # Offense first (Diamonds, Hearts)
        # Fallback if no offensive cards
        if not any(groups[s] for s in priority):
            priority = ["C", "S"]
        best_suit = max(priority, key=lambda s: sum(groups[s]) if groups[s] else 0)
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
                special = "JUKE"        # Diamonds + JKR = Juke Step
            elif groups["H"]:
                special = "STIFF_ARM"   # Hearts + JKR = Stiff Arm
        else:
            if groups["S"]:
                special = "PUNT"        # Spades + JKR = Punt (ball strip)
            elif groups["C"]:
                special = "RUCK"        # Clubs + JKR = Ruck (scrimmage)
    
    # 6. Recycle Unused Cards
    # Keep cards that match best suit OR are Jokers
    # Everything else goes back to BOTTOM of deck (prevents deck burn)
    unused_cards = [c for c in hand if c['suit'] != best_suit and c['val'] != 15]
    for card in unused_cards:
        bot_deck.insert(0, card)  # Bottom of deck for future draws
    
    # 7. Format Display
    display = "".join([f"[{SYMBOLS.get(best_suit, '?')} {v}] " for v in groups[best_suit]])
    if has_jkr:
        display += "[JKR] "
    
    # 8. Return Analysis
    total_val = sum(groups[best_suit])
    max_card = max(groups[best_suit] + [0])
    
    return total_val, best_suit, max_card, display.strip(), special


def reshuffle_bot_deck(bot_deck):
    """
    Reshuffle bot deck (called on user timeout)
    
    Args:
        bot_deck: List to modify in-place
    """
    print(f"   [BOT DECK] Also reshuffling... ({len(bot_deck)} cards)")
    bot_deck[:] = get_fresh_deck_dicts()
    time.sleep(0.5)
