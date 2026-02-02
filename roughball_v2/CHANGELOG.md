# ROUGHBALL: CHANGELOG

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
  - Ruck (♣ + JKR): Annul dice, force stalemate → Breaker
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
- [BUG 4] Ruck just flipped possession — now correctly routes to Breaker (stale play)
- [BUG 5] Punt was a generic flip — now a defensive-only ball strip move
- [BUG 6] Complication save tie had no tiebreaker — driving team is now default offender
- [BUG 7] Bot hand was drawn twice per play — match loop now trusts smart_bot_logic returns
- [BUG 8] JKR standalone input crashed — now properly parsed as suit=JKR, val=15
- [BUG 9] Neutral reset (OOB/Penalty) flipped possession — now correctly keeps current driver
- [FREEZE FIX] display.py clear() replaced os.system() with direct ANSI stdout writes
- [NAME FIX] ai.py special moves corrected: STRIP→PUNT, SCRUM→RUCK

---

## [Planned - BUILD 2: WEEK SPRINT]
- Dynasty Mode (12-week season)
- Weekly activities (Mon-Wed mechanics)
- Match days Thu-Sun across divisions
- Draft Day (4-pick post-season)
- Signature playbook system
- Basic save/load

## [Planned - BUILD 3: MONTH BUILD]
- Regional Championship + Four Nations World Cup
- Club Wipeout Crown
- Full 8-man draft + dual-threat veterans
- Complete roster management
- Advanced persistence
