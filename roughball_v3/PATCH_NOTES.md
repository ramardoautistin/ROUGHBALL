# ROUGHBALL v10.1 - PATCH NOTES
## BUILD 1.1: Bug Fixes + Dynasty Mode (Week Sprint)

### 🐛 CRITICAL BUG FIXES

#### Bug #1: Team ID Mismatch (RESOLVED ✓)
**The Problem**: When selecting teams from the menu, IDs 5/6/13/14 didn't match their internal data
- Menu showed "Eastern EAGLES" at ID 5, but code had "Eastern SEAHAWKS"
- This broke carnage coordinates and bracket pairings

**The Fix**:
```
ID 5:  Eastern EAGLES (Founder) ✓
ID 6:  City PATRIOTS (Founder) ✓
ID 13: Lake SEAHAWKS (Expansion) ✓
ID 14: Eastern ROYALS (Expansion) ✓
```

**Impact**: Founder/Expansion mirrors now work correctly across all brackets

---

#### Bug #2: RUCK Special Move (RESOLVED ✓)
**The Problem**: RUCK (♣ + JKR) was routing to The Breaker instead of guaranteed stoppage

**What the Doc Says**: 
> "Scrimmage. Immediately play goes stale."

**The Fix**: RUCK now works exactly like PUNT:
- Guaranteed stoppage (no dice, no breaker)
- Possession flip
- No points awarded

**Before**:
```python
if move_type == "RUCK":
    print("Routing to BREAKER...")
    return resolve_breaker(...)
```

**After**:
```python
if move_type == "RUCK":
    print("Immediate stoppage. Possession FLIPS!")
    return (0, 0, not u_driving, "RUCK")
```

---

### 🎮 NEW FEATURE: DYNASTY MODE

Full 12-week franchise management system with daily activities!

#### Weekly Structure
```
Mon → 📊 MEDIA MONDAY      (stat penalty)
Tue → 🏋️ TRAINING TUESDAY  (stat bonus - YOUR CHOICE)
Wed → 📚 STUDY WEDNESDAY   (save throw bonus)
Thu → 🏚️ D4 Backyard Match
Fri → 🚌 D3 High School Match
Sat → 🎓 D2 College Match
Sun → 🏈 D1 National Match
```

#### Season Phases
- **Weeks 1-3**: LINEAGE QUALIFIERS (Pre-Season)
- **Weeks 4-6**: CARDINAL CARNAGE (Regular Season)
- **Weeks 7-9**: BLOOD DISQUALIFIERS (Playoffs)
- **Weeks 10-12**: ROUGHBALL WILDCARD (Off-Season)

---

### 📊 MEDIA MONDAY (Automatic)
Random d4 event with d4-1 penalty to random stat:
1. **Press Conference** → TKL penalty
2. **Radio Interview** → AWR penalty
3. **Live Show** → INT penalty
4. **News Article** → PAS penalty

**Era Flavor Examples**:
- Old-Timey: "Regional newspaper column by lead sports writer"
- Golden Age: "Magazine cover feature with unflattering quotes"
- Millennium: "Personal blog article misconstrued by online media"
- Pandemical: "Viral social media post sparks controversy"

---

### 🏋️ TRAINING TUESDAY (Interactive)
YOU choose your drill focus, system rolls d4-1 bonus:

```
[1] ♣ Rush Tackles (TKL) / Scrum Locks (STA)
[2] ♥ Box Snaps (AWR) / Carrier Sprints (SPD)
[3] ♠ Pursuit Tackling (INT) / Post Kicking (KCK)
[4] ♦ Shuffle Passing (PAS) / Contested Catching (CAT)
```

**Result**: +0 to +3 bonus to BOTH stats (primary + saving throw)

**Facilities by Era**:
- Old-Timey: Muddy training field with wooden goalposts
- Golden Age: Professional sports arena dome with turf
- Millennium: Corporate-funded stadium with latest equipment
- Pandemical: Private facility HQ with VR training systems

---

### 📚 STUDY WEDNESDAY (Automatic)
Random d4 method with d4-1 bonus to random saving throw:
1. **Blackboard Lecture** → STA bonus
2. **Film Review** → SPD bonus
3. **Playbook Design** → KCK bonus
4. **Rivalry Analytics** → CAT bonus

**Era Flavor Examples**:
- Old-Timey: "Photographed stills and grainy 8mm film reels"
- Golden Age: "VHS tapes from handycam recordings, frame-by-frame"
- Millennium: "DVD replay highlights compiled and categorized"
- Pandemical: "Instant tablet clip-reviews with AI breakdowns"

**After Wednesday**: Full stat summary displayed
```
[WEEK 1 STAT MODIFIERS]
TKL: +2 | AWR: -1 | INT: +0 | PAS: +3
STA: +1 | SPD: +2 | KCK: +0 | CAT: +1
```

---

### 🏈 MATCH DAYS (Thu-Sun)
Play across all 4 divisions each week:
- **Thursday**: D4 Backyard Amateurs (2 cards)
- **Friday**: D3 High School Pros (3 cards)
- **Saturday**: D2 College Superstars (4 cards)
- **Sunday**: D1 National Legends (5 cards)

**Three Options Per Match**:
- [P] Play (full match simulation)
- [S] Simulate (instant random result)
- [C] Continue (skip this match)

**Tier-Based Naming**: Your team appears as different tiers:
- D1: "Mountain LIONS"
- D2: "College Wildcats"
- D3: "High School Lynx"
- D4: "Backyard Cougars"

---

### 🎯 DYNASTY FLOW

```
1. Select Era (Old-Timey → Pandemical)
2. Select Franchise (1-16, shows Founder/Expansion)
3. Enter Week 1

FOR EACH WEEK (1-12):
  Monday    → Media event (auto penalty)
  Tuesday   → Training drill (your choice, bonus)
  Wednesday → Study session (auto bonus)
  Thursday  → D4 match (play/sim/skip)
  Friday    → D3 match (play/sim/skip)
  Saturday  → D2 match (play/sim/skip)
  Sunday    → D1 match (play/sim/skip)
  
  → Reset stats, advance to next week

4. Week 12 ends → "Draft Day coming in BUILD 3"
```

---

### 🔧 TECHNICAL DETAILS

**Files Modified**:
- `core/teams.py` - Fixed team ID assignments
- `core/resolver.py` - Fixed RUCK special move
- `roughball.py` - Added Dynasty Mode loop
- `CHANGELOG.md` - Full documentation

**Files Added**:
- `core/activities.py` - Complete weekly activities system

**Lines of Code**: ~500+ new (activities module + dynasty loop)

---

### 📋 WHAT'S WORKING NOW

✅ Quick Match (original simulator)
✅ All 16 teams with correct IDs
✅ All JKR special moves (including fixed RUCK)
✅ Dynasty Mode with 12-week season
✅ Media Monday (auto penalties)
✅ Training Tuesday (interactive bonuses)
✅ Study Wednesday (auto bonuses)
✅ Match days across all 4 divisions
✅ Era-specific flavor text (4 eras × ~40 scenarios)
✅ Weekly stat tracking and reset
✅ Season phase progression

---

### 🚧 COMING IN BUILD 2

⏳ Save/Load franchise data
⏳ Signature playbook system
⏳ Draft Day (4-pick post-season)
⏳ Commissioner standings table
⏳ Rivalry tracking
⏳ Full roster depth visualization

---

### 📖 HOW TO TEST

**Quick Test (Bug Fixes)**:
```
1. Launch game → [1] Quick Match
2. Select ID 5 (should be "Eastern EAGLES")
3. Select ID 13 (should be "Lake SEAHAWKS")
4. Play a match, trigger RUCK (♣ + JKR)
   → Should flip possession immediately, no breaker
```

**Dynasty Test (New Feature)**:
```
1. Launch game → [2] Dynasty Mode
2. Select Era 4 (Pandemical)
3. Select Team 1 (Mountain LIONS)
4. Go through Week 1:
   - Mon: See media event + penalty
   - Tue: Choose drill, see bonus
   - Wed: See study method + bonus + stat summary
   - Thu-Sun: Play/sim/skip matches
5. Advance to Week 2, stats should reset
```

---

### 🎮 PLAY IT NOW

```bash
cd roughball_v2
python roughball.py
```

---

### 💬 DEVELOPER NOTES

The dynasty mode represents the core "management simulation" loop that makes Roughball feel like a real sports franchise game. The era-specific flavor text alone (60+ unique descriptions) gives each playthrough a distinct feel.

The stat tracking system is robust - bonuses and penalties accumulate throughout the week and affect matches, then reset cleanly for next week. This creates real strategic decisions around when to play your important matches (after Training Tuesday for max bonus? Or risk Monday penalties?).

**Most Satisfying Feature**: Watching your team name change across divisions. Playing as "High School Lynx" on Friday, then "Mountain LIONS" on Sunday, really sells the "multi-tier league system" concept.

**Most Complex Code**: The activities module with its era-flavor matrices. Each activity has 4 variants × 4 eras = 16 unique text outputs, all while maintaining proper game balance.

---

**END OF PATCH NOTES v10.1**
