"""
ROUGHBALL: Match Engine
Main match loop and user input handling
"""

import random
import time
from .teams import TEAMS, LEAGUES, ERAS, SYMBOLS, get_tier_name
from .cards import get_fresh_deck_dicts
from .display import clear, print_matrix, print_header, print_playbook_status
from .ai import smart_bot_logic, get_bot_hand_as_dicts
from .resolver import resolve_play


def run_match(u_id, b_id, league_key, era_id=4):
    """
    Main match loop
    
    YOUR FLOW PRESERVED:
    - Coin toss ceremony
    - Clear screen before each play
    - Print matrix
    - Bot prepares (hidden)
    - User input with timeout option
    - Reveal both plays
    - Resolve outcome
    - Mercy rule (25 points)
    
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
    
    # --- MAIN MATCH LOOP ---
    while u_score < 25 and b_score < 25:
        clear()
        print_matrix(u_team, b_team, u_score, b_score, league['name'],
                    u_driving, era_data['name'], u_name, b_name)
        
        # 1. BOT PREPARES (Hidden)
        b_val, b_suit, b_max, b_disp, b_special = smart_bot_logic(
            league['rank'], not u_driving, bot_deck)
        
        print(f"\n[REF]: {b_name} are preparing their audible playcall... (Deck: {len(bot_deck)})")
        
        # 2. USER INPUT WITH TIMEOUT
        print(f"[COACH]: Playcalling Limit is {league['rank']} cards")
        
        num_to_play = None
        while True:
            try:
                raw_in = input(f"[TACTICS]: Cards (1-{league['rank']}) or 'T' for Timeout ({u_timeouts} left): ").upper()
                
                # TIMEOUT LOGIC
                if raw_in == 'T':
                    if u_timeouts > 0:
                        u_timeouts -= 1
                        print(f"   >>> TIMEOUT CALLED! Deck Reshuffled. ({u_timeouts} Remaining)")
                        time.sleep(1.5)
                        continue  # Restart loop
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
        u_cards = []
        u_hand = []
        
        v_map = {'J': 11, 'Q': 12, 'K': 13, 'A': 14, 'JKR': 15}
        
        print(f"[INPUT]: CALLING {num_to_play} PLAY CARDS. (Format: 'D 13' or 'H K')")
        
        for i in range(num_to_play):
            raw = input(f"   Card #{i+1}: ").upper().split()
            
            if len(raw) < 2:
                s, v_raw = "C", "2"
            else:
                s, v_raw = raw[0], raw[1]
            
            # Value conversion
            try:
                v = int(v_raw)
            except ValueError:
                v = v_map.get(v_raw, 2)
            
            # Store as dict for resolver
            u_hand.append({"suit": s, "val": v})
            
            # Display formatting
            if v == 15 or s == "JKR":
                u_cards.append("[JKR]")
            else:
                disp_v = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}.get(v, v)
                u_cards.append(f"[{SYMBOLS.get(s, '?')} {disp_v}]")
        
        # 4. BOT FINALIZES HAND
        # Convert bot groups to card dicts
        groups = {"C": [], "H": [], "S": [], "D": [], "JKR": []}
        for _ in range(league['rank']):
            if bot_deck:
                c = bot_deck.pop(0)
                groups[c['suit']].append(c['val'])
        
        # Rebuild with best suit
        b_hand = []
        for val in groups.get(b_suit, []):
            b_hand.append({"suit": b_suit, "val": val})
        if b_special:
            b_hand.append({"suit": "JKR", "val": 15})
        
        # Ensure we have the right number
        while len(b_hand) < league['rank'] and b_hand:
            b_hand = b_hand[:league['rank']]
        
        # Use max card if hand is empty
        if not b_hand:
            b_hand = [{"suit": b_suit, "val": b_max}]
        
        # 5. THE REVEAL
        print(f"\n[REVEAL] {u_name} shows: {' '.join(u_cards)}")
        print(f"[REVEAL] {b_name} flips: {b_disp}")
        time.sleep(2)
        
        # 6. RESOLUTION
        u_pts, b_pts, new_driving, commentary = resolve_play(
            u_team, b_team, u_hand, b_hand, u_driving, league['rank'])
        
        # Update scores
        u_score += u_pts
        b_score += b_pts
        
        # Update possession
        if new_driving is None:
            # Reset to neutral (e.g., after Out of Bounds)
            # For BUILD 1, we'll just flip possession
            u_driving = not u_driving
        else:
            u_driving = new_driving
        
        # Log scoring plays
        if u_pts > 0 or b_pts > 0:
            log_entry = f"{u_name} {u_score} - {b_score} {b_name} | {commentary}"
            play_log.append(log_entry)
        
        # Pause before next play
        input("\n[PRESS ENTER] For next play...")
    
    # --- MATCH END ---
    clear()
    print_header("FINAL SCORE")
    print(f"   {u_name}: {u_score}")
    print(f"   {b_name}: {b_score}")
    print("=" * 60)
    
    if u_score > b_score:
        print(f"\n   >>> {u_name} WINS!")
    else:
        print(f"\n   >>> {b_name} WINS!")
    
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
