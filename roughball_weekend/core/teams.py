"""
ROUGHBALL: Team Data Module
Contains all 16 NRBL teams with stats, locations, and tier systems
"""

TEAMS = {
    "1": {
        "name": "Mountain LIONS",
        "stats": {'TKL': 8, 'AWR': 4, 'INT': 7, 'PAS': 6},
        "loc": "Pike Brown",
        "region": "North",
        "is_founder": True,
        "emoji": "🏔️🦁",
        "nickname": "Mountain Rugged",
        "tiers": {
            5: "Mountain LIONS",
            4: "College Wildcats",
            3: "High School Lynx",
            2: "Backyard Cougars",
            1: "Northern Rookies"
        }
    },
    "2": {
        "name": "Greenland VIKINGS",
        "stats": {'TKL': 6, 'AWR': 7, 'INT': 8, 'PAS': 4},
        "loc": "Green Hills",
        "region": "North",
        "is_founder": True,
        "emoji": "🛶👑",
        "nickname": "Land Raiders",
        "tiers": {
            5: "Greenland VIKINGS",
            4: "College Celtics",
            3: "High School Warriors",
            2: "Backyard Maulers",
            1: "Greenland Rookies"
        }
    },
    "3": {
        "name": "Southern FARMERS",
        "stats": {'TKL': 8, 'AWR': 7, 'INT': 6, 'PAS': 4},
        "loc": "Great Countryside",
        "region": "South",
        "is_founder": True,
        "emoji": "🚜👨‍🌾",
        "nickname": "Southern Hostility",
        "tiers": {
            5: "Southern FARMERS",
            4: "College Cattle",
            3: "High School Hillbillies",
            2: "Backyard Rednecks",
            1: "Great Rookies"
        }
    },
    "4": {
        "name": "Coast SHARKS",
        "stats": {'TKL': 7, 'AWR': 5, 'INT': 8, 'PAS': 5},
        "loc": "Southern Coast",
        "region": "South",
        "is_founder": True,
        "emoji": "🌊🦈",
        "nickname": "Tide Predators",
        "tiers": {
            5: "Coast SHARKS",
            4: "College Hammerheads",
            3: "High School Gators",
            2: "Backyard Marlins",
            1: "Coastal Rookies"
        }
    },
    "5": {
        "name": "Eastern EAGLES",
        "stats": {'TKL': 5, 'AWR': 9, 'INT': 6, 'PAS': 5},
        "loc": "Lake Brown",
        "region": "East",
        "is_founder": True,
        "emoji": "🧭🦅",
        "nickname": "Birds of Prey",
        "tiers": {
            5: "Eastern EAGLES",
            4: "College Crows",
            3: "High School Ravens",
            2: "Backyard Vultures",
            1: "Brown Rookies"
        }
    },
    "6": {
        "name": "City PATRIOTS",
        "stats": {'TKL': 6, 'AWR': 5, 'INT': 5, 'PAS': 9},
        "loc": "Eastern City",
        "region": "East",
        "is_founder": True,
        "emoji": "🏙️🏳️",
        "nickname": "Founding Fathers",
        "tiers": {
            5: "City PATRIOTS",
            4: "College Colonels",
            3: "High School Admirals",
            2: "Backyard Sentinels",
            1: "City Rookies"
        }
    },
    "7": {
        "name": "Western BEARS",
        "stats": {'TKL': 7, 'AWR': 7, 'INT': 6, 'PAS': 5},
        "loc": "Red Desert",
        "region": "West",
        "is_founder": True,
        "emoji": "🧭🐻",
        "nickname": "Bruiser Brawlers",
        "tiers": {
            5: "Western BEARS",
            4: "College Bruins",
            3: "High School Grizzlies",
            2: "Backyard Cubs",
            1: "Red Rookies"
        }
    },
    "8": {
        "name": "Beach PIRATES",
        "stats": {'TKL': 5, 'AWR': 8, 'INT': 6, 'PAS': 6},
        "loc": "Western Beach",
        "region": "West",
        "is_founder": True,
        "emoji": "🏖️🏴‍☠️",
        "nickname": "Treasure Looters",
        "tiers": {
            5: "Beach PIRATES",
            4: "College Raiders",
            3: "High School Bandits",
            2: "Backyard Outlaws",
            1: "Beach Rookies"
        }
    },
    "9": {
        "name": "Pike PANTHERS",
        "stats": {'TKL': 8, 'AWR': 5, 'INT': 7, 'PAS': 5},
        "loc": "Pike Brown",
        "region": "North",
        "is_founder": False,
        "emoji": "🏔️🐆",
        "nickname": "Peak Predators",
        "tiers": {
            5: "Pike PANTHERS",
            4: "College Jaguars",
            3: "High School Tigers",
            2: "Backyard Bobcats",
            1: "Pike Rookies"
        }
    },
    "10": {
        "name": "Greenland SAINTS",
        "stats": {'TKL': 7, 'AWR': 5, 'INT': 9, 'PAS': 4},
        "loc": "Greenland Hills",
        "region": "North",
        "is_founder": False,
        "emoji": "⛰️⚜️",
        "nickname": "Heaven's Gate",
        "tiers": {
            5: "Greenland SAINTS",
            4: "College Monks",
            3: "High School Friars",
            2: "Backyard Preachers",
            1: "Hill Rookies"
        }
    },
    "11": {
        "name": "Countryside STALLIONS",
        "stats": {'TKL': 7, 'AWR': 8, 'INT': 6, 'PAS': 4},
        "loc": "Great Countryside",
        "region": "South",
        "is_founder": False,
        "emoji": "🐎🌾",
        "nickname": "Country Work",
        "tiers": {
            5: "Countryside STALLIONS",
            4: "College Mustangs",
            3: "High School Broncos",
            2: "Backyard Colts",
            1: "Countryside Rookies"
        }
    },
    "12": {
        "name": "Southern STINGRAYS",
        "stats": {'TKL': 6, 'AWR': 5, 'INT': 8, 'PAS': 6},
        "loc": "Southern Coast",
        "region": "South",
        "is_founder": False,
        "emoji": "🌊🪼",
        "nickname": "Coastal Speed",
        "tiers": {
            5: "Southern STINGRAYS",
            4: "College Dolphins",
            3: "High School Seals",
            2: "Backyard Squids",
            1: "Southern Rookies"
        }
    },
    "13": {
        "name": "City ROYALS",
        "stats": {'TKL': 5, 'AWR': 5, 'INT': 6, 'PAS': 9},
        "loc": "Eastern City",
        "region": "East",
        "is_founder": False,
        "emoji": "👑🏙️",
        "nickname": "Elite Passing",
        "tiers": {
            5: "City ROYALS",
            4: "College Knights",
            3: "High School Ambassadors",
            2: "Backyard Legionnaires",
            1: "Eastern Rookies"
        }
    },
    "14": {
        "name": "Eastern SEAHAWKS",
        "stats": {'TKL': 5, 'AWR': 9, 'INT': 6, 'PAS': 5},
        "loc": "Lake Brown",
        "region": "East",
        "is_founder": False,
        "emoji": "🌊🦅",
        "nickname": "Pure Awareness",
        "tiers": {
            5: "Eastern SEAHAWKS",
            4: "College Pelicans",
            3: "High School Skimmers",
            2: "Backyard Talons",
            1: "Lake Rookies"
        }
    },
    "15": {
        "name": "Desert SCORPIONS",
        "stats": {'TKL': 7, 'AWR': 6, 'INT': 5, 'PAS': 7},
        "loc": "Red Desert",
        "region": "West",
        "is_founder": False,
        "emoji": "🦂🏜️",
        "nickname": "Arid Desert",
        "tiers": {
            5: "Desert SCORPIONS",
            4: "College Spiders",
            3: "High School Stingers",
            2: "Backyard Snakes",
            1: "Desert Rookies"
        }
    },
    "16": {
        "name": "Beach SURGERS",
        "stats": {'TKL': 4, 'AWR': 7, 'INT': 6, 'PAS': 9},
        "loc": "Western Beach",
        "region": "West",
        "is_founder": False,
        "emoji": "🌊⚡",
        "nickname": "Tsunami Build",
        "tiers": {
            5: "Beach SURGERS",
            4: "College Volts",
            3: "High School Chargers",
            2: "Backyard Hurricanes",
            1: "Western Rookies"
        }
    }
}

# Initialize team data (saving throws, boosts, playbooks)
for team_id in TEAMS:
    team = TEAMS[team_id]
    
    # Saving throws (derived from primary stats)
    team['save'] = {
        'STA': team['stats']['TKL'],  # Stamina from Tackling
        'SPD': team['stats']['AWR'],  # Speed from Awareness
        'KCK': team['stats']['INT'],  # Kicking from Intercept
        'CAT': team['stats']['PAS']   # Catching from Passing
    }
    
    # Temporary boosts (from weekly activities)
    team['boosts'] = {'TKL': 0, 'AWR': 0, 'INT': 0, 'PAS': 0}
    team['save_boosts'] = {'STA': 0, 'SPD': 0, 'KCK': 0, 'CAT': 0}
    
    # Playbook slots (5 for D1 National Legends)
    team['playbook'] = ["[EMPTY]"] * 5
    
    # Dynasty stats
    team['rivals'] = []
    team['prestige'] = 0


# Configuration dictionaries
LEAGUES = {
    "1": {"name": "D5 - Unranked Rookies", "rank": 1, "slots": 1},
    "2": {"name": "D4 - Backyard Amateurs", "rank": 2, "slots": 2},
    "3": {"name": "D3 - High School Pros", "rank": 3, "slots": 3},
    "4": {"name": "D2 - College Superstars", "rank": 4, "slots": 4},
    "5": {"name": "D1 - National Legends", "rank": 5, "slots": 5}
}

ERAS = {
    1: {"name": "OLD TIMEY", "desc": "Founding Era - Leather Helmets"},
    2: {"name": "GOLDEN AGE", "desc": "Broadcast Era - Iconic Figures"},
    3: {"name": "MILLENNIUM", "desc": "Corporate Era - Capital Expansion"},
    4: {"name": "PANDEMICAL", "desc": "Virtual Era - Streampocalypse"}
}

SYMBOLS = {"C": "♣", "H": "♥", "S": "♠", "D": "♦", "JKR": "JKR"}

SUITS = {"C": "TKL", "H": "AWR", "S": "INT", "D": "PAS"}

SUIT_NAMES = {
    "TKL": "Scrimmagers",
    "AWR": "Field Generals",
    "INT": "Pitch Guards",
    "PAS": "Air Raiders"
}

def get_tier_name(team, division_rank):
    """Get team name for specific division tier"""
    return team['tiers'].get(division_rank, team['name'])
