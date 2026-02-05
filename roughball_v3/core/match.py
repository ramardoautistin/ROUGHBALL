"""
ROUGHBALL: Match Engine v10.3
Complete with kickoff system, ESC backdoor, and formation validation

v10.3 CRITICAL FIXES:
1. ESC works at EVERY input (using safe_input wrapper)
2. KICKOFF system (neutral play determines first driver)
3. Formation validation (enforces suit restrictions)
4. Neutral formation display (mirrored ASCII)
"""

import random
import time
from .teams import TEAMS, LEAGUES, ERAS, SYMBOLS, get_tier_name
from .cards import get_fresh_deck_dicts
from .display import clear, print_matrix, print_header, print_playbook_status, safe_input, EscapeToMenu
from .ai import smart_bot_logic, reshuffle_bot_deck
from .resolver import resolve_play
from .plays import get_hand_description
from .formations import validate_hand_formation, get_formation_help


def run_match(u_id, b_id, league_key, era_id=4):
    """
    Main match loop with kickoff, ESC backdoor, and formation rules
    """
    
    u_team = TEAMS[u_id]
    b_team = TEAMS[b_id]
    league = LEAGUES[league_key]
    u_name = get_tier_name(u_team, league['rank'])
    b_name = get_tier_name(b_team, league['rank'])
    era_data = ERAS.get(era_id, {"name": "STANDARD", "desc": ""})
    
    # --- KICKOFF CEREMONY ---
    print_header("MATCH SETUP")
    print(f"\n[REFEREE]: Teams line up for the KICKOFF...")
    print(f"   Both teams in NEUTRAL formation")
    time.sleep(2)
    
    safe_input("\n[PRESS ENTER] For Kickoff Play...")
    
    # Initialize match state
    u_score = 0
    b_score = 0
    bot_deck = get_fresh_deck_dicts()
    bot_discard = []  # Track used bot cards (prevents JKR duplication)
    u_timeouts = 2
    possession_state = "neutral"  # Start neutral for kickoff
    u_driving = None  # TBD after kickoff
    play_log = []
    is_kickoff = True
    
    print(f"\nMatch Start: {u_name} vs {b_name} (Rank {league['rank']})")
    print_playbook_status(u_team)
    time.sleep(2)
    
    # --- MAIN MATCH LOOP ---
    try:
        while u_score < 25 and b_score < 25:
            clear()
            
            # For kickoff, use neutral possession display
            if is_kickoff:
                print_matrix(u_team, b_team, u_score, b_score, league['name'],
                            False, era_data['name'], u_name, b_name, "neutral")
                print(f"\n[KICKOFF]: NEUTRAL formation - Winner drives first!")
            else:
                print_matrix(u_team, b_team, u_score, b_score, league['name'],
                            u_driving, era_data['name'], u_name, b_name, possession_state)
            
            # Show formation rules
            if is_kickoff:
                print(f"\n[FORMATION]: NEUTRAL - Mixed suits allowed")
            else:
                formation_help = get_formation_help(possession_state, u_driving)
                print(f"\n[FORMATION]: {formation_help}")
            
            # 1. BOT PREPARES
            b_val, b_suit, b_max, b_disp, b_special = smart_bot_logic(
                league['rank'], not u_driving if not is_kickoff else False, 
                bot_deck, possession_state, bot_discard)
            
            print(f"\n[REF]: {b_name} preparing audible... (Bot Deck: {len(bot_deck)} cards)")
            
            # 2. USER INPUT WITH TIMEOUT
            print(f"[COACH]: Playcalling Limit is {league['rank']} cards")
            
            num_to_play = None
            while True:
                try:
                    raw_in = safe_input(f"[TACTICS]: Cards (1-{league['rank']}) or 'T' for Timeout ({u_timeouts} left): ").upper()
                    
                    # TIMEOUT LOGIC
                    if raw_in == 'T':
                        if u_timeouts > 0:
                            u_timeouts -= 1
                            print(f"   >>> TIMEOUT CALLED! ({u_timeouts} Remaining)")
                            print(f"   >>> Both teams reshuffle their decks...")
                            reshuffle_bot_deck(bot_deck)
                            time.sleep(1.5)
                            b_val, b_suit, b_max, b_disp, b_special = smart_bot_logic(
                                league['rank'], not u_driving if not is_kickoff else False,
                                bot_deck, possession_state)
                            continue
                        else:
                            print("   (!) No Timeouts Remaining!")
                            continue
                    
                    num_to_play = int(raw_in)
                    if 1 <= num_to_play <= league['rank']:
                        break
                    print(f"(!) INVALID AMOUNT. Must be 1-{league['rank']}.")
                except ValueError:
                    print("(!) Enter a valid number or 'T' (or ESC to quit).")
            
            # 3. CARD INPUT WITH VALIDATION
            u_cards_display = []
            u_hand = []
            
            v_map = {'J': 11, 'Q': 12, 'K': 13, 'A': 14, 'JKR': 15}
            
            print(f"[INPUT]: CALLING {num_to_play} PLAY CARDS. (Format: 'D 13' or 'H K' or 'JKR')")
            
            for i in range(num_to_play):
                raw = safe_input(f"   Card #{i+1}: ").upper().split()
                
                if not raw:
                    s, v = "C", 2
                elif raw[0] == 'JKR':
                    s, v = "JKR", 15
                elif len(raw) == 1:
                    s, v = raw[0], 2
                else:
                    s = raw[0]
                    v_raw = raw[1]
                    
                    if v_raw == 'JKR':
                        s, v = "JKR", 15
                    else:
                        try:
                            v = int(v_raw)
                        except ValueError:
                            v = v_map.get(v_raw, 2)
                
                if s not in ('C', 'H', 'S', 'D', 'JKR'):
                    s = 'C'
                
                u_hand.append({"suit": s, "val": v})
                
                if v == 15 or s == "JKR":
                    u_cards_display.append("[JKR]")
                else:
                    disp_v = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}.get(v, str(v))
                    u_cards_display.append(f"[{SYMBOLS.get(s, '?')} {disp_v}]")
            
            # VALIDATE FORMATION RULES
            if not is_kickoff:
                is_valid, error_msg = validate_hand_formation(u_hand, possession_state, u_driving)
                if not is_valid:
                    print(f"\n   [!] ILLEGAL FORMATION!")
                    print(f"   [!] {error_msg}")
                    print(f"   [!] Please re-enter your cards...")
                    time.sleep(2)
                    continue  # Loop back to card input
            
            # 4. BUILD BOT HAND AND ADD TO DISCARD
            b_hand = []
            if b_special:
                b_hand.append({"suit": "JKR", "val": 15})
                b_hand.append({"suit": b_suit, "val": b_max})
            else:
                b_hand.append({"suit": b_suit, "val": b_max})
            
            # Add bot's played cards to discard pile (prevents JKR duplication)
            bot_discard.extend(b_hand)
            
            # 5. THE REVEAL (with play names!)
            if is_kickoff:
                u_play_desc = "KICKOFF PLAY"
                b_play_desc = "KICKOFF PLAY"
            else:
                u_play_desc = get_hand_description(u_hand, u_driving)
                b_play_desc = get_hand_description(b_hand, not u_driving)
            
            print(f"\n[REVEAL] {u_name} shows: {' '.join(u_cards_display)}")
            print(f"         Play: {u_play_desc}")
            print(f"[REVEAL] {b_name} flips: {b_disp}")
            print(f"         Play: {b_play_desc}")
            time.sleep(2)
            
            # 5.5. USER DICE INPUT
            u_dice = None
            if not any(c['val'] == 15 or c['suit'] == 'JKR' for c in u_hand):
                try:
                    print(f"\n[YOUR TURN] Roll your physical D66!")
                    d1_input = safe_input("   Die 1 (1-6): ")
                    d2_input = safe_input("   Die 2 (1-6): ")
                    
                    d1 = int(d1_input)
                    d2 = int(d2_input)
                    
                    if 1 <= d1 <= 6 and 1 <= d2 <= 6:
                        u_dice = (d1, d2)
                    else:
                        print("   (!) Invalid dice. Auto-rolling...")
                        u_dice = None
                except ValueError:
                    print("   (!) Invalid input. Auto-rolling...")
                    u_dice = None
            
            # 6. RESOLUTION
            u_pts, b_pts, new_driving, commentary = resolve_play(
                u_team, b_team, u_hand, b_hand,
                u_driving if not is_kickoff else True,  # Kickoff treats user as "driving"
                league['rank'], u_dice, possession_state)
            
            # KICKOFF SPECIAL LOGIC
            if is_kickoff:
                is_kickoff = False
                if u_pts > b_pts or (u_pts == b_pts and new_driving == False):
                    u_driving = True
                    print(f"\n>>> {u_name} wins the kickoff and will DRIVE!")
                elif b_pts > u_pts or (u_pts == b_pts and new_driving == True):
                    u_driving = False
                    print(f"\n>>> {b_name} wins the kickoff and will DRIVE!")
                else:
                    # Tie - user drives by default
                    u_driving = True
                    print(f"\n>>> Kickoff tied! {u_name} drives by default.")
                
                possession_state = "driving"
                time.sleep(2)
                continue  # Skip to next play
            
            # Handle RE-AUDIBLE (FUMBLE case)
            if commentary == "FUMBLE":
                print("\n>>> BOTH TEAMS FUMBLE! Ball is LIVE!")
                print(">>> RE-AUDIBLE: Enter ONE card, biggest wins!")
                
                u_reaud = handle_re_audible(u_team, u_name, u_driving)
                
                if len(bot_deck) < 1:
                    bot_deck[:] = get_fresh_deck_dicts()
                b_reaud = bot_deck.pop()
                
                print(f"\n[RE-AUDIBLE REVEAL]")
                print(f"   {u_name}: [{SYMBOLS.get(u_reaud['suit'], '?')} {u_reaud['val']}]")
                print(f"   {b_name}: [{SYMBOLS.get(b_reaud['suit'], '?')} {b_reaud['val']}]")
                time.sleep(2)
                
                if u_reaud['val'] > b_reaud['val']:
                    print(f"\n   >>> {u_name} RECOVERS THE BALL!")
                    u_pts, b_pts, new_driving, commentary = resolve_re_audible_win(
                        u_reaud, u_driving, True, u_name, b_name)
                elif b_reaud['val'] > u_reaud['val']:
                    print(f"\n   >>> {b_name} RECOVERS THE BALL!")
                    u_pts, b_pts, new_driving, commentary = resolve_re_audible_win(
                        b_reaud, not u_driving, False, u_name, b_name)
                else:
                    print(f"\n   >>> TIE! Ball goes to {u_name if u_driving else b_name} (current driver)")
                    new_driving = u_driving
                    u_pts, b_pts, commentary = 0, 0, "RE-AUDIBLE TIE"
                
                time.sleep(2)
            
            # Update scores
            u_score += u_pts
            b_score += b_pts
            
            # Update possession state
            if new_driving is None:
                # NEUTRAL RESET (OOB / Field Goal)
                possession_state = "neutral"
                print(f"\n>>> NEUTRAL FORMATION: Teams reset to snap point")
                time.sleep(1)
            else:
                u_driving = new_driving
                possession_state = "driving" if u_driving else "holding"
            
            # Enhanced scoring log
            if u_pts > 0 or b_pts > 0:
                u_cards_str = ' '.join(u_cards_display)
                log_entry = f"{u_name} {u_score}-{b_score} {b_name} | {u_cards_str} | {commentary}"
                play_log.append(log_entry)
            
            # Check mercy rule
            if u_score >= 25 or b_score >= 25:
                break
            
            # Continue prompt
            cont = safe_input("\n[PRESS ENTER] Next play or 'q' to quit: ")
            if cont.lower() == 'q':
                break
    
    except EscapeToMenu as e:
        print(f"\n[ESC] {e}")
        time.sleep(1)
        return u_score, b_score
    
    # --- MATCH END ---
    clear()
    print_header("FINAL SCORE")
    print(f"\n   {u_name}: {u_score}")
    print(f"   {b_name}: {b_score}")
    print("\n" + "=" * 60)
    
    if u_score > b_score:
        print(f"\n   >>> {u_name} WINS THE MATCH!")
    elif b_score > u_score:
        print(f"\n   >>> {b_name} WINS THE MATCH!")
    else:
        print(f"\n   >>> IT'S A DRAW!")
    
    # Enhanced scoring summary
    if play_log:
        print("\n" + "=" * 60)
        print("   SCORING SUMMARY")
        print("=" * 60)
        for entry in play_log:
            print(f"   {entry}")
        print("=" * 60)
    
    safe_input("\n[PRESS ENTER] To Continue...")
    
    return u_score, b_score


def handle_re_audible(team, team_name, is_driving):
    """Handle user re-audible input (single card)"""
    
    print(f"\n[{team_name} RE-AUDIBLE]: Enter ONE card!")
    
    v_map = {'J': 11, 'Q': 12, 'K': 13, 'A': 14, 'JKR': 15}
    
    while True:
        try:
            raw = safe_input("   Card (e.g. 'D 13' or 'JKR'): ").upper().split()
            
            if not raw:
                continue
            
            if raw[0] == 'JKR':
                return {"suit": "JKR", "val": 15}
            elif len(raw) == 1:
                return {"suit": raw[0], "val": 2}
            else:
                s = raw[0]
                v_raw = raw[1]
                
                if v_raw == 'JKR':
                    return {"suit": "JKR", "val": 15}
                
                try:
                    v = int(v_raw)
                except ValueError:
                    v = v_map.get(v_raw, 2)
                
                return {"suit": s, "val": v}
        
        except (ValueError, IndexError):
            print("   (!) Invalid input. Try again (or ESC to quit).")


def resolve_re_audible_win(winning_card, was_driving, user_won, u_name, b_name):
    """Resolve re-audible victory"""
    
    winner_name = u_name if user_won else b_name
    suit = winning_card['suit']
    val = winning_card['val']
    
    is_red = suit in ('H', 'D')
    
    if was_driving and is_red:
        if suit == 'D' and val == 13:
            print(f"   >>> {winner_name} FIELD GOAL on the recovery! (+3 PTS)")
            time.sleep(2)
            if user_won:
                return (3, 0, False, "RE-AUDIBLE FG")
            else:
                return (0, 3, True, "RE-AUDIBLE FG")
        else:
            print(f"   >>> {winner_name} REACHES ENDZONE on recovery! (+5 PTS)")
            time.sleep(2)
            if user_won:
                return (5, 0, False, "RE-AUDIBLE TRY")
            else:
                return (0, 5, True, "RE-AUDIBLE TRY")
    else:
        print(f"   >>> {winner_name} recovers, possession secured!")
        time.sleep(2)
        if user_won:
            return (0, 0, not was_driving, "RE-AUDIBLE RECOVERY")
        else:
            return (0, 0, was_driving, "RE-AUDIBLE RECOVERY")
