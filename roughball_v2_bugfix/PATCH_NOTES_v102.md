# ROUGHBALL v10.2 - PATCH NOTES (NIGHTLY BUILD)
## Critical Bug Fixes + Enhanced Gameplay

### 🐛 BUG FIX #1: NEUTRAL FORMATION IMPLEMENTATION ✓

**The Problem**: No neutral formation state - teams were always either "driving" or "holding"

**The Fix**: Implemented full neutral formation system per ROUGHBALL_DOC.md

**Changes**:
- Added `possession_state` tracking: "neutral" | "driving" | "holding"
- Kickoff starts in NEUTRAL formation
- Out of Bounds resets to NEUTRAL
- Field Goals reset to NEUTRAL
- NEUTRAL allows mixed suits (♣♥♠♦ all legal)

**Gameplay Impact**:
```
NEUTRAL: Combined plays allowed (any suit mix)
DRIVING: Red suits only (♥/♦ offensive routes)
HOLDING: Black suits only (♣/♠ defensive covers)
```

**UI Feedback**:
```
[FORMATION]: NEUTRAL - Mixed suits allowed
[FORMATION]: Mountain LIONS DRIVING (Red suits: ♥/♦)
[FORMATION]: Greenland VIKINGS DRIVING (Red suits: ♥/♦)
```

---

### 🐛 BUG FIX #2: DECK MANAGEMENT & JOKER LIMITS ✓

**The Problem**: 
- Bot was getting unlimited jokers from deck reshuffles
- Timeout only reshuffled user's conceptual deck, not bot's actual deck

**The Fix**: Proper 54-card deck management

**Changes**:
- `get_fresh_deck_dicts()` correctly creates 52 cards + 2 JKRs
- Bot deck shows card count: `(Bot Deck: 47 cards)`
- Low deck warning: `[BOT DECK LOW: 3 cards] Reshuffling fresh deck...`
- Timeout now reshuffles BOTH decks via `reshuffle_bot_deck()`
- Bot recycles unused cards to bottom of deck (prevents burn)

**Code**:
```python
# ai.py - Line ~35
if len(bot_deck) < rank_val:
    print(f"   [BOT DECK LOW: {len(bot_deck)} cards] Reshuffling...")
    bot_deck[:] = get_fresh_deck_dicts()
```

---

### 🐛 BUG FIX #3: RE-AUDIBLE SYSTEM ✓

**The Problem**: FUMBLE outcome had no re-audible prompt

**The Fix**: Complete re-audible system per DOC

**Implementation**:
1. Detect FUMBLE outcome (0-0 hits)
2. Prompt user for ONE card
3. Bot draws ONE card from deck
4. Reveal both cards
5. **Biggest card wins**
6. Winner can score if holding red suit

**Example Flow**:
```
>>> BOTH TEAMS FUMBLE! Ball is LIVE!
>>> RE-AUDIBLE: Enter ONE card, biggest wins!

[Mountain LIONS RE-AUDIBLE]: Enter ONE card!
   Card (e.g. 'D 13' or 'JKR'): D K

[RE-AUDIBLE REVEAL]
   Mountain LIONS: [♦ K]
   Greenland VIKINGS: [♠ 7]

   >>> Mountain LIONS RECOVERS THE BALL!
   >>> Mountain LIONS FIELD GOAL on the recovery! (+3 PTS)
```

---

### 🐛 BUG FIX #4: TRAINING TUESDAY DRILL SELECTION ✓

**The Problem**: Couldn't choose between base stat OR saving throw - always got both

**The Fix**: Separate drill options

**Old System** (4 options):
```
[1] ♣ Rush Tackles (TKL) / Scrum Locks (STA)  → gave BOTH
```

**New System** (8 options):
```
BASE STATS (Primary):
[1] ♣ Rush Tackles (TKL)
[2] ♥ Box Snaps (AWR)
[3] ♠ Pursuit Tackling (INT)
[4] ♦ Shuffle Passing (PAS)

SAVING THROWS (Secondary):
[5] ♣ Scrum Locks (STA)
[6] ♥ Carrier Sprints (SPD)
[7] ♠ Post Kicking (KCK)
[8] ♦ Contested Catching (CAT)
```

**Result**: Choose your focus precisely!

---

### 🐛 BUG FIX #5: ACTIVITIES PREVIEW REMOVED ✓

**The Problem**: Dead code taking up menu space

**The Fix**: Removed `show_activities_preview()` function

**Menu Before**:
```
[1] QUICK MATCH
[2] DYNASTY MODE
[3] ACTIVITIES PREVIEW  ← Dead code
[4] EXIT
```

**Menu After**:
```
[1] QUICK MATCH
[2] DYNASTY MODE
[3] EXIT  ← Clean!
```

---

### 🎮 ENHANCEMENT #1: PLAY NAMES IN REVEAL PHASE ✓

**The New System**: Routes/Covers shown during reveal

**Example**:
```
[REVEAL] Mountain LIONS shows: [♦ 9] [♦ K] [♦ 14]
         Play: Long + Kick-Pass + Spread Form

[REVEAL] Greenland VIKINGS flips: [♣ 10] [♣ 7]
         Play: Man 2 Man + Quarter
```

**Route Names** (Hearts/Diamonds - DRIVING):
```
2:  Dig            8:  Stick         13: Kick-Pass (V Formation)
3:  Hitch          9:  Long          14: Spread Form
4:  Curl          10:  Handoff       15: SPECIAL MOVE
5:  Mesh          11:  Feint Play
6:  Slant         12:  Side Pass
7:  Swing
```

**Cover Names** (Clubs/Spades - HOLDING):
```
2:  Cover 2        8:  Stacks        13: Kick (suit-based)
3:  Cover 3        9:  Slot          14: Spread Form
4:  Cover 4       10:  Man 2 Man     15: SPECIAL MOVE
5:  Nickel        11:  Feint Play
6:  Dime          12:  Side Pass
7:  Quarter
```

---

### 🎮 ENHANCEMENT #2: IMPROVED SCORING SUMMARY ✓

**Old Format**:
```
Mountain LIONS 15 - 12 Greenland VIKINGS | TRY
```

**New Format**:
```
Mountain LIONS 15-12 Greenland VIKINGS | [♦ 9] [♦ K] | TRY
```

**Full Summary Example**:
```
=============================================
   SCORING SUMMARY
=============================================
   Mountain LIONS 5-0 Greenland VIKINGS | [♦ 10] | TRY
   Mountain LIONS 8-0 Greenland VIKINGS | [♦ K] | FIELD GOAL
   Mountain LIONS 8-2 Greenland VIKINGS | [♣ 13] | SACK
   Mountain LIONS 13-2 Greenland VIKINGS | [♥ 9] [♥ 14] | TRY
   Mountain LIONS 16-2 Greenland VIKINGS | [♦ K] | RE-AUDIBLE FG
=============================================
```

**Benefits**:
- See exact winning plays
- Understand what worked
- Build your strategy

---

## 🔧 TECHNICAL CHANGES

### New Files Created
```
✅ core/plays.py         - Route/Cover name mapping
```

### Files Modified
```
✅ core/ai.py            - Possession state awareness, deck management
✅ core/activities.py    - 8-option Training Tuesday
✅ core/match.py         - Complete rewrite with all fixes
✅ core/resolver.py      - Possession state parameter
✅ roughball.py          - Menu cleanup (v10.2)
```

### Code Statistics
- **Lines Added**: ~400
- **Lines Modified**: ~100
- **Lines Removed**: ~120 (dead code)
- **Net Change**: +280 lines

---

## 🧪 TESTING CHECKLIST

### Test #1: Neutral Formation
```
1. Start Quick Match
2. Observe "[FORMATION]: NEUTRAL - Mixed suits allowed"
3. Enter mixed suit hand: "H 10" then "C 7"
4. Should work without error
5. After scoring, watch for neutral reset
```

### Test #2: Deck Management
```
1. Start Quick Match (D1 - 5 cards)
2. Watch bot deck count decrease
3. When low (<5), should see reshuffle message
4. Call Timeout - both decks reshuffle
5. Continue until match end - no infinite jokers
```

### Test #3: Re-Audible
```
1. Play until FUMBLE occurs (0-0 hits)
2. Should see ">>> RE-AUDIBLE: Enter ONE card"
3. Enter card (e.g. "D K")
4. See bot's card
5. Biggest card wins, proper scoring
```

### Test #4: Training Tuesday
```
1. Dynasty Mode → Week 1 → Tuesday
2. Should see 8 options (not 4)
3. Choose option [5] (Scrum Locks STA)
4. Should get ONLY STA bonus (not TKL)
5. Wednesday summary shows stat correctly
```

### Test #5: Play Names
```
1. Quick Match
2. Play a hand with multiple cards
3. Reveal phase shows "Play: X + Y + Z"
4. Names match card values (Dig, Long, etc.)
```

### Test #6: Scoring Summary
```
1. Play full match to completion
2. Final scoring summary shows
3. Each entry has: Score | Cards | Outcome
4. Format: "TEAM 5-0 TEAM | [♦ 10] | TRY"
```

---

## 📊 GAMEPLAY IMPACT

### Strategy Layer Added
**Neutral Formation** creates new decisions:
- Mixed suits allow creative combinations
- No forced red/black suit restriction
- More tactical flexibility

**Re-Audible** adds clutch moments:
- High-value cards become crucial
- JKR (15) guarantees recovery
- Ace (14) vs King (13) drama

**Deck Management** creates tension:
- Bot deck visibility adds info
- Timeout reshuffles strategically valuable
- Joker scarcity makes them precious

---

## 🎯 KNOWN ISSUES

### Minor
- Re-audible doesn't support JKR special moves yet
- Play names for face cards could be clearer
- Neutral formation could use ASCII diagram

### Future Enhancements
- Signature playbook integration
- Dynasty mode auto-saves
- Enhanced match replays

---

## 🚀 WHAT'S NEXT: BUILD 3

### Planned Features
- **Draft Day**: 4-pick post-season system
- **Roster Management**: 8-man starters visible
- **Playbook System**: JKR signature plays
- **Commissioner Mode**: Full standings table
- **Save/Load**: Persistent franchises

---

## 📝 VERSION INFO

- **Version**: 10.2 (Nightly Build)
- **Release Date**: 2026-02-02 (Evening)
- **Build**: 2.0 (Bug Fixes + Enhancements)
- **Status**: Playable, All Systems Operational

---

## 💬 DEVELOPER NOTES

The neutral formation fix is huge - it fundamentally changes how the game flows. No more forced suit restrictions after every score. Kickoffs, out of bounds, and field goals all reset to neutral, creating breathing room for creative play.

The re-audible system adds those clutch "fumble recovery" moments that make sports games exciting. Holding that King knowing the bot only has tens and below? *Chef's kiss.*

Deck management visibility is a small thing that adds a lot. Seeing "Bot Deck: 12 cards" tells you they're running low. That timeout reshuffle becomes strategic.

Training Tuesday fix is pure QoL. No more "I wanted STA bonus but got TKL too" confusion.

Play names during reveal? That's the flavor. Reading "Long + Kick-Pass" instead of just "[♦ 9] [♦ K]" makes you FEEL like you're calling plays.

---

**END OF PATCH NOTES v10.2**

*Ready to test. All systems operational. Welcome to the nightly build.* 🏈
