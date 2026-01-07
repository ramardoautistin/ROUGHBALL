[ROUGHBALL SIMULATION SYSTEM - v3.0]
### 1. PLAYCALLING & MOVEMENT MATRIX

     1   2   3   4   5   6   7   8
  |----------------------------------| (Away Endzone + Goal Post)
A |  .   .   .   RB   .   .   .   .  | 
B |  .   .   .   .   QB   .   .   .  | 
C |  WR  .   .   .   .   .    .   TE | 
D |  .   .   DE  OT  DT  OG   .   .  | (OFFENSE)
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx << NEUTRAL SNAP POINT >>
E |  .   .   OG  DT  OT  DE  .    .  | (DEFENSE)
F |  .   .   .   .   .   .   .    .  | 
G |  .   .   .   SG   .   .   .   .  | 
H | CB   .   .   .   SG   .   .   LB | 
  |----------------------------------| (Home Endzone + Goal Post)

## ROUGHBALL STAT & SAVING THROW TABLE
+----------+----------------+----------------+-----------+------------+
| SUIT     | PRIMARY STAT   | SAVING THROW   | PLAY TYPE | POSITION   |
+----------+----------------+----------------+-----------+------------+
|Clubs    ♣| TKL (Tackle)   | STA (Stamina)  | ZONE  ♣   | (DT/DE/LB) |
|Hearts   ♥| AWR (Awareness)| SPD (Speed)    | RUN   ♥   | (QG/RG/SG) |
|Spades   ♠| INT (Intercept)| KCK (Kicking)  | BLITZ ♠   | (OG/OT/CB) |
|Diamonds ♦| PAS (Pass)     | CAT (Catching) | PASS  ♦   | (WB/TB/SG) |
+----------+----------------+----------------+-----------+------------+

## SPECIAL MOVES & SIGNATURE PLAYBOOK (JKR ENFORCEMENT)
+----------+------------------+------------------------------------------+
| SUIT     | SPECIAL MOVE     | EFFECT                                   |
+----------+------------------+------------------------------------------+
| Clubs    | Scrum	      | Scrimmage. Immediately play goes stale.  |
| Hearts   | Stiff Arm        | Force Move. Advance regardless of clash. |
| Spades   | Fumble Recover   | Ball Strip. Force immediate possession.  |
| Diamonds | Juke Step        | Perfect Ankle Breaker. Reached Endzone!  |
+----------+------------------+------------------------------------------+
* PLAYS driven can be saved into a PLAYBOOOK, the amount # determined by the current rank.
- Allows coaches to callout "signature plays" on any JKR drawn (using corresponding SLOT #).

### 2. THE PLAY CYCLE & POSSESSION
* PHASE I: THE AUDIBLE
  - Players reveal their plays simultaneously.
  - Formation: Set based on suit and current position (Neutral/Offense/Defense)
  - Possession: Hearts/Diamonds = Offense. Clubs/Spades = Defense.
* PHASE II: THE CLASH (D66)
  - Calculate Hits based on Rank Success Window. Stats only affect TIE-BREAKERS!
    - I. Unranked Rookies:   1 Success Window    | 1 Floor STAT + 1 SP (Unranked)
    - II. Backyard Amateurs: 1-2 Success Window  | 2 Floor STAT + 2 SP (D4 Prospect)
    - III. High School Pros:    1-3 Success Window  | 3 Floor STAT + 3 SP (D3 Prospect)
    - IV. College Superstars: 1-4 Succes Window | 4 Floor STAT + 4 SP (D2 Prospect)
    - V. National Legends:   1-5 Success Window  | 5 Floor STAT + 5 SP (D1 Prospect)
   * Skill Points are added during the PRE-SEASON, following division promotions.
* PHASE III: RESOLUTION
  - Clean Win: Highest hits wins. Play advancement or conversion.
  - The Stale: Hits match. Proceed to "THE BREAKER".
  - Dual-Split: Both roll [1 Hit / 1 Miss]. Trigger D4 Complication!
  - Fumble (XX): Both roll [0 Hits]. Ball is live! AWR/INT SAVING THROW.

### 3. THE BREAKER (STAT-MATCH SCRAMBLE)
* Rule: Only add card values if primary stats are equal.
  1. Compare Primary Stats: Higher stat wins the tie-breaker.
  2. Card Value Addition (If stats are equal): [Primary Stat] + [Card Value].
     - 2-10: Face Value
     - J: 11 (Feint Play / Posts Formation)
     - Q: 12 (Side Pass / Y Formation)
     - K: 13 (Kick Pass / Dash Formation)
     - A: 14 (Spread Form)
     - JKR: 15 (SPECIAL MOVES TABLE!)
  3. Final Saving Throw: If still tied, compare Saving Throw stats in brackets.

### 4. D4 COMPLICATIONS (THE DUAL-SPLIT)
* Logic: Lower Saving Throw STAT results in being the offender/offendee.
  - [1] SACK (Check SPD): Instant loss of possession + 2 points for opponent.
  - [2] OUT OF BOUNDS (Check CAT): Reset play to Neutral.
  - [3] PENALTY (Check STA): Personal Foul triggers Field Goal: +3pt.
  - [4] INTERCEPTION (Check KCK): Instant possession flip for live play: + 1pt.

### 5. ROUTE & COVER REFERENCE (#2-10)
+-------+------------------+------------------+
| VALUE | ROUTE (OFFENSE)  | COVER (DEFENSE)  |
+-------+------------------+------------------+
| 2     | Dig              | Cover 2          |
| 3     | Hitch            | Cover 3          |
| 4     | Curl             | Cover 4          |
| 5     | Mesh             | Nickel           |
| 6     | Slant            | Dime             |
| 7     | Swing            | Quarter          |
| 8     | Stick            | Stacks           |
| 9     | Long             | Slants           |
| 10    | Handoff          | Man 2 Man        |
+-------+------------------+------------------+

### 6. FRANCHISES & DINASTIES (12 WEEK "YEAR" SEASONS, 7 DAY WEEKLY SCHEDULE)

[MEDIA monday/TRAINING tuesday/STUDY wednesday/BY thursday/HS friday/CL saturday/NL sunday]

> WEEKLY ACTIVITIES: serve as roleplaying events and general structure for a team.

- d4 MEDIA: 1. Press Conference / 2. Radio Interview / 3. Live Show / 4. News Article

- TRAINING DRILLS: ♣: Rush Tackle / ♥: Box Snaps / ♠: Pursuit Tackle / ♦: Shuffle Catch
* Weekly, select a different drill to work on: adding a temporary d4 bonus to STATS! (+ 0-3)

- d4 STUDY: 1. Blackboard Lecture / 2. Film Review / 3. Play Calling / 4. Rivalry Simulation

> SEASON SCHEDULE
* Draft Day for GM to fill up 4 ROSTER SPOTS (1 p/suit) w/ 4 CARD PICKS + d6-1 STARS!
- Star Quality grants temporary +X STAT for SUIT during seasons (+ trades always possible!)
- 8 Roster Spots are present: INCOMING (4 draft, 4 promos) OUTGOING (4 promoted, 4 retired)
[W1 - W2 - W3] ---> [W4 - W5 - W6] ---> [W7 - W8 - W9] ---> [W10 - W11 - W12]
 PRE-SEASON	        REGULAR SEASON	     PLAYOFF SEASON	    OFF-SEASON
- studies + drilling  - 2 games per week     - 1 game per week    - draft day
- divisional: f vs. e - conference standings - final elimination  - team rosters
- lineage qualifiers  - franchise carnage    - cardinal kings     - friendly matchups

[ROUGHBALL ERAS: Old Timey / Golden Age / Millenium / Pandemical] -> Roleplaying "Flavors"

# MANAGER HIERARCHY: GM: "General Manager"/COACH: "Playmaker & Analyst"/TEAM: "Pawns & Rooks"
* ROOKIES -> UNRANKED: "free agents" that can become draft picks. (X SEASONS = +1 RANK)

[National Legends/College Superstars/High School Pros/Backyard Amateurs/Unranked Rookies]
(D1: PRO-LEAGUE)   (D2: COLLEGE)         (D3: HIGH SCHOOL L.)   (D4: BACKYARD LEAGUE)

LIONS/PANTHERS     Wildcats/Jaguars      Lynx/Tigers            Cougars/Bobcats

VIKINGS/SAINTS     Celtics/Monks         Warriors/Friars        Maulers/Preachers

FARMERS/STALLIONS  Cattle/Mustangs       Hillbillies/Broncos    Rednecks/Colts

SHARKS/STINGRAYS   Hammerheads/Dolphins  Gators/Seals           Marlins/Squids

PATRIOTS/ROYALS    Colonels/Knights      Admirals/Ambassadors   Sentinels/Legionnaires

EAGLES/SEAHAWKS    Crows/Pelicans        Ravens/Skimmers        Vultures/Talons

BEARS/SCORPIONS    Bruins/Spiders        Grizzlies/Stingers     Cubs/Snakes

PIRATES/SURGERS    Raiders/Chargers      Bandits/Volts          Outlaws/Hurricanes

# BONUS SECTION: NATIONAL PRO-LEAGUE FRANCHISES (FOUNDING VS. EXPANSIONS)
* NORTH CONFERENCE: 
    - Mountain LIONS 🏔️🦁    (♣: 8 ♥: 4 ♠: 7 ♦: 6) [Mountain Rugged]
    - Greenland VIKINGS 🛶👑 (♣: 6 ♥: 7 ♠: 8 ♦: 4) [Land Raiders]
* SOUTH CONFERENCE:
    - Southern FARMERS 🚜👨‍🌾 (♣: 8 ♥: 7 ♠: 6 ♦: 4) [Southern Hostility]
    - Coast SHARKS 🌊🦈     (♣: 7 ♥: 5 ♠: 8 ♦: 5) [Tide Predators]
* EAST DIVISION:
    - City PATRIOTS 🏙️🏳️  (♣: 6 ♥: 5 ♠: 5 ♦: 9) [Founding Fathers]	
    - Eastern EAGLES 🧭🦅 (♣: 5 ♥: 9 ♠: 6 ♦: 5) [Birds of Prey]
* WEST DIVISION:
    - Western BEARS 🧭🐻  (♣: 7 ♥: 7 ♠: 6 ♦: 5) [Bruiser Brawlers]
    - Beach PIRATES 🏖️🏴‍☠️  (♣: 5 ♥: 8 ♠: 6 ♦: 6) [Treasure Looters]

* NORTH CONFERENCE (Expansion): 
    - Pike Brown PANTHERS 🏔️🐆  (♣: 8 ♥: 5 ♠: 7 ♦: 5) [Peak Predators]
    - Greenland SAINTS ⛰️⚜️     (♣: 7 ♥: 5 ♠: 9 ♦: 4) [Heaven's Gate]
* SOUTH CONFERENCE (Expansion):
    - Countryside STALLIONS 🐎🌾 (♣: 7 ♥: 8 ♠: 6 ♦: 4) [Country Work]
    - Southern STINGRAYS 🌊🪁    (♣: 6 ♥: 5 ♠: 8 ♦: 6) [Coastal Speed]
* EAST DIVISION (Expansion):
    - Eastern ROYALS 👑🏙️        (♣: 5 ♥: 5 ♠: 6 ♦: 9) [Elite Passing]
    - Lake Brown SEAHAWKS 🌊🦅   (♣: 5 ♥: 9 ♠: 6 ♦: 5) [Pure Awareness]
* WEST DIVISION (Expansion):
    - Red Desert SCORPIONS 🦂🏜️  (♣: 7 ♥: 6 ♠: 5 ♦: 7) [Arid Desert]
    - Western SURGERS 🌊⚡       (♣: 4 ♥: 7 ♠: 6 ♦: 9) [Tsunami Build]

================================================================================================
                                ROUGHBALL D88 CARNAGE COORDINATES                                 
================================================================================================
 DIE A (Home)  | 1:PANTH | 2:SAINT | 3:STALL | 4:RAYS  | 5:SEAHA | 6:ROYAL | 7:SCORP | 8:SURGE |
---------------+---------+---------+---------+---------+---------+---------+---------+---------+
 1: LIONS      | [1,1]*  | [1,2]   | [1,3]   | [1,4]   | [1,5]   | [1,6]   | [1,7]   | [1,8]   |
 2: VIKINGS    | [2,1]   | [2,2]*  | [2,3]   | [2,4]   | [2,5]   | [2,6]   | [2,7]   | [2,8]   |
 3: FARMERS    | [3,1]   | [3,2]   | [3,3]*  | [3,4]   | [3,5]   | [3,6]   | [3,7]   | [3,8]   |
 4: SHARKS     | [4,1]   | [4,2]   | [4,3]   | [4,4]*  | [4,5]   | [4,6]   | [4,7]   | [4,8]   |
 5: EAGLES     | [5,1]   | [5,2]   | [5,3]   | [5,4]   | [5,5]*  | [5,6]   | [5,7]   | [5,8]   |
 6: PATRIOTS   | [6,1]   | [6,2]   | [6,3]   | [6,4]   | [6,5]   | [6,6]*  | [6,7]   | [6,8]   |
 7: BEARS      | [7,1]   | [7,2]   | [7,3]   | [7,4]   | [7,5]   | [7,6]   | [7,7]*  | [7,8]   |
 8: PIRATES    | [8,1]   | [8,2]   | [8,3]   | [8,4]   | [8,5]   | [8,6]   | [8,7]   | [8,8]*  |
================================================================================================
 * = Direct Geography Rivalry (Maximum Bad Blood)
================================================================================================

# HISTORICAL RANKINGS PER FRANCHISE/ERA
+----------+-------------+-------------+--------------+--------------+--------------+
|ERA       |#1 CHAMPIONS |#2 RUNNER UP |#3 WILDCARD   |#4 REVELATION |DISGRACEFUL!  |
+----------+-------------+-------------+--------------+--------------+--------------+
|OLD TIMEY |Patriots 🏙️🏳️|Bears 🧭🐻   |Vikings 🛶👑  |Lions 🏔️🦁    |SAINTS ⛰️⚜️   |
+----------+-------------+-------------+--------------+--------------+--------------+
|GOLDEN AGE|Pirates 🏖️🏴‍☠️ |Panthers 🏔️  |Eagles 🧭🦅   |Farmers 🚜👨‍🌾  |SCORPIONS 🦂🏜|
+----------+-------------+-------------+--------------+--------------+--------------+
|MILLENIUM |Saints ⛰️⚜️  |Seahawks 🌊🦅|Scorpions 🦂🏜️|Stallions 🐎🌾|BEARS 🧭🐻    |
+----------+-------------+-------------+--------------+--------------+--------------+
|PANDEMICAL|Lions 🏔️🦁   |Surge 🌊⚡   |Royals 👑🏙️   |Sharks 🌊🦈   |STINGRAYS 🌊🪁|
+----------+-------------+-------------+--------------+--------------+--------------+

