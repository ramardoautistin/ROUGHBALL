"""
ROUGHBALL: Play Resolution Engine
Handles Audible -> Clash -> Resolution flow

CORRECTED per ROUGHBALL_DOC.md:
- Dual-Split (1-1) now routes to D4 Complication, NOT Breaker
- Stalemate (Breaker) only triggers on 2-2
- Clean win scoring checks suit: H/D offense = TRY, D+K = Field Goal, else Defensive Stop
- Breaker compares same stat context, not cross-suit
- RUCK routes to Breaker (play goes stale = stat resolution)
- PUNT = defensive possession grab (ball strip)
- Saving throw map: C=STA, H=SPD, S=KCK, D=CAT (per DOC)
"""

import random
import time
from .dice import roll_d66, count_hits, roll_d4, roll_d6, get_success_window
from .teams import TEAMS, SYMBOLS, SUITS


# Canonical save map per DOC: suit -> saving throw stat
SAVE_MAP = {'C': 'STA', 'H': 'SPD', 'S': 'KCK', 'D': 'CAT'}


def resolve_play(u_team, b_team, u_cards, b_cards, u_driving, division_rank, u_dice=None, possession_state="driving"):
    """
    Main play resolution engine.
    
    Flow: Check JKR first, then standard D66 clash.
    
    Args:
        u_dice: Optional tuple (die1, die2) for user input
        possession_state: "neutral", "driving", or "holding" (for formation awareness)
    
    Returns:
        Tuple of (points_user, points_bot, new_u_driving, commentary)
        new_u_driving = None means neutral reset (possession stays, no flip)
    """
    
    # Check for JKR special moves first
    u_has_jkr = any(c['val'] == 15 or c['suit'] == 'JKR' for c in u_cards)
    b_has_jkr = any(c['val'] == 15 or c['suit'] == 'JKR' for c in b_cards)
    
    if u_has_jkr or b_has_jkr:
        return resolve_jkr_moves(u_team, b_team, u_cards, b_cards, u_driving, u_has_jkr, b_has_jkr)
    
    # Standard clash (pass user dice through)
    return resolve_clash(u_team, b_team, u_cards, b_cards, u_driving, division_rank, u_dice)


def _get_primary_suit(cards):
    """
    Get the primary (non-JKR) suit from a hand.
    Falls back to 'C' if only jokers.
    """
    for c in cards:
        if c['suit'] not in ('JKR', 'JOKER'):
            return c['suit']
    return 'C'


def resolve_clash(u_team, b_team, u_cards, b_cards, u_driving, division_rank, u_dice=None):
    """
    Resolve D66 clash with proper success windows.
    
    CORRECTED outcome routing (per DOC Phase III):
      - Clean Win:  highest hits wins -> score based on suit
      - Stalemate:  hits match AND both >= 2 -> THE BREAKER
      - Dual-Split: both exactly 1 hit  -> D4 COMPLICATION
      - Fumble:     both 0 hits         -> RE-AUDIBLE
    
    QoL v2:
      - u_dice: Optional tuple (die1, die2) for user to input their own dice rolls
    """
    
    # Bot always rolls
    b_dice = roll_d66()
    
    # User can provide their own dice or we roll for them
    if u_dice is None:
        u_dice = roll_d66()
    
    # Get success window for this division
    success_window = get_success_window(division_rank)
    
    # Count hits
    u_hits = count_hits(u_dice, success_window)
    b_hits = count_hits(b_dice, success_window)
    
    print(f"\n[PHYSICS] Rolling D66 (Target: {division_rank} or less)")
    print(f"   > {u_team['name']}: [{u_dice[0]}|{u_dice[1]}] = {u_hits} HITS")
    print(f"   > {b_team['name']}: [{b_dice[0]}|{b_dice[1]}] = {b_hits} HITS")
    time.sleep(2)
    
    # --- ROUTE BY OUTCOME ---
    
    # FUMBLE: both 0 hits -> ball is live, re-audible
    if u_hits == 0 and b_hits == 0:
        print("\n>>> FUMBLE (XX)! Both teams drop it! Ball is LIVE!")
        print("    RE-AUDIBLE next play. Possession unchanged.")
        time.sleep(2)
        return (0, 0, u_driving, "FUMBLE - RE-AUDIBLE")
    
    # DUAL-SPLIT: both exactly 1 hit -> D4 Complication
    if u_hits == 1 and b_hits == 1:
        print("\n>>> DUAL-SPLIT! [1 Hit / 1 Miss] each side!")
        time.sleep(1)
        return resolve_complication(u_team, b_team, u_driving)
    
    # STALEMATE: hits match (must be 2-2 at this point) -> THE BREAKER
    if u_hits == b_hits:
        print(f"\n>>> STALEMATE! ({u_hits}-{b_hits}) Line is locked!")
        time.sleep(1)
        return resolve_breaker(u_team, b_team, u_cards, b_cards, u_driving)
    
    # CLEAN WIN: one side has more hits
    u_suit = _get_primary_suit(u_cards)
    b_suit = _get_primary_suit(b_cards)
    
    if u_hits > b_hits:
        print(f"\n   > WINNER: {u_team['name']} ({SYMBOLS.get(u_suit, '?')})")
        time.sleep(1)
        return resolve_clean_win(u_team, b_team, u_suit, u_cards, u_driving, user_won=True)
    else:
        print(f"\n   > WINNER: {b_team['name']} ({SYMBOLS.get(b_suit, '?')})")
        time.sleep(1)
        return resolve_clean_win(u_team, b_team, b_suit, b_cards, u_driving, user_won=False)


def resolve_clean_win(u_team, b_team, winner_suit, winner_cards, u_driving, user_won):
    """
    Handle clean win. Scoring depends on WHO won and WHETHER they were driving.
    
    Per DOC:
    - Offense wins (driver wins the clash):
        H or D suit  -> TRY (+5 pts), possession flips
        D + King(13) -> KICK PASS / FIELD GOAL (+3 pts), possession flips
        C or S suit  -> Defensive Stoppage (no pts, possession flips)
    - Defense wins (holder wins the clash):
        -> Possession flips to the defender (they take the ball)
    """
    
    winner_was_driving = (user_won and u_driving) or (not user_won and not u_driving)
    winner_name = u_team['name'] if user_won else b_team['name']
    
    if winner_was_driving:
        # --- OFFENSE SCORED ---
        max_val = max(c['val'] for c in winner_cards)
        
        # Check for Kick Pass: Diamonds + King (val 13)
        if winner_suit == 'D' and max_val == 13:
            pts = 3
            print(f"   > KICK PASS! {winner_name} aims at the GOAL POST! FIELD GOAL! (+3 PTS)")
            time.sleep(2)
        # Check for TRY: Hearts or Diamonds
        elif winner_suit in ('H', 'D'):
            pts = 5
            print(f"   > TRY SUCCESSFUL! {winner_name} reaches the ENDZONE! (+5 PTS)")
            time.sleep(2)
        else:
            # Clubs or Spades while driving = no scoring conversion
            pts = 0
            print(f"   >>> DEFENSIVE STOPPAGE! {winner_name} advances but no conversion.")
            time.sleep(2)
            # Possession flips (offense lost the ball trying wrong suit)
            return (0, 0, not u_driving, "DEFENSIVE STOPPAGE (wrong suit)")
        
        # Award points to the winner
        if user_won:
            return (pts, 0, not u_driving, f"TRY" if pts == 5 else "FIELD GOAL")
        else:
            return (0, pts, not u_driving, f"TRY (Bot)" if pts == 5 else "FIELD GOAL (Bot)")
    
    else:
        # --- DEFENSE SCORED (possession flip, no points) ---
        print(f"   >>> DEFENSIVE STOPPAGE! {winner_name} holds the line! Possession flips!")
        time.sleep(2)
        return (0, 0, not u_driving, "DEFENSIVE STOP")


def resolve_breaker(u_team, b_team, u_cards, b_cards, u_driving):
    """
    THE BREAKER: Stat-based stalemate scrambler.
    
    Per DOC Section 3:
    1. Compare Primary Stats (same stat for both, based on clash context)
    2. If tied, add card values: [Primary Stat] + [Card Value total]
    3. If STILL tied, Final Saving Throw (d6 + save stat)
    4. If SOMEHOW still tied, RE-AUDIBLE
    
    CORRECTED: Both teams compare the SAME stat (the driving team's suit stat,
    since that's the relevant play context). This prevents the old bug where
    each team compared their own suit's stat against each other asymmetrically.
    """
    
    print("\n>>> THE BREAKER! Stat-based scramble...")
    time.sleep(1)
    
    u_suit = _get_primary_suit(u_cards)
    b_suit = _get_primary_suit(b_cards)
    
    # Use the driving team's suit to determine the contested stat
    if u_driving:
        contested_stat = SUITS.get(u_suit, 'TKL')
    else:
        contested_stat = SUITS.get(b_suit, 'TKL')
    
    # 1. COMPARE PRIMARY STATS (same stat, both teams)
    u_base = u_team['stats'][contested_stat] + u_team['boosts'].get(contested_stat, 0)
    b_base = b_team['stats'][contested_stat] + b_team['boosts'].get(contested_stat, 0)
    
    print(f"   [BREAKER 1] {contested_stat} Check: {u_team['name']} [{u_base}] vs {b_team['name']} [{b_base}]")
    time.sleep(1)
    
    if u_base > b_base:
        print(f"   >>> {u_team['name']} wins via STAT ADVANTAGE!")
        time.sleep(2)
        return _breaker_winner(u_team, b_team, u_suit, u_cards, u_driving, user_won=True)
    elif b_base > u_base:
        print(f"   >>> {b_team['name']} wins via STAT ADVANTAGE!")
        time.sleep(2)
        return _breaker_winner(u_team, b_team, b_suit, b_cards, u_driving, user_won=False)
    
    # 2. CARD VALUE ADDITION (stats are equal)
    u_card_total = sum(c['val'] for c in u_cards)
    b_card_total = sum(c['val'] for c in b_cards)
    u_total = u_base + u_card_total
    b_total = b_base + b_card_total
    
    print(f"   [BREAKER 2] Stats tied! Adding card values...")
    print(f"   {u_team['name']}: {u_base} + {u_card_total} = {u_total}")
    print(f"   {b_team['name']}: {b_base} + {b_card_total} = {b_total}")
    time.sleep(1)
    
    if u_total > b_total:
        print(f"   >>> {u_team['name']} wins via CARD VALUE!")
        time.sleep(2)
        return _breaker_winner(u_team, b_team, u_suit, u_cards, u_driving, user_won=True)
    elif b_total > u_total:
        print(f"   >>> {b_team['name']} wins via CARD VALUE!")
        time.sleep(2)
        return _breaker_winner(u_team, b_team, b_suit, b_cards, u_driving, user_won=False)
    
    # 3. FINAL SAVING THROW
    u_save_key = SAVE_MAP.get(u_suit, 'STA')
    b_save_key = SAVE_MAP.get(b_suit, 'STA')
    
    u_save_base = u_team['save'][u_save_key] + u_team.get('save_boosts', {}).get(u_save_key, 0)
    b_save_base = b_team['save'][b_save_key] + b_team.get('save_boosts', {}).get(b_save_key, 0)
    
    u_save_roll = u_save_base + roll_d6()
    b_save_roll = b_save_base + roll_d6()
    
    print(f"   [BREAKER 3] SAVING THROWS!")
    print(f"   {u_team['name']} {u_save_key}: {u_save_base} + d6 = {u_save_roll}")
    print(f"   {b_team['name']} {b_save_key}: {b_save_base} + d6 = {b_save_roll}")
    time.sleep(2)
    
    if u_save_roll > b_save_roll:
        print(f"   >>> {u_team['name']} wins via SAVING THROW!")
        time.sleep(2)
        return _breaker_winner(u_team, b_team, u_suit, u_cards, u_driving, user_won=True)
    elif b_save_roll > u_save_roll:
        print(f"   >>> {b_team['name']} wins via SAVING THROW!")
        time.sleep(2)
        return _breaker_winner(u_team, b_team, b_suit, b_cards, u_driving, user_won=False)
    
    # 4. SOMEHOW STILL TIED -> RE-AUDIBLE
    print("\n   UNBELIEVABLE! Still locked after full Breaker! RE-AUDIBLE!")
    time.sleep(2)
    return (0, 0, u_driving, "RE-AUDIBLE (Breaker Tie)")


def _breaker_winner(u_team, b_team, winner_suit, winner_cards, u_driving, user_won):
    """
    Route a Breaker winner through the same clean-win scoring logic.
    This ensures suit-based scoring is consistent whether you won via
    D66 or via Breaker.
    """
    return resolve_clean_win(u_team, b_team, winner_suit, winner_cards, u_driving, user_won)


def resolve_complication(u_team, b_team, u_driving):
    """
    D4 COMPLICATIONS (Dual-Split trigger).
    
    Per DOC Section 4:
    Logic: Lower Saving Throw ROLL (BASE ST + d6) = offender.
    
    [1] SACK   (Check SPD): possession FLIP + 2pts for sacker
    [2] OUT OF BOUNDS (Check CAT): Reset to NEUTRAL
    [3] PENALTY (Check STA): Personal Foul -> Field Goal +3pts
    [4] INTERCEPTION (Check KCK): possession FLIP + 1pt
    """
    
    comp_roll = roll_d4()
    
    # D4 -> complication type + which save stat to check
    COMPLICATIONS = {
        1: ('SACK',           'SPD', 2),   # +2 pts, flip
        2: ('OUT OF BOUNDS',  'CAT', 0),   # reset neutral
        3: ('PENALTY',        'STA', 3),   # +3 pts (field goal)
        4: ('INTERCEPTION',   'KCK', 1),   # +1 pt, flip
    }
    
    comp_type, save_key, pts = COMPLICATIONS[comp_roll]
    
    print(f"\n[!] COMPLICATION ROLLED: [{comp_roll}] {comp_type}!")
    print(f"    > {save_key} CHECK")
    time.sleep(1)
    
    # Determine offender: lower saving throw roll = offender
    u_save = u_team['save'][save_key] + u_team.get('save_boosts', {}).get(save_key, 0)
    b_save = b_team['save'][save_key] + b_team.get('save_boosts', {}).get(save_key, 0)
    
    u_roll = u_save + roll_d6()
    b_roll = b_save + roll_d6()
    
    print(f"    > {u_team['name']}: {u_save} + d6 = {u_roll}")
    print(f"    > {b_team['name']}: {b_save} + d6 = {b_roll}")
    time.sleep(1)
    
    user_is_offender = u_roll < b_roll
    # Tie on the save roll: driving team is offender (they committed the action)
    if u_roll == b_roll:
        user_is_offender = u_driving
    
    # --- RESOLVE BY COMPLICATION TYPE ---
    
    if comp_type == 'SACK':
        # SACK only lands on the DRIVING team
        if user_is_offender and u_driving:
            print(f"    >>> QG SACK! {b_team['name']} strips the ball! (+2 PTS). Possession flips!")
            time.sleep(2)
            return (0, 2, not u_driving, "SACK")
        elif not user_is_offender and not u_driving:
            print(f"    >>> QG SACK! {u_team['name']} strips the ball! (+2 PTS). Possession flips!")
            time.sleep(2)
            return (2, 0, not u_driving, "SACK")
        else:
            print(f"    >>> MISSED TACKLE! Sack attempt fails. Play continues.")
            time.sleep(2)
            return (0, 0, u_driving, "SACK MISSED")
    
    elif comp_type == 'OUT OF BOUNDS':
        print(f"    >>> Ball goes OUT OF BOUNDS! Play RESET to Neutral Snap Point.")
        time.sleep(2)
        return (0, 0, None, "OUT OF BOUNDS")  # None = neutral reset
    
    elif comp_type == 'PENALTY':
        if user_is_offender:
            print(f"    >>> PERSONAL FOUL! {u_team['name']} penalized! {b_team['name']} awarded Field Goal! (+3 PTS)")
            time.sleep(2)
            return (0, 3, None, "PENALTY FG")
        else:
            print(f"    >>> PERSONAL FOUL! {b_team['name']} penalized! {u_team['name']} awarded Field Goal! (+3 PTS)")
            time.sleep(2)
            return (3, 0, None, "PENALTY FG")
    
    elif comp_type == 'INTERCEPTION':
        # INT only lands on the DRIVING team
        if user_is_offender and u_driving:
            print(f"    >>> INTERCEPTED! {b_team['name']} picks it off! (+1 PT). Possession flips!")
            time.sleep(2)
            return (0, 1, not u_driving, "INT")
        elif not user_is_offender and not u_driving:
            print(f"    >>> INTERCEPTED! {u_team['name']} picks it off! (+1 PT). Possession flips!")
            time.sleep(2)
            return (1, 0, not u_driving, "INT")
        else:
            print(f"    >>> MISSED PICK! Offense holds the ball.")
            time.sleep(2)
            return (0, 0, u_driving, "INT MISSED")
    
    # Fallback (should never reach here)
    return (0, 0, u_driving, "COMPLICATION RESOLVED")


def resolve_jkr_moves(u_team, b_team, u_cards, b_cards, u_driving, u_has_jkr, b_has_jkr):
    """
    JKR Special Moves resolution.
    
    Per DOC Special Moves Table:
    - JKR + Clubs    = RUCK:       "Scrimmage. Immediately play goes stale."
                                   -> Routes to BREAKER (stale = stat resolution)
    - JKR + Hearts   = STIFF ARM:  "Force Move. Advance regardless of clash."
                                   -> Guaranteed TRY if driving (+5)
    - JKR + Spades   = PUNT:       "Ball strip becomes offensive punting!"
                                   -> Defensive possession grab (holder takes ball)
    - JKR + Diamonds = JUKE STEP:  "Perfect Ankle Breaker. Reached Endzone!"
                                   -> Guaranteed TRY if driving (+5)
    
    Solo JKR (no accompanying suit) = PLAYBOOK RECALL (not implemented BUILD 1)
    """
    
    print("\n>>> JOKER TRIGGERED! <<<")
    time.sleep(2)
    
    # Determine special moves from accompanying suits
    u_special = None
    b_special = None
    
    if u_has_jkr:
        u_suits = [c['suit'] for c in u_cards if c['suit'] not in ('JKR', 'JOKER')]
        if u_suits:
            u_special = {"C": "RUCK", "H": "STIFF_ARM", "S": "PUNT", "D": "JUKE"}.get(u_suits[0])
    
    if b_has_jkr:
        b_suits = [c['suit'] for c in b_cards if c['suit'] not in ('JKR', 'JOKER')]
        if b_suits:
            b_special = {"C": "RUCK", "H": "STIFF_ARM", "S": "PUNT", "D": "JUKE"}.get(b_suits[0])
    
    # BOTH teams play JKR -> clash, saving throw decides who activates
    if u_special and b_special:
        print("   JKR CLASH! Both teams activate special moves!")
        print("   Rolling SAVING THROWS to determine who activates...")
        time.sleep(2)
        
        u_roll = roll_d6() + sum(u_team['save'].values()) // 4
        b_roll = roll_d6() + sum(b_team['save'].values()) // 4
        
        print(f"   {u_team['name']}: {u_roll} | {b_team['name']}: {b_roll}")
        time.sleep(1)
        
        if u_roll > b_roll:
            print(f"   >>> {u_team['name']} SURVIVES! {u_special} activates!")
            time.sleep(2)
            return apply_special_move(u_team, b_team, u_cards, u_special, u_driving, user_activated=True)
        elif b_roll > u_roll:
            print(f"   >>> {b_team['name']} SURVIVES! {b_special} activates!")
            time.sleep(2)
            return apply_special_move(u_team, b_team, b_cards, b_special, u_driving, user_activated=False)
        else:
            print("   >>> JKR CLASH STALEMATE! Both moves cancel. RE-AUDIBLE!")
            time.sleep(2)
            return (0, 0, u_driving, "JKR CLASH TIE")
    
    # Only user plays JKR
    if u_special:
        return apply_special_move(u_team, b_team, u_cards, u_special, u_driving, user_activated=True)
    
    # Only bot plays JKR
    if b_special:
        return apply_special_move(u_team, b_team, b_cards, b_special, u_driving, user_activated=False)
    
    # Solo JKR(s) with no suit = PLAYBOOK RECALL
    print("   >>> JKR PLAYBOOK RECALL (signature plays - BUILD 2)")
    time.sleep(2)
    return (0, 0, u_driving, "JKR PLAYBOOK")


def apply_special_move(u_team, b_team, activator_cards, move_type, u_driving, user_activated):
    """
    Apply JKR special move effects.
    
    CORRECTED per DOC:
    - RUCK: play goes STALE -> route to Breaker
    - STIFF ARM: TRY if driving, fails if not
    - PUNT: ball strip -> possession grab (defender takes ball)
    - JUKE: TRY if driving, fails if not
    """
    
    activator = u_team if user_activated else b_team
    activator_is_driving = (user_activated and u_driving) or (not user_activated and not u_driving)
    
    if move_type == "RUCK":
        print(f"   > {activator['name']} plays RUCK! Scrimmage locks! Play goes STALE!")
        print(f"   > Immediate stoppage. Possession FLIPS!")
        time.sleep(3)
        return (0, 0, not u_driving, "RUCK")
    
    elif move_type == "STIFF_ARM":
        if activator_is_driving:
            print(f"   > {activator['name']} STIFF ARM! Shakes all tackles! UNSTOPPABLE!")
            print(f"   > TRY! (+5 PTS)")
            time.sleep(3)
            if user_activated:
                return (5, 0, not u_driving, "STIFF ARM TRY")
            else:
                return (0, 5, not u_driving, "STIFF ARM TRY (Bot)")
        else:
            print(f"   > {activator['name']} attempts STIFF ARM but isn't driving! Move fails.")
            time.sleep(2)
            return (0, 0, u_driving, "STIFF ARM FAILED")
    
    elif move_type == "PUNT":
        if not activator_is_driving:
            print(f"   > {activator['name']} PUNT! Ball stripped! Offensive punt launched!")
            print(f"   > Possession secured by {activator['name']}!")
            time.sleep(3)
            return (0, 0, not u_driving, "PUNT")
        else:
            print(f"   > {activator['name']} attempts PUNT but is already driving! Move fails.")
            time.sleep(2)
            return (0, 0, u_driving, "PUNT FAILED")
    
    elif move_type == "JUKE":
        if activator_is_driving:
            print(f"   > {activator['name']} JUKE STEP! ANKLES BROKEN!")
            print(f"   > Perfect route to the ENDZONE! TRY! (+5 PTS)")
            time.sleep(3)
            if user_activated:
                return (5, 0, not u_driving, "JUKE STEP TRY")
            else:
                return (0, 5, not u_driving, "JUKE STEP TRY (Bot)")
        else:
            print(f"   > {activator['name']} attempts JUKE but isn't driving! Move fails.")
            time.sleep(2)
            return (0, 0, u_driving, "JUKE FAILED")
    
    # Fallback
    return (0, 0, u_driving, "SPECIAL MOVE")
