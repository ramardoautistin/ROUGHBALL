# ROUGHBALL v10.3 - CRITICAL PATCH NOTES
## ESC Backdoor + True Neutral Formation + Kickoff System

---

## 🚨 CRITICAL FIX #1: ESC BACKDOOR EVERYWHERE ✓

**The Problem**: ESC only worked at specific prompts, not universally

**The Solution**: Created `safe_input()` wrapper that REPLACES all `input()` calls

**Implementation**:
```python
# display.py - New function
def safe_input(prompt):
    """
    Universal input wrapper with ESC checking.
    EVERY input in the game now uses this!
    """
    try:
        user_input = input(prompt)
        check_escape(user_input)
        return user_input
    except KeyboardInterrupt:
        # Ctrl+C also triggers ESC
        raise EscapeToMenu("Ctrl+C - returning to menu")
```

**What Works Now**:
- ✅ Card number selection
- ✅ Individual card inputs
- ✅ Dice rolls
- ✅ Continue prompts
- ✅ Timeout decisions
- ✅ Re-audible inputs
- ✅ Training Tuesday selections
- ✅ ANY input in the game

**How to Use**:
- Type `ESC` or `esc` at ANY prompt
- Press Ctrl+C at ANY prompt
- Both instantly return to main menu

---

## 🚨 CRITICAL FIX #2: TRUE NEUTRAL FORMATION ✓

**The Problem**: 
- Neutral formation was just a label
- No enforcement of suit restrictions
- No visual difference in formation display

**The Solution**: Complete neutral mechanics implementation

### A. Suit Validation (NEW MODULE: `formations.py`)

```python
def validate_hand_formation(cards, possession_state, is_driving):
    """
    Enforces formation rules:
    - NEUTRAL: Any suits (♣♥♠♦ all legal)
    - DRIVING: Red suits ONLY (♥/♦)
    - HOLDING: Black suits ONLY (♣/♠)
    """
```

**Gameplay Impact**:
```
[FORMATION]: DRIVING: Red suits only (♥ Hearts / ♦ Diamonds)
[INPUT]: D 10
   Card #1: C 7  ← BLACK SUIT!

   [!] ILLEGAL FORMATION!
   [!] DRIVING formation requires RED suits (♥/♦) only! Invalid: ♣
   [!] Please re-enter your cards...
```

### B. Visual Formation Display

**NEUTRAL Formation** (Mirrored - from DOC):
```
      1   2   3   4   5   6   7   8
   |----------------------------------| (AWAY Endzone)
A  |  .   .   .  DT   .  DE   .   .  |
B  |  .   .  OG   .  OT   .   .   .  |
C  |  .   .   .  QG   .   .   .   .  |
D  | WB   .   .   .  RG   .   .  TB  |
 xxxxxxxxxxxxxxxxxxxOxxxxxxxxxxxxxxxxxxx << NEUTRAL SNAP POINT >>
E  | WB   .   .   .  RG   .   .  TB  |
F  |  .   .   .  QG   .   .   .   .  |
G  |  .   .  OG   .  OT   .   .   .  |
H  |  .   .   .  DT   .  DE   .   .  |
   |----------------------------------| (HOME Endzone)
```

**DRIVING/HOLDING Formation** (Asymmetric - original):
```
      1   2   3   4   5   6   7   8
   |----------------------------------| (AWAY Endzone)
A  |  .   .   .  RB   .   .   .   .  |
B  |  .   .   .   .  QB   .   .   .  |
C  | WR   .   .   .   .   .   .  TE  |
D  |  .   .  DE  OT  DT  OG   .   .  | < HOME DRIVING
 xxxxxxxxxxxxxxxxxxxOxxxxxxxxxxxxxxxxxxx << NEUTRAL SNAP POINT >>
E  |  .   .  OG  DT  OT  DE   .   .  | < AWAY HOLDING
F  |  .   .   .   .   .   .   .   .  |
G  |  .   .   .  SG   .   .   .   .  |
H  | CB   .   .   .  SG   .   .  LB  |
   |----------------------------------| (HOME Endzone)
```

**When Formations Change**:
- **Kickoff** → NEUTRAL (mirrored)
- **After scoring** → NEUTRAL (reset)
- **Out of Bounds** → NEUTRAL (reset)
- **Field Goal** → NEUTRAL (reset)
- **Normal play** → DRIVING/HOLDING (asymmetric)

---

## 🚨 CRITICAL FIX #3: KICKOFF PLAY SYSTEM ✓

**The Problem**: Coin toss determined possession (not lore-accurate)

**The Solution**: Full kickoff play resolves first possession

### Kickoff Flow:

**1. Match Setup**
```
[REFEREE]: Teams line up for the KICKOFF...
   Both teams in NEUTRAL formation

[PRESS ENTER] For Kickoff Play...
```

**2. Kickoff Play**
```
[FORMATION]: NEUTRAL - Mixed suits allowed

[COACH]: Playcalling Limit is 5 cards
[TACTICS]: Cards (1-5) or 'T' for Timeout (2 left): 3
[INPUT]: CALLING 3 PLAY CARDS.
   Card #1: H 10
   Card #2: D K
   Card #3: S 7  ← Mixed suits legal!

[REVEAL] Mountain LIONS shows: [♥ 10] [♦ K] [♠ 7]
         Play: KICKOFF PLAY
[REVEAL] Greenland VIKINGS flips: [♣ 9] [♣ 12]
         Play: KICKOFF PLAY
```

**3. Resolution**
```
[YOUR TURN] Roll your physical D66!
   Die 1 (1-6): 4
   Die 2 (1-6): 5

>>> Mountain LIONS wins the kickoff and will DRIVE!

[Next play shows DRIVING formation with red suit restriction]
```

**Kickoff Outcomes**:
- **Winner** → Drives first (offense)
- **Loser** → Holds first (defense)
- **Tie** → User drives by default

**Post-Kickoff**:
- Formation changes to DRIVING/HOLDING
- Suit restrictions NOW enforced
- Normal gameplay begins

---

## 📋 FILE CHANGES

### New Files Created:
```
✅ core/formations.py  - Suit validation logic (~70 lines)
```

### Files Modified:
```
✅ core/display.py     - safe_input() wrapper + neutral ASCII
✅ core/match.py       - Kickoff system + validation loop
✅ core/ai.py          - Kickoff possession handling
```

---

## 🧪 TESTING GUIDE

### Test #1: ESC Backdoor
```
1. Quick Match
2. At "Cards (1-5):" type: ESC
   → Should return to menu immediately
3. Try again, at "Card #1:" type: ESC
   → Should return to menu immediately
4. Try Ctrl+C at any prompt
   → Should return to menu immediately
```

### Test #2: Formation Validation
```
1. Quick Match through kickoff
2. After kickoff, when DRIVING:
3. Try entering: C 10 (black suit)
   → Should show error: "DRIVING requires RED suits only!"
4. Re-enter: D 10 (red suit)
   → Should accept and continue
```

### Test #3: Neutral Formation Display
```
1. Quick Match
2. At kickoff, observe ASCII:
   → Rows A-D and E-H should be MIRRORED
   → DT/DE/OG/OT/QG/RG/WB/TB symmetric
3. After kickoff, observe ASCII:
   → Should change to asymmetric (RB/QB/WR/TE vs CB/LB/SG)
```

### Test #4: Kickoff System
```
1. Quick Match
2. Should see "Teams line up for KICKOFF"
   → NOT "coin toss"
3. Play kickoff with mixed suits:
   → Enter: H 10, D 8, C 5 (mixed - legal in neutral)
4. See winner determined by play resolution
5. Next play enforces suit restrictions
```

### Test #5: Neutral Resets
```
1. Play until Out of Bounds occurs
   → Formation should reset to NEUTRAL
   → Mixed suits allowed again
2. Play until Field Goal scored
   → Formation should reset to NEUTRAL
3. Continue - next play is normal formation
```

---

## 🎮 GAMEPLAY CHANGES

### Strategic Depth:
**Kickoff Phase**:
- Can use mixed suit combinations
- No restrictions = more creative plays
- Winner gets offensive advantage

**Neutral Resets**:
- OOB/FG create "breathing room"
- Both teams can reorganize
- Mixed plays allowed again

**Formation Restrictions**:
- DRIVING: Forced to use offensive cards (♥/♦)
- HOLDING: Forced to use defensive cards (♣/♠)
- Can't "accidentally" play wrong suit

---

## 🐛 KNOWN ISSUES FIXED

### v10.2 → v10.3:
- ❌ ESC didn't work everywhere → ✅ Works at EVERY prompt
- ❌ No suit validation → ✅ Formation rules enforced
- ❌ No visual formation difference → ✅ ASCII shows neutral/driving
- ❌ Coin toss (not lore-accurate) → ✅ Kickoff play system
- ❌ Mixed suits always allowed → ✅ Only in neutral formation

---

## 📊 CODE STATISTICS

- **New Module**: formations.py (70 lines)
- **Modified**: display.py (+80 lines)
- **Modified**: match.py (+150 lines, major refactor)
- **Modified**: ai.py (+5 lines)
- **Net Change**: +305 lines
- **Functions Added**: 3 (safe_input, validate_hand_formation, get_formation_help)

---

## 🚀 WHAT'S NEXT: v11.0 (BUILD 3)

### Planned Features:
- **Draft Day**: Full 4-pick post-season
- **Roster Visualization**: See your 8-man roster
- **Signature Playbook**: JKR play storage
- **Save/Load**: Persistent dynasties
- **Commissioner Standings**: Full league table

---

## 💬 DEVELOPER NOTES

The kickoff system changes the entire flow - you now EARN possession through play, not luck. This is huge for competitive balance.

Formation validation prevents "oops wrong suit" mistakes and forces strategic deckbuilding. Do you hold your red cards for offense or burn them early?

The neutral formation visual is subtle but important - seeing those mirrored positions tells you "this is a reset moment" without reading text.

ESC working everywhere was the most requested QoL fix. No more being trapped in a match you want to exit!

---

**END OF PATCH NOTES v10.3**

*The game is now fully lore-accurate. Welcome to true Roughball.* 🏈
