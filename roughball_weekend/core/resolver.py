"""
ROUGHBALL: Play Resolution Engine
Handles Audible → Clash → Resolution flow
"""

import random
import time
from .dice import roll_d66, count_hits, roll_d4, roll_d6, get_success_window
from .teams import TEAMS, SYMBOLS, SUIT_NAMES


def resolve_play(u_team, b_team, u_cards, b_cards, u_driving, division_rank):
    """
    Main play resolution engine
    
    Args:
        u_team: User team dict
        b_team: Bot team dict
        u_cards: List of user card dicts
        b_cards: List of bot card dicts
        u_driving: Bool, is user currently driving
        division_rank: Int 1-5
    
    Returns:
        Tuple of (points_user, points_bot, new_u_driving, commentary)
    """
    
    # Check for JKR special moves first
    u_has_jkr = any(c['val'] == 15 or c['suit'] == 'JKR' for c in u_cards)
    b_has_jkr = any(c['val'] == 15 or c['suit'] == 'JKR' for c in b_cards)
    
    if u_has_jkr or b_has_jkr:
        return resolve_jkr_moves(u_team, b_team, u_cards, b_cards, u_driving, u_has_jkr, b_has_jkr)
    
    # Standard clash resolution
    return resolve_clash(u_team, b_team, u_cards, b_cards, u_driving, division_rank)


def resolve_clash(u_team, b_team, u_cards, b_cards, u_driving, division_rank):
    """
    Resolve D66 clash with proper success windows
    """
    
    # Roll D66 for both teams
    u_dice = roll_d66()
    b_dice = roll_d66()
    
    # Get success window
    success_window = get_success_window(division_rank)
    
    # Count hits
    u_hits = count_hits(u_dice, success_window)
    b_hits = count_hits(b_dice, success_window)
    
    print(f"\n[CLASH]: User rolls {u_dice} = {u_hits} HITS | Bot rolls {b_dice} = {b_hits} HITS")
    time.sleep(2)
    
    # Determine outcome
    if u_hits > b_hits:
        # User wins clean
        return resolve_clean_win(u_team, b_team, u_driving, True)
    
    elif b_hits > u_hits:
        # Bot wins clean
        return resolve_clean_win(u_team, b_team, u_driving, False)
    
    elif u_hits == b_hits and u_hits > 0:
        # Stalemate
        return resolve_breaker(u_team, b_team, u_cards, b_cards, u_driving)
    
    elif u_hits == 1 and b_hits == 1:
        # Dual-split (both 1 hit / 1 miss)
        return resolve_complication(u_team, b_team, u_driving)
    
    elif u_hits == 0 and b_hits == 0:
        # Fumble (both 0 hits)
        print("\n>>> FUMBLE! Both teams drop it! Ball is LIVE! RE-AUDIBLE!")
        time.sleep(2)
        return (0, 0, u_driving, "FUMBLE - RE-AUDIBLE!")


def resolve_clean_win(u_team, b_team, u_driving, user_won):
    """
    Handle clean win (one team has more hits)
    """
    
    if user_won:
        if u_driving:
            # User driving wins = TRY
            print(f"\n   > {u_team['name']} drives successfully! TRY! (+5 PTS)")
            time.sleep(2)
            return (5, 0, False, "TRY")  # Scorer goes HOLDING (False)
        else:
            # User holding wins = Take ball
            print(f"\n   > {u_team['name']} defense HOLDS! Possession flips!")
            time.sleep(2)
            return (0, 0, True, "DEFENSIVE STOP")  # Holder goes DRIVING (True)
    
    else:
        if not u_driving:
            # Bot driving wins = TRY
            print(f"\n   > {b_team['name']} drives successfully! TRY! (+5 PTS)")
            time.sleep(2)
            return (0, 5, True, "TRY (Bot)")  # Scorer goes HOLDING (user drives)
        else:
            # Bot holding wins = Take ball
            print(f"\n   > {b_team['name']} defense HOLDS! Possession flips!")
            time.sleep(2)
            return (0, 0, False, "DEFENSIVE STOP (Bot)")  # Holder goes DRIVING (user holds)


def resolve_breaker(u_team, b_team, u_cards, b_cards, u_driving):
    """
    Resolve stalemate via stat-based breaker
    
    Steps:
    1. Compare primary stats
    2. If tied, add card values
    3. If still tied, saving throw
    4. If STILL tied, re-audible
    """
    
    print("\n>>> STALEMATE! Going to BREAKER...")
    time.sleep(2)
    
    # Get primary stats based on suits played
    u_suit = u_cards[0]['suit'] if u_cards[0]['suit'] != 'JKR' else 'C'
    b_suit = b_cards[0]['suit'] if b_cards[0]['suit'] != 'JKR' else 'C'
    
    from .teams import SUITS
    u_stat_key = SUITS.get(u_suit, 'TKL')
    b_stat_key = SUITS.get(b_suit, 'TKL')
    
    u_stat = u_team['stats'][u_stat_key] + u_team['boosts'][u_stat_key]
    b_stat = b_team['stats'][b_stat_key] + b_team['boosts'][b_stat_key]
    
    print(f"   Stat Check: User {u_stat_key}={u_stat} | Bot {b_stat_key}={b_stat}")
    
    if u_stat > b_stat:
        print(f"   >>> User wins via STAT ADVANTAGE!")
        time.sleep(2)
        return resolve_clean_win(u_team, b_team, u_driving, True)
    
    elif b_stat > u_stat:
        print(f"   >>> Bot wins via STAT ADVANTAGE!")
        time.sleep(2)
        return resolve_clean_win(u_team, b_team, u_driving, False)
    
    # Stats tied - add card values
    u_total = u_stat + sum(c['val'] for c in u_cards)
    b_total = b_stat + sum(c['val'] for c in b_cards)
    
    print(f"   Stats tied! Adding card values...")
    print(f"   User total: {u_total} | Bot total: {b_total}")
    
    if u_total > b_total:
        print(f"   >>> User wins via CARD VALUE!")
        time.sleep(2)
        return resolve_clean_win(u_team, b_team, u_driving, True)
    
    elif b_total > u_total:
        print(f"   >>> Bot wins via CARD VALUE!")
        time.sleep(2)
        return resolve_clean_win(u_team, b_team, u_driving, False)
    
    # Still tied - saving throw
    print(f"   Still tied! Rolling SAVING THROWS...")
    
    SAVE_MAP = {'C': 'STA', 'H': 'SPD', 'S': 'KCK', 'D': 'CAT'}
    u_save_key = SAVE_MAP.get(u_suit, 'STA')
    b_save_key = SAVE_MAP.get(b_suit, 'STA')
    
    u_save = u_team['save'][u_save_key] + u_team.get('save_boosts', {}).get(u_save_key, 0)
    b_save = b_team['save'][b_save_key] + b_team.get('save_boosts', {}).get(b_save_key, 0)
    
    u_roll = u_save + roll_d6()
    b_roll = b_save + roll_d6()
    
    print(f"   User {u_save_key}: {u_save} + d6 = {u_roll}")
    print(f"   Bot {b_save_key}: {b_save} + d6 = {b_roll}")
    time.sleep(2)
    
    if u_roll > b_roll:
        print(f"   >>> User wins via SAVING THROW!")
        time.sleep(2)
        return resolve_clean_win(u_team, b_team, u_driving, True)
    
    elif b_roll > u_roll:
        print(f"   >>> Bot wins via SAVING THROW!")
        time.sleep(2)
        return resolve_clean_win(u_team, b_team, u_driving, False)
    
    # STILL tied?!
    print("\n   UNBELIEVABLE! Still tied after breaker! RE-AUDIBLE!")
    time.sleep(2)
    return (0, 0, u_driving, "RE-AUDIBLE (Breaker Tie)")


def resolve_complication(u_team, b_team, u_driving):
    """
    Resolve D4 complication (dual-split: both 1 hit / 1 miss)
    """
    
    print("\n>>> DUAL-SPLIT! Rolling D4 COMPLICATION...")
    time.sleep(2)
    
    comp_roll = roll_d4()
    
    COMPLICATIONS = {
        1: ('SACK', 'SPD'),
        2: ('OUT_OF_BOUNDS', 'CAT'),
        3: ('PENALTY', 'STA'),
        4: ('INTERCEPTION', 'KCK')
    }
    
    comp_type, save_key = COMPLICATIONS[comp_roll]
    
    print(f"   Complication: {comp_type} (Check {save_key})")
    
    # Determine offender via saving throw (lower roll = offender)
    u_save = u_team['save'][save_key] + u_team.get('save_boosts', {}).get(save_key, 0)
    b_save = b_team['save'][save_key] + b_team.get('save_boosts', {}).get(save_key, 0)
    
    u_roll = u_save + roll_d6()
    b_roll = b_save + roll_d6()
    
    user_is_offender = u_roll < b_roll
    
    if comp_type == 'SACK':
        if user_is_offender and u_driving:
            print(f"    >>> SACK! {b_team['name']} strips the ball! (+2 PTS)")
            time.sleep(2)
            return (0, 2, False, "SACK")
        elif not user_is_offender and not u_driving:
            print(f"    >>> SACK! {u_team['name']} strips the ball! (+2 PTS)")
            time.sleep(2)
            return (2, 0, True, "SACK")
        else:
            print(f"    >>> Sack attempt failed!")
            time.sleep(2)
            return (0, 0, u_driving, "SACK ATTEMPT FAILED")
    
    elif comp_type == 'OUT_OF_BOUNDS':
        print(f"    >>> Ball goes OUT OF BOUNDS! Reset to NEUTRAL!")
        time.sleep(2)
        return (0, 0, None, "OUT OF BOUNDS")  # None = reset to neutral
    
    elif comp_type == 'PENALTY':
        if user_is_offender:
            print(f"    >>> PENALTY! {b_team['name']} awarded Field Goal! (+3 PTS)")
            time.sleep(2)
            return (0, 3, None, "PENALTY FG")
        else:
            print(f"    >>> PENALTY! {u_team['name']} awarded Field Goal! (+3 PTS)")
            time.sleep(2)
            return (3, 0, None, "PENALTY FG")
    
    elif comp_type == 'INTERCEPTION':
        if user_is_offender and u_driving:
            print(f"    >>> INTERCEPTION! {b_team['name']} picks it off! (+1 PT)")
            time.sleep(2)
            return (0, 1, False, "INT")
        elif not user_is_offender and not u_driving:
            print(f"    >>> INTERCEPTION! {u_team['name']} picks it off! (+1 PT)")
            time.sleep(2)
            return (1, 0, True, "INT")
        else:
            print(f"    >>> INT attempt failed!")
            time.sleep(2)
            return (0, 0, u_driving, "INT ATTEMPT FAILED")
    
    return (0, 0, u_driving, "COMPLICATION RESOLVED")


def resolve_jkr_moves(u_team, b_team, u_cards, b_cards, u_driving, u_has_jkr, b_has_jkr):
    """
    Resolve JKR special moves
    
    Types:
    - JKR + ♣ = RUCK (annul dice, force stalemate)
    - JKR + ♥ = STIFF ARM (guaranteed TRY)
    - JKR + ♠ = PUNT (possession flip)
    - JKR + ♦ = JUKE STEP (humiliating TRY)
    """
    
    print("\n>>> JOKER TRIGGERED! <<<")
    time.sleep(2)
    
    # Determine which special move
    u_special = None
    b_special = None
    
    if u_has_jkr:
        # Find accompanying suit
        u_suits = [c['suit'] for c in u_cards if c['suit'] != 'JKR']
        if u_suits:
            u_suit = u_suits[0]
            u_special = {"C": "RUCK", "H": "STIFF_ARM", "S": "PUNT", "D": "JUKE"}.get(u_suit)
    
    if b_has_jkr:
        b_suits = [c['suit'] for c in b_cards if c['suit'] != 'JKR']
        if b_suits:
            b_suit = b_suits[0]
            b_special = {"C": "RUCK", "H": "STIFF_ARM", "S": "PUNT", "D": "JUKE"}.get(b_suit)
    
    # Both teams play JKR? Clash!
    if u_special and b_special:
        print("   JKR CLASH! Both teams activate special moves!")
        print("   Rolling SAVING THROWS to determine winner...")
        time.sleep(2)
        
        # Saving throw clash
        u_roll = roll_d6() + sum(u_team['save'].values()) // 4
        b_roll = roll_d6() + sum(b_team['save'].values()) // 4
        
        if u_roll > b_roll:
            print(f"   >>> {u_team['name']} SURVIVES! {u_special} activates!")
            time.sleep(2)
            return apply_special_move(u_team, b_team, u_special, u_driving, True)
        elif b_roll > u_roll:
            print(f"   >>> {b_team['name']} SURVIVES! {b_special} activates!")
            time.sleep(2)
            return apply_special_move(u_team, b_team, b_special, u_driving, False)
        else:
            print("   >>> UNBELIEVABLE! JKR CLASH STALEMATE! RE-AUDIBLE!")
            time.sleep(2)
            return (0, 0, u_driving, "JKR CLASH TIE")
    
    # Only user plays JKR
    elif u_special:
        return apply_special_move(u_team, b_team, u_special, u_driving, True)
    
    # Only bot plays JKR
    elif b_special:
        return apply_special_move(u_team, b_team, b_special, u_driving, False)
    
    # JKR without suit = Playbook recall (not implemented in BUILD 1)
    print("   >>> JKR PLAYBOOK RECALL (not yet implemented)")
    time.sleep(2)
    return (0, 0, u_driving, "JKR PLAYBOOK")


def apply_special_move(u_team, b_team, move_type, u_driving, user_activated):
    """Apply the effect of a JKR special move"""
    
    team = u_team if user_activated else b_team
    
    if move_type == "RUCK":
        print(f"   > {team['name']} plays RUCK! Dice ANNULLED! Forced stalemate!")
        print(f"   > Possession flips!")
        time.sleep(2)
        return (0, 0, not u_driving, "RUCK")
    
    elif move_type == "STIFF_ARM":
        if (user_activated and u_driving) or (not user_activated and not u_driving):
            print(f"   > {team['name']} STIFF ARM! UNSTOPPABLE! TRY! (+5 PTS)")
            time.sleep(2)
            if user_activated:
                return (5, 0, False, "STIFF ARM TRY")
            else:
                return (0, 5, True, "STIFF ARM TRY (Bot)")
        else:
            print(f"   > {team['name']} attempts STIFF ARM but isn't driving!")
            time.sleep(2)
            return (0, 0, u_driving, "STIFF ARM FAILED")
    
    elif move_type == "PUNT":
        print(f"   > {team['name']} PUNTS! Massive boot! Possession secured!")
        time.sleep(2)
        if user_activated:
            return (0, 0, True, "PUNT")
        else:
            return (0, 0, False, "PUNT (Bot)")
    
    elif move_type == "JUKE":
        if (user_activated and u_driving) or (not user_activated and not u_driving):
            print(f"   > {team['name']} JUKE STEP! ANKLES BROKEN! HUMILIATION! TRY! (+5 PTS)")
            time.sleep(2)
            if user_activated:
                return (5, 0, False, "JUKE STEP TRY")
            else:
                return (0, 5, True, "JUKE STEP TRY (Bot)")
        else:
            print(f"   > {team['name']} attempts JUKE but isn't driving!")
            time.sleep(2)
            return (0, 0, u_driving, "JUKE FAILED")
    
    return (0, 0, u_driving, "SPECIAL MOVE")
