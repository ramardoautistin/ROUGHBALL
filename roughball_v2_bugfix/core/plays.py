"""
ROUGHBALL: Route & Cover Reference
Maps card values to play names (from ROUGHBALL_DOC.md Section 5)
"""

# Route names for DRIVING (Offensive plays - Hearts/Diamonds)
ROUTES = {
    2: "Dig",
    3: "Hitch",
    4: "Curl",
    5: "Mesh",
    6: "Slant",
    7: "Swing",
    8: "Stick",
    9: "Long",
    10: "Handoff",
    11: "Feint Play (T Formation)",
    12: "Side Pass (Y Formation)",
    13: "Kick Pass (V Formation)",
    14: "Spread Form",
    15: "SPECIAL MOVE"
}

# Cover names for HOLDING (Defensive plays - Clubs/Spades)
COVERS = {
    2: "Cover 2",
    3: "Cover 3",
    4: "Cover 4",
    5: "Nickel",
    6: "Dime",
    7: "Quarter",
    8: "Stacks",
    9: "Slot",
    10: "Man 2 Man",
    11: "Feint Play (T Formation)",
    12: "Side Pass (Y Formation)",
    13: "Kick Based on Suit",
    14: "Spread Form",
    15: "SPECIAL MOVE"
}

# Kick variations (for K = 13)
KICK_TYPES = {
    'C': "Defensive Punt",
    'H': "Self-Kick",
    'S': "Offensive Punt",
    'D': "Kick-Pass"
}


def get_play_name(card_val, suit, is_driving):
    """
    Get play name for a card
    
    Args:
        card_val: Card value (2-15)
        suit: Card suit ('C', 'H', 'S', 'D', 'JKR')
        is_driving: Bool, is team driving (offensive routes) or holding (defensive covers)
    
    Returns:
        String play name
    """
    
    # Special cases
    if card_val == 15 or suit == 'JKR':
        return "SPECIAL MOVE"
    
    if card_val == 13:  # King = Kick
        return KICK_TYPES.get(suit, "Kick Pass")
    
    # Standard plays
    if is_driving:
        return ROUTES.get(card_val, "Unknown Play")
    else:
        return COVERS.get(card_val, "Unknown Cover")


def get_hand_description(cards, is_driving):
    """
    Get description of entire hand (for reveal phase)
    
    Args:
        cards: List of card dicts [{"suit": "H", "val": 10}, ...]
        is_driving: Bool, is team driving
    
    Returns:
        String description like "Handoff + Long Route"
    """
    
    play_names = []
    
    for card in cards:
        name = get_play_name(card['val'], card['suit'], is_driving)
        play_names.append(name)
    
    if not play_names:
        return "No plays"
    
    if len(play_names) == 1:
        return play_names[0]
    
    # Join multiple plays
    return " + ".join(play_names)
