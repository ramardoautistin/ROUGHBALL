import random
import os
import time
import sys

# =======================================================
#           ROUGHBALL: DEFINITIVE EDITION 
# =======================================================

# --- THE ROUGHBALL DATABASE (EXPANSION ERA) ---
TEAMS = {
    "1": {
        "name": "Mountain LIONS", "stats": {'TKL': 8, 'AWR': 4, 'INT': 7, 'PAS': 6}, "loc": "Pike Brown", "region": "North", "is_founder": True,
        "tiers": {5: "Mountain LIONS", 4: "College Wildcats", 3: "High School Lynx", 2: "Backyard Cougars", 1: "Northern Rookies"}
    },
    "2": {
        "name": "Greenland VIKINGS", "stats": {'TKL': 6, 'AWR': 7, 'INT': 8, 'PAS': 4}, "loc": "Green Hills", "region": "North", "is_founder": True,
        "tiers": {5: "Greenland VIKINGS", 4: "College Celtics", 3: "High School Warriors", 2: "Backyard Maulers", 1: "Greenland Rookies"}
    },
    "3": {
        "name": "Southern FARMERS", "stats": {'TKL': 8, 'AWR': 7, 'INT': 6, 'PAS': 4}, "loc": "Great Countryside", "region": "South", "is_founder": True,
        "tiers": {5: "Southern FARMERS", 4: "College Cattle", 3: "High School Hillbillies", 2: "Backyard Rednecks", 1: "Great Rookies"}
    },
    "4": {
        "name": "Coast SHARKS", "stats": {'TKL': 7, 'AWR': 5, 'INT': 8, 'PAS': 5}, "loc": "Southern Coast", "region": "South", "is_founder": True,
        "tiers": {5: "Coast SHARKS", 4: "College Hammerheads", 3: "High School Gators", 2: "Backyard Marlins", 1: "Coastal Rookies"}
    },
    "5": {
        "name": "Eastern EAGLES", "stats": {'TKL': 5, 'AWR': 9, 'INT': 6, 'PAS': 5}, "loc": "Lake Brown", "region": "East", "is_founder": True,
        "tiers": {5: "Eastern EAGLES", 4: "College Crows", 3: "High School Ravens", 2: "Backyard Vultures", 1: "Brown Rookies"}
    },
    "6": {
        "name": "City PATRIOTS", "stats": {'TKL': 6, 'AWR': 5, 'INT': 5, 'PAS': 9}, "loc": "Eastern City", "region": "East", "is_founder": True,
        "tiers": {5: "City PATRIOTS", 4: "College Colonels", 3: "High School Admirals", 2: "Backyard Sentinels", 1: "City Rookies"}
    },
    "7": {
        "name": "Western BEARS", "stats": {'TKL': 7, 'AWR': 7, 'INT': 6, 'PAS': 5}, "loc": "Red Desert", "region": "West", "is_founder": True,
        "tiers": {5: "Western BEARS", 4: "College Bruins", 3: "High School Grizzlies", 2: "Backyard Cubs", 1: "Red Rookies"}
    },
    "8": {
        "name": "Beach PIRATES", "stats": {'TKL': 5, 'AWR': 8, 'INT': 6, 'PAS': 6}, "loc": "Western Beach", "region": "West", "is_founder": True,
        "tiers": {5: "Beach PIRATES", 4: "College Raiders", 3: "High School Bandits", 2: "Backyard Outlaws", 1: "Beach Rookies"}
    },
    "9": {
        "name": "Pike PANTHERS", "stats": {'TKL': 8, 'AWR': 5, 'INT': 7, 'PAS': 5}, "loc": "Pike Brown", "region": "North", "is_founder": False,
        "tiers": {5: "Pike PANTHERS", 4: "College Jaguars", 3: "High School Tigers", 2: "Backyard Bobcats", 1: "Pike Rookies"}
    },
    "10": {
        "name": "Greenland SAINTS", "stats": {'TKL': 7, 'AWR': 5, 'INT': 9, 'PAS': 4}, "loc": "Greenland Hills", "region": "North", "is_founder": False,
        "tiers": {5: "Greenland SAINTS", 4: "College Monks", 3: "High School Friars", 2: "Backyard Preachers", 1: "Hill Rookies"}
    },
    "11": {
        "name": "Countryside STALLIONS", "stats": {'TKL': 7, 'AWR': 8, 'INT': 6, 'PAS': 4}, "loc": "Great Countryside", "region": "South", "is_founder": False,
        "tiers": {5: "Countryside STALLIONS", 4: "College Mustangs", 3: "High School Broncos", 2: "Backyard Colts", 1: "Countryside Rookies"}
    },
    "12": {
        "name": "Southern STINGRAYS", "stats": {'TKL': 6, 'AWR': 5, 'INT': 8, 'PAS': 6}, "loc": "Southern Coast", "region": "South", "is_founder": False,
        "tiers": {5: "Southern STINGRAYS", 4: "College Dolphins", 3: "High School Seals", 2: "Backyard Squids", 1: "Southern Rookies"}
    },
    "13": {
        "name": "City ROYALS", "stats": {'TKL': 5, 'AWR': 5, 'INT': 6, 'PAS': 9}, "loc": "Eastern City", "region": "East", "is_founder": False,
        "tiers": {5: "City ROYALS", 4: "College Knights", 3: "High School Ambassadors", 2: "Backyard Legionnaires", 1: "Eastern Rookies"}
    },
    "14": {
        "name": "Eastern SEAHAWKS", "stats": {'TKL': 5, 'AWR': 9, 'INT': 6, 'PAS': 5}, "loc": "Lake Brown", "region": "East", "is_founder": False,
        "tiers": {5: "Eastern SEAHAWKS", 4: "College Pelicans", 3: "High School Skimmers", 2: "Backyard Talons", 1: "Lake Rookies"}
    },
    "15": {
        "name": "Desert SCORPIONS", "stats": {'TKL': 7, 'AWR': 6, 'INT': 5, 'PAS': 7}, "loc": "Red Desert", "region": "West", "is_founder": False,
        "tiers": {5: "Desert SCORPIONS", 4: "College Spiders", 3: "High School Stingers", 2: "Backyard Snakes", 1: "Desert Rookies"}
    },
    "16": {
        "name": "Beach SURGERS", "stats": {'TKL': 4, 'AWR': 7, 'INT': 6, 'PAS': 9}, "loc": "Western Beach", "region": "West", "is_founder": False,
        "tiers": {5: "Beach SURGERS", 4: "College Volts", 3: "High School Chargers", 2: "Backyard Hurricanes", 1: "Western Rookies"}
    }
}

# --- INITIALIZATION & ROGUELIKE PLAYBOOKS ---
for t in TEAMS:
    # Combat Stats
    TEAMS[t]['save'] = {'STA': TEAMS[t]['stats']['TKL'], 'SPD': TEAMS[t]['stats']['AWR'], 'KCK': TEAMS[t]['stats']['INT'], 'CAT': TEAMS[t]['stats']['PAS']}
    TEAMS[t]['boosts'] = {'TKL': 0, 'AWR': 0, 'INT': 0, 'PAS': 0}
    
    # Roguelike Progression Slots (The "Soul" of the team)
    TEAMS[t]['playbook'] = ["[EMPTY]"] * 5  # 5 Signature Play Slots
    TEAMS[t]['rivals'] = []                 # List of teams that beat us in Playoffs
    TEAMS[t]['prestige'] = 0                # Eras Survived

# --- [2] CONFIGURATION DICTIONARIES ---
LEAGUES = {
    "1": {"name": "D5 - Unranked Rookies", "rank": 1, "slots": 1},
    "2": {"name": "D4 - Backyard Amateurs", "rank": 2, "slots": 2},
    "3": {"name": "D3 - High School Pros", "rank": 3, "slots": 3},
    "4": {"name": "D2 - College Superstars", "rank": 4, "slots": 4},
    "5": {"name": "D1 - National Legends", "rank": 5, "slots": 5}
}

SUITS = {"C": "TKL", "H": "AWR", "S": "INT", "D": "PAS"}
SYMBOLS = {"C": "♣", "H": "♥", "S": "♠", "D": "♦", "JKR": "JKR"}
#SYMBOLS = {"C": "♧", "H": "♡", "S": "♤", "D": "◇", "JKR": "JKR"}
SAVING_MAP = {"1": "STA", "2": "CAT", "3": "KCK", "4": "SPD"} 

POSITIONS = {
    "DT": "Defensive Tackle (Scrimmager ♣)",
    "DE": "Defensive End (Scrimmager ♣)",
    "LB": "Linebacker (Scrimmager ♣)",
    "QG": "Quarter Guard (Field General ♥)",
    "RG": "Running Guard (Field General ♥)",
    "CB": "Cornerback (Pitch Guard ♠)",
    "OT": "Offensive Tackle (Pitch Guard ♠)",
    "SG": "Safety Guard ♠)",
    "WB": "Wide Back (Air Raider ♦)",
    "TB": "Tight Back (Air Raider ♦)"
}

WEEKLY_SCHEDULE = {
    "Mon": {"act": "MEDIA MONDAY",    "desc": "Public Image Management."},
    "Tue": {"act": "TRAINING TUESDAY", "desc": "PICK STAT BONUS (D4-1)."},
    "Wed": {"act": "STUDY WEDNESDAY",  "desc": "Film-Room Review."},
    "Thu": {"act": "BACKYARD THURSDAY",    "desc": "Amateur Scrimmage."},
    "Fri": {"act": "HIGH SCHOOL FRIDAY", "desc": "Prospects Match."},
    "Sat": {"act": "COLLEGE SATURDAY",     "desc": "Superstar Showdown."},
    "Sun": {"act": "NATIONAL SUNDAY",    "desc": "National Bad Blood."}
}

ERAS = {
    1: {"name": "OLD TIMEY", "desc": "Founding Era - Leather Helmets"},
    2: {"name": "GOLDEN AGE", "desc": "Broadcast Era - Iconic Figures"},
    3: {"name": "MILLENNIUM", "desc": "Corporate Era - Capital Expansion"},
    4: {"name": "PANDEMICAL", "desc": "Virtual Era - Streampocalypse"}
}

# --- [3] INITIALIZATION ---
for t in TEAMS:
    # Tie Saving Stats to Primary Stats (Design Doc Requirement)
    TEAMS[t]['save'] = {
        'STA': TEAMS[t]['stats']['TKL'], # Tackle -> Stamina
        'SPD': TEAMS[t]['stats']['AWR'], # Awareness -> Speed
        'KCK': TEAMS[t]['stats']['INT'], # Intercept -> Kick
        'CAT': TEAMS[t]['stats']['PAS']  # Pass -> Catch
    }
    TEAMS[t]['boosts'] = {'TKL': 0, 'AWR': 0, 'INT': 0, 'PAS': 0}

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def get_fresh_deck():
    deck = []
    for s in ["C", "H", "S", "D"]:
        for v in range(2, 15):
            deck.append({"val": v, "suit": s})
    deck.append({"val": 15, "suit": "JKR"})
    deck.append({"val": 15, "suit": "JKR"})
    random.shuffle(deck)
    return deck

def get_tier_name(team_data, rank):
    return team_data['tiers'].get(rank, team_data['name'])

# --- [4] RESOLUTION ENGINE ---
def resolve_complication(u_team, b_team, u_driving, u_name, b_name):
    d4 = random.randint(1, 4)
    stat_key = SAVING_MAP[str(d4)]
    primary_key = {"STA": "TKL", "SPD": "AWR", "KCK": "INT", "CAT": "PAS"}[stat_key]
    
    # Calc Rolls
    # Logic update to include Study Wednesday enhancements
    s_boost = u_team.get('save_boosts', {}).get(stat_key, 0)
    u_base = u_team['save'][stat_key] + u_team['boosts'].get(primary_key, 0) + s_boost
    b_base = b_team['save'][stat_key]
    u_roll = random.randint(1, 6) + u_base
    b_roll = random.randint(1, 6) + b_base
    
    # Detailed Flavor Text
    events = {
        1: ("SACK! (Loss of possession)", "(STA) CHECK", 2),
        2: ("OUT OF BOUNDS! (Reset play to NEUTRAL)", "(CAT) CHECK ", 0),
        3: ("PENALTY! (Personal Foul)", "(KCK) CHECK", 3),
        4: ("INTERCEPTION! (Possession Flip)", "(AWR) CHECK", 1)
    }
    name, check_desc, pts = events[d4]
    
    print(f"\n[!] COMPLICATION ROLLED: {name}")
    print(f"    > {check_desc}: {u_name} [{u_roll}] vs {b_name} [{b_roll}]")
    
    u_failed = u_roll < b_roll
    if u_failed: print(f"    > FAIL! {u_name} crumbles under pressure!")
    else: print(f"    > SAVE! {u_name} holds their ground!")

    flip_possession = False
    
    # Outcome Logic
    if d4 == 1: # SACK
        if u_driving: 
            if u_failed: print(f"    >>> QG SACK!(+2 PTS). Possession Flip!"); return True, 2, True
            else: print("    >>> ESCAPE! Field General sheds tackle. Play continues."); return False, 0, False
        else: # Defense committed sack
             if u_failed: print(f"    >>> MISSED TACKLE!. Offense gains ground."); return True, 0, False 
             else: print(f"    >>> QG SACK! (+2 PTS). Possession Flip!"); return False, 2, True
             #u_score += 2 

    elif d4 == 2: # OB
        print("    >>> Play RESET to Neutral Snap Point.")
        return False, 0, False 

    elif d4 == 3: # PENALTY
        if u_failed: print(f"    >>> PERSONAL FOUL! Opponent awarded Field Goal (+3 PTS)."); return True, 3, False
        else: print("    >>> DISCIPLINED! Rulebook enforced."); return False, 0, False

    elif d4 == 4: # INT
        if u_driving:
             if u_failed: print(f"    >>> INTERCEPTED! Turnover! (+1 Momentum PT)"); return True, 1, True
             else: print("    >>> FAILED PICK! Possession remains..."); return False, 0, False
        else:
             if not u_failed: print(f"    >>> PICKED OFF! (+1 PT)"); return False, 1, True
             else: print("    >>> MISSED PICK! Offense holds ball..."); return True, 0, False
             
    return False, 0, False

def print_matrix(u_team, b_team, u_score, b_score, league_name, u_driving, era_name, u_name, b_name):
    # THE ORIGINAL ASCII MAT RESTORED
    board = {"A4": "RB", "B5": "QB", "C1": "TE", "C8": "WR", "D3": "DE", "D4": "OT", "D5": "DT", "D6": "OG", "E3": "OG", "E4": "DT", "E5": "OT", "E6": "DE", "G4": "SG", "H1": "CB", "H5": "SG", "H8": "LB"}
    print(f"\nSCR: [{u_name}] {u_score} | [{b_name}] {b_score} | {league_name}")
    if era_name: print(f"ERA: {era_name} | SELECTED TEAM: {u_name}")
    print("\n      1   2   3   4   5   6   7   8")
    print(f"   |----------------------------------| ({b_name.upper()} Endzone)")
    for r in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        line = f"{r}  | "
        for c in range(1, 9):
            line += f" {board.get(f'{r}{c}', '.').ljust(2)} "
        suffix = ""
        if r == 'D': suffix = f" < {u_name.upper()} {'DRIVING' if u_driving else 'HOLDING'} ({u_team['loc']})"
        elif r == 'E': suffix = f" < {b_name.upper()} {'DRIVING' if not u_driving else 'HOLDING'} ({b_team['loc']})"
        print(line + " |" + suffix)
        if r == 'D': print(" xxxxxxxxxxxxxxxxxxxOxxxxxxxxxxxxxxxxxxx << NEUTRAL SNAP POINT >>")
    print(f"   |----------------------------------| ({u_name.upper()} Endzone)")

def smart_bot_logic(rank_val, bot_is_driving, bot_deck):
    # 1. Refill if empty (Safety Net)
    if len(bot_deck) < rank_val: 
        bot_deck[:] = get_fresh_deck()
    
    # 2. Draw Hand
    hand = [bot_deck.pop() for _ in range(rank_val)]
    
    # 3. Analyze Groups
    groups = {"C": [], "H": [], "S": [], "D": [], "JKR": []}
    hand_vals = []
    
    for c in hand:
        groups[c['suit']].append(c['val'])
        hand_vals.append(c['val'])
    
    # 4. Pick Best Suit
    # Logic: If driving, prefer Diamonds/Hearts (Offense). If Defending, Clubs/Spades.
    if bot_is_driving:
        priority = ["D", "H"]
        # Fallback if no offensive cards
        if not any(groups[s] for s in priority): priority = ["C", "S"]
    else:
        priority = ["C", "S"]
        if not any(groups[s] for s in priority): priority = ["D", "H"]
        
    best_suit = max(priority, key=lambda s: sum(groups[s]) if groups[s] else 0)
    
    # Fallback for empty hands (rare edge case)
    if not groups[best_suit] and "JKR" not in groups:
        best_suit = "C" # Default

    # 5. Identify Special Moves
    special = None
    if 15 in hand_vals:
        if bot_is_driving:
            if groups["D"]: special = "JUKE"
            elif groups["H"]: special = "STIFF_ARM"
        else:
            if groups["S"]: special = "STRIP"
            elif groups["C"]: special = "SCRUM"
    
    # --- FIX: RECYCLE UNUSED CARDS ---
    # We keep cards that match the Best Suit OR are Jokers (val 15)
    # Everything else goes back to the bottom of the deck to prevent burning out.
    unused_cards = [c for c in hand if c['suit'] != best_suit and c['val'] != 15]
    for card in unused_cards:
        bot_deck.insert(0, card) # Recycle to bottom of deck

    # Format Display
    display = "".join([f"[{SYMBOLS.get(best_suit, '?')} {v}] " for v in groups[best_suit]])
    if 15 in hand_vals: display += "[JKR] "
    time.sleep(2)
    
    return sum(groups[best_suit]), best_suit, max(groups[best_suit]+[0]), display, special

def run_match(u_id, b_id, league_key, era_id=None):
    u_team, b_team = TEAMS[u_id], TEAMS[b_id]
    league = LEAGUES[league_key]
    u_name = get_tier_name(u_team, league['rank'])
    b_name = get_tier_name(b_team, league['rank'])
    era_data = ERAS.get(era_id, {"name": "STANDARD"})
    
    # --- [RESTORED] THE KICKOFF CEREMONY (FORCED FATE) ---
    print(f"\n[REFEREE]: Teams at center field for the toss...")
    time.sleep(2)
    
    # Randomly assign Heads/Tails to the Home team (User)
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

    u_score, b_score = 0, 0
    bot_deck = get_fresh_deck()

    # --- [RESTORED] TIMEOUT TRACKER ---
    u_timeouts = 2
    
    print(f"\nMatch Start: {u_name} vs {b_name} (Rank {league['rank']})")
    # Show Roguelike Playbook Status
    pb = TEAMS[u_id].get('playbook', [])
    print(f"   [PLAYBOOK SLOTS]: {pb}")
    time.sleep(2)

    while u_score < 25 and b_score < 25:
        clear()
        print_matrix(u_team, b_team, u_score, b_score, league['name'], u_driving, era_data['name'], u_name, b_name)
        
        # 1. BOT PREPARES (HIDDEN)
        b_val, b_suit, b_max, b_disp, b_special = smart_bot_logic(league['rank'], not u_driving, bot_deck)
        print(f"\n[REF]: {b_name} are preparing their audible playcall... (Deck: {len(bot_deck)})")
        
        # 2. USER INPUT
        try:
            print(f"[COACH]: Playcalling Limit is {league['rank']} cards")
            
            # --- [RESTORED] TACTICS & TIMEOUT INPUT ---
            while True:
                try:
                    raw_in = input(f"[TACTICS]: Cards (1-{league['rank']}) or 'T' for Timeout ({u_timeouts} left): ").upper()
                    
                    # TIMEOUT LOGIC
                    if raw_in == 'T':
                        if u_timeouts > 0:
                            u_timeouts -= 1
                            print(f"   >>> TIMEOUT CALLED! Deck Reshuffled. ({u_timeouts} Remaining)")
                            time.sleep(1.5)
                            continue # Restart loop to let user pick new cards
                        else:
                            print("   (!) No Timeouts Remaining!")
                            continue
                            
                    num_to_play = int(raw_in)
                    if 1 <= num_to_play <= league['rank']:
                        break
                    print(f"(!) INVALID AMOUNT. Must be 1-{league['rank']}.")
                except ValueError:
                    print("(!) Enter a valid number or 'T'.")

            # 2. INITIALIZE THE GHOST VARIABLES
            u_val = 0
            u_suit = ""
            u_max = 0
            u_hand = []
            u_cards = [] 
            v_map = {'J':11, 'Q':12, 'K':13, 'A':14, 'JKR':15}
            u_special = False
            b_special = False
            u_played_jkr = False

            print(f"[INPUT]: CALLING {num_to_play} PLAY CARDS. (Format: 'D 13' or 'H K')")
            # 3. THE UNIFIED LOOP
            for i in range(num_to_play):
                raw = input(f"   Card #{i+1}: ").upper().split()
                if len(raw) < 2:
                    s, v_raw = "C", "2"
                else:
                    s, v_raw = raw[0], raw[1]

                # Value Conversion
                try:
                    v = int(v_raw); disp_v = v_raw
                except ValueError:
                    v = v_map.get(v_raw, 2); disp_v = v_raw

                # --- UI STORAGE / Visual Mapping for Reveal ---
                # If it is a Joker, we force a clean single tag
                if v == 15 or s == "JKR":
                    u_cards.append("[JKR]")
                else:
                    disp_v = {11:'J', 12:'Q', 13:'K', 14:'A'}.get(v, v)
                    u_cards.append(f"[{SYMBOLS.get(s, '?')} {disp_v}]")

                # --- MATH & RULES ---
                u_val += v 
                if i == 0: u_suit = s 
                if v > u_max: u_max = v 
                u_hand.append({'val': v, 'suit': s})
                
                # JKR Tracking
                if v == 15 or s == "JKR":
                    u_played_jkr = True
            
            # --- LOGIC: DETERMINE SPECIALS AFTER HAND IS FULL ---
            if u_played_jkr:
                # 1. Scan hand for a 'Driver' suit (ignoring the JKR itself)
                effective_suit = u_suit # Default to first card
                for c in u_hand:
                    if c['suit'] not in ["JKR", "JOKER", "None"]:
                        effective_suit = c['suit']
                        break
                
                # 2. Map Effective Suit to Special Move
                # If effective_suit is still "JKR" (Solo JKR), this returns None -> Triggers Playbook
                u_special = {"C":"SCRUM", "H":"STIFF_ARM", "S":"STRIP", "D":"JUKE"}.get(effective_suit)

            # =======================================================
            # BOT DRAW & ENGINE REVEAL (STATIC BLOCK)
            # =======================================================
            # --- THE SMART BOT BRIDGE ---
            b_val, b_suit, b_max, b_disp, b_special = smart_bot_logic(
                league['rank'], not u_driving, bot_deck)
            
            # Re-map for the Engine
            b_hand = [{'val': b_max, 'suit': b_suit}] 
            
            # 3. THE REVEAL (Simultaneous)
            print(f"\n[REVEAL] {u_name} shows: {' '.join(u_cards)}")
            print(f"[REVEAL] {b_name} flips: {b_disp}")
            time.sleep(2)
            
            # 4. JOKER RESOLUTION
            u_played_jkr = any("JKR" in str(c) for c in u_cards)
            
            if u_special or b_special or u_played_jkr:
                print("\n>>> JOKER TRIGGERED! <<<")
                
                # BRANCH A: ENFORCED SPECIAL MOVES (JKR + SUIT)
                if u_special:
                    if u_special == "JUKE" and u_driving: 
                        print(f"   > {u_name} hits a JUKE! Ankle breaker to ENDZONE! (+5 PTS)")
                        time.sleep(3)
                        u_score += 5; u_driving = False; continue
                    elif u_special == "STIFF_ARM" and u_driving:
                        print(f"   > {u_name} performs STIFF ARM! Shaken tackles... (+5 PTS)")
                        time.sleep(3)
                        u_score += 5; u_driving = False; continue
                    elif u_special == "STRIP" and not u_driving:
                        print(f"   > {u_name} BUTTER FINGERS! Fumble recovered! (+1 PT)")
                        time.sleep(3)
                        u_score += 1; u_driving = True; continue
                    elif u_special == "SCRUM":
                        print(f"   > SCRIMMAGE! Stalemate triggered. Possession Flips.")
                        time.sleep(3)
                        u_driving = not u_driving; continue
                
                # BRANCH B: SIGNATURE PLAYBOOK (SOLO JKR)
                elif u_played_jkr:
                    pb = u_team.get('playbook', [])
                    active_plays = [p for p in pb if p != "Empty Slot"]
                    
                    if not active_plays:
                        print(f"    [!] {u_name} draws a JKR but has no Signature Plays saved!")
                    else:
                        print(f"\n    --- {u_name} SIGNATURE PLAYBOOK ---")
                        for idx, play in enumerate(pb[:league['rank']]):
                            print(f"    [{idx+1}] {play}")
                        
                        sel = input(f"    > Call Signature (1-{league['rank']}) or 'N' to pass: ").upper()
                        if sel.isdigit() and 0 < int(sel) <= league['rank']:
                            selected = pb[int(sel)-1]
                            if selected != "Empty Slot":
                                print(f"    >>> {u_name} REVEALS SIGNATURE: {selected}!")
                                u_score += 7; u_driving = not u_driving; continue

                # Bot Jokers
                print(f"!!! BOT USES SPECIAL MOVE: {b_special} !!!")

                if b_special == "JUKE" and not u_driving:
                    print(f"   > {b_name} JUKED you! TRY! (+5 PTS)")
                    time.sleep(3)
                    b_score += 5; u_driving = True; continue
                elif b_special == "STIFF_ARM" and not u_driving:
                    print(f"{b_name} performs STIFF ARM! Shaken tackles... TRY! (+5 PTS)")
                    time.sleep(3)
                    b_score += 5; u_driving = True; continue
                elif b_special == "STRIP" and u_driving:
                    print(f"   > {b_name} PICKED OFF! Turnover! (+1 PT)")
                    time.sleep(3)
                    b_score += 1; u_driving = False; continue
                elif b_special == "SCRUM" and u_driving:
                    print(f"   > {b_name} SCRIMMAGE! Stalemate triggered. Possession Flips.")
                    time.sleep(3)
                    u_driving = not u_driving; continue
                time.sleep(3)
            
            # 5. HITS CALCULATION (D66 TWIN-DICE SYSTEM)
            print(f"\n[PHYSICS] Rolling D66 (Target: {league['rank']} or less)")
            
            # --- BOT ROLL (Twin Dice) ---
            b_d1 = random.randint(1, 6)
            b_d2 = random.randint(1, 6)
            b_hits = 0
            if b_d1 <= league['rank']: b_hits += 1
            if b_d2 <= league['rank']: b_hits += 1
            
            # --- USER ROLL (Twin Dice) ---
            try:
                u_d1 = int(input("   > Enter Die 1 Result: "))
                u_d2 = int(input("   > Enter Die 2 Result: "))
                u_hits = 0
                if u_d1 <= league['rank']: u_hits += 1
                if u_d2 <= league['rank']: u_hits += 1
            except ValueError:
                print("(!) Dice Error: Defaulting to 0 hits."); u_hits = 0
            print(f"   > {u_name}: {u_hits} HITS | {b_name}: {b_hits} HITS")
            
            
            # --- RESOLUTION (Matches your existing logic) ---
            if u_hits != b_hits:
                u_win = u_hits > b_hits
                # Determine the high card values for the Kick Pass check
                u_max = max(u_hand, key=lambda x: x['val'])['val']
                b_max = max(b_hand, key=lambda x: x['val'])['val']
                w_max = u_max if u_win else b_max
                winner = u_name if u_win else b_name
                w_suit = u_suit if u_win else b_suit
                print(f"   > WINNER: {winner} ({SYMBOLS.get(w_suit, '?')})")
                
                if (u_win and u_driving) or (not u_win and not u_driving):
                    # Offense Wins
                    pts = 0 
                    if w_suit == "D" and w_max == 13: 
                        pts = 3
                        print(f"KICK PASS! {winner} aim high at the GOAL POST for +3 PTS!")
                        time.sleep(2)
                    elif w_suit in ["D", "H"]:
                        pts = 5
                        print(f"TRY SUCCESSFUL! {winner} reaches the ENDZONE for +5 PTS!")
                        time.sleep(2)
                    else:
                        pts = 0                
                        print("   >>> DEFENSIVE STOPPAGE! No Points.")
                        u_driving = not u_driving
                    
                    if pts > 0:
                        if u_win: u_score += pts
                        else: b_score += pts
                        u_driving = not u_driving
                    time.sleep(2)

                else:
                    # Defense Wins 
                    print("   >>> DEFENSIVE STOPPAGE! No Points.")
                    u_driving = not u_driving

            else:
                # 6. TIE = COMPLICATION 
                print(f"\n>>>> STALEMATE! ({u_hits}-{b_hits}) <<<<")
                print(f"The line is locked. Do you call a RE-AUDIBLE?")
                
                choice = input("Spend 1 Card to Re-Audible? (y/n): ").lower()
                audible_success = False 
                
                if choice == 'y':
                    print(f"\n[RE-AUDIBLE]: Commit a new card to break the lock!")
                    # 1. INPUT THE RECALL CARD
                    raw_r = input("   [RECALL] Card (Suit + Val, e.g., 'H 10'): ").upper().split()
                    rs = raw_r[0] if len(raw_r) > 0 else "C"
            
                    # 2. MAP SUIT TO YOUR 4 SAVING THROW STATS
                    suit_to_save = {
                        'C': 'STA', 'S': 'SPD', 'D': 'KCK', 'H': 'CAT'
                    }
            
                    save_stat = suit_to_save.get(rs, 'STA')

                    # 3. GET THE MODIFIERS 
                    u_mod = u_team['stats'].get(save_stat, 0)
                    b_mod = b_team['stats'].get(save_stat, 0)
            
                    # 4. THE WEIGHTED D6 ROLL 
                    u_roll = random.randint(1, 6) + u_mod
                    b_roll = random.randint(1, 6) + b_mod
            
                    print(f"   [DICE]: {save_stat} SAVE! You: {u_roll} (Roll+{u_mod}) vs Bot: {b_roll} (Roll+{b_mod})")

                    # 5. RESOLUTION
                    if rs in ['C', 'S']: 
                        if u_roll >= b_roll:
                            print(f"> OPPONENT CRUSHED! {u_team['name']} secured the ball via {save_stat} Save.")
                            time.sleep(3)
                            u_driving = not u_driving
                            audible_success = True
                        else:
                            print(f"> ROUGHBALL STRIPPED! Turnover.")
                            time.sleep(3)
                            u_driving = not u_driving
                            audible_success = True

                    elif rs in ['H', 'D']: 
                        if u_roll > b_roll:
                            pts = 3 if rs == 'D' else 5 
                            u_score += pts
                            print(f"> CONVERSION! {u_team['name']} rolls the {save_stat} for +{pts} pt!")
                            time.sleep(3)
                            u_driving = not u_driving
                            audible_success = True
                        else:
                            print(f"> STOPPAGE! No points awarded, possession flips.")
                            time.sleep(3)
                            u_driving = not u_driving
                            audible_success = True

                    else:
                        print(" > STILL LOCKED. Exhaustion sets in...")
                
                # If Re-Audible fails or is declined
                if not audible_success:
                    print("   >>> NO BREAKTHROUGH. Triggering Saving Throw...")
                    u_fail, pts, flip = resolve_complication(u_team, b_team, u_driving, u_name, b_name)
                    
                    if u_fail: b_score += pts
                    else: u_score += pts
                        
                    if flip: u_driving = not u_driving

        except ValueError:
            print("(!) Input Error. Please enter 'Suit Value' (e.g. 'D 12')")
            time.sleep(2)
        
        if u_score >= 25 or b_score >= 25:
            print("\n==========================================")
            print(f" [MERCY RULE!] FINAL: {u_score} / {b_score} ")
            print("============================================")
            break
            
        if input("\n[PRESS ENTER] Next Play or 'q' to Quit: ") == 'q': break
    
    return u_score, b_score

# --- [5] DYNASTY ENGINE (COMMISSIONER MODE + WEEKLY FLAVOR) ---
def daily_activity_roll(day, team_id, tier_name):
    # TUESDAY: TRAINING MINI-GAME
    if day == "Tue":
        print(f"\n[TRAINING TUESDAY] Select Weekly Focus for {tier_name}:")
        print("   [1] Rush Tackle ♣    [2] Box Snaps ♥")
        print("   [3] Pursuit Tackle ♠ [4] Shuffle Catch ♦")
        
        c = input("   > Choice: ")
        stat = {"1": "TKL", "2": "AWR", "3": "INT", "4": "PAS"}.get(c, "TKL")
        
        # Risk Mechanic: Roll 1-4, subtract 1. Result is 0, 1, 2, or 3.
        boost = max(0, random.randint(1, 4) - 1)
        
        TEAMS[team_id]['boosts'] = {'TKL': 0, 'AWR': 0, 'INT': 0, 'PAS': 0} #reset
        TEAMS[team_id]['boosts'][stat] = boost
        
        if boost == 0:
            print(f"   > BAD PRACTICE: Players performance looked sluggish. ({stat} +0)")
        else:
            print(f"   > TRAINING DRILLS: Provided {stat} +{boost} STAT BONUS for this week.")
        time.sleep(2)
        return

# MONDAY & WEDNESDAY: MECHANICAL TABLES
    d4 = random.randint(1, 4)
    penalty_bonus = max(0, random.randint(1, 4) - 1) # The D4-1 Formula
    
    if day == "Mon":
        acts = {1: "Press Conference", 2: "Radio Interview", 3: "Live Show", 4: "Written Article"}
        # Map d4 to the suit/stat being penalized
        stat_map = {1: "TKL", 2: "AWR", 3: "INT", 4: "PAS"}
        target_stat = stat_map[d4]
        
        # Apply negative boost
        TEAMS[team_id]['boosts'][target_stat] = -penalty_bonus
        
        print(f"   > [MEDIA ACTIVITY]: {acts[d4]}")
        print(f"   > Media Critics remarks provided STAT PENALTY to: {target_stat} -{penalty_bonus} for the week")
        
    elif day == "Wed":
        acts = {1: "Blackboard Lecture", 2: "Film Review", 3: "Playbook Calls", 4: "Rivalry Sim"}
        # Map d4 to the Saving Throw being enhanced
        save_map = {1: "STA", 2: "SPD", 3: "KCK", 4: "CAT"}
        target_save = save_map[d4]
        
        # Initialize and Apply Saving Throw Bonus
        if 'save_boosts' not in TEAMS[team_id]:
            TEAMS[team_id]['save_boosts'] = {'STA': 0, 'SPD': 0, 'KCK': 0, 'CAT': 0}
        
        # Reset and Apply
        TEAMS[team_id]['save_boosts'] = {'STA': 0, 'SPD': 0, 'KCK': 0, 'CAT': 0}
        TEAMS[team_id]['save_boosts'][target_save] = penalty_bonus
        
        print(f"   > [STUDY SESSION]: {acts[d4]}")
        print(f"   > Technical FOCUS provided SAVING THROW BONUS: {target_save} +{penalty_bonus} for the week")
    
    time.sleep(2)

# --- LEAGUE MANAGEMENT (UPDATED: Side Selection) ---
def manage_slate(league_key, matchups, my_team_id, era_id):
    print(f"\n   --- {LEAGUES[league_key]['name']} SLATE ---")
    active_games = [m for m in matchups if m[0] != my_team_id and m[1] != my_team_id]
    
    for idx, (a,b) in enumerate(active_games):
         n1 = get_tier_name(TEAMS[a], LEAGUES[league_key]['rank'])
         n2 = get_tier_name(TEAMS[b], LEAGUES[league_key]['rank'])
         print(f"   {idx+1}. {n1} vs {n2}")
    
    sel = input("   > Enter Game # to Play/Manage (or Enter to Return): ")
    if sel.isdigit() and 0 < int(sel) <= len(active_games):
        g_a, g_b = active_games[int(sel)-1]
        
        # [NEW LOGIC] Select Side
        n_home = TEAMS[g_a]['name']
        n_away = TEAMS[g_b]['name']
        print(f"\n   > MATCHUP: {n_home} [Home] vs {n_away} [Away]")
        side = input(f"   > Play as [H]ome or [A]way? ").upper()
        
        print(f"   > TAKING CONTROL...")
        time.sleep(2)
        
        # If user picks Away, we swap the order so (User, Bot) becomes (g_b, g_a)
        if side == 'A':
            run_match(g_b, g_a, league_key, era_id)
        else:
            run_match(g_a, g_b, league_key, era_id)

# --- DRAFT DAY MECHANIC ---
def run_draft_day(team_id):
    clear()
    team_name = TEAMS[team_id]['name']
    print(f"\n==========================================")
    print(f"   DRAFT DAY: {team_name} (OFF-SEASON)   ")
    print(f"==========================================")
    
    # Reset Boosts for the new season
    TEAMS[team_id]['boosts'] = {'TKL': 0, 'AWR': 0, 'INT': 0, 'PAS': 0}
    
    for i in range(1, 5):
        input(f"\n[DRAFT CLOCK]: Press Enter to draft Slot #{i}...")
        
        # RNG Generation
        suit = random.choice(["C", "H", "S", "D"])
        coin = random.choice(["H", "T"])
        stars = max(1, random.randint(1, 6) - 1) # Ensure at least +1 star
        is_jkr = random.randint(1, 100) > 95 # 5% Chance of a "Generational Talent" (Joker)
        
        # Determine Position Title
        if is_jkr: 
            pos_title = POSITIONS[suit]['spec'] + " [GENERATIONAL]"
            stars += 2 # Bonus stats for Joker recruits
        else: 
            pos_title = POSITIONS[suit][coin]
        
        stat_key = POSITIONS[suit]['stat']
        
        # Apply Permanent Stat Growth
        TEAMS[team_id]['stats'][stat_key] += stars
        
        print(f">> DRAFTED: {pos_title} ({SYMBOLS[suit]})")
        print(f"   scouting report: +{stars} to {stat_key}")
        time.sleep(2)
        
    print("\n[COMMISSIONER]: Draft Complete. Roster updated for the next Era.")
    TEAMS[team_id]['prestige'] += 1 # Era progression
    time.sleep(4)

# --- THE GLADIATOR SCHEDULE ---
def run_dynasty():
    clear()
    print("--- ROUGHBALL DYNASTY MODE [FRANCHISE MANAGER] ---")
    print("Select Era: ")
    # Era Selection
    for k, v in ERAS.items(): print(f"[{k}] {v['name']} - {v['desc']}")
    era_id = int(input("Your Choice: "))
    #try:
    #    era_id = int(input("Select Era: "))
    #except:
    #    era_id = 1 

    #print("\n[SELECT DIVISION]")
    #for k, v in LEAGUES.items(): print(f"[{k}] {v['name']}")
    #league_key = input("Division Choice: ")
    
    # Team Selection
    print("\nSelect Your Franchise ID (1-16):")
    for k, v in TEAMS.items(): 
        if int(k) <= 16: print(f"[{k}] {v['name']}")
    my_team_id = input("Team ID: ")
    if my_team_id not in TEAMS: my_team_id = "1"
    my_team = TEAMS[my_team_id]
    
    # Bracket Logic
    bracket_pairs = [("1","2"), ("9","10"), ("3","4"), ("11","12"), ("5","6"), ("13","14"), ("7","8"), ("15","16")]
    
    # THE GLADIATOR LOOP
    for w in range(1, 13):
        clear()
        franchise_name = my_team['name']
        # --- PHASE DETERMINATION ---
        phase_title = ""
        if w <= 3: phase_title = "LINEAGE QUALIFIERS (PRE-SEASON)"
        elif w <= 6: phase_title = "CARDINAL CARNAGE (REG-SEASON)"
        elif w <= 9: phase_title = "BLOOD DISQUALIFIERS (PLAY-OFFS)"
        elif w <= 11: phase_title = "ROUGHBALL WILDCARD (OFF-SEASON)"
        else: phase_title = "WEEK 12: BAD-BLOOD GAUNTLET (CHAMPIONSHIP GAME)"
                
        print(f"============================================================")
        print(f" SUCCESSFULLY REACHED: {phase_title}")
        print(f" WEEK {w} / 12 | ERA: {ERAS.get(era_id, {'name':'Unknown'})['name']} | TEAM: {franchise_name}")
        print(f"============================================================")
        
        # Find My Opponent (Logic: Swaps based on Phase)
        # Note: In a full sim, this would dynamically update. 
        # For Solo Play, we default to the Bracket Pair to keep the "Founder vs Expansion" narrative alive.
        my_opp = "2"
        for a, b in bracket_pairs:
            if a == my_team_id: my_opp = b
            elif b == my_team_id: my_opp = a
        opp_team = TEAMS[my_opp]
        
        # DAILY SCHEDULE LOOP (With Flavor & League Mgmt)
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for day in days:
            day_title = WEEKLY_SCHEDULE[day].get('title', WEEKLY_SCHEDULE[day].get('act', 'Activity'))
            print(f"\n>>> TODAY IS: {day_title}")
            
            # Activity Roll (Mon-Wed)
            if day in ["Mon", "Tue", "Wed"]:
                daily_activity_roll(day, my_team_id, my_team['name'])
            
            # Game Days (Thu-Sun)
            day_map = {"Thu": "2", "Fri": "3", "Sat": "4", "Sun": "5"}
            
            if day in day_map:
                l_key = day_map[day]
                # Dynamic Tier Naming based on Phase
                t_name = get_tier_name(my_team, LEAGUES[l_key]['rank'])
                o_name = get_tier_name(opp_team, LEAGUES[l_key]['rank'])
                
                print(f"[{LEAGUES[l_key]['name']}] {t_name} vs {o_name}")
                print("   [P]lay Franchise Game")
                print("   [S]imulate Franchise Game")
                print("   [M]anage League Slate (Commissioner Mode)")
                
                ch = input("   > Choice: ").upper()

                if ch == 'P':
                    # Play the match
                    us, bs = run_match(my_team_id, my_opp, l_key, era_id)
                    # --- ADD THIS: Record User or Bot Win ---
                    if us > bs:
                        TEAMS[my_team_id]['wins'] = TEAMS[my_team_id].get('wins', 0) + 1
                    else:
                        TEAMS[my_opp]['wins'] = TEAMS[my_opp].get('wins', 0) + 1
                        
                elif ch == 'S':
                    u_sim, b_sim = random.randint(0,25), random.randint(0,25)
                    print(f"   > Simulation Result: {t_name} {u_sim} - {b_sim} {o_name}")
                    # --- ADD THIS: Record Sim Win ---
                    if u_sim > b_sim:
                        TEAMS[my_team_id]['wins'] = TEAMS[my_team_id].get('wins', 0) + 1
                    else:
                        TEAMS[my_opp]['wins'] = TEAMS[my_opp].get('wins', 0) + 1 

        # END OF SEASON TRIGGER
        if w == 12:
            print("\n>>> THE SEASON HAS ENDED. THE OFF-SEASON BEGINS.")
            print("    (Calculating Retirements and Draft Order...)")
            time.sleep(2)
            input("[PRESS ENTER] TO BEGIN DRAFT DAY...")
            run_draft_day(my_team_id)
            break 
            
        if input("\n(End of Week) Continue to next week? (y/n): ").lower() == 'n': break

def run_mock_draft():
    clear()
    print("===========================================")
    print("   LEAGUE SCOUTING REPORT: MOCK DRAFT     ")
    print("===========================================")
    
    # 1. Team Exclusion
    print("Select YOUR Team ID to exclude (1-16):")
    u_sel = input("> ")
    deck = get_fresh_deck() 
    
    # 2. Rank Logic: Table stays 1-16, but Teams are Shuffled
    shuffled_ids = list(TEAMS.keys())
    random.shuffle(shuffled_ids)
    # Standings Logic: Sort by Wins (Ascending = Worst teams first / Wins = 0 Shuffles as lottery)
    #all_ids = list(TEAMS.keys())
    #random.shuffle(all_ids) # Randomize ties
    #draft_order = sorted(all_ids, key=lambda x: TEAMS[x].get('wins', 0))
    
    print(f"\n[SCOUTING]: Simulating 15 franchises. Team {u_sel} is EXCLUDED.")
    print("-" * 85)
    print(f"{'RANK':<5} | {'ID':<3} | {'FRANCHISE NAME':<18} | {'STATUS':<8} | {'PICKS'}")
    print("-" * 85)

    finalists_assigned = 0

    for rank, t_id in enumerate(shuffled_ids, 1):
        if t_id == u_sel:
            print(f"{rank:<5} | {t_id:<3} | {TEAMS[t_id]['name'].ljust(18)} | [USER]   | (Physical Draw)")
            continue
        
        # 3. Deck Math: 4 Finalists (2 picks), 11 Rebuild (4 picks)
        if finalists_assigned < 4:
            num_picks = 2; status = "FINALIST"
            finalists_assigned += 1
        else:
            num_picks = 4; status = "REBUILD"
        
        picks = []
        for _ in range(num_picks):
            if not deck: break
            c = deck.pop()
            
            # --- THE FIX: Define 'suit_letter' clearly for logic vs display ---
            suit_letter = c['suit']
            is_jkr = (c['val'] == 15 or suit_letter == "JKR")
            
            # 4. POSITIONAL MAP (RESTORED EXACTLY)
            coin = random.choice([1, 2])
            pos_map = {
                "C": {1: "DT", 2: "DE", "JKR": "LB"},
                "H": {1: "QG", 2: "RG", "JKR": "SG"},
                "S": {1: "OT", 2: "OG", "JKR": "CB"},
                "D": {1: "WR", 2: "TB", "JKR": "SG"}
            }
            
            if is_jkr:
                # Joker pulls specialty from a random suit letter
                j_suit_letter = random.choice(["C", "H", "S", "D"])
                pos_title = f"{pos_map[j_suit_letter]['JKR']}[JKR]"
                pick_suit_icon = SYMBOLS[j_suit_letter] # Use symbols for display
            else:
                # Standard lookup using the card's suit letter
                pos_title = pos_map.get(suit_letter, pos_map["D"])[coin]
                pick_suit_icon = SYMBOLS.get(suit_letter, "?")

            # 5. D6-1 Star Quality
            stars = max(0, random.randint(1, 6) - 1)
            star_rating = "*" * stars if stars > 0 else "BUST"
            
            # FORMAT: SUIT POS (QUA)
            picks.append(f"{pick_suit_icon} {pos_title}({star_rating})")
        
        t_name = TEAMS[t_id]['name']
        print(f"{rank:<5} | {t_id:<3} | {t_name.ljust(18)} | {status.ljust(8)} | {' | '.join(picks)}")

    input("\n[PRESS ENTER] To Return to Menu...")

def main():
    while True:
        clear()
        print("===========================================")
        print("   ROUGHBALL: END-GAME SIMULATOR v10.0     ")
        print("===========================================")
        print("[1] QUICK MATCH (Original Simulator)")
        print("[2] DYNASTY MODE (Gladiator Schedule)")
        print("[3] MOCK DRAFT (Scouting Manager)")
        print("[4] EXIT BIG LEAGUES... ")
        
        choice = input("\nSelect Mode: ")
        
        if choice == '1':
            hid = input("Home Team ID (1-16): ")
            aid = input("Away Team ID (1-16): ")
            lid = input("League Level (1-5): ")
            run_match(hid, aid, lid, 1)
        elif choice == '2':
            run_dynasty()
        elif choice == '3':
            run_mock_draft()
        elif choice == '4' or choice.lower() == 'q':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid Option.")
            time.sleep(1)

if __name__ == "__main__": main()










