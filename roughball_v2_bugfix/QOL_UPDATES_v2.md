# ROUGHBALL: Quality of Life Updates v2

## What's New

### 1. ESC Key Backdoor Exit
- **Trigger**: Press ESC at any input prompt
- **Effect**: Instant return to main menu (great for debugging!)
- **Where**: Works during card input, dice rolls, timeout prompts, and continue prompts
- **How**: Just type `ESC` or hit the actual ESC key (chr(27))

### 2. Physical Dice Input
- **What**: You can now roll your own D66 and input the results!
- **When**: After card reveal, before resolution (if no JKR played)
- **Format**: Input each die separately (1-6)
- **Why**: The tactile IRL feel of praying over your dice rolls!
- **Fallback**: Invalid input = auto-roll

### 3. Territorial Rivalry Fix
- **ID Swaps Performed**:
  - `5 <-> 14`: EAGLES ↔ SEAHAWKS (Lake Brown rivals)
  - `6 <-> 13`: PATRIOTS ↔ ROYALS (Eastern City rivals)
- **Result**: Carnage coordinates now reflect proper geographical feuds
- **Effect**: Diagonal rivalries [5,5] and [6,6] are now same-location blood wars

### 4. Neutral Formation (Planned)
- **Status**: Acknowledged but deferred to BUILD 2
- **Concept**: After Field Goals, display mirrored neutral formations
- **Reason**: Requires formation state tracking + rendering logic
- **Priority**: Medium (nice-to-have visual flourish)

## Updated Controls

### During Match
- **ESC** = Return to main menu (anywhere)
- **T** = Timeout (deck reshuffle, 2 per match)
- **q** = Quit match (at continue prompt)

### Dice Input
```
[YOUR TURN] Roll your physical D66!
   Die 1 (1-6) or ESC: 4
   Die 2 (1-6) or ESC: 6
```

## Technical Notes

### Files Modified
- `core/display.py`: Added `check_escape()` and `EscapeToMenu` exception
- `core/match.py`: Wrapped main loop in try-except, added dice input prompt
- `core/resolver.py`: Modified `resolve_clash()` to accept `u_dice` parameter
- `core/teams.py`: Swapped team ID assignments (5↔14, 6↔13)
- `roughball.py`: Updated team selection menu

### Exception Flow
```
User presses ESC
  → check_escape() raises EscapeToMenu
  → match.py catches it in main loop
  → Returns to main menu cleanly
```

### Dice Input Flow
```
User reveals cards
  → If no JKR: prompt for dice input
  → User enters d1, d2
  → Pass to resolve_clash(u_dice=(d1,d2))
  → Bot still auto-rolls
  → Compare user input vs bot roll
```

## Backward Compatibility
- All v1 features still work
- ESC is optional (ignore it if you don't need it)
- Dice input has auto-roll fallback (just press Enter)
- Team ID swaps don't break saves (stats preserved)
