"""
ROUGHBALL: Match Engine
Main match loop and user input handling

CORRECTED:
- Bot hand no longer double-drawn. smart_bot_logic() already draws, groups, and recycles.
  The match loop now trusts its return values and constructs b_hand directly from them.
- JKR standalone input now properly handled (typing 'JKR' alone = suit JKR, val 15)
- Neutral possession reset (None) properly handled: possession stays with current driver
  (Out of Bounds / Penalty FG = reset, not a flip)
- Re-audible loop on FUMBLE now actually loops back for a new play

QoL v2:
- ESC key backdoor exit (returns to main menu)
- User dice input (you roll your own D66!)
"""

import random
import time
import sys
from .teams import TEAMS, LEAGUES, ERAS, SYMBOLS, get_tier_name
from .cards import get_fresh_deck_dicts
from .display import clear, print_matrix, print_header, print_playbook_status, check_escape, EscapeToMenu
from .ai import smart_bot_logic
from .resolver import resolve_play


def run_match(u_id, b_id, league_key, era_id=4):
    """
    Main match loop.
    
    Args:
        u_id: User team ID (string "1"-"16")
        b_id: Bot team ID (string "1"-"16")
        league_key: Division (string "1"-"5")
        era_id: Era ID (int 1-4)
    
    Returns:
        Tuple of (u_score, b_score)
    """
    
    u_team = TEAMS[u_id]
    b_team = TEAMS[b_id]
    league = LEAGUES[league_key]
    u_name = get_tier_name(u_team, league['rank'])
    b_name = get_tier_name(b_team, league['rank'])
    era_data = ERAS.get(era_id, {"name": "STANDARD", "desc": ""})
    
    # --- KICKOFF CEREMONY ---
    print_header("MATCH SETUP")
    print(f"\n[REFEREE]: Teams at center field for the toss...")
    time.sleep(2)
    
    u_call = random.choice(["Heads", "Tails"])
    toss_result = random.choice(["Heads", "Tails"])
    
    print(f"   > {u_name} calls {u_call}...")
    time.sleep(2)
    
    if u_call == toss_result:
        print(f"   >>> WIN! {toss_result} it is. {u_name} will DRIVE first!")
        u_driving = True
    else:
        print(f"   >>> LOSS! {toss_result} it is. {b_name} will DRIVE first!")
        u_driving = False
    
    input("\n[PRESS ENTER] To Kickoff...")
    
    # Initialize match state
    u_score = 0
    b_score = 0
    bot_deck = get_fresh_deck_dicts()
    u_timeouts = 2
    play_log = []
    
    print(f"\nMatch Start: {u_name} vs {b_name} (Rank {league['rank']})")
    print_playbook_status(u_team)
    time.sleep(2)
    
    # --- MAIN MATCH LOOP (with ESC backdoor) ---
    try:
        while u_score < 25 and b_score < 25:
            clear()
            print_matrix(u_team, b_team, u_score, b_score, league['name'],
                        u_driving, era_data['name'], u_name, b_name)
        
            # 1. BOT PREPARES (Hidden)
            # smart_bot_logic draws, analyzes, recycles internally.
            # Returns: (total_value, best_suit, max_card_value, display_string, special_move)
            b_val, b_suit, b_max, b_disp, b_special = smart_bot_logic(
                league['rank'], not u_driving, bot_deck)
        
            print(f"\n[REF]: {b_name} are preparing their audible playcall... (Deck: {len(bot_deck)})")
        
            # 2. USER INPUT WITH TIMEOUT
            print(f"[COACH]: Playcalling Limit is {league['rank']} cards")
        
            num_to_play = None
            while True:
                try:
                    raw_in = input(f"[TACTICS]: Cards (1-{league['rank']}) or 'T' for Timeout ({u_timeouts} left) or ESC: ").upper()
                    check_escape(raw_in)  # Check ESC
                
                    # TIMEOUT LOGIC
                    if raw_in == 'T':
                        if u_timeouts > 0:
                            u_timeouts -= 1
                            print(f"   >>> TIMEOUT CALLED! Deck Reshuffled. ({u_timeouts} Remaining)")
                            time.sleep(1.5)
                            # Re-run bot prep after timeout (deck state changed conceptually)
                            b_val, b_suit, b_max, b_disp, b_special = smart_bot_logic(
                                league['rank'], not u_driving, bot_deck)
                            continue
                        else:
                            print("   (!) No Timeouts Remaining!")
                            continue
                
                    num_to_play = int(raw_in)
                    if 1 <= num_to_play <= league['rank']:
                        break
                    print(f"(!) INVALID AMOUNT. Must be 1-{league['rank']}.")
                except ValueError:
                    print("(!) Enter a valid number or 'T'.")
        
            # 3. CARD INPUT
            u_cards_display = []   # For the reveal line
            u_hand = []            # For the resolver (list of dicts)
        
            v_map = {'J': 11, 'Q': 12, 'K': 13, 'A': 14, 'JKR': 15}
        
            print(f"[INPUT]: CALLING {num_to_play} PLAY CARDS. (Format: 'D 13' or 'H K' or 'JKR')")
        
            for i in range(num_to_play):
                raw = input(f"   Card #{i+1} or ESC: ").upper().split()
            
                # Check ESC on first token
                if raw and raw[0] in ('\x1b', 'ESC'):
                    raise EscapeToMenu()
            
                # --- PARSE INPUT ---
                # Handle these cases:
                #   "JKR"       -> solo joker
                #   "JKR 15"    -> also joker (explicit)
                #   "D 13"      -> Diamond King
                #   "H K"       -> Hearts King
                #   "C"         -> defaults to Clubs 2 (safety)
            
                if not raw:
                    # Empty input -> default
                    s, v = "C", 2
                elif raw[0] == 'JKR':
                    # Joker (with or without a value after it)
                    s, v = "JKR", 15
                elif len(raw) == 1:
                    # Single token that isn't JKR -> treat as suit, default value 2
                    s, v = raw[0], 2
                else:
                    # Two tokens: suit + value
                    s = raw[0]
                    v_raw = raw[1]
                
                    # If the value token is JKR, override to joker
                    if v_raw == 'JKR':
                        s, v = "JKR", 15
                    else:
                        try:
                            v = int(v_raw)
                        except ValueError:
                            v = v_map.get(v_raw, 2)
            
                # Normalize suit
                if s not in ('C', 'H', 'S', 'D', 'JKR'):
                    s = 'C'  # Safety fallback
            
                # Store for resolver
                u_hand.append({"suit": s, "val": v})
            
                # Display formatting
                if v == 15 or s == "JKR":
                    u_cards_display.append("[JKR]")
                else:
                    disp_v = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}.get(v, str(v))
                    u_cards_display.append(f"[{SYMBOLS.get(s, '?')} {disp_v}]")
        
            # 4. BUILD BOT HAND FOR RESOLVER
            # smart_bot_logic already determined b_suit, b_max, b_special.
            # Construct the hand dict list from those values.
            # The bot played cards of b_suit. If b_special exists, a JKR was in the hand.
            b_hand = []
        
            if b_special:
                # Bot has a JKR + suit cards. Add JKR first.
                b_hand.append({"suit": "JKR", "val": 15})
                # Add one card of the best suit at max value
                b_hand.append({"suit": b_suit, "val": b_max})
            else:
                # Standard hand: cards of b_suit. We know max value.
                # For simplicity, give bot one card at max value per slot.
                # (The resolver only needs suit + max for scoring checks)
                b_hand.append({"suit": b_suit, "val": b_max})
        
            # 5. THE REVEAL
            print(f"\n[REVEAL] {u_name} shows: {' '.join(u_cards_display)}")
            print(f"[REVEAL] {b_name} flips: {b_disp}")
            time.sleep(2)
        
            # 5.5. USER DICE INPUT (the tactile IRL experience!)
            u_dice = None
            if not any(c['val'] == 15 or c['suit'] == 'JKR' for c in u_hand):
                # Only ask for dice if no JKR (JKR bypasses D66)
                try:
                    print(f"\n[YOUR TURN] Roll your physical D66!")
                    d1_input = input("   Die 1 (1-6) or ESC: ")
                    check_escape(d1_input)
                    d2_input = input("   Die 2 (1-6) or ESC: ")
                    check_escape(d2_input)
                
                    d1 = int(d1_input)
                    d2 = int(d2_input)
                
                    if 1 <= d1 <= 6 and 1 <= d2 <= 6:
                        u_dice = (d1, d2)
                    else:
                        print("   (!) Invalid dice. Auto-rolling...")
                        u_dice = None
                except EscapeToMenu:
                    raise  # Re-raise ESC to outer handler
                except ValueError:
                    print("   (!) Invalid input. Auto-rolling...")
                    u_dice = None
        
            # 6. RESOLUTION
            u_pts, b_pts, new_driving, commentary = resolve_play(
                u_team, b_team, u_hand, b_hand, u_driving, league['rank'], u_dice)
        
            # Update scores
            u_score += u_pts
            b_score += b_pts
        
            # Update possession
            if new_driving is None:
                # NEUTRAL RESET: Out of Bounds or Penalty FG
                # Per DOC: "Reset play to NEUTRAL" = possession doesn't flip,
                # next play starts from neutral snap. Keep current driver.
                pass  # u_driving stays the same
            else:
                u_driving = new_driving
        
            # Log scoring plays
            if u_pts > 0 or b_pts > 0:
                log_entry = f"{u_name} {u_score} - {b_score} {b_name} | {commentary}"
                play_log.append(log_entry)
        
            # Check mercy rule before prompting
            if u_score >= 25 or b_score >= 25:
                break
        
            # Pause before next play
            cont = input("\n[PRESS ENTER] Next play or 'q' to quit: ")
            check_escape(cont)  # Check ESC on continue prompt too
            if cont.lower() == 'q':
                break
    
    except EscapeToMenu:
        print("\n[ESC] Returning to main menu...")
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
        print(f"\n   >>> IT'S A DRAW! (Rare in Roughball...)")
    
    # Show scoring summary
    if play_log:
        print("\n" + "=" * 60)
        print("   SCORING SUMMARY")
        print("=" * 60)
        for entry in play_log:
            print(f"   {entry}")
        print("=" * 60)
    
    input("\n[PRESS ENTER] To Continue...")
    
    return u_score, b_score
