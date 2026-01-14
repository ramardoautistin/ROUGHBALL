[ROUGHBALL SIMULATION SYSTEM - v3.0]
### 1. PLAYCALLING & MOVEMENT MATRIX
> ROUGHBALL is a proto-ball game combining techniques and mechanics from
both its Rugby and American Football counterparts, while fixing "flow" 
issues present in both games, such as: the ban on the "forward pass"
established in rugby, the lack of "free punting" the ball in football,
plus the entire "yardage" and "downs" system which makes the games 
harder to watch. however, both sports contain fascinating rulings as well:
the playcalling and general strategy implied in american football, the 
basis for our ROUGHBALL simplified formation system, as well as our 
ZONE/RUN/BLITZ/PASS system which enhances the familiarity. brought from
rugby: the side pass, live ball & kicking mechanics, scrum and general 
constant scrimmages, PROPER tackling techniques, and field goal penalties 
granted for unsportsmanlike conducts between teams! 
* ROUGHBALL effectively bridges the gap between strategically calling routes
or covers based upon the requirements of the current field, but focusing instead 
on live ball mechanics & perpetual possession "flippages" ensued during the match!

[ ROUGHBALL SCORING: TRY = 5pts | FIELD GOAL = 3pts | SACK = 2pts | INT = 1 pt ]

## OFFENSIVE AND DEFENSIVE FORMATIONS
     1   2   3   4   5   6   7   8
  |----------------------------------| (AWAY Endzone + Goal Post)
A |  .   .   .   RG   .   .   .   .  | 
B |  .   .   .   .   QG   .   .   .  | 
C |  WB  .   .   .   .   .    .   TB | 
D |  .   .   DE  OT  DT  OG   .   .  | (OFFENSE -> DRIVING)
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx << NEUTRAL SNAP POINT >>
E |  .   .   OG  DT  OT  DE  .    .  | (DEFENSE -> HOLDING)
F |  .   .   .   .   .   .   .    .  | 
G |  .   .   .   SG   .   .   .   .  | 
H | CB   .   .   .   SG   .   .   LB | 
  |----------------------------------| (HOME Endzone + Goal Post)

## ROUGHBALL STAT & SAVING THROW TABLE
+-------------------+-----------+--------------+------------------------------+
| SUIT / PLAY       | STATS     | SAVING THROW | KEY PERSONNEL (POSITIONS)    |
+-------------------+-----------+--------------+------------------------------+
| ♣ CLUBS (ZONE)    | TKL       | STA          | (DT) d. tackle (LB) lineback |
| (Scrimmagers)     |(tackling) | (stamina)    | (DE) defensive end           |
+-------------------+-----------+--------------+------------------------------|
| ♡ HEARTS (RUN)    | AWR       | SPD          | (QG) quarterg. (SG) safety   |
| (Field Generals)  |(awareness)| (speed)      | (RG) running guard   guard   |
+-------------------+-----------+--------------+------------------------------+
| ♠ SPADES (BLITZ)  | INT       | KCK          | (OG) of. guard (CB) cornerb. | 
| (Pitch Guards)    |(intercpt.)| (kicking)    | (OT) offensive tackle        |
+-------------------+-----------+--------------+------------------------------+
| ♢ DIAMONDS (PASS) | PAS       | CAT          | (WB) wide back (SG) safety   |
| (Air Raiders)     | (passing) | (catching)   | (TB) tight back      guard   |
+-------------------+---------+-----+-------+---------------------------------+

## SPECIAL MOVES & SIGNATURE PLAYBOOK (JKR ENFORCEMENT)
+----------+------------------+------------------------------------------+
| SUIT     | SPECIAL MOVE     | EFFECT                                   |
+----------+------------------+------------------------------------------+
| Clubs    | Ruck	          | Scrimmage. Immediately play goes stale.  |
| Hearts   | Stiff Arm        | Force Move. Advance regardless of clash. |
| Spades   | Punt             | Ball strip becomes defensive punting!    |
| Diamonds | Juke Step        | Perfect Ankle Breaker. Reached Endzone!  |
+----------+------------------+------------------------------------------+

* PLAYS driven can be STORED into a team's PLAYBOOOK, the # of plays determined by current rank.
- Allows coaches to callout SIGNATURE PLAYS on any JKR drawn (engaging a SLOT #, without further cards).

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
     - J: 11 (Feint Play / T Formation)
     - Q: 12 (Side Pass / Y Formation)
     - K: 13 (Kick Pass / V Formation)
     - A: 14 (Spread Form)
     - JKR: 15 (SPECIAL MOVES TABLE! when combined with specific SUIT.)
  3. Final Saving Throw: If still tied, compare Saving Throw rolls + outcome.
- STILL TIED? Draw a new RE-AUDIBLE PLAY for a clean tie-breaker!

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

[ J = FEINT PLAY | Q = SIDE PASS | K = KICK PASS | A = SPREAD FORM | JKR = SPECIAL! ]
[ (T FORMATION)  | (Y FORMATION) | (V FORMATION) | > CALL SIGNATURE PLAYS OR MOVES  ]

### 6. FRANCHISES & DINASTIES (12 WEEK "YEAR" SEASONS, 7 DAY WEEKLY SCHEDULE)
> WEEKLY ACTIVITIES: serve as roleplaying events and general structure for a team:

[MEDIA monday|TRAINING tuesday|STUDY wednesday|BY thursday|HS friday|CL saturday|NL sunday]

1. MEDIA MONDAY TABLE: 1. Press Conference / 2. Radio Interview / 3. Live Show / 4. News Article
- Weekly, an event triggers a d4-1 PENALTY on any given STAT: (1. TKL | 2. AWR | 3. INT | 4. PAS)

2. TRAINING TUESDAY DRILLS: ♣: Rush Tackle / ♡: Box Snaps / ♠: Pursuit Tackle / ♢: Shuffle Catch
- Weekly, select a different drill to work on: adding a temporary d4-1 BONUS to selected STAT! (+0-3)

3. STUDY WEDNESDAY TABLE: 1. Blackboard Lecture / 2. Film Review / 3. Play Calling / 4. Rivalry Simulation
- Weekly, studying provides a d4-1 BONUS on any given SAVING THROW: (1. STA | 2. SPD | 3. KCK | 4. CAT)

4. BACKYARD THURSDAY: engage in D-4 "Backyard Amateur" matches between neighbourhoods!

5. HIGH SCHOOL FRIDAY: engage in D-3 "High School Pros" matches between schools!

6. COLLEGE SATURDAY: engage in D-2 "College Superstars" matches between universities!

7. NATIONAL SUNDAY: engage in D-1 "National Legend" matches between regional blood-rivals!

> SEASON SCHEDULE
* Draft Day allows GM to fill up 4 ROSTER SPOTS (1 per suit) w/ 4 CARD PICKS + d6-1 STARS!
- Star Quality grants temporary +X STAT for SUIT during seasons (& trades always possible!)
- 8 Roster Spots are present: INCOMING (4 draft, 4 promos) OUTGOING (4 promoted, 4 retired)

[W1 - W2 - W3] ---> [W4 - W5 - W6] ---> [W7 - W8 - W9] ---> [W10 - W11 - W12]
[ PRE-SEASON	        REGULAR SEASON	      PLAYOFF SEASON	   OFF-SEASON ]
- studies + drilling  - 2 games per week     - 1 game per week    - draft day
- divisional: f vs. e - conference standings - final elimination  - team rosters
- lineage qualifiers  - franchise carnage    - cardinal kings     - friendly matchups

[ ROUGHBALL ERAS: Old Timey | Golden Age | Millenium | Pandemical ] -> Roleplaying "Flavors"

[ MANAGER HIERARCHY: GM: "General Manager" | COACH: "Playmaker & Analyst" | TEAM: "Pawns & Rooks" ]

* ROOKIES -> UNRANKED: "free agents" that can become draft picks. (X SEASONS = +1 RANK)

[National Legends | College Superstars | High School Pros | Backyard Amateurs | Unranked Rookies]

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
    - Mountain LIONS 🏔️🦁    (♣: 8 ♡: 4 ♠: 7 ♢: 6) [Mountain Rugged]
    - Greenland VIKINGS 🛶👑 (♣: 6 ♡: 7 ♠: 8 ♢: 4) [Land Raiders]
* SOUTH CONFERENCE:
    - Southern FARMERS 🚜👨‍🌾 (♣: 8 ♡: 7 ♠: 6 ♢: 4) [Southern Hostility]
    - Coast SHARKS 🌊🦈     (♣: 7 ♡: 5 ♠: 8 ♢: 5) [Tide Predators]
* EAST DIVISION:
    - City PATRIOTS 🏙️🏳️  (♣: 6 ♡: 5 ♠: 5 ♢: 9) [Founding Fathers]	
    - Eastern EAGLES 🧭🦅 (♣: 5 ♡: 9 ♠: 6 ♢: 5) [Birds of Prey]
* WEST DIVISION:
    - Western BEARS 🧭🐻  (♣: 7 ♡: 7 ♠: 6 ♢: 5) [Bruiser Brawlers]
    - Beach PIRATES 🏖️🏴‍☠️  (♣: 5 ♡: 8 ♠: 6 ♢: 6) [Treasure Looters]

* NORTH CONFERENCE (Expansion): 
    - Pike Brown PANTHERS 🏔️🐆  (♣: 8 ♡: 5 ♠: 7 ♢: 5) [Peak Predators]
    - Green Hill SAINTS ⛰️⚜️     (♣: 7 ♡: 5 ♠: 9 ♢: 4) [Heaven's Gate]
* SOUTH CONFERENCE (Expansion):
    - Countryside STALLIONS 🐎🌾 (♣: 7 ♡: 8 ♠: 6 ♢: 4) [Country Work]
    - Southern STINGRAYS 🌊🐋    (♣: 6 ♡: 5 ♠: 8 ♢: 6) [Coastal Speed]
* EAST DIVISION (Expansion):
    - Eastern ROYALS 👑🏙️        (♣: 5 ♡: 5 ♠: 6 ♢: 9) [Elite Passing]
    - Lake Brown SEAHAWKS 🌊🦅   (♣: 5 ♡: 9 ♠: 6 ♢: 5) [Pure Awareness]
* WEST DIVISION (Expansion):
    - Red Desert SCORPIONS 🦂🏜️  (♣: 7 ♡: 6 ♠: 5 ♢: 7) [Arid Desert]
    - Western SURGERS 🌊⚡       (♣: 4 ♡: 7 ♠: 6 ♢: 9) [Tsunami Build]

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
+----------+--------------+----------------+-----------------+---------------+----------------+
|ERA       | #1 CHAMPIONS | #2 RUNNER UP   | #3 WILDCARD     | #4 REVELATION | DISGRACEFUL!   |
+----------+--------------+----------------+-----------------+---------------+----------------+
|OLD TIMEY | Patriots 🏙️🏳️| Bears 🧭🐻     | Vikings 🛶👑    | Lions 🏔️🦁    | SAINTS ⛰️⚜️    |
+----------+--------------+----------------+-----------------+---------------+----------------+
|GOLDEN AGE| Pirates 🏖️🏴‍☠️ | Panthers 🏔️    | Eagles 🧭🦅     | Farmers 🚜👨‍🌾  |SCORPIONS 🦂🏜 |
+----------+--------------+----------------+-----------------+---------------+----------------+
|MILLENIUM | Saints ⛰️⚜️  | Seahawks 🌊🦅  | Scorpions 🦂🏜️  |Stallions 🐎🌾 | BEARS 🧭🐻     |
+----------+--------------+----------------+-----------------+---------------+----------------+
|PANDEMICAL| Lions 🏔️🦁   | Surge 🌊⚡     | Royals 👑🏙️     |Sharks 🌊🦈    | STINGRAYS 🌊🐋 |
+----------+--------------+----------------+-----------------+---------------+----------------+




