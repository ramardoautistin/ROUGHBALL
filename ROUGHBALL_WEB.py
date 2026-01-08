import streamlit as st
import random
import time
import pandas as pd

# =======================================================
#       ROUGHBALL PRO: DEFINITIVE EDITION (WEB)
#       Source: ROUGHBALL_DEFINITIVE.py
# =======================================================

st.set_page_config(page_title="ROUGHBALL PRO", layout="wide", initial_sidebar_state="expanded")

# --- [1] THE DEFINITIVE DATABASE (16 TEAMS) ---
TEAMS = {
    "1": {"name": "Mountain LIONS", "stats": {'TKL': 8, 'AWR': 4, 'INT': 7, 'PAS': 6}, "region": "North", "tiers": {5: "Mountain LIONS", 4: "College Wildcats", 3: "High School Lynx", 2: "Backyard Cougars", 1: "Northern Rookies"}},
    "2": {"name": "Greenland VIKINGS", "stats": {'TKL': 6, 'AWR': 7, 'INT': 8, 'PAS': 4}, "region": "North", "tiers": {5: "Greenland VIKINGS", 4: "College Celtics", 3: "High School Warriors", 2: "Backyard Maulers", 1: "Greenland Rookies"}},
    "3": {"name": "Southern FARMERS", "stats": {'TKL': 8, 'AWR': 7, 'INT': 6, 'PAS': 4}, "region": "South", "tiers": {5: "Southern FARMERS", 4: "College Cattle", 3: "High School Hillbillies", 2: "Backyard Rednecks", 1: "Great Rookies"}},
    "4": {"name": "Coast SHARKS", "stats": {'TKL': 7, 'AWR': 5, 'INT': 8, 'PAS': 5}, "region": "South", "tiers": {5: "Coast SHARKS", 4: "College Hammerheads", 3: "High School Gators", 2: "Backyard Marlins", 1: "Coastal Rookies"}},
    "5": {"name": "Eastern EAGLES", "stats": {'TKL': 5, 'AWR': 9, 'INT': 6, 'PAS': 5}, "region": "East", "tiers": {5: "Eastern EAGLES", 4: "College Crows", 3: "High School Ravens", 2: "Backyard Vultures", 1: "Brown Rookies"}},
    "6": {"name": "City PATRIOTS", "stats": {'TKL': 6, 'AWR': 5, 'INT': 5, 'PAS': 9}, "region": "East", "tiers": {5: "City PATRIOTS", 4: "College Colonels", 3: "High School Admirals", 2: "Backyard Sentinels", 1: "City Rookies"}},
    "7": {"name": "Western BEARS", "stats": {'TKL': 7, 'AWR': 7, 'INT': 6, 'PAS': 5}, "region": "West", "tiers": {5: "Western BEARS", 4: "College Bruins", 3: "High School Grizzlies", 2: "Backyard Cubs", 1: "Red Rookies"}},
    "8": {"name": "Beach PIRATES", "stats": {'TKL': 5, 'AWR': 8, 'INT': 6, 'PAS': 6}, "region": "West", "tiers": {5: "Beach PIRATES", 4: "College Raiders", 3: "High School Bandits", 2: "Backyard Outlaws", 1: "Beach Rookies"}},
    "9": {"name": "Pike PANTHERS", "stats": {'TKL': 8, 'AWR': 5, 'INT': 7, 'PAS': 5}, "region": "North", "tiers": {5: "Pike PANTHERS", 4: "College Jaguars", 3: "High School Tigers", 2: "Backyard Bobcats", 1: "Pike Rookies"}},
    "10": {"name": "Greenland SAINTS", "stats": {'TKL': 7, 'AWR': 5, 'INT': 9, 'PAS': 4}, "region": "North", "tiers": {5: "Greenland SAINTS", 4: "College Monks", 3: "High School Friars", 2: "Backyard Preachers", 1: "Hill Rookies"}},
    "11": {"name": "Countryside STALLIONS", "stats": {'TKL': 7, 'AWR': 8, 'INT': 6, 'PAS': 4}, "region": "South", "tiers": {5: "Countryside STALLIONS", 4: "College Mustangs", 3: "High School Broncos", 2: "Backyard Colts", 1: "Countryside Rookies"}},
    "12": {"name": "Southern STINGRAYS", "stats": {'TKL': 6, 'AWR': 5, 'INT': 8, 'PAS': 6}, "region": "South", "tiers": {5: "Southern STINGRAYS", 4: "College Dolphins", 3: "High School Seals", 2: "Backyard Squids", 1: "Southern Rookies"}},
    "13": {"name": "City ROYALS", "stats": {'TKL': 5, 'AWR': 5, 'INT': 6, 'PAS': 9}, "region": "East", "tiers": {5: "City ROYALS", 4: "College Knights", 3: "High School Ambassadors", 2: "Backyard Legionnaires", 1: "Eastern Rookies"}},
    "14": {"name": "Eastern SEAHAWKS", "stats": {'TKL': 5, 'AWR': 9, 'INT': 6, 'PAS': 5}, "region": "East", "tiers": {5: "Eastern SEAHAWKS", 4: "College Pelicans", 3: "High School Skimmers", 2: "Backyard Talons", 1: "Lake Rookies"}},
    "15": {"name": "Desert SCORPIONS", "stats": {'TKL': 7, 'AWR': 6, 'INT': 5, 'PAS': 7}, "region": "West", "tiers": {5: "Desert SCORPIONS", 4: "College Spiders", 3: "High School Stingers", 2: "Backyard Snakes", 1: "Desert Rookies"}},
    "16": {"name": "Beach SURGERS", "stats": {'TKL': 4, 'AWR': 7, 'INT': 6, 'PAS': 9}, "region": "West", "tiers": {5: "Beach SURGERS", 4: "College Volts", 3: "High School Chargers", 2: "Backyard Hurricanes", 1: "Western Rookies"}}
}

LEAGUES = {
    "1": {"name": "D5 - Unranked Rookies", "rank": 1},
    "2": {"name": "D4 - Backyard Amateurs", "rank": 2},
    "3": {"name": "D3 - High School Pros", "rank": 3},
    "4": {"name": "D2 - College Superstars", "rank": 4},
    "5": {"name": "D1 - National Legends", "rank": 5}
}

SYMBOLS = {"C": "♣", "H": "♥", "S": "♠", "D": "♦", "JKR": "★"}
SAVING_MAP = {"1": "STA", "2": "CAT", "3": "KCK", "4": "SPD"}

# --- [2] CORE UTILS ---
def get_fresh_deck():
    suits = ['C', 'H', 'S', 'D']
    deck = [{'val': r, 'suit': s} for s in suits for r in range(2, 15)]
    deck.append({'val': 15, 'suit': 'JKR'})
    deck.append({'val': 15, 'suit': 'JKR'})
    random.shuffle(deck)
    return deck

def get_tier_name(team_data, rank):
    return team_data['tiers'].get(rank, team_data['name'])

def init_stats():
    # Helper to calculate derived stats
    for t in TEAMS:
        TEAMS[t]['save'] = {
            'STA': TEAMS[t]['stats']['TKL'],
            'SPD': TEAMS[t]['stats']['AWR'],
            'KCK': TEAMS[t]['stats']['INT'],
            'CAT': TEAMS[t]['stats']['PAS']
        }
        TEAMS[t]['playbook'] = ["[EMPTY]"] * 5
        TEAMS[t]['boosts'] = {'TKL': 0, 'AWR': 0, 'INT': 0, 'PAS': 0} # Week Event Boosts

# --- [3] STATE MANAGEMENT ---
if 'init_done' not in st.session_state:
    init_stats()
    st.session_state.game_mode = 'MENU' # MENU, MATCH, DYNASTY, DRAFT
    st.session_state.match_active = False
    st.session_state.dynasty_data = None
    st.session_state.draft_data = None
    st.session_state.init_done = True

# --- [4] DYNASTY & DRAFT LOGIC ---
def generate_draft_class():
    prospects = []
    positions = ['QB', 'RB', 'WR', 'TE', 'OL', 'DL', 'LB', 'CB', 'S', 'K']
    for i in range(10): # Generate 10 prospects
        pos = random.choice(positions)
        suit = random.choice(list(SYMBOLS.keys())[:-1]) # No JKR suit
        stars = random.randint(1, 5)
        if random.randint(1, 10) == 10: stars = 0 # BUST chance
        prospects.append({
            'id': i+1, 'pos': pos, 'suit': suit, 
            'true_stars': stars, 'scouted': False
        })
    return prospects

def init_dynasty(user_team_id, league_rank):
    schedule = []
    # Create a 5-week schedule
    opponents = [tid for tid in TEAMS if tid != user_team_id]
    random.shuffle(opponents)
    
    for week in range(1, 6):
        opp_id = opponents.pop()
        schedule.append({'week': week, 'opp_id': opp_id, 'result': None, 'score': None})
    
    return {
        'user_id': user_team_id,
        'league_rank': league_rank,
        'schedule': schedule,
        'record': {'W': 0, 'L': 0, 'T': 0},
        'current_week': 1,
        'week_day': 'Mon' # Simulates WEEKLY_SCHEDULE progression
    }

# --- [5] SMART BOT ---
def smart_bot_logic(rank_val, bot_is_driving, bot_deck):
    if len(bot_deck) < rank_val: bot_deck[:] = get_fresh_deck()
    hand = [bot_deck.pop() for _ in range(rank_val)]
    
    groups = {"C": [], "H": [], "S": [], "D": [], "JKR": []}
    hand_vals = []
    for c in hand:
        groups[c['suit']].append(c['val'])
        hand_vals.append(c['val'])
    
    if bot_is_driving:
        priority = ["D", "H"]
        if not any(groups[s] for s in priority): priority = ["C", "S"]
    else:
        priority = ["C", "S"]
        if not any(groups[s] for s in priority): priority = ["D", "H"]
        
    best_suit = max(priority, key=lambda s: sum(groups[s]) if groups[s] else 0)
    if not groups[best_suit] and "JKR" not in groups: best_suit = "C"

    special = None
    if 15 in hand_vals:
        if bot_is_driving:
            if groups["D"]: special = "JUKE"
            elif groups["H"]: special = "STIFF_ARM"
        else:
            if groups["S"]: special = "STRIP"
            elif groups["C"]: special = "SCRUM"
    
    unused_cards = [c for c in hand if c['suit'] != best_suit and c['val'] != 15]
    for card in unused_cards: bot_deck.insert(0, card)

    display = "".join([f"[{SYMBOLS.get(best_suit, '?')} {v}] " for v in groups[best_suit]])
    if 15 in hand_vals: display += "[JKR] "
    
    return sum(groups[best_suit]), best_suit, max(groups[best_suit]+[0]), display, special

# --- [6] COMPLICATION RESOLVER (FLAVOR TEXT PRESERVED) ---
def resolve_complication_web(u_team, b_team, u_driving, u_name, b_name):
    d4 = random.randint(1, 4)
    stat_key = SAVING_MAP[str(d4)]
    st.markdown(f"**[!] COMPLICATION ROLLED (D4):** {d4} - Checking {stat_key}")
    
    # Calculate stats with any Dynasty Boosts applied
    u_base = u_team['save'][stat_key] + u_team['boosts'].get(stat_key, 0)
    b_base = b_team['save'][stat_key]
    u_roll = random.randint(1, 6) + u_base
    b_roll = random.randint(1, 6) + b_base
    
    user_failed = u_roll < b_roll
    points, flip = 0, False
    
    if d4 == 1: # SACK
        st.write(f"   > **SACK! (Loss of possession)** - (STA) CHECK")
        st.write(f"   > {u_name} [{u_roll}] vs {b_name} [{b_roll}]")
        if u_driving and user_failed:
             st.error("   >>> QG SACKED! (+2 PTS). Possession Flip!"); points = 2; flip = True
        elif not u_driving and not user_failed:
             st.success("   >>> QG SACKED! (+2 PTS). Possession Flip!"); points = 2; flip = True
        else: st.info("   >>> TACKLE SHED! Play continues.")

    elif d4 == 2: # OUT OF BOUNDS
        st.write(f"   > **OUT OF BOUNDS! (Reset play)** - (CAT) CHECK")
        st.info("   >>> Play RESET to Neutral Snap Point.")

    elif d4 == 3: # PENALTY
        st.write(f"   > **PENALTY! (Personal Foul)** - (KCK) CHECK")
        st.write(f"   > {u_name} [{u_roll}] vs {b_name} [{b_roll}]")
        if user_failed: st.error("   >>> PERSONAL FOUL! Opponent +3 PTS."); points = 3
        else: st.success("   >>> DISCIPLINED! No foul.")

    elif d4 == 4: # INTERCEPTION
        st.write(f"   > **INTERCEPTION! (Possession Flip)** - (AWR) CHECK")
        st.write(f"   > {u_name} [{u_roll}] vs {b_name} [{b_roll}]")
        if u_driving and user_failed:
            st.error("   >>> TURNOVER! (+1 Momentum PT)"); points = 1; flip = True
        elif not u_driving and not user_failed:
            st.success("   >>> PICKED OFF! (+1 PT)"); points = 1; flip = True
        else: st.info("   >>> INCOMPLETE/DROPPED!")

    time.sleep(1.5)
    return user_failed, points, flip

# =======================================================
#               THE MATCH ENGINE (MODULAR)
# =======================================================
def render_match_engine():
    if 'match_state' not in st.session_state:
        st.session_state.match_state = 'KICKOFF'
    
    md = st.session_state.match_data
    
    # --- SIDEBAR SCOREBOARD ---
    with st.sidebar:
        st.title("MATCH CENTER")
        st.metric(md['u_name'], md['u_score'], "Driving" if md['u_driving'] else None)
        st.metric(md['b_name'], md['b_score'], "Driving" if not md['u_driving'] else None)
        st.write(f"**Deck:** {len(md['bot_deck'])} | **TOs:** {md['u_timeouts']}")
        if st.button("ABORT MATCH", type="primary"):
            st.session_state.game_mode = st.session_state.return_mode
            st.rerun()

    # --- KICKOFF PHASE ---
    if st.session_state.match_state == 'KICKOFF':
        st.header(f"{md['u_name']} vs {md['b_name']}")
        st.write("The referee holds the coin...")
        if st.button("FLIP COIN"):
            uc = random.choice(["Heads", "Tails"])
            res = random.choice(["Heads", "Tails"])
            st.write(f"Call: {uc} | Result: {res}")
            if uc == res:
                st.success("You won the toss! Driving first.")
                md['u_driving'] = True
            else:
                st.error("Lost the toss. Defending.")
                md['u_driving'] = False
            time.sleep(1)
            st.session_state.match_state = 'TACTICS'
            st.rerun()

    # --- TACTICS PHASE ---
    elif st.session_state.match_state == 'TACTICS':
        rank = md['league_rank']
        st.subheader(f"TACTICS (Limit: {rank})")
        
        c1, c2 = st.columns([3, 1])
        with c1:
            with st.form("tactics"):
                nc = st.number_input("Cards to Play", 1, rank, 1)
                if st.form_submit_button("LOCK IN"):
                    st.session_state.num_cards = nc
                    st.session_state.match_state = 'INPUT'
                    st.rerun()
        with c2:
            if st.button("TIMEOUT (T)"):
                if md['u_timeouts'] > 0:
                    md['u_timeouts'] -= 1
                    md['bot_deck'] = get_fresh_deck()
                    st.toast("Timeout called! Deck reshuffled.")
                else: st.error("No timeouts!")

    # --- INPUT PHASE ---
    elif st.session_state.match_state == 'INPUT':
        num = st.session_state.num_cards
        st.subheader(f"INPUT {num} CARDS")
        with st.form("inputs"):
            cards = [st.text_input(f"Card {i+1}", key=f"c{i}") for i in range(num)]
            if st.form_submit_button("HIKE"):
                u_cards, u_hand, u_val, u_suit, u_max = [], [], 0, "", 0
                v_map = {'J':11, 'Q':12, 'K':13, 'A':14, 'JKR':15}
                played_jkr = False
                
                for i, c in enumerate(cards):
                    raw = c.upper().split()
                    if len(raw) < 2: s, vr = ("JKR", "15") if "JKR" in c.upper() else ("C", "2")
                    else: s, vr = raw[0], raw[1]
                    try: v = int(vr)
                    except: v = v_map.get(vr, 2)
                    
                    if v == 15 or s == "JKR": u_cards.append("[JKR]"); played_jkr = True
                    else: u_cards.append(f"[{SYMBOLS.get(s,'?')} {vr}]")
                    
                    u_val += v
                    if i == 0: u_suit = s
                    if v > u_max: u_max = v
                    u_hand.append({'val':v, 'suit':s})
                
                u_spec = None
                if played_jkr:
                    eff = u_suit
                    for x in u_hand: 
                        if x['suit'] not in ["JKR", "None"]: eff = x['suit']; break
                    u_spec = {"C":"SCRUM", "H":"STIFF_ARM", "S":"STRIP", "D":"JUKE"}.get(eff)
                
                st.session_state.play_data = {
                    'u_cards': u_cards, 'u_hand': u_hand, 'u_max': u_max, 
                    'u_suit': u_suit, 'u_spec': u_spec, 'u_jkr': played_jkr
                }
                st.session_state.match_state = 'RESOLVE'
                st.rerun()

    # --- RESOLVE PHASE ---
    elif st.session_state.match_state == 'RESOLVE':
        pd = st.session_state.play_data
        b_val, b_suit, b_max, b_disp, b_spec = smart_bot_logic(md['league_rank'], not md['u_driving'], md['bot_deck'])
        
        st.write(f"**YOU:** {' '.join(pd['u_cards'])}")
        time.sleep(0.5)
        st.write(f"**BOT:** {b_disp}")
        time.sleep(0.5)
        
        over = False
        if pd['u_spec'] or b_spec or pd['u_jkr']:
            st.markdown("### >>> JOKER TRIGGERED! <<<")
            
            if pd['u_spec']:
                if pd['u_spec'] == "JUKE" and md['u_driving']: md['u_score']+=5; st.success("JUKE! +5 PTS"); md['u_driving']=False; over=True
                elif pd['u_spec'] == "STIFF_ARM" and md['u_driving']: md['u_score']+=5; st.success("STIFF ARM! +5 PTS"); md['u_driving']=False; over=True
                elif pd['u_spec'] == "STRIP" and not md['u_driving']: md['u_score']+=1; st.success("STRIP! +1 PT"); md['u_driving']=True; over=True
                elif pd['u_spec'] == "SCRUM": st.warning("SCRUM! Flip Poss."); md['u_driving'] = not md['u_driving']; over=True
            
            elif b_spec and not over:
                 if b_spec == "JUKE" and not md['u_driving']: md['b_score']+=5; st.error("BOT JUKE! +5 PTS"); md['u_driving']=True; over=True
                 elif b_spec == "STIFF_ARM" and not md['u_driving']: md['b_score']+=5; st.error("BOT STIFF ARM! +5 PTS"); md['u_driving']=True; over=True
                 elif b_spec == "STRIP" and md['u_driving']: md['b_score']+=1; st.error("BOT STRIP! +1 PT"); md['u_driving']=False; over=True
                 elif b_spec == "SCRUM": st.warning("BOT SCRUM! Flip Poss."); md['u_driving'] = not md['u_driving']; over=True
            time.sleep(2)

        if not over:
            st.write("Rolling Physics (D66)...")
            b_hits = sum(1 for _ in range(2) if random.randint(1,6) <= md['league_rank'])
            u_d1, u_d2 = random.randint(1,6), random.randint(1,6)
            u_hits = (1 if u_d1 <= md['league_rank'] else 0) + (1 if u_d2 <= md['league_rank'] else 0)
            st.write(f"YOU: {u_hits} hits | BOT: {b_hits} hits")
            
            if u_hits != b_hits:
                win = u_hits > b_hits
                winner = md['u_name'] if win else md['b_name']
                ws = pd['u_suit'] if win else b_suit
                wm = pd['u_max'] if win else b_max
                st.markdown(f"**WINNER:** {winner} ({SYMBOLS.get(ws,'?')})")
                
                if (win and md['u_driving']) or (not win and not md['u_driving']):
                    pts = 0
                    if ws == "D" and wm == 13: pts=3; st.success("KICK PASS (FG)! +3 PTS")
                    elif ws in ["D", "H"]: pts=5; st.success("TRY SCORED! +5 PTS")
                    else: st.info("Marching downfield...")
                    if pts > 0:
                        if win: md['u_score'] += pts
                        else: md['b_score'] += pts
                        md['u_driving'] = not md['u_driving']
                else:
                    st.info("Defensive Stop.")
                    md['u_driving'] = not md['u_driving']
            else:
                st.warning("STALEMATE!")
                st.session_state.match_state = 'STALEMATE'
                st.rerun()

        if md['u_score'] >= 25 or md['b_score'] >= 25:
            st.success("MATCH OVER")
            if st.button("FINISH"):
                if st.session_state.return_mode == 'DYNASTY':
                    rec = st.session_state.dynasty_data['record']
                    if md['u_score'] > md['b_score']: rec['W'] += 1
                    elif md['b_score'] > md['u_score']: rec['L'] += 1
                    else: rec['T'] += 1
                    curr = st.session_state.dynasty_data['current_week']
                    st.session_state.dynasty_data['schedule'][curr-1]['result'] = f"{md['u_score']}-{md['b_score']}"
                    st.session_state.dynasty_data['current_week'] += 1
                st.session_state.game_mode = st.session_state.return_mode
                st.rerun()
        else:
            if st.button("NEXT PLAY"):
                st.session_state.match_state = 'TACTICS'
                st.rerun()

    elif st.session_state.match_state == 'STALEMATE':
        st.info("Stalemate! Call Re-Audible?")
        c1, c2 = st.columns(2)
        if c1.button("YES"): st.session_state.match_state = 'REAUDIBLE'; st.rerun()
        if c2.button("NO"):
            uf, pts, fl = resolve_complication_web(md['u_team'], md['b_team'], md['u_driving'], md['u_name'], md['b_name'])
            if uf: md['b_score']+=pts
            else: md['u_score']+=pts
            if fl: md['u_driving'] = not md['u_driving']
            if st.button("CONTINUE"): st.session_state.match_state = 'TACTICS'; st.rerun()
            
    elif st.session_state.match_state == 'REAUDIBLE':
        rc = st.text_input("Recall Card (Suit Val):")
        if st.button("RECALL"):
             st.success("Re-Audible Processed (Success!)") # Simplified
             st.session_state.match_state = 'TACTICS'; st.rerun()

# =======================================================
#               MAIN APP NAVIGATION
# =======================================================

if st.session_state.game_mode == 'MENU':
    st.title("ROUGHBALL PRO: DEFINITIVE EDITION")
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Quick Play")
        h = st.selectbox("User Team", list(TEAMS.keys()), format_func=lambda x: TEAMS[x]['name'])
        a = st.selectbox("CPU Team", list(TEAMS.keys()), index=1, format_func=lambda x: TEAMS[x]['name'])
        l = st.selectbox("League", list(LEAGUES.keys()), format_func=lambda x: LEAGUES[x]['name'])
        
        if st.button("START MATCH"):
            ut, bt = TEAMS[h], TEAMS[a]
            lr = LEAGUES[l]
            st.session_state.match_data = {
                'u_team': ut, 'b_team': bt,
                'u_name': get_tier_name(ut, lr['rank']),
                'b_name': get_tier_name(bt, lr['rank']),
                'league_rank': lr['rank'],
                'u_score': 0, 'b_score': 0, 'u_driving': True,
                'bot_deck': get_fresh_deck(), 'u_timeouts': 2
            }
            st.session_state.return_mode = 'MENU'
            st.session_state.game_mode = 'MATCH'
            st.rerun()
            
    with c2:
        st.subheader("Dynasty Mode")
        # DYNASTY SETUP FORM [Restored Franchise Selector]
        with st.form("dynasty_setup"):
            st.write("Initialize Season 1")
            dy_team = st.selectbox("Select Franchise", list(TEAMS.keys()), format_func=lambda x: TEAMS[x]['name'])
            dy_league = st.selectbox("Starting League", list(LEAGUES.keys()), format_func=lambda x: LEAGUES[x]['name'])
            
            if st.form_submit_button("BEGIN DYNASTY"):
                st.session_state.dynasty_data = init_dynasty(dy_team, LEAGUES[dy_league]['rank'])
                st.session_state.game_mode = 'DYNASTY'
                st.rerun()

        st.subheader("Scouting")
        if st.button("ENTER MOCK DRAFT"):
            st.session_state.draft_data = {'pool': generate_draft_class(), 'picks': []}
            st.session_state.game_mode = 'DRAFT'
            st.rerun()

elif st.session_state.game_mode == 'MATCH':
    render_match_engine()

elif st.session_state.game_mode == 'DYNASTY':
    dd = st.session_state.dynasty_data
    u_team = TEAMS[dd['user_id']]
    st.title(f"{u_team['name']} | Week {dd['current_week']}")
    
    rec = dd['record']
    st.metric("Season Record", f"{rec['W']}-{rec['L']}-{rec['T']}")
    
    # Weekly Schedule View
    if dd['current_week'] <= 5:
        nxt = dd['schedule'][dd['current_week']-1]
        opp = TEAMS[nxt['opp_id']]
        st.subheader(f"UPCOMING: vs {opp['name']}")
        
        if st.button("PLAY MATCH"):
            lr = LEAGUES[str(dd['league_rank'])]
            st.session_state.match_data = {
                'u_team': u_team, 'b_team': opp,
                'u_name': get_tier_name(u_team, dd['league_rank']),
                'b_name': get_tier_name(opp, dd['league_rank']),
                'league_rank': dd['league_rank'],
                'u_score': 0, 'b_score': 0, 'u_driving': True,
                'bot_deck': get_fresh_deck(), 'u_timeouts': 2
            }
            st.session_state.return_mode = 'DYNASTY'
            st.session_state.game_mode = 'MATCH'
            st.rerun()
    else:
        st.success("SEASON COMPLETE!")
        if st.button("RETURN TO MENU"): st.session_state.game_mode = 'MENU'; st.rerun()

elif st.session_state.game_mode == 'DRAFT':
    st.title("MOCK DRAFT: CLASS OF '26")
    st.markdown("### SCOUTING MANAGER & LEAGUE SIMULATION")
    
    # "Run Simulation" Button (The Trigger)
    if st.button("RUN MOCK DRAFT SIMULATION", type="primary"):
        st.session_state.draft_results = []
        
        # 1. ESTABLISH DRAFT ORDER (Reverse of default ID for demo, or random)
        draft_order = list(TEAMS.keys())
        random.shuffle(draft_order)
        
        # 2. GENERATE PICKS FOR EVERY TEAM
        for rank, t_id in enumerate(draft_order):
            team_name = TEAMS[t_id]['name']
            
            # Generate 3 Rounds of Picks per Team (As per your loop)
            team_picks = []
            for _ in range(3):
                # ROUGHBALL GENERATION LOGIC
                s_key = random.choice(list(SYMBOLS.keys())[:-1]) # No JKR
                suit_icon = SYMBOLS[s_key]
                
                pos = random.choice(['QB', 'RB', 'WR', 'TE', 'OL', 'DL', 'LB', 'CB', 'S', 'K'])
                
                # Star Rating Math (Weighted)
                # 10% Chance of 5-Star, 20% 4-Star, etc.
                roll = random.randint(1, 100)
                if roll > 95: stars = 5
                elif roll > 80: stars = 4
                elif roll > 50: stars = 3
                elif roll > 20: stars = 2
                else: stars = 1
                
                # 5% Chance of Total Bust (0 Stars)
                if random.randint(1, 20) == 1: stars = 0
                
                star_str = "★" * stars if stars > 0 else "BUST"
                
                # THE FLAVOR STRING: "♥ QB(★★★)"
                pick_str = f"{suit_icon} {pos}({star_str})"
                team_picks.append(pick_str)
            
            st.session_state.draft_results.append({
                'Rank': rank + 1,
                'Team': team_name,
                'R1': team_picks[0],
                'R2': team_picks[1],
                'R3': team_picks[2]
            })

    # DISPLAY THE BOARD (If simulation ran)
    if 'draft_results' in st.session_state and st.session_state.draft_results:
        # We use a dataframe for that clean "Terminal Table" look on Web
        df = pd.DataFrame(st.session_state.draft_results)
        st.dataframe(
            df, 
            column_config={
                "Rank": st.column_config.NumberColumn(format="%d"),
                "Team": st.column_config.TextColumn(width="medium"),
                "R1": st.column_config.TextColumn(width="large"),
                "R2": st.column_config.TextColumn(width="large"),
                "R3": st.column_config.TextColumn(width="large"),
            },
            hide_index=True,
            use_container_width=True
        )
        
        st.caption("Key: ★ = Talent Rating | BUST = 0 Stars | Suit indicates primary attribute bias.")

    st.write("---")
    if st.button("RETURN TO MENU"):
        st.session_state.game_mode = 'MENU'
        st.rerun()
