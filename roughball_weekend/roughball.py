#!/usr/bin/env python3
"""
ROUGHBALL: WEEKEND PROTOTYPE
Main entry point
"""

import sys
import time
from core.display import clear, print_header
from core.match import run_match


def main():
    """
    Main menu loop
    
    YOUR EXACT FORMAT PRESERVED
    """
    
    while True:
        clear()
        print("=" * 60)
        print("   ROUGHBALL: END-GAME SIMULATOR v10.0 (WEEKEND BUILD)")
        print("=" * 60)
        print("[1] QUICK MATCH (Original Simulator)")
        print("[2] ACTIVITIES PREVIEW (See Your Tables)")
        print("[3] EXIT BIG LEAGUES...")
        
        choice = input("\nSelect Mode: ")
        
        if choice == '1':
            run_quick_match()
        
        elif choice == '2':
            show_activities_preview()
        
        elif choice == '3' or choice.lower() == 'q':
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
    print("5. Eastern EAGLES      | 13. City ROYALS")
    print("6. City PATRIOTS       | 14. Eastern SEAHAWKS")
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


def show_activities_preview():
    """
    Show preview of activities tables
    (Full implementation in BUILD 2)
    """
    
    clear()
    print_header("WEEKLY ACTIVITIES PREVIEW")
    
    print("""
This is a preview of the activities system that will be
fully implemented in BUILD 2: WEEK SPRINT.

=== MEDIA MONDAY ===
Events (d4-1 penalty to random stat):
1. Press Conference
   - prestigious regional media event (Old-Timey)
   - scandalous paparazzi interrogation (Golden Age)
   - corporate sponsored presentation (Millennium)
   - global live-streaming statement (Pandemical)

2. Radio Interview
   - early morning local radio column (Old-Timey)
   - primetime radio broadcast (Golden Age)
   - exclusive insider interview on air (Millennium)
   - podcast clip gone viral (Pandemical)

3. Live Show
   - daily morning sports network (Old-Timey)
   - late night talk show (Golden Age)
   - reality tv 'confessions' (Millennium)
   - streaming channel feature (Pandemical)

4. News Article
   - regional newspaper column (Old-Timey)
   - magazine cover chronic (Golden Age)
   - personal blog article (Millennium)
   - viral social media post (Pandemical)

=== TRAINING TUESDAY ===
Drills (d4-1 bonus to selected stat - USER CHOICE):
- ♣ Rush Tackles (TKL) / Scrum Locks (STA)
- ♥ Box Snaps (AWR) / Carrier Sprints (SPD)
- ♠ Pursuit Tackling (INT) / Post Kicking (KCK)
- ♦ Shuffle Passing (PAS) / Contested Catching (CAT)

Facilities by era:
1. muddy training field (Old-Timey)
2. sports arena dome (Golden Age)
3. corpo-funded stadium (Millennium)
4. private facility HQ (Pandemical)

=== STUDY WEDNESDAY ===
Methods (d4-1 bonus to random saving throw):
1. Blackboard Lecture
   - sticks on a sandbox (Old-Timey)
   - chalk and blackboards (Golden Age)
   - projectors in lecture halls (Millennium)
   - online campus zoom meeting (Pandemical)

2. Film Review
   - photographed stills and 8mm film (Old-Timey)
   - vhs tapes taken from handycam (Golden Age)
   - replay highlights compiled onto dvds (Millennium)
   - instant tablet clip-reviews (Pandemical)

3. Playbook Design
   - callouts and signaling (Old-Timey)
   - scribbled out notepads (Golden Age)
   - thick-bound textbook (Millennium)
   - virtual online playbook (Pandemical)

4. Rivalry Analytics
   - word of mouth and rumors (Old-Timey)
   - surveillance-espionage tendencies (Golden Age)
   - computed spreadsheet analysis (Millennium)
   - virtual reality predictive simulations (Pandemical)

=== MATCH DAYS ===
Thu: D4 Backyard Amateur (crackhead vibes: hood brawls, smelly locker rooms)
Fri: D3 High School Pros (highschool sweetheart: lifelong friends, marching band)
Sat: D2 College Superstars (superstar life: private dorms, big arenas)
Sun: D1 National Legends (you made it: huge stadiums, flashing lights, luxury)
    """)
    
    input("\n[PRESS ENTER] To Return to Menu...")


if __name__ == "__main__":
    main()
