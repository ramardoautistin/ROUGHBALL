# ROUGHBALL: CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project follows a build-based versioning scheme.

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
  - Ruck (♣ + JKR): Annul dice, force stalemate
  - Stiff Arm (♥ + JKR): Guaranteed TRY
  - Punt (♠ + JKR): Possession flip
  - Juke Step (♦ + JKR): Humiliating TRY
  - JKR clash resolution (saving throw determines winner)

- **Smart Bot Opponent**
  - Situation-aware card selection (offense vs defense)
  - Suit-based priority system
  - Card recycling (unused cards return to bottom of deck)
  - JKR special move detection
  - Unbiased decision making

- **UI/UX (Original Design Preserved)**
  - 8x8 field matrix display with formations
  - Score header with era and team info
  - Playbook status display
  - Timeout system (T to reshuffle, 2 per match)
  - Card input format: `D 13`, `H K`, `JKR`
  - Scoring-only play log

- **Activities System Preview**
  - Complete tables for Media Monday (4 events × 4 era variants)
  - Complete tables for Training Tuesday (drills × facilities)
  - Complete tables for Study Wednesday (4 methods × 4 era variants)
  - Match day descriptions (Thu-Sun, D4-D1)
  - Ready for integration in BUILD 2

- **Documentation**
  - Complete README with usage instructions
  - Testing checklist
  - File structure documentation
  - Control reference
  - Known issues and limitations

### Technical Details
- Modular architecture (core package with 8 modules)
- Proper package initialization
- Clean separation of concerns (display, logic, AI, data)
- Compatible with Python 3.6+

### Known Limitations
- Dynasty Mode not implemented (BUILD 2)
- Draft system not implemented (BUILD 2)
- Save/Load not implemented (BUILD 3)
- JKR playbook recall shows message but doesn't function
- Neutral possession reset flips instead of true kickoff
- Era-specific commentary is basic (will enhance in BUILD 2)

---

## [Planned - BUILD 2: WEEK SPRINT]

### Planned Features
- Dynasty Mode (12-week season structure)
- Weekly activities with era-specific flavor
  - Media Monday (d4-1 penalty system)
  - Training Tuesday (d4-1 bonus, user selects stat)
  - Study Wednesday (d4-1 saving throw bonus)
- Match days across divisions (Thu-Sun, D4-D1)
- Draft Day (4-pick post-season roster refresh)
- Signature playbook system (functional storage and recall)
- Basic save/load (JSON-based persistence)
- Season standings tracker
- Stat boost/penalty tracking

---

## [Planned - BUILD 3: MONTH BUILD]

### Planned Features
- Regional Championship mode (16 teams, 4 regions, playoff bracket)
- Four Nations World Cup (4-year cycle tournament)
- Club Wipeout Crown (32 international teams)
- Full 8-man draft system
- Dual-threat veteran mechanics (JKR combinations)
- Star rating system (d6-1, veterancy progression)
- Complete roster management (8 starters + 4 backups)
- Advanced save/load (complete dynasty persistence)
- Match/season summary exports
- Historical era progression
- Team rivalry tracking

---

## Development Notes

**Design Philosophy:**
1. Honor original mechanics from handbook
2. Focus on gameplay with properly implemented logic
3. Preserve hand-written flavor text (double quotes)
4. Maintain "simplistic" addictive feel

**Commit Strategy:**
- BUILD 1: Core mechanics foundation
- BUILD 2: Weekly progression systems
- BUILD 3: Full companion tool features

**Testing Focus per Build:**
- BUILD 1: Mechanics accuracy, UI clarity, bot fairness
- BUILD 2: Activity flavor, progression feel, save reliability
- BUILD 3: Tournament structure, persistence, export quality
