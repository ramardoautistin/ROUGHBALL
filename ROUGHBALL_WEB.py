import streamlit as st
import random
import time
import os

# =======================================================
#           ROUGHBALL: DEFINITIVE WEB EDITION
#             (Source: ROUGHBALL_DEFINITIVE.py)
# =======================================================

st.set_page_config(page_title="ROUGHBALL DEFINITIVE", layout="wide")

# --- [1] THE ROUGHBALL DATABASE (FULL 16 TEAMS) ---
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

# --- [2] CONFIGURATION DICTIONARIES ---
LEAGUES = {
    "1": {"name": "D5 - Unranked Rookies", "rank": 1, "slots": 1},
    "2": {"name": "D4 - Backyard Amateurs", "rank": 2, "slots": 2},
    "3": {"name": "D3 - High School Pros", "rank": 3, "slots": 3},
    "4": {"name": "D2 - College Superstars", "rank": 4, "slots": 4},
    "5": {"name": "D1 - National Legends", "rank": 5, "slots": 5}
}

SYMBOLS = {"C": "♣", "H": "♥", "S": "♠", "D": "♦", "JKR": "★"}
SAVING_MAP = {"1": "STA", "2": "CAT", "3": "KCK", "4": "SPD"} 

# --- [3] UTILS ---
def get_fresh_deck():
    suits = ['C', 'H', 'S', 'D']
    # Range 2-14 (A) + 15 (JKR)
    deck = [{'val': r, 'suit': s} for s in suits for r in range(2, 15)]
    deck.append({'val': 15, 'suit': 'JKR'})
    deck.append({'val': 15, 'suit': 'JKR'})
    random.shuffle(deck)
    return deck

def get_tier_name(team_data, rank):
    # This logic pulls the specific Tier Name (e.g. "College Wildcats") based on League
    return team_data['tiers'].get(rank, team_data['name'])

# --- [4] SESSION STATE ---
if 'game_state' not in st.session_state:
    # Initialize STATS derived from TEAMS (The "Design Doc Requirement")
    for t in TEAMS:
        TEAMS[t]['save'] = {
            'STA': TEAMS[t]['stats']['TKL'],
            'SPD': TEAMS[t]['stats']['AWR'],
            'KCK': TEAMS[t]['stats']['INT'],
            'CAT': TEAMS[t]['stats']['PAS']
        }
        TEAMS[t]['boosts'] = {'TKL': 0, 'AWR': 0, 'INT': 0, 'PAS': 0}
        TEAMS[t]['playbook'] = ["[EMPTY]"] * 5
    
    st.session_state.game_state = 'MENU'
    st.session_state.match_data = {}

# --- [5] SMART BOT LOGIC (RECYCLING ENABLED) ---
def smart_bot_logic(rank_val, bot_is_driving, bot_deck):
    # 1. Refill
    if len(bot_deck) < rank_val: 
        bot_deck[:] = get_fresh_deck()
    
    # 2. Draw
    hand = [bot_deck.pop() for _ in range(rank_val)]
    
    # 3. Analyze
    groups = {"C": [], "H": [], "S": [], "D": [], "JKR": []}
    hand_vals = []
    
    for c in hand:
        groups[c['suit']].append(c['val'])
        hand_vals.append(c['val'])
    
    # 4. Pick Best
    if bot_is_driving:
        priority = ["D", "H"]
        if not any(groups[s] for s in priority): priority = ["C", "S"]
    else:
        priority = ["C", "S"]
        if not any(groups[s] for s in priority): priority = ["D", "H"]
        
    best_suit = max(priority, key=lambda s: sum(groups[s]) if groups[s] else 0)
    if not groups[best_suit] and "JKR" not in groups: best_suit = "C"

    # 5. Specials
    special = None
    if 15 in hand_vals:
        if bot_is_driving:
            if groups["D"]: special = "JUKE"
            elif groups["H"]: special = "STIFF_ARM"
        else:
            if groups["S"]: special = "STRIP"
            elif groups["C"]: special = "SCRUM"
    
    # --- RECYCLE ---
    unused_cards = [c for c in hand if c['suit'] != best_suit and c['val'] != 15]
    for card in unused_cards:
        bot_deck.insert(0, card)

    display = "".join([f"[{SYMBOLS.get(best_suit, '?')} {v}] " for v in groups[best_suit]])
    if 15 in hand_vals: display += "[JKR] "
    
    return sum(groups[best_suit]), best_suit, max(groups[best_suit]+[0]), display, special

# --- [6] COMPLICATION RESOLVER (THE DEFINITIVE VERSION) ---
def resolve_complication_web(u_team, b_team, u_driving, u_name, b_name):
    # Based on the DEFINITIVE.py logic
    d4 = random.randint(1, 4)
    stat_key = SAVING_MAP[str(d4)]
    
    # Map back to Primary Stats for display
    # STA->TKL, SPD->AWR, KCK->INT, CAT->PAS
    
    st.markdown(f"**[!] COMPLICATION ROLLED (D4):** {d4}")
    
    # Stats from team dictionary
    u_base = u_team['save'][stat_key]
    b_base = b_team['save'][stat_key]
    
    u_roll = random.randint(1, 6) + u_base
    b_roll = random.randint(1, 6) + b_base
    
    user_failed = u_roll < b_roll
    points = 0
    flip_turnover = False
    
    # Specific Events from your file
    if d4 == 1: # SACK (STA Check)
        st.write(f"   > **SACK! (Loss of possession)** - (STA) CHECK")
        st.write(f"   > {u_name} [{u_roll}] vs {b_name} [{b_roll}]")
        if u_driving:
            if user_failed:
                st.error(f"   >>> QG SACKED! (+2 PTS). Possession Flip!")
                points = 2; flip_turnover = True
            else:
                st.success("   >>> ESCAPE! Field General sheds tackle. Play continues.")
        else:
            # User is Defense
            if user_failed: # User Defense failed to sack
                 st.error("   >>> MISSED TACKLE! Offense gains ground.")
            else:
                 st.success("   >>> QG SACKED! (+2 PTS). Possession Flip!")
                 points = 2; flip_turnover = True

    elif d4 == 2: # OUT OF BOUNDS (CAT Check)
        st.write(f"   > **OUT OF BOUNDS!** - (CAT) CHECK")
        st.info("   >>> Play RESET to Neutral Snap Point.")
        # No points, just reset context usually, but here we just continue

    elif d4 == 3: # PENALTY (KCK Check - Discipline)
        st.write(f"   > **PENALTY! (Personal Foul)** - (KCK) CHECK")
        st.write(f"   > {u_name} [{u_roll}] vs {b_name} [{b_roll}]")
        if user_failed:
             st.error("   >>> PERSONAL FOUL! Opponent awarded Field Goal (+3 PTS).")
             points = 3
        else:
             st.success("   >>> DISCIPLINED! Rulebook enforced.")

    elif d4 == 4: # INTERCEPTION (AWR Check)
        st.write(f"   > **INTERCEPTION! (Possession Flip)** - (AWR) CHECK")
        st.write(f"   > {u_name} [{u_roll}] vs {b_name} [{b_roll}]")
        if u_driving:
            if user_failed:
                st.error("   >>> INTERCEPTED! Turnover! (+1 Momentum PT)")
                points = 1; flip_turnover = True
            else:
                st.success("   >>> FAILED PICK! Possession remains...")
        else:
            # User is Defense
            if not user_failed:
                st.success("   >>> PICKED OFF! (+1 PT)")
                points = 1; flip_turnover = True
            else:
                st.error("   >>> MISSED PICK! Offense holds ball...")

    time.sleep(2)
    return user_failed, points, flip_turnover

# =======================================================
#               WEB UI STRUCTURE
# =======================================================

# --- SIDEBAR ---
with st.sidebar:
    st.title("ROUGHBALL OS")
    if st.session_state.game_state != 'MENU':
        md = st.session_state.match_data
        
        c1, c2 = st.columns(2)
        c1.metric(md['u_name'], md['u_score'], delta="Driving" if md['u_driving'] else None)
        c2.metric(md['b_name'], md['b_score'], delta="Driving" if not md['u_driving'] else None)
        
        st.divider()
        st.write(f"**League:** {md['league_name']}")
        st.write(f"**Era:** {md['era_name']}")
        st.write(f"**Timeouts:** {md['u_timeouts']}")
        st.write(f"**Bot Deck:** {len(md['bot_deck'])}")
        
        st.divider()
        st.write("PLAYER PLAYBOOK:")
        for p in md['u_playbook']: st.caption(f"- {p}")

# --- MAIN LOGIC ---

if st.session_state.game_state == 'MENU':
    st.header("ROUGHBALL: END-GAME SIMULATOR")
    st.caption("DEFINITIVE EDITION (v10.0)")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        # Full 16 Team List
        h_id = st.selectbox("Home Team", list(TEAMS.keys()), format_func=lambda x: TEAMS[x]['name'])
    with col2:
        a_id = st.selectbox("Away Team", list(TEAMS.keys()), index=1, format_func=lambda x: TEAMS[x]['name'])
    with col3:
        l_id = st.selectbox("League Level", list(LEAGUES.keys()), format_func=lambda x: LEAGUES[x]['name'])
        
    if st.button("KICKOFF", use_container_width=True):
        u_team, b_team = TEAMS[h_id], TEAMS[a_id]
        league = LEAGUES[l_id]
        
        # Use TIERED NAMES
        u_name = get_tier_name(u_team, league['rank'])
        b_name = get_tier_name(b_team, league['rank'])
        
        st.session_state.match_data = {
            'u_team': u_team, 'b_team': b_team,
            'u_name': u_name, 'b_name': b_name,
            'league_rank': league['rank'],
            'league_name': league['name'],
            'era_name': "STANDARD",
            'u_score': 0, 'b_score': 0,
            'u_timeouts': 2,
            'bot_deck': get_fresh_deck(),
            'u_playbook': u_team.get('playbook', []),
            'u_driving': True 
        }
        st.session_state.game_state = 'KICKOFF'
        st.rerun()

elif st.session_state.game_state == 'KICKOFF':
    md = st.session_state.match_data
    st.subheader("THE KICKOFF CEREMONY")
    
    if st.button("Flip Coin"):
        st.write(f"[REFEREE]: Teams at center field for the toss...")
        time.sleep(1)
        
        u_call = random.choice(["Heads", "Tails"])
        toss_result = random.choice(["Heads", "Tails"])
        
        st.write(f"   > {md['u_name']} calls {u_call}...")
        time.sleep(1)
        
        if u_call == toss_result:
            st.success(f"   >>> WIN! {toss_result} it is. {md['u_name']} will DRIVE first!")
            md['u_driving'] = True
        else:
            st.error(f"   >>> LOSS! {toss_result} it is. {md['b_name']} will DRIVE first!")
            md['u_driving'] = False
        
        time.sleep(2)
        st.session_state.game_state = 'TACTICS'
        st.rerun()

elif st.session_state.game_state == 'TACTICS':
    md = st.session_state.match_data
    rank = md['league_rank']
    
    st.subheader(f"[COACH]: Playcalling Limit is {rank} cards")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        with st.form("tactics_form"):
            num_cards = st.number_input(f"Commit Cards (1-{rank})", min_value=1, max_value=rank, value=1)
            if st.form_submit_button("Set Formation"):
                st.session_state.num_cards_to_play = num_cards
                st.session_state.game_state = 'INPUT_CARDS'
                st.rerun()
    with col2:
        st.write(f"Timeouts: {md['u_timeouts']}")
        if st.button("Call Timeout (T)"):
            if md['u_timeouts'] > 0:
                md['u_timeouts'] -= 1
                md['bot_deck'] = get_fresh_deck()
                st.warning(">>> TIMEOUT CALLED! Deck Reshuffled.")
                st.rerun()
            else:
                st.error("No Timeouts Remaining!")

elif st.session_state.game_state == 'INPUT_CARDS':
    md = st.session_state.match_data
    num = st.session_state.num_cards_to_play
    st.subheader(f"[INPUT]: ENTER {num} CARDS")
    st.caption("Format: 'D 13', 'H K', 'S 10', 'JKR'")
    
    with st.form("card_input"):
        inputs = [st.text_input(f"Card #{i+1}", key=f"c_{i}") for i in range(num)]
        
        if st.form_submit_button("HIKE BALL"):
            u_val, u_suit, u_max = 0, "", 0
            u_hand, u_cards = [], []
            v_map = {'J':11, 'Q':12, 'K':13, 'A':14, 'JKR':15}
            u_played_jkr = False

            for i, txt in enumerate(inputs):
                raw = txt.upper().split()
                if len(raw) < 2: 
                    if "JKR" in txt.upper(): s, v_raw = "JKR", "15"
                    else: s, v_raw = "C", "2"
                else: s, v_raw = raw[0], raw[1]

                try: v = int(v_raw); disp_v = v_raw
                except ValueError: v = v_map.get(v_raw, 2); disp_v = v_raw

                if v == 15 or s == "JKR": u_cards.append("[JKR]")
                else:
                    disp_v = {11:'J', 12:'Q', 13:'K', 14:'A'}.get(v, v)
                    u_cards.append(f"[{SYMBOLS.get(s, '?')} {disp_v}]")

                u_val += v
                if i == 0: u_suit = s
                if v > u_max: u_max = v
                u_hand.append({'val': v, 'suit': s})
                if v == 15 or s == "JKR": u_played_jkr = True

            # Determine Specials
            u_special = None
            if u_played_jkr:
                eff_suit = u_suit
                for c in u_hand:
                    if c['suit'] not in ["JKR", "JOKER", "None"]:
                        eff_suit = c['suit']
                        break
                u_special = {"C":"SCRUM", "H":"STIFF_ARM", "S":"STRIP", "D":"JUKE"}.get(eff_suit)

            st.session_state.play_data = {
                'u_cards': u_cards, 'u_hand': u_hand, 'u_val': u_val,
                'u_suit': u_suit, 'u_max': u_max, 'u_special': u_special,
                'u_played_jkr': u_played_jkr
            }
            st.session_state.game_state = 'RESOLUTION'
            st.rerun()

elif st.session_state.game_state == 'RESOLUTION':
    md = st.session_state.match_data
    pd = st.session_state.play_data
    
    # 1. BOT PREPARES
    b_val, b_suit, b_max, b_disp, b_special = smart_bot_logic(md['league_rank'], not md['u_driving'], md['bot_deck'])
    b_hand = [{'val': b_max, 'suit': b_suit}]
    
    st.subheader("THE PLAY UNFOLDS...")
    st.write(f"**[REVEAL] {md['u_name']} shows:** {' '.join(pd['u_cards'])}")
    time.sleep(0.5)
    st.write(f"**[REVEAL] {md['b_name']} flips:** {b_disp}")
    time.sleep(1)
    
    turn_over = False
    
    # 2. JOKER RESOLUTION
    if pd['u_special'] or b_special or pd['u_played_jkr']:
        st.markdown("### >>> JOKER TRIGGERED! <<<")
        
        # USER
        if pd['u_special']:
            if pd['u_special'] == "JUKE" and md['u_driving']:
                st.success(f"   > {md['u_name']} hits a JUKE! (+5 PTS)")
                md['u_score'] += 5; md['u_driving'] = False; turn_over = True
            elif pd['u_special'] == "STIFF_ARM" and md['u_driving']:
                st.success(f"   > {md['u_name']} STIFF ARM! (+5 PTS)")
                md['u_score'] += 5; md['u_driving'] = False; turn_over = True
            elif pd['u_special'] == "STRIP" and not md['u_driving']:
                st.success(f"   > {md['u_name']} BUTTER FINGERS! (+1 PT)")
                md['u_score'] += 1; md['u_driving'] = True; turn_over = True
            elif pd['u_special'] == "SCRUM":
                st.warning("   > SCRIMMAGE! Possession Flips.")
                md['u_driving'] = not md['u_driving']; turn_over = True
        
        # SIGNATURE (Simplified for Web)
        elif pd['u_played_jkr'] and not turn_over:
             st.info(f"   >>> {md['u_name']} REVEALS SIGNATURE PLAY!")
             md['u_score'] += 7; md['u_driving'] = not md['u_driving']; turn_over = True

        # BOT
        if b_special and not turn_over:
            st.markdown(f"**!!! BOT USES {b_special} !!!**")
            if b_special == "JUKE" and not md['u_driving']:
                st.error(f"   > {md['b_name']} JUKED you! (+5 PTS)")
                md['b_score'] += 5; md['u_driving'] = True; turn_over = True
            elif b_special == "STIFF_ARM" and not md['u_driving']:
                st.error(f"   > {md['b_name']} STIFF ARM! (+5 PTS)")
                md['b_score'] += 5; md['u_driving'] = True; turn_over = True
            elif b_special == "STRIP" and md['u_driving']:
                st.error(f"   > {md['b_name']} PICKED OFF! (+1 PT)")
                md['b_score'] += 1; md['u_driving'] = False; turn_over = True
            elif b_special == "SCRUM" and md['u_driving']:
                st.warning("   > SCRIMMAGE! Possession Flips.")
                md['u_driving'] = not md['u_driving']; turn_over = True
        
        time.sleep(3)

    # 3. PHYSICS
    if not turn_over:
        st.write(f"\n**[PHYSICS]** Rolling D66 (Target: {md['league_rank']})")
        b_hits = sum(1 for _ in range(2) if random.randint(1, 6) <= md['league_rank'])
        u_d1, u_d2 = random.randint(1,6), random.randint(1,6)
        u_hits = (1 if u_d1 <= md['league_rank'] else 0) + (1 if u_d2 <= md['league_rank'] else 0)
        
        st.write(f"   > {md['u_name']}: {u_hits} HITS")
        st.write(f"   > {md['b_name']}: {b_hits} HITS")
        
        if u_hits != b_hits:
            u_win = u_hits > b_hits
            w_max = pd['u_max'] if u_win else b_max
            winner = md['u_name'] if u_win else md['b_name']
            w_suit = pd['u_suit'] if u_win else b_suit
            
            st.write(f"   > **WINNER:** {winner} ({SYMBOLS.get(w_suit, '?')})")
            
            if (u_win and md['u_driving']) or (not u_win and not md['u_driving']):
                pts = 0
                if w_suit == "D" and w_max == 13:
                    pts = 3; st.success(f"KICK PASS! {winner} FIELD GOAL (+3 PTS)!")
                elif w_suit in ["D", "H"]:
                    pts = 5; st.success(f"TRY SUCCESSFUL! {winner} ENDZONE (+5 PTS)!")
                else:
                    st.warning("   >>> DEFENSIVE STOPPAGE! No Points.")
                    md['u_driving'] = not md['u_driving']
                
                if pts > 0:
                    if u_win: md['u_score'] += pts
                    else: md['b_score'] += pts
                    md['u_driving'] = not md['u_driving']
            else:
                st.warning("   >>> DEFENSIVE STOPPAGE! No Points.")
                md['u_driving'] = not md['u_driving']
        else:
            st.warning(f"\n>>>> STALEMATE! ({u_hits}-{b_hits}) <<<<")
            st.session_state.game_state = 'STALEMATE_DECISION'
            st.rerun()

    # CHECK GAME OVER
    if md['u_score'] >= 25 or md['b_score'] >= 25:
        st.session_state.game_state = 'GAME_OVER'
    else:
        if st.button("NEXT PLAY >>>"):
            st.session_state.game_state = 'TACTICS'
            st.rerun()

elif st.session_state.game_state == 'STALEMATE_DECISION':
    st.info("The line is locked. Do you call a RE-AUDIBLE? (Spend 1 Card)")
    c1, c2 = st.columns(2)
    if c1.button("YES (Re-Audible)"):
        st.session_state.game_state = 'STALEMATE_INPUT'
        st.rerun()
    if c2.button("NO (Risk Complication)"):
        md = st.session_state.match_data
        u_fail, pts, flip = resolve_complication_web(md['u_team'], md['b_team'], md['u_driving'], md['u_name'], md['b_name'])
        if u_fail: md['b_score'] += pts
        else: md['u_score'] += pts
        if flip: md['u_driving'] = not md['u_driving']
        if st.button("Continue"):
            st.session_state.game_state = 'TACTICS'
            st.rerun()

elif st.session_state.game_state == 'STALEMATE_INPUT':
    st.subheader("[RE-AUDIBLE]: Commit a new card to break the lock!")
    card_re = st.text_input("Recall Card (Suit + Val):")
    if st.button("COMMIT RECALL"):
        md = st.session_state.match_data
        raw_r = card_re.upper().split()
        rs = raw_r[0] if len(raw_r) > 0 else "C"
        
        suit_to_save = {'C': 'STA', 'S': 'SPD', 'D': 'KCK', 'H': 'CAT'}
        save_stat = suit_to_save.get(rs, 'STA')
        
        u_mod = md['u_team']['stats'].get(save_stat, 0)
        b_mod = md['b_team']['stats'].get(save_stat, 0)
        u_roll = random.randint(1, 6) + u_mod
        b_roll = random.randint(1, 6) + b_mod
        
        st.write(f"   [DICE]: {save_stat} SAVE! You: {u_roll} vs Bot: {b_roll}")
        
        success = False
        if rs in ['C', 'S']:
            if u_roll >= b_roll:
                st.success(f"> OPPONENT CRUSHED! {md['u_name']} secures ball.")
                md['u_driving'] = True; success = True
            else:
                st.error(f"> ROUGHBALL STRIPPED! Turnover."); md['u_driving'] = False; success = True
        elif rs in ['H', 'D']:
            if u_roll > b_roll:
                pts = 3 if rs == 'D' else 5
                md['u_score'] += pts
                st.success(f"> CONVERSION! {md['u_name']} scores {pts} pt!")
                md['u_driving'] = not md['u_driving']; success = True
            else:
                st.warning(f"> STOPPAGE! No points."); md['u_driving'] = not md['u_driving']; success = True
        
        if not success:
            st.write(" > STILL LOCKED. Exhaustion sets in...")
            u_fail, pts, flip = resolve_complication_web(md['u_team'], md['b_team'], md['u_driving'], md['u_name'], md['b_name'])
            if u_fail: md['b_score'] += pts
            else: md['u_score'] += pts
            if flip: md['u_driving'] = not md['u_driving']

        if st.button("Continue"):
            st.session_state.game_state = 'TACTICS'
            st.rerun()

elif st.session_state.game_state == 'GAME_OVER':
    md = st.session_state.match_data
    st.title("GAME OVER")
    st.header(f"FINAL: {md['u_name']} {md['u_score']} - {md['b_name']} {md['b_score']}")
    if st.button("RETURN TO MENU"):
        st.session_state.game_state = 'MENU'
        st.rerun()
