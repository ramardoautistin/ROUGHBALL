"""
ROUGHBALL: Formation Validator
Enforces suit restrictions based on possession state

v10.3 NEW MODULE:
- Validates card suits against formation rules
- NEUTRAL: Mixed suits allowed
- DRIVING: Red suits only (♥/♦)
- HOLDING: Black suits only (♣/♠)
"""

from .teams import SYMBOLS


def validate_hand_formation(cards, possession_state, is_driving):
    """
    Validate that hand follows formation rules.
    
    Args:
        cards: List of card dicts [{"suit": "H", "val": 10}, ...]
        possession_state: "neutral", "driving", or "holding"
        is_driving: Bool, is this team currently driving
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    
    if possession_state == "neutral":
        # NEUTRAL: All suits allowed (combined plays)
        return (True, "")
    
    # Extract suits (excluding JKR which is always valid)
    suits = [c['suit'] for c in cards if c['suit'] != 'JKR']
    
    if not suits:
        # All JKRs - always valid
        return (True, "")
    
    # Check formation restrictions
    if is_driving:
        # DRIVING: Red suits only (♥/♦)
        invalid_suits = [s for s in suits if s not in ('H', 'D')]
        if invalid_suits:
            invalid_symbols = [SYMBOLS.get(s, s) for s in invalid_suits]
            return (False, f"DRIVING formation requires RED suits (♥/♦) only! Invalid: {', '.join(invalid_symbols)}")
    else:
        # HOLDING: Black suits only (♣/♠)
        invalid_suits = [s for s in suits if s not in ('C', 'S')]
        if invalid_suits:
            invalid_symbols = [SYMBOLS.get(s, s) for s in invalid_suits]
            return (False, f"HOLDING formation requires BLACK suits (♣/♠) only! Invalid: {', '.join(invalid_symbols)}")
    
    return (True, "")


def get_formation_help(possession_state, is_driving):
    """
    Get help text for current formation.
    
    Args:
        possession_state: "neutral", "driving", or "holding"
        is_driving: Bool
    
    Returns:
        Help string
    """
    
    if possession_state == "neutral":
        return "NEUTRAL: Mix any suits (♣/♥/♠/♦)"
    elif is_driving:
        return "DRIVING: Red suits only (♥ Hearts / ♦ Diamonds)"
    else:
        return "HOLDING: Black suits only (♣ Clubs / ♠ Spades)"
