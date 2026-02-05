# THE DRAFT - QUICK REFERENCE CARD

## Main Menu Option [3]

```
[3] THE DRAFT (Roster Management)
    ├── [1] Full 8-Man Roster Draft (New Franchise)
    ├── [2] Seasonal 4-Pick Draft (Post-Season)
    ├── [3] Mock Draft Scouting Report
    └── [4] Return to Main Menu
```

## Position Mapping

### Card Value → Position
- **Number Cards (2-10)**: BOTTOM position
- **Face Cards (J/Q/K/A)**: TOP position
- **JKR + Number**: CORNER position
- **JKR + Face**: DUAL THREAT VETERAN
- **JKR + JKR**: WILDCARD (choose any dual threat)

### Suits → Position Groups
```
♣ CLUBS (TKL)       ♥ HEARTS (AWR)      ♠ SPADES (INT)      ♦ DIAMONDS (PAS)
Scrimmagers         Field Generals      Pitch Guards        Air Raiders
─────────────────────────────────────────────────────────────────────────────
TOP:    DT          TOP:    QG          TOP:    OG          TOP:    WB
BOTTOM: DE          BOTTOM: RG          BOTTOM: OT          BOTTOM: TB
CORNER: LB          CORNER: SG          CORNER: CB          CORNER: SG
```

## Star Quality System

**Base Roll**: d6 - 1 = 0 to 5 stars

**Bonuses**:
- Corner Position: +1 star
- Dual Threat Veteran: +2 stars
- Wildcard (JKR+JKR): +3 stars

**Cap**: Maximum 5 stars total

**Display**:
- 0 stars = `[BUST]`
- 1-5 stars = `★★★★★`

## Dual Threat Veterans

| Card Combo | Archetype | Suits | Description |
|------------|-----------|-------|-------------|
| JKR + Jack (any) | PITCH GENERAL | ♠+♥ | Kicking + Playcalling |
| JKR + Red Queen | WING BACKER | ♣+♦ | Scrimmage + Reception |
| JKR + Red Ace | FIELD RAIDER | ♥+♦ | Handovers + Routes |
| JKR + Black Ace | SCRUM GUARD | ♣+♠ | Rucking + Punting |
| JKR + King (any) | AIR PITCHER | ♦+♠ | Catching + Goaling |
| JKR + Black Queen | TACKLE CARRIER | ♣+♥ | Scrum + Ball Protection |
| JKR + JKR | WILDCARD | Any | Choose archetype |

## Draft Modes

### Full 8-Man Roster Draft
- **Use**: New franchises or complete rebuild
- **Picks**: 8 starters
- **Goal**: 2 per suit minimum for balance
- **Returns**: Complete starting roster

### Seasonal 4-Pick Draft
- **Use**: Post-season roster expansion
- **Picks**: 4 backup players
- **Goal**: Depth and trade assets
- **Returns**: 4 players for backup roster

### Mock Draft Scouting
- **Use**: See what other teams are doing
- **Picks**: Simulates all 16 teams
- **Info**: Finalists (2 picks) vs Rebuilding (4 picks)
- **Returns**: Nothing (just information)

## Example Draft Flow

```
1. Press ENTER to draw card
2. Card revealed: [♣ 13] (King of Clubs)
3. Position determined: DT (Defensive Tackle - TOP position)
4. Star roll: d6-1 = 4 stars
5. Result: "DT (Scrimmager) - ★★★★ (4/5)"
```

### With Joker:
```
1. Card drawn: [JKR]
2. Second card: [♥ 12] (Red Queen)
3. Archetype: WING BACKER (Scrimmage + Reception)
4. Star roll: d6-1 = 3, +2 bonus = 5 stars
5. Result: "WING_BACKER - ★★★★★ (5/5) [DUAL THREAT]"
```

## Integration Status

**✅ COMPLETE**:
- Main menu integration
- All three draft modes functional
- Proper position mapping
- Joker mechanics working
- Star quality system

**🔄 IN PROGRESS**:
- Dynasty Mode integration (Week 12)
- Roster persistence
- Stat application to teams

**📋 PLANNED**:
- Trading system
- Player development tracking
- Veterancy (9+ seasons)
- Coaching archetypes from veterans

## File Locations

```
roughball_v2/
├── roughball.py              (UPDATED - main menu)
├── core/
│   ├── draft.py              (NEW - draft system)
│   ├── teams.py              (existing)
│   ├── display.py            (existing)
│   └── ...
└── DRAFT_UPDATE_v104.md      (this update notes)
```

## Quick Test

1. `python roughball.py`
2. Select `[3]`
3. Select `[1]` (Full Roster Draft)
4. Press ENTER 8 times to draft your team
5. Check final roster display

## Design Doc Compliance

✅ Position mapping matches ROUGHBALL_DOC.md exactly  
✅ Joker system per design specs  
✅ Star quality d6-1 formula  
✅ Dual threat archetypes correct  
✅ 8-man starter / 4-man backup structure  
✅ Deck management and reshuffling  

---

**Version**: 10.4 "The Draft Update"  
**Status**: Production Ready  
**Next**: Dynasty Mode integration
