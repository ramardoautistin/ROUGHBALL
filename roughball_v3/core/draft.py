"""
ROUGHBALL: Draft System Module
Complete implementation of the NRBL draft mechanics
"""

import random
import time
from .display import clear, print_header

# --- POSITION MAPPING (DESIGN DOC COMPLIANT) ---
POSITION_MAP = {
    "C": {
        "top": "DT", "bottom": "DE", "corner": "LB",
        "name": "Scrimmager", "stat": "TKL"
    },
    "H": {
        "top": "QG", "bottom": "RG", "corner": "SG",
        "name": "Field General", "stat": "AWR"
    },
    "S": {
        "top": "OG", "bottom": "OT", "corner": "CB",
        "name": "Pitch Guard", "stat": "INT"
    },
    "D": {
        "top": "WB", "bottom": "TB", "corner": "SG",
        "name": "Air Raider", "stat": "PAS"
    }
}

# --- DUAL THREAT VETERAN ARCHETYPES ---
DUAL_THREAT_MAP = {
    "11": {"name": "PITCH GENERAL", "suits": ["S", "H"], "desc": "Kicking + Playcalling"},
    "12_RED": {"name": "WING BACKER", "suits": ["C", "D"], "desc": "Scrimmage + Reception"},
    "14_RED": {"name": "FIELD RAIDER", "suits": ["H", "D"], "desc": "Handovers + Routes"},
    "14_BLACK": {"name": "SCRUM GUARD", "suits": ["C", "S"], "desc": "Rucking + Punting"},
    "13": {"name": "AIR PITCHER", "suits": ["D", "S"], "desc": "Catching + Goaling"},
    "12_BLACK": {"name": "TACKLE CARRIER", "suits": ["C", "H"], "desc": "Scrum + Ball Protection"},
    "JKR": {"name": "WILDCARD VETERAN", "suits": ["C", "H", "S", "D"], "desc": "Choose Any Dual Threat"}
}

SYMBOLS = {"C": "♣", "H": "♥", "S": "♠", "D": "♦"}


def create_deck():
    """Generate a fresh 54-card deck"""
    deck = []
    for suit in ["C", "H", "S", "D"]:
        for value in range(2, 15):
            deck.append({"suit": suit, "value": value})
    deck.append({"suit": "JKR", "value": 15})
    deck.append({"suit": "JKR", "value": 15})
    random.shuffle(deck)
    return deck


def get_star_quality():
    """Roll d6-1 for star quality (0-5 stars)"""
    return max(0, random.randint(1, 6) - 1)


def format_card(card):
    """Display card in readable format"""
    if card['suit'] == "JKR":
        return "[JKR]"
    
    face_map = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
    display_val = face_map.get(card['value'], card['value'])
    return f"[{SYMBOLS[card['suit']]} {display_val}]"


def determine_position(card):
    """
    Determine position based on card value and suit.
    Returns: (position_code, position_full_name, is_special)
    """
    if card['suit'] == "JKR":
        return ("JKR", "JOKER [NEEDS 2ND CARD]", True)
    
    pos_data = POSITION_MAP[card['suit']]
    
    if card['value'] >= 11:  # Face cards = TOP
        return (pos_data["top"], f"{pos_data['top']} ({pos_data['name']})", False)
    else:  # Number cards = BOTTOM
        return (pos_data["bottom"], f"{pos_data['bottom']} ({pos_data['name']})", False)


def handle_joker_pull(deck):
    """
    Handle JKR card pull - draw second card.
    Returns: (position_code, description, is_dual_threat, star_bonus)
    """
    print("\n    [!] JOKER PULLED! Drawing second card...")
    time.sleep(1.5)
    
    if not deck:
        print("    [!] Deck empty! Reshuffling...")
        deck.extend(create_deck())
    
    second_card = deck.pop()
    print(f"    [>>] Second Card: {format_card(second_card)}")
    time.sleep(1)
    
    suit = second_card['suit']
    val = second_card['value']
    
    # JKR + JKR = Wildcard Veteran
    if suit == "JKR":
        print("\n    [!!!] DOUBLE JOKER! WILDCARD VETERAN!")
        print("    [>>>] Choose ANY Dual Threat Archetype!")
        time.sleep(2)
        
        print("\n    Available Dual Threat Archetypes:")
        archetypes = [
            "1. PITCH GENERAL (♠+♥) - Kicking + Playcalling",
            "2. WING BACKER (♣+♦) - Scrimmage + Reception",
            "3. FIELD RAIDER (♥+♦) - Handovers + Routes",
            "4. SCRUM GUARD (♣+♠) - Rucking + Punting",
            "5. AIR PITCHER (♦+♠) - Catching + Goaling",
            "6. TACKLE CARRIER (♣+♥) - Scrum + Ball Protection"
        ]
        for arch in archetypes:
            print(f"       {arch}")
        
        choice = input("\n    > Select archetype (1-6): ")
        choice_map = {
            "1": ("PITCH_GEN", "PITCH GENERAL (♠+♥)"),
            "2": ("WING_BACK", "WING BACKER (♣+♦)"),
            "3": ("FIELD_RAID", "FIELD RAIDER (♥+♦)"),
            "4": ("SCRUM_GRD", "SCRUM GUARD (♣+♠)"),
            "5": ("AIR_PITCH", "AIR PITCHER (♦+♠)"),
            "6": ("TACKLE_CAR", "TACKLE CARRIER (♣+♥)")
        }
        
        pos_code, desc = choice_map.get(choice, ("PITCH_GEN", "PITCH GENERAL (♠+♥)"))
        return (pos_code, desc, True, 3)
    
    # JKR + Face Card = Dual Threat Veteran
    elif val >= 11:
        color = "RED" if suit in ["H", "D"] else "BLACK"
        
        if val == 11:
            archetype = DUAL_THREAT_MAP["11"]
        elif val == 12:
            archetype = DUAL_THREAT_MAP[f"12_{color}"]
        elif val == 13:
            archetype = DUAL_THREAT_MAP["13"]
        elif val == 14:
            archetype = DUAL_THREAT_MAP[f"14_{color}"]
        
        pos_code = archetype["name"].replace(" ", "_").upper()
        desc = f"{archetype['name']} ({archetype['desc']})"
        
        print(f"\n    [***] DUAL THREAT VETERAN: {desc}")
        time.sleep(2)
        
        return (pos_code, desc, True, 2)
    
    # JKR + Number Card = Corner Position
    else:
        pos_data = POSITION_MAP[suit]
        pos_code = pos_data["corner"]
        desc = f"{pos_code} [CORNER] ({pos_data['name']})"
        
        print(f"\n    [>>] Corner Position: {desc}")
        time.sleep(1)
        
        return (pos_code, desc, False, 1)


def draft_single_pick(deck, pick_num):
    """
    Draft a single player.
    Returns: player_data dict
    """
    print(f"\n{'='*60}")
    print(f"   DRAFT PICK #{pick_num}")
    print(f"{'='*60}")
    
    if not deck:
        print("   [!] Deck empty! Reshuffling...")
        deck.extend(create_deck())
    
    input("   [PRESS ENTER] To draw card...")
    card = deck.pop()
    print(f"\n   [CARD DRAWN]: {format_card(card)}")
    time.sleep(1.5)
    
    pos_code, pos_desc, is_special = determine_position(card)
    
    star_bonus = 0
    is_dual_threat = False
    
    if is_special:
        pos_code, pos_desc, is_dual_threat, star_bonus = handle_joker_pull(deck)
    
    base_stars = get_star_quality()
    total_stars = min(5, base_stars + star_bonus)
    
    star_display = "★" * total_stars if total_stars > 0 else "[BUST]"
    
    print(f"\n   [POSITION]: {pos_desc}")
    print(f"   [STAR QUALITY]: {star_display} ({total_stars}/5)")
    
    if is_dual_threat:
        print(f"   [SPECIAL]: DUAL THREAT VETERAN (+{star_bonus} bonus stars)")
    elif star_bonus > 0:
        print(f"   [SPECIAL]: Corner Specialist (+{star_bonus} bonus star)")
    
    time.sleep(2)
    
    return {
        "position": pos_code,
        "description": pos_desc,
        "stars": total_stars,
        "card": card,
        "is_dual_threat": is_dual_threat,
        "is_corner": star_bonus == 1 and not is_dual_threat
    }


def full_roster_draft():
    """Draft a complete 8-man starter roster"""
    clear()
    print_header("FULL 8-MAN ROSTER DRAFT")
    print("   Building a brand new franchise from scratch!")
    print("   You will draft 8 starters (2 per suit minimum).")
    print("="*60)
    
    deck = create_deck()
    roster = []
    suit_count = {"C": 0, "H": 0, "S": 0, "D": 0}
    
    for i in range(8):
        player = draft_single_pick(deck, i + 1)
        roster.append(player)
        
        if not player["is_dual_threat"]:
            suit = player["card"]["suit"]
            if suit != "JKR":
                suit_count[suit] += 1
    
    # Display final roster
    print("\n" + "="*60)
    print("   DRAFT COMPLETE! FINAL 8-MAN ROSTER")
    print("="*60)
    
    for idx, player in enumerate(roster, 1):
        stars = "★" * player["stars"] if player["stars"] > 0 else "[BUST]"
        special = ""
        if player["is_dual_threat"]:
            special = " [DUAL THREAT]"
        elif player["is_corner"]:
            special = " [CORNER]"
        
        print(f"   [{idx}] {player['position'].ljust(12)} | {stars.ljust(10)} | {player['description']}{special}")
    
    print(f"\n   Suit Distribution: ♣:{suit_count['C']} ♥:{suit_count['H']} ♠:{suit_count['S']} ♦:{suit_count['D']}")
    print("="*60)
    
    input("\n[PRESS ENTER] To continue...")
    return roster


def seasonal_draft():
    """Draft 4 backup players for existing roster"""
    clear()
    print_header("SEASONAL 4-PICK DRAFT (OFF-SEASON)")
    print("   The season has ended. Time to draft backup talent!")
    print("   You will draft 4 players (1 per suit recommended).")
    print("="*60)
    
    deck = create_deck()
    picks = []
    
    for i in range(4):
        player = draft_single_pick(deck, i + 1)
        picks.append(player)
    
    # Display final picks
    print("\n" + "="*60)
    print("   DRAFT COMPLETE! NEW ROSTER ADDITIONS")
    print("="*60)
    
    for idx, player in enumerate(picks, 1):
        stars = "★" * player["stars"] if player["stars"] > 0 else "[BUST]"
        special = ""
        if player["is_dual_threat"]:
            special = " [DUAL THREAT]"
        elif player["is_corner"]:
            special = " [CORNER]"
        
        print(f"   [{idx}] {player['position'].ljust(12)} | {stars.ljust(10)} | {player['description']}{special}")
    
    print("="*60)
    print("   These players can be used as backups or traded.")
    
    input("\n[PRESS ENTER] To continue...")
    return picks


def mock_draft_scouting(user_team_id=None):
    """Simulate other teams drafting"""
    clear()
    print_header("MOCK DRAFT SCOUTING REPORT")
    print("   Simulating draft picks for 15 other franchises...")
    print("="*60)
    
    time.sleep(2)
    
    teams = list(range(1, 17))
    if user_team_id:
        teams.remove(int(user_team_id))
    
    deck = create_deck()
    
    print(f"\n{'TEAM':<6} | {'STATUS':<10} | {'PICKS':<50}")
    print("-" * 85)
    
    for team_id in teams:
        num_picks = 4 if team_id > 4 else 2
        status = "REBUILD" if num_picks == 4 else "FINALIST"
        
        picks_display = []
        for _ in range(num_picks):
            if not deck:
                deck = create_deck()
            
            card = deck.pop()
            pos_code, pos_desc, is_special = determine_position(card)
            
            if is_special and deck:
                second = deck.pop()
                if second['suit'] == "JKR":
                    pos_code = "WILDCARD"
                elif second['value'] >= 11:
                    pos_code = "DUAL_THR"
                else:
                    pos_code = POSITION_MAP[second['suit']]["corner"]
            
            stars = get_star_quality()
            star_display = "★" * stars if stars > 0 else "BUST"
            
            picks_display.append(f"{SYMBOLS.get(card['suit'], '?')} {pos_code}({star_display})")
        
        picks_str = " | ".join(picks_display)
        print(f"T{team_id:<4} | {status:<10} | {picks_str}")
    
    print("-" * 85)
    input("\n[PRESS ENTER] To return to menu...")
