#!/usr/bin/env python3
"""
ROUGHBALL: WEEKEND PROTOTYPE + WEEK SPRINT
Main entry point with Quick Match and Dynasty Mode
"""

import sys
import time
from core.display import clear, print_header
from core.match import run_match
from core.teams import TEAMS, LEAGUES, ERAS, get_tier_name
from core.activities import daily_activity_roll, WEEKLY_SCHEDULE
from core.draft import full_roster_draft, seasonal_draft, mock_draft_scouting


def main():
    """
    Main menu loop
    
    YOUR EXACT FORMAT PRESERVED
    """
    
    while True:
        clear()
        print("=" * 60)
        print("   ROUGHBALL: END-GAME SIMULATOR v10.3 (LORE-ACCURATE)")
        print("=" * 60)
        print("[1] QUICK MATCH (Original Simulator)")
        print("[2] DYNASTY MODE (Gladiator Schedule)")
        print("[3] THE DRAFT (Roster Management)")
        print("[4] EXIT BIG LEAGUES...")
        
        choice = input("\nSelect Mode: ")
        
        if choice == '1':
            run_quick_match()
        
        elif choice == '2':
            run_dynasty()
        
        elif choice == '3':
            run_draft_mode()
        
        elif choice == '4' or choice.lower() == 'q':
            print("\nExiting...")
            sys.exit()
        
        else:
            print("Invalid Option.")
            time.sleep(1)


def run_quick_match():
    """Quick Match setup and execution"""
    
    clear()
    print_header("QUICK MATCH SETUP")
    
    # Team selection
    print("\n=== TEAM SELECTION ===")
    print("FOUNDERS: 1-8 | EXPANSION: 9-16")
    print()
    print("1. Mountain LIONS      |  9. Pike PANTHERS")
    print("2. Greenland VIKINGS   | 10. Greenland SAINTS")
    print("3. Southern FARMERS    | 11. Countryside STALLIONS")
    print("4. Coast SHARKS        | 12. Southern STINGRAYS")
    print("5. Eastern EAGLES      | 13. Lake SEAHAWKS")
    print("6. City PATRIOTS       | 14. Eastern ROYALS")
    print("7. Western BEARS       | 15. Desert SCORPIONS")
    print("8. Beach PIRATES       | 16. Beach SURGERS")
    
    hid = input("\nHome Team ID (1-16): ")
    aid = input("Away Team ID (1-16): ")
    
    # Division selection
    print("\n=== DIVISION SELECTION ===")
    print("[1] D5 - Unranked Rookies (1 card)")
    print("[2] D4 - Backyard Amateurs (2 cards)")
    print("[3] D3 - High School Pros (3 cards)")
    print("[4] D2 - College Superstars (4 cards)")
    print("[5] D1 - National Legends (5 cards)")
    
    lid = input("\nDivision (1-5): ")
    
    # Era selection
    print("\n=== ERA SELECTION ===")
    print("[1] OLD TIMEY - Founding Era")
    print("[2] GOLDEN AGE - Broadcast Era")
    print("[3] MILLENNIUM - Corporate Era")
    print("[4] PANDEMICAL - Virtual Era")
    
    eid = input("\nEra (1-4): ")
    
    try:
        era_id = int(eid)
    except:
        era_id = 4
    
    # Validate inputs
    if hid not in [str(i) for i in range(1, 17)]:
        hid = "1"
    if aid not in [str(i) for i in range(1, 17)]:
        aid = "2"
    if lid not in [str(i) for i in range(1, 6)]:
        lid = "5"
    
    # Run the match!
    run_match(hid, aid, lid, era_id)


def run_dynasty():
    """
    DYNASTY MODE: 12-Week Gladiator Schedule
    
    Full franchise management with:
    - Weekly activities (Mon-Wed)
    - Match days (Thu-Sun)
    - Stat bonuses/penalties
    - Season progression
    """
    
    clear()
    print_header("DYNASTY MODE - FRANCHISE MANAGEMENT")
    
    # Era Selection
    print("\n=== ERA SELECTION ===")
    for k, v in ERAS.items():
        print(f"[{k}] {v['name']} - {v['desc']}")
    
    try:
        era_id = int(input("\nYour Choice: "))
        if era_id not in ERAS:
            era_id = 4
    except:
        era_id = 4
    
    # Team Selection
    print("\n=== SELECT YOUR FRANCHISE ===")
    print("FOUNDERS: 1-8 | EXPANSION: 9-16")
    print()
    for i in range(1, 17):
        team = TEAMS[str(i)]
        status = "F" if team['is_founder'] else "E"
        print(f"[{i:2d}] {team['name']:25s} {team['emoji']} [{status}]")
    
    try:
        my_team_id = input("\nTeam ID (1-16): ")
        if my_team_id not in TEAMS:
            my_team_id = "1"
    except:
        my_team_id = "1"
    
    my_team = TEAMS[my_team_id]
    franchise_name = my_team['name']
    
    # Determine opponent (bracket pairing)
    bracket_pairs = [
        ("1","9"), ("2","10"), ("3","11"), ("4","12"),
        ("5","13"), ("6","14"), ("7","15"), ("8","16")
    ]
    
    my_opp = "2"
    for a, b in bracket_pairs:
        if a == my_team_id:
            my_opp = b
        elif b == my_team_id:
            my_opp = a
    
    opp_team = TEAMS[my_opp]
    
    # THE GLADIATOR LOOP (12 weeks)
    for week in range(1, 13):
        clear()
        
        # Determine phase
        if week <= 3:
            phase = "LINEAGE QUALIFIERS (PRE-SEASON)"
        elif week <= 6:
            phase = "CARDINAL CARNAGE (REGULAR SEASON)"
        elif week <= 9:
            phase = "BLOOD DISQUALIFIERS (PLAYOFFS)"
        else:
            phase = "ROUGHBALL WILDCARD (OFF-SEASON)"
        
        print("=" * 70)
        print(f" WEEK {week} / 12 | {phase}")
        print(f" ERA: {ERAS[era_id]['name']} | FRANCHISE: {franchise_name} {my_team['emoji']}")
        print("=" * 70)
        
        # DAILY SCHEDULE LOOP
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        
        for day in days:
            day_info = WEEKLY_SCHEDULE[day]
            print(f"\n>>> {day_info['name']}")
            print(f"    {day_info['desc']}")
            
            # Activity Days (Mon-Wed)
            if day in ["Mon", "Tue", "Wed"]:
                result = daily_activity_roll(day, my_team_id, era_id)
                print(result)
                
                if day == "Wed":
                    # Show current stat modifiers after all activities
                    print(f"\n   [WEEK {week} STAT MODIFIERS]")
                    print(f"   TKL: {my_team['boosts']['TKL']:+d} | AWR: {my_team['boosts']['AWR']:+d} | INT: {my_team['boosts']['INT']:+d} | PAS: {my_team['boosts']['PAS']:+d}")
                    if 'save_boosts' in my_team:
                        print(f"   STA: {my_team['save_boosts']['STA']:+d} | SPD: {my_team['save_boosts']['SPD']:+d} | KCK: {my_team['save_boosts']['KCK']:+d} | CAT: {my_team['save_boosts']['CAT']:+d}")
                
                input("\n[PRESS ENTER] To Continue...")
            
            # Match Days (Thu-Sun)
            elif day in ["Thu", "Fri", "Sat", "Sun"]:
                league_key = day_info['division']
                league = LEAGUES[league_key]
                
                t_name = get_tier_name(my_team, league['rank'])
                o_name = get_tier_name(opp_team, league['rank'])
                
                print(f"\n   [{league['name']}]")
                print(f"   {t_name} vs {o_name}")
                print()
                print("   [P] Play Franchise Game")
                print("   [S] Simulate Result")
                print("   [C] Continue (Skip)")
                
                ch = input("\n   > Choice: ").upper()
                
                if ch == 'P':
                    # Play the match
                    run_match(my_team_id, my_opp, league_key, era_id)
                    
                elif ch == 'S':
                    # Simulate with simple random
                    import random
                    u_sim = random.randint(0, 25)
                    b_sim = random.randint(0, 25)
                    print(f"\n   > SIMULATION: {t_name} {u_sim} - {b_sim} {o_name}")
                    time.sleep(2)
                
                # Continue regardless
        
        # End of week
        print("\n" + "=" * 70)
        print(f" END OF WEEK {week}")
        print("=" * 70)
        
        # Reset weekly bonuses
        my_team['boosts'] = {'TKL': 0, 'AWR': 0, 'INT': 0, 'PAS': 0}
        my_team['save_boosts'] = {'STA': 0, 'SPD': 0, 'KCK': 0, 'CAT': 0}
        
        if week == 12:
            print("\n>>> THE SEASON HAS ENDED!")
            print("    Draft Day and roster management coming in BUILD 3...")
            input("\n[PRESS ENTER] To Return to Menu...")
            break
        
        cont = input("\nContinue to next week? (y/n): ").lower()
        if cont != 'y':
            break


def run_draft_mode():
    """
    THE DRAFT MODE: Roster Management
    
    Three sub-modes:
    1. Full 8-Man Roster Draft (New Franchise)
    2. Seasonal 4-Pick Draft (Post-Season)
    3. Mock Draft Scouting Report
    """
    
    while True:
        clear()
        print_header("THE DRAFT - ROSTER MANAGEMENT")
        
        print("\n[1] Full 8-Man Roster Draft (New Franchise)")
        print("[2] Seasonal 4-Pick Draft (Post-Season)")
        print("[3] Mock Draft Scouting Report")
        print("[4] Return to Main Menu")
        
        choice = input("\n> Select option: ").strip()
        
        if choice == "1":
            roster = full_roster_draft()
            # TODO: Save roster to team when franchise mode is integrated
            
        elif choice == "2":
            picks = seasonal_draft()
            # TODO: Add to backup roster when franchise mode is integrated
            
        elif choice == "3":
            user_team = input("\n> Enter your team ID (1-16) to exclude (or press ENTER to skip): ").strip()
            user_team_id = user_team if user_team else None
            mock_draft_scouting(user_team_id)
            
        elif choice == "4":
            break
            
        else:
            print("\n[!] Invalid option. Try again.")
            time.sleep(1)


if __name__ == "__main__":
    main()
