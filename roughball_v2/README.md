# ROUGHBALL: WEEKEND PROTOTYPE

**BUILD 1: Core Mechanics & Quick Match**

## What's Working

✅ **Quick Match Mode**
- Team selection (all 16 NRBL teams)
- Division selection (D1-D5, 1-5 cards per play)
- Era selection (4 eras with flavor)
- Your exact UI (field display, score header, playbook status)
- Your exact input system (`D 13`, `H K`, `T` for timeout)

✅ **Core Mechanics**
- Proper D66 success windows (1-5 based on division)
- Stat-based breaker (primary stat → card values → saving throw)
- D4 complications (Sack, Out of Bounds, Penalty, Interception)
- JKR special moves (Ruck, Stiff Arm, Punt, Juke Step)
- Live ball mechanics (fumbles, re-audibles)
- Mercy rule (first to 25 points)

✅ **Smart Bot Opponent**
- Suit-based card selection (offense vs defense)
- Card recycling (unused cards go back to deck)
- JKR special move detection
- Unbiased decision making

✅ **Activities Preview**
- Your complete tables with era-specific variants
- Ready for BUILD 2 integration

## How to Run

```bash
cd roughball_weekend
python roughball.py
```

## Controls

### Main Menu
- `1` = Quick Match
- `2` = Activities Preview
- `3` = Exit

### In Match
- **Card Input**: `D 13` or `H K` (suit + value)
  - Suits: `C` `H` `S` `D`
  - Values: `2-10`, `J`, `Q`, `K`, `A`, `JKR`
- **Timeout**: Type `T` (2 per match, reshuffles deck)

## File Structure

```
roughball_weekend/
├── roughball.py           # Main entry point
├── core/
│   ├── __init__.py        # Package init
│   ├── teams.py           # 16 NRBL teams + data
│   ├── cards.py           # 54-card deck system
│   ├── dice.py            # D66, D4, D6 mechanics
│   ├── display.py         # UI (FIXED: no-freeze clear())
│   ├── ai.py              # Bot (FIXED: RUCK/PUNT names)
│   ├── resolver.py        # Resolution engine (9 bugs fixed)
│   └── match.py           # Match loop (9 bugs fixed)
├── CHANGELOG.md
├── PATCH_NOTES.md         # Full bug-fix documentation
└── README.md
```

## What's NOT in BUILD 1
❌ Dynasty Mode (BUILD 2)
❌ Draft system (BUILD 2)
❌ Save/Load (BUILD 3)
❌ Tournament modes (BUILD 3)
