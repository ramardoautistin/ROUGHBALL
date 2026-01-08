import streamlit as st
import random
import time
import pandas as pd

# =======================================================
#       ROUGHBALL PRO: LOGBOOK EDITION (v10.0)
#       UI Monolith: ROUGHBALL_LOGBOOK.pdf
#       Roughball Monolith: ROUGHBALL_DEFINITIVE.py
# =======================================================

st.set_page_config(page_title="NRBL COMMISSIONER LOG", layout="wide", initial_sidebar_state="expanded")

# --- [1] THE MONOLITH DATABASE (16 TEAMS + LORE) ---
# Derived from DEFINITIVE.py + LOGBOOK.pdf
TEAMS = {
    # NORTH DIVISION (MOUNTAIN/GREENLAND)
    "1": {"name": "Mountain LIONS", "stats": {'TKL': 8, 'AWR': 4, 'INT': 7, 'PAS': 6}, "region": "NORTH", "tiers": {5: "Mountain LIONS", 1: "Northern Rookies"}},
    "2": {"name": "Greenland VIKINGS", "stats": {'TKL': 6, 'AWR': 7, 'INT': 8, 'PAS': 4}, "region": "NORTH", "tiers": {5: "Greenland VIKINGS", 1: "Greenland Rookies"}},
    "9": {"name": "Pike PANTHERS", "stats": {'TKL': 8, 'AWR': 5, 'INT': 7, 'PAS': 5}, "region": "NORTH", "tiers": {5: "Pike PANTHERS", 1: "Pike Rookies"}},
    "10": {"name": "Greenland SAINTS", "stats": {'TKL': 7, 'AWR': 5, 'INT': 9, 'PAS': 4}, "region": "NORTH", "tiers": {5: "Greenland SAINTS", 1: "Hill Rookies"}},
    
    # SOUTH DIVISION (COUNTRYSIDE/COAST)
    "3": {"name": "Southern FARMERS", "stats": {'TKL': 8, 'AWR': 7, 'INT': 6, 'PAS': 4}, "region": "SOUTH", "tiers": {5: "Southern FARMERS", 1: "Great Rookies"}},
    "4": {"name": "Coast SHARKS", "stats": {'TKL': 7, 'AWR': 5, 'INT': 8, 'PAS': 5}, "region": "SOUTH", "tiers": {5: "Coast SHARKS", 1: "Coastal Rookies"}},
    "11": {"name": "Countryside STALLIONS", "stats": {'TKL': 7, 'AWR': 8, 'INT': 6, 'PAS': 4}, "region": "SOUTH", "tiers": {5: "Countryside STALLIONS", 1: "Countryside Rookies"}},
    "12": {"name": "Southern STINGRAYS", "stats": {'TKL': 6, 'AWR': 5, 'INT': 8, 'PAS': 6}, "region": "SOUTH", "tiers": {5: "Southern STINGRAYS", 1: "Southern Rookies"}},
    
    # EAST DIVISION (CITY/LAKE)
    "5": {"name": "Eastern EAGLES", "stats": {'TKL': 5, 'AWR': 9, 'INT': 6, 'PAS': 5}, "region": "EAST", "tiers": {5: "Eastern EAGLES", 1: "Brown Rookies"}},
    "6": {"name": "City PATRIOTS", "stats": {'TKL': 6, 'AWR': 5, 'INT': 5, 'PAS': 9}, "region": "EAST", "tiers": {5: "City PATRIOTS", 1: "City Rookies"}},
    "13": {"name": "City ROYALS", "stats": {'TKL': 5, 'AWR': 5, 'INT': 6, 'PAS': 9}, "region": "EAST", "tiers": {5: "City ROYALS", 1: "Eastern Rookies"}},
    "14": {"name": "Eastern SEAHAWKS", "stats": {'TKL': 5, 'AWR': 9, 'INT': 6, 'PAS': 5}, "region": "EAST", "tiers": {5: "Eastern SEAHAWKS", 1: "Lake Rookies"}},
    
    # WEST DIVISION (DESERT/BEACH)
    "7": {"name": "Western BEARS", "stats": {'TKL': 7, 'AWR': 7, 'INT': 6, 'PAS': 5}, "region": "WEST", "tiers": {5: "Western BEARS", 1: "Red Rookies"}},
    "8": {"name": "Beach PIRATES", "stats": {'TKL': 5, 'AWR': 8, 'INT': 6, 'PAS': 6}, "region": "WEST", "tiers": {5: "Beach PIRATES", 1: "Beach Rookies"}},
    "15": {"name": "Desert SCORPIONS", "stats": {'TKL': 7, 'AWR': 6, 'INT': 5, 'PAS': 7}, "region": "WEST", "tiers": {5: "Desert SCORPIONS", 1: "Desert Rookies"}},
    "16": {"name": "Beach SURGERS", "stats": {'TKL': 4, 'AWR': 7, 'INT': 6, 'PAS': 9}, "region": "WEST", "tiers": {5: "Beach SURGERS", 1: "Western Rookies"}}
}

LEAGUES = {
    "1": {"name": "D5 - Unranked Rookies", "rank": 1},
    "2": {"name": "D4 - Backyard Amateurs", "rank": 2},
    "3": {"name": "D3 - High School Pros", "rank": 3},
    "4": {"name": "D2 - College Superstars", "rank": 4},
    "5": {"name": "D1 - National Legends", "rank": 5}
}

ERAS = {
    "STANDARD": {"name": "STANDARD ERA", "desc": "The Definitive Ruleset"},
    "GOLDEN": {"name": "GOLDEN AGE", "desc": "High Scoring, High Flying"},
    "OLD": {"name": "OLD TIMEY", "desc": "Gritty, Muddy, Defensive"}
}

# LOGBOOK MAPPING
SYMBOLS = {"C": "♣", "H": "♥", "S": "♠", "D": "♦", "JKR": "★"}
UNIT_MAP = {
    'TKL': {'suit': 'C', 'unit': 'SCRIMMAGERS', 'pos': 'DT/DE/LB', 'save': 'STA'},
    'AWR': {'suit': 'H', 'unit': 'FIELD GENERALS', 'pos': 'QB/SG/C', 'save': 'SPD'},
    'INT': {'suit': 'S', 'unit': 'PITCH GUARDS', 'pos': 'CB/LB/S', 'save': 'KCK'},
    'PAS': {'suit': 'D', 'unit': 'AIR RAIDERS', 'pos': 'WR/TE/RB', 'save': 'CAT'}
}
WEEK_DAYS = ["Media Monday", "Training Tuesday", "Waiver Wednesday", "Travel Thursday", "GAME DAY"]

# --- [2] SYSTEM UTILITIES ---

def get_fresh_deck():
    suits = ['C', 'H', 'S', 'D']
    # Range 2-14 (A) + 15 (JKR)
    deck = [{'val': r, 'suit': s} for s in suits for r in range(2, 15)]
    deck.append({'val': 15, 'suit': 'JKR'})
    deck.append({'val': 15, 'suit': 'JKR'})
    random.shuffle(deck)
    return deck

def get_display_name(team_data, rank):
    # Tiered name logic from Definitive
    return team_data['tiers'].get(rank, team_data['name'])

def init_stats():
    # Maps generic stats to the Logbook Saving Throws
    for t in TEAMS:
        TEAMS[t]['save'] = {
            'STA': TEAMS[t]['stats']['TKL'],
            'SPD': TEAMS[t]['stats']['AWR'],
            'KCK': TEAMS[t]['stats']['INT'],
            'CAT': TEAMS[t]['stats']['PAS']
        }
        TEAMS[t]['playbook'] = ["[EMPTY SLOT]"] * 5
        TEAMS[t]['record'] = {'W': 0, 'L': 0, 'T': 0}

# --- [3] SESSION STATE INIT ---
if 'init_done' not in st.session_state:
    init_stats()
    st.session_state.game_mode = 'MENU'
    st.session_state.match_active = False
    st.session_state.dynasty_data = None
    st.session_state.draft_data = None
    st.session_state.init_done = True

# --- [4] MECHANICS: BOT LOGIC (With Recycling) ---
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
    
    # 4. Pick Best Suit (Logic from Definitive.py)
    if bot_is_driving:
        priority = ["D", "H"] # Offense Pref
        if not any(groups[s] for s in priority): priority = ["C", "S"]
    else:
        priority = ["C", "S"] # Defense Pref
        if not any(groups[s] for s in priority): priority = ["D", "H"]
        
    best_suit = max(priority, key=lambda s: sum(groups[s]) if groups[s] else 0)
    # Fallback
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
    
    # --- RECYCLING (Crucial Feature) ---
    unused_cards = [c for c in hand if c['suit'] != best_suit and c['val'] != 15]
    for card in unused_cards:
        bot_deck.insert(0, card)

    # Display String
    display = "".join([f"[{SYMBOLS.get(best_suit, '?')} {v}] " for v in groups[best_suit]])
    if 15 in hand_vals: display += "[JKR] "
    
    return sum(groups[best_suit]), best_suit, max(groups[best_suit]+[0]), display, special

# --- [5] MECHANICS: COMPLICATION RESOLVER (Logbook D4) ---
def resolve_complication_web(u_team, b_team, u_driving, u_name, b_name):
    # Based on DEFINITIVE.py D4 Table
    d4 = random.randint(1, 4)
    # Mapping: 1=STA(TKL), 2=CAT(PAS), 3=KCK(INT), 4=SPD(AWR) note: Definitive used generic, Logbook is specific
    # We use the Logbook keys from UNIT_MAP logic
    
    st.markdown(f"**[!] COMPLICATION ROLLED (D4):** {d4}")
    
    points, flip = 0, False
    user_failed = False
    
    if d4 == 1: # SACK (STA CHECK)
        st.write(f"   > **SACK ATTEMPT** (Check vs STA)")
        u_roll = random.randint(1, 6) + u_team['save']['STA']
        b_roll = random.randint(1, 6) + b_team['save']['STA']
        st.caption(f"{u_name} ({u_roll}) vs {b_name} ({b_roll})")
        user_failed = u_roll < b_roll
        
        if u_driving and user_failed:
             st.error("   >>> QG SACKED! (+2 PTS). Possession Flip!"); points = 2; flip = True
        elif not u_driving and not user_failed:
             st.success("   >>> QG SACKED! (+2 PTS). Possession Flip!"); points = 2; flip = True
        else: st.info("   >>> TACKLE SHED! Play continues.")

    elif d4 == 2: # OOB (CAT CHECK)
        st.write(f"   > **OUT OF BOUNDS** (Check vs CAT)")
        st.info("   >>> Play RESET to Neutral Snap Point.")

    elif d4 == 3: # PENALTY (KCK CHECK)
        st.write(f"   > **PENALTY** (Check vs KCK)")
        u_roll = random.randint(1, 6) + u_team['save']['KCK']
        b_roll = random.randint(1, 6) + b_team['save']['KCK']
        user_failed = u_roll < b_roll
        
        if user_failed: st.error("   >>> PERSONAL FOUL! Opponent +3 PTS."); points = 3
        else: st.success("   >>> DISCIPLINED! No foul.")

    elif d4 == 4: # INT (SPD/AWR CHECK)
        st.write(f"   > **INTERCEPTION** (Check vs SPD)")
        u_roll = random.randint(1, 6) + u_team['save']['SPD']
        b_roll = random.randint(1, 6) + b_team['save']['SPD']
        user_failed = u_roll < b_roll
        
        if u_driving and user_failed:
            st.error("   >>> TURNOVER! (+1 Momentum PT)"); points = 1; flip = True
        elif not u_driving and not user_failed:
            st.success("   >>> PICKED OFF! (+1 PT)"); points = 1; flip = True
        else: st.info("   >>> INCOMPLETE/DROPPED!")

    time.sleep(1.5)
    return user_failed, points, flip

# =======================================================
#               DYNASTY ENGINE
# =======================================================

def init_dynasty(user_id, league_rank):
    # Generates a 7-Week Season (Divisional Round Robin + 2 OOC)
    schedule = []
    
    # 1. Find User Region
    u_reg = TEAMS[user_id]['region']
    div_rivals = [tid for tid, data in TEAMS.items() if data['region'] == u_reg and tid != user_id]
    others = [tid for tid, data in TEAMS.items() if data['region'] != u_reg]
    random.shuffle(others)
    
    # 3 Division Games + 4 Random
    opponents = div_rivals + others[:4]
    random.shuffle(opponents)
    
    for i, opp in enumerate(opponents):
        schedule.append({
            'week': i+1, 'opp_id': opp, 'result': None, 'score': None, 'played': False
        })
        
    return {
        'user_id': user_id,
        'league_rank': league_rank,
        'schedule': schedule,
        'current_week': 1,
        'day_index': 0, # 0=Monday
        'standings': {t: {'W':0, 'L':0, 'T':0} for t in TEAMS}
    }

def sim_rest_of_league(dynasty_data):
    # Simulates games for all non-user teams
    # This keeps the "League Table" alive
    user_id = dynasty_data['user_id']
    current_opp = dynasty_data['schedule'][dynasty_data['current_week']-1]['opp_id']
    
    active_teams = [t for t in TEAMS if t != user_id and t != current_opp]
    random.shuffle(active_teams)
    
    while len(active_teams) >= 2:
        t1 = active_teams.pop()
        t2 = active_teams.pop()
        
        # Simple weighted sim based on stats sum
        s1 = sum(TEAMS[t1]['stats'].values()) + random.randint(0,5)
        s2 = sum(TEAMS[t2]['stats'].values()) + random.randint(0,5)
        
        standings = dynasty_data['standings']
        if s1 > s2: standings[t1]['W']+=1; standings[t2]['L']+=1
        elif s2 > s1: standings[t2]['W']+=1; standings[t1]['L']+=1
        else: standings[t1]['T']+=1; standings[t2]['T']+=1

# =======================================================
#               UI MODULES
# =======================================================

def render_sidebar():
    with st.sidebar:
        st.title("[ NRBL LOGBOOK ]")
        st.write("COMMISSIONER ACCESS")
        st.markdown("---")
        
        if st.session_state.game_mode == 'DYNASTY':
            dd = st.session_state.dynasty_data
            u_team = TEAMS[dd['user_id']]
            st.header(f"{u_team['name']}")
            rec = dd['standings'][dd['user_id']]
            st.caption(f"REGION: {u_team['region']} | RECORD: {rec['W']}-{rec['L']}-{rec['T']}")
            
            st.markdown("#### UNIT ROSTER")
            # Logbook Style Stats
            for stat, meta in UNIT_MAP.items():
                val = u_team['stats'][stat]
                st.write(f"**{SYMBOLS[meta['suit']]} {meta['unit']}**: {val}")
                st.caption(f"({meta['pos']}) - {meta['save']} Save")
                
            st.markdown("---")
            st.write(f"**ERA:** {ERAS['STANDARD']['name']}")
            
        elif st.session_state.game_mode == 'MATCH':
            md = st.session_state.match_data
            st.header("MATCH IN PROGRESS")
            c1, c2 = st.columns(2)
            c1.metric("USER", md['u_score'])
            c2.metric("CPU", md['b_score'])
            st.write(f"**POSSESSION:** {'USER' if md['u_driving'] else 'CPU'}")
            st.write(f"**TIMEOUTS:** {md['u_timeouts']}")
            st.write(f"**BOT DECK:** {len(md['bot_deck'])}")
            
        else:
            st.info("Select a mode to initialize Logbook.")

def render_match_engine():
    # The Core Gameplay Loop
    if 'match_state' not in st.session_state: st.session_state.match_state = 'KICKOFF'
    md = st.session_state.match_data
    
    # 1. KICKOFF
    if st.session_state.match_state == 'KICKOFF':
        st.subheader(f"WEEK {md.get('week', 'Ex')} KICKOFF")
        st.write(f"**{md['u_name']}** vs **{md['b_name']}**")
        if st.button("COIN TOSS"):
            if random.choice([True, False]):
                st.success("WON TOSS! You receive.")
                md['u_driving'] = True
            else:
                st.error("LOST TOSS! You defend.")
                md['u_driving'] = False
            time.sleep(1)
            st.session_state.match_state = 'TACTICS'
            st.rerun()

    # 2. TACTICS
    elif st.session_state.match_state == 'TACTICS':
        rank = md['league_rank']
        st.markdown(f"### TACTICAL PHASE (Rank {rank})")
        
        c1, c2 = st.columns([3,1])
        with c1:
            with st.form("tactics"):
                nc = st.slider("Cards to Commit", 1, rank, 1)
                if st.form_submit_button("BREAK HUDDLE"):
                    st.session_state.num_cards = nc
                    st.session_state.match_state = 'INPUT'
                    st.rerun()
        with c2:
            if st.button("TIMEOUT (T)"):
                if md['u_timeouts']>0: 
                    md['u_timeouts']-=1; md['bot_deck']=get_fresh_deck()
                    st.toast("Timeout! Deck Reshuffled.")
                else: st.error("None left!")

    # 3. INPUT
    elif st.session_state.match_state == 'INPUT':
        st.markdown("### PLAYCALL INPUT")
        st.caption("Format: 'D 13', 'H K', 'S 10' or 'JKR'")
        with st.form("inputs"):
            cols = st.columns(st.session_state.num_cards)
            cards = []
            for i, col in enumerate(cols):
                cards.append(col.text_input(f"Card {i+1}"))
            
            if st.form_submit_button("HIKE BALL"):
                # Processing Logic
                u_cards, u_hand, u_val, u_suit, u_max = [], [], 0, "", 0
                v_map = {'J':11, 'Q':12, 'K':13, 'A':14, 'JKR':15}
                played_jkr = False
                
                for i, c in enumerate(cards):
                    raw = c.upper().split()
                    if len(raw)<2: s, vr = ("JKR", "15") if "JKR" in c.upper() else ("C", "2")
                    else: s, vr = raw[0], raw[1]
                    
                    try: v = int(vr)
                    except: v = v_map.get(vr, 2)
                    
                    if v==15 or s=="JKR": u_cards.append("[JKR]"); played_jkr=True
                    else: u_cards.append(f"[{SYMBOLS.get(s,'?')} {vr}]")
                    
                    u_val += v
                    if i==0: u_suit = s
                    if v > u_max: u_max = v
                    u_hand.append({'val':v, 'suit':s})
                
                # Special Check
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

    # 4. RESOLVE (Flavor Heavy)
    elif st.session_state.match_state == 'RESOLVE':
        pd = st.session_state.play_data
        b_val, b_suit, b_max, b_disp, b_spec = smart_bot_logic(md['league_rank'], not md['u_driving'], md['bot_deck'])
        
        st.write(f"**YOU:** {' '.join(pd['u_cards'])}")
        time.sleep(0.5)
        st.write(f"**OPP:** {b_disp}")
        time.sleep(0.5)
        
        over = False
        # Joker Flavor Text from DEFINITIVE.py
        if pd['u_spec'] or b_spec or pd['u_jkr']:
            st.markdown("### >>> JOKER TRIGGERED! <<<")
            
            if pd['u_spec']:
                if pd['u_spec'] == "JUKE" and md['u_driving']: md['u_score']+=5; st.success("JUKE! Ankle breaker to ENDZONE! (+5)"); md['u_driving']=False; over=True
                elif pd['u_spec'] == "STIFF_ARM" and md['u_driving']: md['u_score']+=5; st.success("STIFF ARM! Shaken tackles... (+5)"); md['u_driving']=False; over=True
                elif pd['u_spec'] == "STRIP" and not md['u_driving']: md['u_score']+=1; st.success("BUTTER FINGERS! Fumble recovered! (+1)"); md['u_driving']=True; over=True
                elif pd['u_spec'] == "SCRUM": st.warning("SCRIMMAGE! Stalemate triggered. Possession Flips."); md['u_driving'] = not md['u_driving']; over=True
            
            elif b_spec and not over:
                 st.error(f"BOT USES {b_spec}!")
                 if b_spec == "JUKE" and not md['u_driving']: md['b_score']+=5; md['u_driving']=True; over=True
                 elif b_spec == "STIFF_ARM" and not md['u_driving']: md['b_score']+=5; md['u_driving']=True; over=True
                 elif b_spec == "STRIP" and md['u_driving']: md['b_score']+=1; md['u_driving']=False; over=True
                 elif b_spec == "SCRUM": md['u_driving'] = not md['u_driving']; over=True
            time.sleep(2)

        if not over:
            st.write("Rolling Physics (D66)...")
            b_hits = sum(1 for _ in range(2) if random.randint(1,6) <= md['league_rank'])
            u_d1, u_d2 = random.randint(1,6), random.randint(1,6)
            u_hits = (1 if u_d1 <= md['league_rank'] else 0) + (1 if u_d2 <= md['league_rank'] else 0)
            
            st.write(f"YOU: {u_hits} hits | OPP: {b_hits} hits")
            
            if u_hits != b_hits:
                win = u_hits > b_hits
                winner = md['u_name'] if win else md['b_name']
                ws = pd['u_suit'] if win else b_suit
                wm = pd['u_max'] if win else b_max
                st.markdown(f"**WINNER:** {winner} ({SYMBOLS.get(ws,'?')})")
                
                # Scoring Logic
                if (win and md['u_driving']) or (not win and not md['u_driving']):
                    pts = 0
                    if ws == "D" and wm == 13: pts=3; st.success("KICK PASS! Aim high at GOAL POST! (+3)")
                    elif ws in ["D", "H"]: pts=5; st.success("TRY SUCCESSFUL! Reaches ENDZONE! (+5)")
                    else: st.info("MARCHING! Gains significant yardage.")
                    
                    if pts > 0:
                        if win: md['u_score'] += pts
                        else: md['b_score'] += pts
                        md['u_driving'] = not md['u_driving']
                else:
                    st.info("DEFENSIVE STOPPAGE! No Points.")
                    md['u_driving'] = not md['u_driving']
            else:
                st.warning("STALEMATE!")
                st.session_state.match_state = 'STALEMATE'
                st.rerun()

        # End Check
        if md['u_score'] >= 25 or md['b_score'] >= 25:
            st.success("MATCH FINAL")
            if st.button("FINISH"):
                if st.session_state.return_mode == 'DYNASTY':
                    # Update Record
                    dd = st.session_state.dynasty_data
                    rec = dd['standings'][dd['user_id']]
                    if md['u_score'] > md['b_score']: rec['W'] += 1
                    elif md['b_score'] > md['u_score']: rec['L'] += 1
                    else: rec['T'] += 1
                    # Log result
                    dd['schedule'][dd['current_week']-1]['result'] = f"{md['u_score']}-{md['b_score']}"
                    dd['schedule'][dd['current_week']-1]['played'] = True
                    dd['current_week'] += 1
                    dd['day_index'] = 0 # Reset week day
                    # Sim rest of league
                    sim_rest_of_league(dd)
                
                st.session_state.game_mode = st.session_state.return_mode
                st.rerun()
        else:
            if st.button("NEXT PLAY"):
                st.session_state.match_state = 'TACTICS'
                st.rerun()

    elif st.session_state.match_state == 'STALEMATE':
        st.info("Line Locked. Call Re-Audible?")
        c1, c2 = st.columns(2)
        if c1.button("YES"): st.session_state.match_state='REAUDIBLE'; st.rerun()
        if c2.button("NO"):
             uf, pts, fl = resolve_complication_web(md['u_team'], md['b_team'], md['u_driving'], md['u_name'], md['b_name'])
             if uf: md['b_score']+=pts
             else: md['u_score']+=pts
             if fl: md['u_driving'] = not md['u_driving']
             if st.button("CONTINUE"): st.session_state.match_state='TACTICS'; st.rerun()

    elif st.session_state.match_state == 'REAUDIBLE':
        rc = st.text_input("Recall Card:")
        if st.button("SUBMIT"):
            st.success("Audible Processed.") # Simplified for web
            st.session_state.match_state = 'TACTICS'; st.rerun()

# =======================================================
#               MAIN NAVIGATION
# =======================================================

render_sidebar()

if st.session_state.game_mode == 'MENU':
    st.title("ROUGHBALL: LOGBOOK EDITION")
    st.markdown("*The Official NRBL Commissioner Suite*")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Quick Play")
        h = st.selectbox("Home Team", list(TEAMS.keys()), format_func=lambda x: TEAMS[x]['name'])
        a = st.selectbox("Away Team", list(TEAMS.keys()), index=1, format_func=lambda x: TEAMS[x]['name'])
        l = st.selectbox("League", list(LEAGUES.keys()), format_func=lambda x: LEAGUES[x]['name'])
        
        if st.button("LAUNCH MATCH"):
            ut, bt = TEAMS[h], TEAMS[a]
            lr = LEAGUES[l]
            st.session_state.match_data = {
                'u_team': ut, 'b_team': bt,
                'u_name': get_display_name(ut, lr['rank']),
                'b_name': get_display_name(bt, lr['rank']),
                'league_rank': lr['rank'],
                'u_score': 0, 'b_score': 0, 'u_driving': True,
                'bot_deck': get_fresh_deck(), 'u_timeouts': 2
            }
            st.session_state.return_mode = 'MENU'
            st.session_state.game_mode = 'MATCH'
            st.rerun()

    with col2:
        st.subheader("Dynasty")
        with st.form("dynasty"):
            team = st.selectbox("Select Franchise", list(TEAMS.keys()), format_func=lambda x: TEAMS[x]['name'])
            league = st.selectbox("Starting Tier", list(LEAGUES.keys()), format_func=lambda x: LEAGUES[x]['name'])
            if st.form_submit_button("BEGIN SEASON"):
                st.session_state.dynasty_data = init_dynasty(team, LEAGUES[league]['rank'])
                st.session_state.game_mode = 'DYNASTY'
                st.rerun()
        
        st.write("---")
        if st.button("MOCK DRAFT MANAGER"):
            st.session_state.game_mode = 'DRAFT'
            st.rerun()

elif st.session_state.game_mode == 'MATCH':
    render_match_engine()

elif st.session_state.game_mode == 'DYNASTY':
    dd = st.session_state.dynasty_data
    u_team = TEAMS[dd['user_id']]
    
    st.title(f"{u_team['name']} | WEEK {dd['current_week']}")
    st.progress((dd['current_week']-1)/7)
    
    # DAILY SCHEDULE LOGIC
    day = WEEK_DAYS[dd['day_index']]
    st.subheader(f"TODAY IS: {day}")
    
    if dd['day_index'] < 4:
        # Pre-Game Days
        if st.button("ADVANCE DAY"):
            dd['day_index'] += 1
            st.rerun()
    else:
        # GAME DAY
        if dd['current_week'] <= 7:
            match = dd['schedule'][dd['current_week']-1]
            opp = TEAMS[match['opp_id']]
            st.warning(f"GAME DAY vs {opp['name']}")
            
            if st.button("PLAY MATCH"):
                lr = LEAGUES[str(dd['league_rank'])]
                st.session_state.match_data = {
                    'u_team': u_team, 'b_team': opp,
                    'u_name': get_display_name(u_team, dd['league_rank']),
                    'b_name': get_display_name(opp, dd['league_rank']),
                    'league_rank': dd['league_rank'],
                    'u_score': 0, 'b_score': 0, 'u_driving': True,
                    'bot_deck': get_fresh_deck(), 'u_timeouts': 2,
                    'week': dd['current_week']
                }
                st.session_state.return_mode = 'DYNASTY'
                st.session_state.game_mode = 'MATCH'
                st.rerun()
        else:
            st.success("SEASON COMPLETE")
            if st.button("EXIT"): st.session_state.game_mode = 'MENU'; st.rerun()
            
    # STANDINGS TABLE
    st.write("---")
    st.subheader("DIVISION STANDINGS")
    rows = []
    for tid, rec in dd['standings'].items():
        t = TEAMS[tid]
        rows.append({'Team': t['name'], 'Region': t['region'], 'W': rec['W'], 'L': rec['L'], 'T': rec['T']})
    df = pd.DataFrame(rows).sort_values(by=['W'], ascending=False)
    st.dataframe(df, hide_index=True)

elif st.session_state.game_mode == 'DRAFT':
    st.title("MOCK DRAFT MANAGER")
    if st.button("RUN SIMULATION (TOP 4 PENALTY ACTIVE)", type="primary"):
        random.seed(time.time())
        st.session_state.draft_results = []
        
        # Rankings Shuffle
        order = list(TEAMS.keys())
        random.shuffle(order)
        
        for rank, tid in enumerate(order):
            team_name = TEAMS[tid]['name']
            picks = 2 if rank < 4 else 4
            status = "PENALTY" if rank < 4 else "STD"
            
            team_picks = []
            for _ in range(picks):
                # Specific Position Logic from LOGBOOK
                unit = random.choice(list(UNIT_MAP.values()))
                pos_specific = random.choice(unit['pos'].split('/'))
                suit_icon = SYMBOLS[unit['suit']]
                
                stars = random.choices([1,2,3,4,5,0], weights=[10,30,30,20,5,5])[0]
                star_str = "★"*stars if stars>0 else "BUST"
                
                team_picks.append(f"{suit_icon} {pos_specific}({star_str})")
            
            while len(team_picks) < 4: team_picks.append("---")
            
            st.session_state.draft_results.append({
                'Rank': rank+1, 'Team': team_name, 'Status': status,
                'R1': team_picks[0], 'R2': team_picks[1], 'R3': team_picks[2], 'R4': team_picks[3]
            })
            
    if 'draft_results' in st.session_state:
        df = pd.DataFrame(st.session_state.draft_results)
        st.dataframe(df, hide_index=True, use_container_width=True)
        
    if st.button("EXIT"): st.session_state.game_mode = 'MENU'; st.rerun()
