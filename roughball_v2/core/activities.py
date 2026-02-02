"""
ROUGHBALL: Weekly Activities Module
Handles Media Monday, Training Tuesday, and Study Wednesday mechanics
"""

import random
import time
from .teams import TEAMS, ERAS
from .dice import roll_d4


def daily_activity_roll(day, team_id, era_id=4):
    """
    Execute daily activity for a team.
    
    Args:
        day: Day of week ("Mon", "Tue", "Wed")
        team_id: Team ID string
        era_id: Era ID for flavor text (1-4)
    
    Returns:
        String describing the activity outcome
    """
    
    team = TEAMS[team_id]
    era_name = ERAS.get(era_id, ERAS[4])['name']
    
    if day == "Mon":
        return media_monday(team, era_id)
    elif day == "Tue":
        return training_tuesday(team, era_id)
    elif day == "Wed":
        return study_wednesday(team, era_id)
    else:
        return f"   > No activity scheduled for {day}"


def media_monday(team, era_id):
    """
    MEDIA MONDAY: d4-1 penalty to random stat
    
    Four event types based on d4 roll:
    1. Press Conference
    2. Radio Interview
    3. Live Show
    4. News Article
    
    Each has era-specific flavor text
    """
    
    # Roll for event type
    event_roll = roll_d4()
    
    # Roll for penalty (d4-1 = 0-3)
    penalty = max(0, roll_d4() - 1)
    
    # Map roll to stat
    stat_map = {1: "TKL", 2: "AWR", 3: "INT", 4: "PAS"}
    target_stat = stat_map[event_roll]
    
    # Apply penalty
    team['boosts'][target_stat] = -penalty
    
    # ERA-SPECIFIC FLAVOR TEXT
    era_events = {
        1: {  # OLD TIMEY
            1: "Prestigious regional media conference at town hall",
            2: "Early morning local radio column on AM waves",
            3: "Morning sports segment at the community center",
            4: "Regional newspaper column by lead sports writer"
        },
        2: {  # GOLDEN AGE
            1: "Scandalous paparazzi interrogation after practice",
            2: "Primetime radio broadcast with call-in questions",
            3: "Late night talk show appearance gone awkward",
            4: "Magazine cover feature with unflattering quotes"
        },
        3: {  # MILLENNIUM
            1: "Corporate-sponsored press presentation with investors",
            2: "Exclusive insider interview on sports radio network",
            3: "Reality TV 'confessions' episode filmed at facility",
            4: "Personal blog article misconstrued by online media"
        },
        4: {  # PANDEMICAL
            1: "Global live-streaming statement analyzed in real-time",
            2: "Podcast clip gone viral on social media platforms",
            3: "Streaming channel feature with chat reactions",
            4: "Viral social media post sparks controversy"
        }
    }
    
    event_names = {
        1: "Press Conference",
        2: "Radio Interview",
        3: "Live Show",
        4: "News Article"
    }
    
    event_desc = era_events[era_id][event_roll]
    event_name = event_names[event_roll]
    
    output = []
    output.append(f"\n[📊 MEDIA MONDAY] {event_name}")
    output.append(f"   Context: {event_desc}")
    
    if penalty == 0:
        output.append(f"   > Media appearance was NEUTRAL. No impact on team morale.")
    else:
        output.append(f"   > Media CRITICISM affects {target_stat}: -{penalty} for this week!")
    
    time.sleep(2)
    return "\n".join(output)


def training_tuesday(team, era_id):
    """
    TRAINING TUESDAY: USER CHOICE drill for d4-1 bonus
    
    Four drill categories (Base Stats or Saving Throws):
    1. Rush Tackles (TKL) / Scrum Locks (STA)
    2. Box Snaps (AWR) / Carrier Sprints (SPD)
    3. Pursuit Tackling (INT) / Post Kicking (KCK)
    4. Shuffle Passing (PAS) / Contested Catching (CAT)
    
    User chooses focus, system rolls d4-1 for bonus (0-3)
    """
    
    # ERA-SPECIFIC FACILITIES
    era_facilities = {
        1: "Muddy training field with wooden goalposts",
        2: "Professional sports arena dome with turf",
        3: "Corporate-funded stadium with latest equipment",
        4: "Private facility HQ with VR training systems"
    }
    
    facility = era_facilities.get(era_id, era_facilities[4])
    
    print(f"\n[🏋️ TRAINING TUESDAY] Select Weekly Focus")
    print(f"   Facility: {facility}\n")
    print("   [1] ♣ Rush Tackles (TKL) / Scrum Locks (STA)")
    print("   [2] ♥ Box Snaps (AWR) / Carrier Sprints (SPD)")
    print("   [3] ♠ Pursuit Tackling (INT) / Post Kicking (KCK)")
    print("   [4] ♦ Shuffle Passing (PAS) / Contested Catching (CAT)")
    
    choice = input("\n   > Choice (1-4): ")
    
    # Validate input
    if choice not in ['1', '2', '3', '4']:
        print("   (!) Invalid choice, defaulting to Rush Tackles")
        choice = '1'
    
    # Map choice to stats
    drill_map = {
        '1': ('TKL', 'STA', 'Rush Tackles / Scrum Locks'),
        '2': ('AWR', 'SPD', 'Box Snaps / Carrier Sprints'),
        '3': ('INT', 'KCK', 'Pursuit Tackling / Post Kicking'),
        '4': ('PAS', 'CAT', 'Shuffle Passing / Contested Catching')
    }
    
    primary_stat, save_stat, drill_name = drill_map[choice]
    
    # Roll for bonus (d4-1 = 0-3)
    bonus = max(0, roll_d4() - 1)
    
    # Apply bonus to BOTH primary stat AND saving throw
    team['boosts'][primary_stat] = bonus
    if 'save_boosts' not in team:
        team['save_boosts'] = {'STA': 0, 'SPD': 0, 'KCK': 0, 'CAT': 0}
    team['save_boosts'][save_stat] = bonus
    
    output = []
    output.append(f"\n   > DRILL FOCUS: {drill_name}")
    
    if bonus == 0:
        output.append(f"   > BAD PRACTICE: Players looked sluggish. No bonus.")
    else:
        output.append(f"   > TRAINING RESULTS: {primary_stat} +{bonus} | {save_stat} +{bonus} for this week!")
    
    time.sleep(2)
    print("\n".join(output))
    return "\n".join(output)


def study_wednesday(team, era_id):
    """
    STUDY WEDNESDAY: d4-1 bonus to random saving throw
    
    Four study methods based on d4 roll:
    1. Blackboard Lecture (STA)
    2. Film Review (SPD)
    3. Playbook Design (KCK)
    4. Rivalry Analytics (CAT)
    
    Each has era-specific flavor text
    """
    
    # Roll for method type
    method_roll = roll_d4()
    
    # Roll for bonus (d4-1 = 0-3)
    bonus = max(0, roll_d4() - 1)
    
    # Map roll to saving throw
    save_map = {1: "STA", 2: "SPD", 3: "KCK", 4: "CAT"}
    target_save = save_map[method_roll]
    
    # Apply bonus
    if 'save_boosts' not in team:
        team['save_boosts'] = {'STA': 0, 'SPD': 0, 'KCK': 0, 'CAT': 0}
    team['save_boosts'][target_save] = bonus
    
    # ERA-SPECIFIC FLAVOR TEXT
    era_methods = {
        1: {  # OLD TIMEY
            1: "Sticks drawn in sandbox, chalk on makeshift boards",
            2: "Photographed stills and grainy 8mm film reels",
            3: "Handwritten callouts and secret signaling practice",
            4: "Word of mouth rumors and local gossip intelligence"
        },
        2: {  # GOLDEN AGE
            1: "Chalk and blackboards in proper lecture hall",
            2: "VHS tapes from handycam recordings, frame-by-frame",
            3: "Scribbled notepads with detailed route diagrams",
            4: "Surveillance-style espionage on rival teams"
        },
        3: {  # MILLENNIUM
            1: "Projector presentations in modern lecture theater",
            2: "DVD replay highlights compiled and categorized",
            3: "Thick-bound textbook with laminated play sheets",
            4: "Excel spreadsheet analysis with statistical models"
        },
        4: {  # PANDEMICAL
            1: "Online campus Zoom meeting with screen sharing",
            2: "Instant tablet clip-reviews with AI breakdowns",
            3: "Virtual online playbook with 3D formations",
            4: "VR predictive simulations of opponent tendencies"
        }
    }
    
    method_names = {
        1: "Blackboard Lecture",
        2: "Film Review",
        3: "Playbook Design",
        4: "Rivalry Analytics"
    }
    
    method_desc = era_methods[era_id][method_roll]
    method_name = method_names[method_roll]
    
    output = []
    output.append(f"\n[📚 STUDY WEDNESDAY] {method_name}")
    output.append(f"   Method: {method_desc}")
    
    if bonus == 0:
        output.append(f"   > Study session was DISTRACTED. No focus gained.")
    else:
        output.append(f"   > TECHNICAL FOCUS: {target_save} +{bonus} saving throw bonus!")
    
    time.sleep(2)
    return "\n".join(output)


# Weekly schedule reference
WEEKLY_SCHEDULE = {
    "Mon": {
        "name": "MEDIA MONDAY",
        "desc": "Public Image Management",
        "function": media_monday
    },
    "Tue": {
        "name": "TRAINING TUESDAY",
        "desc": "Physical Drill Focus",
        "function": training_tuesday
    },
    "Wed": {
        "name": "STUDY WEDNESDAY",
        "desc": "Film Room & Analytics",
        "function": study_wednesday
    },
    "Thu": {
        "name": "BACKYARD THURSDAY",
        "desc": "D4 Amateur Scrimmage",
        "division": "2"
    },
    "Fri": {
        "name": "HIGH SCHOOL FRIDAY",
        "desc": "D3 Prospects Match",
        "division": "3"
    },
    "Sat": {
        "name": "COLLEGE SATURDAY",
        "desc": "D2 Superstar Showdown",
        "division": "4"
    },
    "Sun": {
        "name": "NATIONAL SUNDAY",
        "desc": "D1 National Bad Blood",
        "division": "5"
    }
}
