# ROUGHBALL: CHANGELOG

## [BUILD 1.1 - BUG FIXES + WEEK SPRINT] - 2026-02-02

### Critical Bug Fixes
1. **TEAM ID SWAP (Issue #1)**
   - **Problem**: Team IDs were mismatched between menu display and internal data
   - **Fix**: Corrected team assignments:
     - ID 5: Now "Eastern EAGLES" (Founder) - was "Eastern SEAHAWKS"
     - ID 6: Now "City PATRIOTS" (Founder) - was "City ROYALS"
     - ID 13: Now "Lake SEAHAWKS" (Expansion) - was "City PATRIOTS"
     - ID 14: Now "Eastern ROYALS" (Expansion) - was "Eastern EAGLES"
   - **Impact**: Carnage Coordinates and bracket pairings now work correctly
   - **Files Modified**: `core/teams.py`

2. **RUCK SPECIAL MOVE (Issue #2)**
   - **Problem**: RUCK was routing to Breaker instead of guaranteed stoppage
   - **Doc Reference**: "Scrimmage. Immediately play goes stale." (no breaker mentioned)
   - **Fix**: RUCK now works exactly like PUNT - guaranteed stoppage with possession flip
   - **Code Change**: Removed Breaker routing, added immediate possession flip
   - **Files Modified**: `core/resolver.py` (lines 465-474)

### Major Feature Addition: DYNASTY MODE

#### Weekly Activities System
- **New Module**: `core/activities.py`
- **Implements**: Full Mon-Wed activity mechanics from ROUGHBALL_DOC

**MEDIA MONDAY**
- D4 roll determines event type (Press Conference, Radio Interview, Live Show, News Article)
- D4-1 penalty applied to random stat (TKL, AWR, INT, or PAS)
- Era-specific flavor text for all 4 eras × 4 events = 16 unique descriptions
- Automatic stat penalty tracking (0-3 penalty range)

**TRAINING TUESDAY**
- USER CHOICE of drill focus (4 options: ♣ ♥ ♠ ♦)
- D4-1 bonus applied to BOTH primary stat AND saving throw
- Era-specific facility descriptions (muddy field → VR systems)
- Interactive menu with clear drill names and stat targets

**STUDY WEDNESDAY**
- D4 roll determines study method (Blackboard, Film, Playbook, Analytics)
- D4-1 bonus applied to random saving throw (STA, SPD, KCK, or CAT)
- Era-specific method descriptions for all 4 eras × 4 methods = 16 unique texts
- Summary display of all weekly modifiers after Wednesday

#### Gladiator Schedule (12-Week Season)
- **Week 1-3**: LINEAGE QUALIFIERS (Pre-Season)
- **Week 4-6**: CARDINAL CARNAGE (Regular Season)
- **Week 7-9**: BLOOD DISQUALIFIERS (Playoffs)
- **Week 10-12**: ROUGHBALL WILDCARD (Off-Season)

**Daily Flow**:
- Monday-Wednesday: Automated activities with stat tracking
- Thursday-Sunday: Match days across all 4 divisions (D4, D3, D2, D1)
- Each match day: Play, Simulate, or Skip options
- Weekly stat reset between weeks

**Dynasty Features**:
- Franchise selection (16 teams, Founder vs Expansion status shown)
- Era selection (affects all flavor text throughout season)
- Bracket pairing system (founder vs expansion matchups)
- Tier-based naming (teams appear as College/HS/Backyard versions per division)
- End-of-week stat reset (bonuses/penalties cleared)

### UI/UX Improvements
- Updated main menu to show "v10.1 (WEEK SPRINT)"
- Dynasty Mode added as option [2]
- Activities Preview remains as option [3]
- Improved team selection display (shows founder/expansion status with emoji)
- Clear weekly phase headers with progress tracking
- Stat modifier summary after Study Wednesday

### Code Architecture
- Separated activities logic into dedicated module
- Maintained compatibility with existing Quick Match mode
- Clean separation between activity days and match days
- Modular structure allows easy addition of BUILD 3 features

---

## [BUILD 1 - WEEKEND PROTOTYPE] - 2026-01-31

### Added
- **Quick Match Mode**
  - Team selection (all 16 NRBL teams with stats and tier systems)
  - Division selection (D1-D5, configurable card count 1-5)
  - Era selection (Old-Timey, Golden Age, Millennium, Pandemical)
  - Complete match flow with coin toss ceremony

- **Core Play Resolution Engine**
  - D66 clash with proper success windows (1-5 based on division rank)
  - Stat-based breaker system (primary stat → card values → saving throw → re-audible)
  - D4 complications (Sack, Out of Bounds, Penalty, Interception)
  - Fumble detection (both teams roll XX)
  - Live ball mechanics

- **JKR Special Moves**
  - Ruck (♣ + JKR): Guaranteed stoppage with possession flip
  - Stiff Arm (♥ + JKR): Guaranteed TRY if driving
  - Punt (♠ + JKR): Defensive ball strip → possession grab
  - Juke Step (♦ + JKR): Guaranteed TRY if driving
  - JKR clash resolution (saving throw determines winner)

- **Smart Bot Opponent**
  - Situation-aware card selection (offense vs defense)
  - Suit-based priority system
  - Card recycling (unused cards return to bottom of deck)
  - JKR special move detection

- **UI/UX**
  - 8x8 field matrix display with formations
  - Score header with era and team info
  - Timeout system (2 per match)
  - Scoring-only play log

### Corrections Applied (POST-DELIVERY PATCH)
- [BUG 1] Dual-Split (1-1) was dead code — now correctly routes to D4 Complication
- [BUG 2] Clean Win didn't check suit for scoring — now H/D = TRY, D+K = FG, else stop
- [BUG 3] Breaker stat comparison was asymmetric — now both teams compare same contested stat
- [BUG 4] Ruck just flipped possession — NOW FIXED to guaranteed stoppage
- [BUG 5] Punt was a generic flip — now a defensive-only ball strip move
- [BUG 6] Complication save tie had no tiebreaker — driving team is now default offender
- [BUG 7] Bot hand was drawn twice per play — match loop now trusts smart_bot_logic returns
- [BUG 8] JKR standalone input crashed — now properly parsed as suit=JKR, val=15
- [BUG 9] Neutral reset (OOB/Penalty) flipped possession — now correctly keeps current driver
- [FREEZE FIX] display.py clear() replaced os.system() with direct ANSI stdout writes
- [NAME FIX] ai.py special moves corrected: STRIP→PUNT, SCRUM→RUCK

---

## [Planned - BUILD 2: COMPLETE DYNASTY] - Coming Soon
- Save/Load system for franchise progression
- Signature playbook system (JKR recall mechanics)
- Roster depth tracking (8-man starters visible)
- Draft Day implementation (4-pick post-season)
- Commissioner standings table
- Rivalry tracking system

## [Planned - BUILD 3: MONTH BUILD] - Future
- Regional Championship bracket (founder vs expansion)
- Four Nations World Cup (4-year cycle)
- Club Wipeout Crown (hemispherical brackets)
- Full 8-man roster draft
- Dual-threat veterans (JKR specialist positions)
- Star rating system (d6-1 quality)
- Trade system
- Complete persistence with save files
