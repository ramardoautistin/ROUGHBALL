# ROUGHBALL v10.1 - WEEK SPRINT BUILD

A card-based proto-ball sports simulation combining Rugby and American Football mechanics with live ball gameplay and franchise management.

## 🎮 QUICK START

```bash
cd roughball_v2
python roughball.py
```

---

## 🆕 WHAT'S NEW IN v10.1

### Critical Bug Fixes
- ✅ **Team ID Swap**: Fixed IDs 5/6/13/14 (Eagles/Patriots/Seahawks/Royals)
- ✅ **RUCK Special Move**: Now correctly guaranteed stoppage (was routing to breaker)

### Major New Feature
- 🎮 **Dynasty Mode**: Full 12-week franchise management with daily activities!

---

## 📋 GAME MODES

### [1] QUICK MATCH
- Original simulator
- Pick 2 teams from 16 franchises
- Choose division (D1-D5)
- Choose era (Old-Timey → Pandemical)
- Play full match with D66 resolution

### [2] DYNASTY MODE ⭐ NEW
- 12-week season structure
- Daily activities (Mon-Wed)
- Match days across all divisions (Thu-Sun)
- Stat tracking and weekly reset
- Era-specific flavor text
- Phase progression (Pre-Season → Playoffs)

### [3] ACTIVITIES PREVIEW
- View all weekly activities
- See era-specific descriptions
- Understand stat systems

---

## 🏈 ROUGHBALL BASICS

### The Sport
**ROUGHBALL** bridges Rugby and American Football:
- **From Rugby**: Side passing, live ball, scrums, proper tackling
- **From Football**: Play calling, formations, strategic routes
- **Innovation**: No downs/yardage, free punting, constant flow

### Scoring
- **TRY**: 5 points (reach endzone with H/D suit)
- **FIELD GOAL**: 3 points (D + King kick pass or penalty)
- **SACK**: 2 points (defensive QB strip)
- **INT**: 1 point (interception)

### Core Mechanics
- **D66 Clash**: Roll 2d6, count hits based on division rank
- **Success Windows**: 1-5 depending on league (Rookies → Legends)
- **Suit System**: ♣ Scrimmagers / ♥ Field Generals / ♠ Pitch Guards / ♦ Air Raiders
- **Special Moves**: JKR + Suit = RUCK / STIFF ARM / PUNT / JUKE

---

## 📊 DYNASTY MODE DEEP DIVE

### Season Structure (12 Weeks)
```
Weeks 1-3:  LINEAGE QUALIFIERS (Pre-Season)
Weeks 4-6:  CARDINAL CARNAGE (Regular Season)
Weeks 7-9:  BLOOD DISQUALIFIERS (Playoffs)
Weeks 10-12: ROUGHBALL WILDCARD (Off-Season)
```

### Weekly Flow
```
Monday    → 📊 Media Monday (auto penalty)
Tuesday   → 🏋️ Training Tuesday (YOUR CHOICE bonus)
Wednesday → 📚 Study Wednesday (auto bonus)
Thursday  → 🏚️ D4 Backyard Match
Friday    → 🚌 D3 High School Match
Saturday  → 🎓 D2 College Match
Sunday    → 🏈 D1 National Match
```

### Daily Activities

#### 📊 MEDIA MONDAY
- Random event (Press Conference / Radio / Show / Article)
- D4-1 penalty to random stat (0-3)
- Era-specific flavor (16 unique descriptions)

#### 🏋️ TRAINING TUESDAY
- **YOU CHOOSE** drill focus:
  - ♣ Rush Tackles (TKL) / Scrum Locks (STA)
  - ♥ Box Snaps (AWR) / Carrier Sprints (SPD)
  - ♠ Pursuit Tackling (INT) / Post Kicking (KCK)
  - ♦ Shuffle Passing (PAS) / Contested Catching (CAT)
- D4-1 bonus to BOTH stats (0-3)
- Era-specific facilities (mud → VR)

#### 📚 STUDY WEDNESDAY
- Random method (Blackboard / Film / Playbook / Analytics)
- D4-1 bonus to random saving throw (0-3)
- Full weekly stat summary displayed
- Era-specific methods (16 unique descriptions)

---

## 🎯 THE FOUR ERAS

Each era affects ALL flavor text throughout the game:

### OLD TIMEY (1)
*Founding Era - Leather Helmets*
- Regional newspapers
- Muddy training fields
- 8mm film reels
- Small town atmosphere

### GOLDEN AGE (2)
*Broadcast Era - Iconic Figures*
- Magazine covers
- Sports arena domes
- VHS tape reviews
- Peak media coverage

### MILLENNIUM (3)
*Corporate Era - Capital Expansion*
- Blog controversies
- Corporate stadiums
- DVD compilations
- Analytics obsession

### PANDEMICAL (4)
*Virtual Era - Streampocalypse*
- Viral social posts
- VR training
- Tablet reviews
- Streaming culture

---

## 🏆 THE 16 TEAMS

### North Conference
- **1. Mountain LIONS** 🏔️🦁 (F) - Mountain Rugged
- **2. Greenland VIKINGS** 🛶👑 (F) - Land Raiders
- **9. Pike PANTHERS** 🏔️🐆 (E) - Peak Predators
- **10. Greenland SAINTS** ⛰️⚜️ (E) - Heaven's Gate

### South Conference
- **3. Southern FARMERS** 🚜👨‍🌾 (F) - Southern Hostility
- **4. Coast SHARKS** 🌊🦈 (F) - Tide Predators
- **11. Countryside STALLIONS** 🐎🌾 (E) - Country Work
- **12. Southern STINGRAYS** 🌊🪼 (E) - Coastal Speed

### East Division
- **5. Eastern EAGLES** 🧭🦅 (F) - Birds of Prey
- **6. City PATRIOTS** 🏙️🏳️ (F) - Founding Fathers
- **13. Lake SEAHAWKS** 🌊🦅 (E) - Pure Awareness
- **14. Eastern ROYALS** 👑🏙️ (E) - Elite Passing

### West Division
- **7. Western BEARS** 🧭🐻 (F) - Bruiser Brawlers
- **8. Beach PIRATES** 🏖️🏴‍☠️ (F) - Treasure Looters
- **15. Desert SCORPIONS** 🦂🏜️ (E) - Arid Desert
- **16. Beach SURGERS** 🌊⚡ (E) - Tsunami Build

*F = Founder | E = Expansion*

---

## 🎲 GAME MECHANICS

### The Audible (Play Call)
- Draw 1-5 cards based on division
- First card suit = play type
- Hearts/Diamonds = Offensive routes
- Clubs/Spades = Defensive covers

### The Clash (D66)
- Roll 2d6
- Success window = division rank (1-5)
- Count hits: die ≤ success window = hit
- Higher hits wins

### Outcomes
- **Clean Win**: Highest hits → score based on suit
- **Stalemate (2-2)**: THE BREAKER → stat comparison
- **Dual-Split (1-1)**: D4 COMPLICATION → save throw
- **Fumble (0-0)**: Ball is live → re-audible

### JKR Special Moves
- **♣ + JKR = RUCK**: Immediate stoppage, possession flip
- **♥ + JKR = STIFF ARM**: Guaranteed TRY if driving
- **♠ + JKR = PUNT**: Defensive ball strip
- **♦ + JKR = JUKE**: Guaranteed TRY if driving

---

## 🔧 TECHNICAL INFO

### Files Structure
```
roughball_v2/
├── roughball.py          # Main entry + Dynasty loop
├── core/
│   ├── teams.py          # 16 teams + stats (FIXED)
│   ├── resolver.py       # Play resolution (FIXED RUCK)
│   ├── activities.py     # Weekly system (NEW)
│   ├── match.py          # Match simulation
│   ├── display.py        # UI/formatting
│   ├── cards.py          # Deck management
│   ├── dice.py           # D66/D4 rolling
│   └── ai.py             # Bot opponent
└── docs/
    ├── CHANGELOG.md      # Full version history
    ├── PATCH_NOTES.md    # v10.1 details
    └── IMPLEMENTATION_SUMMARY.md
```

### Dependencies
- Python 3.6+
- Standard library only (no external packages!)

### Platform Support
- ✅ Windows
- ✅ macOS
- ✅ Linux

---

## 🐛 BUG FIXES IN v10.1

### Bug #1: Team ID Mismatch
**Problem**: Menu selections didn't match internal team data
**Impact**: Broke carnage coordinates and bracket pairings
**Fix**: Corrected IDs 5/6/13/14 in `core/teams.py`

### Bug #2: RUCK Special Move
**Problem**: Routing to Breaker instead of guaranteed stoppage
**Doc Says**: "Immediately play goes stale" (no breaker)
**Fix**: Changed to instant possession flip in `core/resolver.py`

---

## 📖 DOCUMENTATION

### Quick References
- `CHANGELOG.md` - Full version history
- `PATCH_NOTES.md` - Detailed v10.1 changes
- `IMPLEMENTATION_SUMMARY.md` - Developer overview
- `/mnt/project/ROUGHBALL_DOC.md` - Complete rules

### Design Philosophy
From `SCRIPT_RE-MAKE_DOCS.md`:
> "ROUGHBALL is a realistic visual sports strategy simulator that tries to capture the honor and glory of the 'gentleman's sport' and its values."

Three target audiences:
1. Managerial nerds (statistical paperwork lovers)
2. Playcalling aficionados (tactical supremacy)
3. Nostalgia players (dice-rolling fantasy teams)

---

## 🚀 COMING SOON

### BUILD 2: Complete Dynasty
- Save/Load franchise data
- Signature playbook system (JKR recall)
- Draft Day (4-pick post-season)
- Commissioner standings table
- Rivalry tracking

### BUILD 3: Month Build
- Regional Championship brackets
- Four Nations World Cup (4-year cycle)
- Club Wipeout Crown (hemispherical)
- Full 8-man roster draft
- Dual-threat veterans
- Star rating system
- Trade mechanics

---

## 🎮 GAMEPLAY TIPS

### Quick Match
- Training Tuesday drills compound (stat + save throw)
- Media Monday can ruin your best players
- Save important matches for post-Wednesday

### Dynasty Strategy
- Plan your Training Tuesday around match schedule
- D1 Sunday games are most affected by weekly bonuses
- Tier system means different team names per division

### Advanced Tactics
- RUCK for guaranteed stoppage when desperate
- JUKE/STIFF ARM only work when driving
- PUNT only works when defending
- D4 Complications favor the prepared (saving throws!)

---

## 💬 CREDITS

**Design & Implementation**: Based on ROUGHBALL_DOC.md tabletop rules
**Original Concept**: A childhood dream of "tonto del rugby" realized
**Code Refactor**: v10.1 fixes and Dynasty Mode implementation
**Era Flavor**: 60+ unique descriptions across 4 eras

---

## 📝 VERSION INFO

- **Version**: 10.1 (Week Sprint Build)
- **Release Date**: 2026-02-02
- **Build**: 1.1 (Bug Fixes + Dynasty)
- **Status**: Playable, fully functional

---

## 🎯 START PLAYING

```bash
python roughball.py
```

Choose your path:
- **Quick Match**: Jump into a single game
- **Dynasty Mode**: Build a franchise legacy
- **Preview**: Learn the systems

---

**Welcome to the Big Leagues!** 🏈

*"From muddy backyards to luxury stadiums - this is ROUGHBALL."*
