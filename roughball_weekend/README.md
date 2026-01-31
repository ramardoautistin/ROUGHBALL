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
# Make sure you're in the roughball_weekend directory
cd roughball_weekend

# Run the game
python3 roughball.py

# Or make it executable
chmod +x roughball.py
./roughball.py
```

## Controls

### Main Menu
- `1` = Quick Match
- `2` = Activities Preview (your tables)
- `3` = Exit

### In Match
- **Card Input Format**: `D 13` or `H K` (suit + value)
  - Suits: `C` (Clubs), `H` (Hearts), `S` (Spades), `D` (Diamonds)
  - Values: `2-10`, `J`, `Q`, `K`, `A`, `JKR`
  
- **Timeout**: Type `T` instead of card count
  - Reshuffles your deck
  - 2 timeouts per match

### Input Examples
```
[TACTICS]: Cards (1-5) or 'T' for Timeout (2 left): 3
[INPUT]: CALLING 3 PLAY CARDS.
   Card #1: H 7
   Card #2: D Q
   Card #3: JKR
```

## File Structure

```
roughball_weekend/
├── roughball.py           # Main entry point
├── core/
│   ├── __init__.py       # Package init
│   ├── teams.py          # Team data (16 NRBL teams)
│   ├── cards.py          # Deck management
│   ├── dice.py           # D66, D4 rolling
│   ├── display.py        # UI functions (your original)
│   ├── ai.py             # Smart bot logic (your original)
│   ├── resolver.py       # Play resolution engine
│   └── match.py          # Match loop (your original flow)
└── README.md             # This file
```

## What's NOT in BUILD 1

❌ Dynasty Mode (coming in BUILD 2)
❌ Draft system (coming in BUILD 2)
❌ Save/Load (coming in BUILD 3)
❌ Tournament modes (coming in BUILD 3)

## Testing Checklist

### Basic Functionality
- [ ] Can start a Quick Match
- [ ] Field displays correctly
- [ ] Card input works (various formats)
- [ ] Timeout system works
- [ ] Bot makes intelligent decisions

### Mechanics
- [ ] D66 success windows work correctly for each division
- [ ] Stat-based breaker resolves properly
- [ ] D4 complications trigger and resolve
- [ ] JKR special moves activate (test all 4 types)
- [ ] Fumbles trigger re-audibles
- [ ] Possession flips correctly

### Scoring
- [ ] TRY awards 5 points + flips possession
- [ ] SACK awards 2 points + flips possession
- [ ] PENALTY FG awards 3 points
- [ ] INT awards 1 point + flips possession
- [ ] Mercy rule ends game at 25 points

### Edge Cases
- [ ] Both teams roll 0 hits (fumble)
- [ ] Both teams roll same hits (stalemate)
- [ ] Both teams play JKR (JKR clash)
- [ ] Timeout with no timeouts left
- [ ] Deck runs out (should reshuffle)

## Known Issues / Limitations

1. **Bot hand construction**: Bot's hand is rebuilt from groups, which works but could be cleaner
2. **Neutral possession reset**: Currently flips possession instead of true neutral kickoff
3. **JKR playbook recall**: Not implemented (shows message, doesn't crash)
4. **Era flavor**: Commentary is basic, will be enhanced in BUILD 2

## Next Steps (BUILD 2)

When you're ready for the Week Sprint:
1. Dynasty Mode (12-week season)
2. Weekly activities (Mon-Wed with your tables)
3. Match days (Thu-Sun across divisions)
4. Draft Day (4-pick post-season)
5. Playbook system (signature plays functional)
6. Basic save/load

## Your Feedback Needed

After playtesting, please let me know:
1. Does the match flow feel right?
2. Are the mechanics working as expected?
3. Is the UI clear and readable?
4. Does the bot opponent feel fair?
5. Any bugs or unexpected behavior?
6. What should be prioritized for BUILD 2?

---

**Built with your design philosophy:**
- Honor original mechanics
- Use properly implemented logic
- Preserve your hand-written flavor text
- Maintain the "simplistic" addictive feel

Ready to test! 🏈⚡
