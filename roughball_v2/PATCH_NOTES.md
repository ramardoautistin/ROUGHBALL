================================================================================
 ROUGHBALL WEEKEND PROTOTYPE — CORRECTION PATCH NOTES
 Files Changed: core/display.py | core/ai.py | core/resolver.py | core/match.py
================================================================================

FILE: core/display.py
================================================================================

[FREEZE FIX] clear() USED os.system() — BLOCKED ON NON-STANDARD TERMINALS
  WHERE:  clear()
  BEFORE: os.system('cls' if os.name == 'nt' else 'clear')
          This spawns a subprocess. On Termux, Neovim :terminal, and certain
          CMD configurations the subprocess BLOCKS — the game loop resolves
          the play correctly, iterates back, calls clear(), and hangs before
          the next frame renders. Terminal-dependent subprocess = unreliable.
  AFTER:  Direct stdout writes only. Zero subprocess, zero shell spawn.
          Windows: enables VT processing via Win32 API so ANSI works in CMD.
          All platforms: writes \033[H\033[2J directly to sys.stdout.
          Works on: CMD, PowerShell, Windows Terminal, bash, zsh, Termux,
                    Neovim :terminal, Git Bash, mintty.

================================================================================

FILE: core/ai.py
================================================================================

[NAME FIX] SPECIAL MOVE NAMES DIDN'T MATCH THE DOC
  WHERE:  smart_bot_logic() — JKR detection block
  BEFORE: Spades + JKR = "STRIP" | Clubs + JKR = "SCRUM"
  AFTER:  Spades + JKR = "PUNT"  | Clubs + JKR = "RUCK"
  DOC REF: Special Moves Table:
           "Clubs  | Ruck  | Scrimmage. Immediately play goes stale."
           "Spades | Punt  | Ball strip becomes offensive punting!"

================================================================================

FILE: core/resolver.py
================================================================================

[BUG 1] DUAL-SPLIT DETECTION WAS DEAD CODE
  WHERE:  resolve_clash() — outcome routing block
  BEFORE: Checked "u_hits == b_hits" FIRST, which caught 1-1 and routed it
          to the Breaker. The "u_hits == 1 and b_hits == 1" check below was
          unreachable.
  AFTER:  Routing order is now:
            0-0  -> FUMBLE (re-audible)
            1-1  -> DUAL-SPLIT (D4 Complication)
            2-2  -> STALEMATE (Breaker)
            else -> CLEAN WIN
  DOC REF: Phase III: "Dual-Split: Both roll [1 Hit / 1 Miss]. Trigger D4
           Complication!" vs "The Stale: Hits match. Proceed to THE BREAKER."

[BUG 2] CLEAN WIN DIDN'T CHECK SUIT FOR SCORING
  WHERE:  resolve_clean_win()
  BEFORE: Any offensive win = instant TRY (+5). No suit check.
  AFTER:  Hearts or Diamonds -> TRY (+5)
          Diamonds + King (13) -> KICK PASS / FIELD GOAL (+3)
          Clubs or Spades while driving -> Defensive Stoppage (0, flip)
  DOC REF: Section 5 Route Reference. "K = KICK BASED ON SUIT: D = KICK-PASS"

[BUG 3] BREAKER STAT COMPARISON WAS ASYMMETRIC
  WHERE:  resolve_breaker()
  BEFORE: Each team compared their OWN suit's stat against each other.
          You could "win" the breaker by playing a suit where your team is
          strong, regardless of the actual play context.
  AFTER:  Both teams compare the SAME stat: determined by the DRIVING
          team's suit (the play is about whether the drive succeeds).
  DOC REF: Section 3: "Compare Primary Stats: Higher stat wins."

[BUG 4] RUCK SPECIAL MOVE JUST FLIPPED POSSESSION
  WHERE:  apply_special_move() — RUCK case
  BEFORE: Ruck = flip possession.
  AFTER:  Ruck = route to THE BREAKER. DOC says "play goes stale" = Breaker.
          Opponent gets a fallback Clubs 2 hand (worst possible position).
  DOC REF: Special Moves: "Ruck | Scrimmage. Immediately play goes stale."

[BUG 5] PUNT SPECIAL MOVE WAS JUST A POSSESSION FLIP
  WHERE:  apply_special_move() — PUNT case
  BEFORE: Punt = flip possession regardless of state.
  AFTER:  Punt is DEFENSIVE only. Works when activator is HOLDING.
          Effect: holder strips ball, converts to their own offensive possession.
          If activator is driving, move fails (can't strip your own ball).
  DOC REF: Special Moves: "Punt | Ball strip becomes offensive punting!"

[BUG 6] COMPLICATION SAVE ROLL TIE HAD NO TIEBREAKER
  WHERE:  resolve_complication()
  BEFORE: Tie defaulted to user_is_offender = False (arbitrary).
  AFTER:  On tie, the DRIVING team is the offender (they committed the action).
  DOC REF: Section 4: "Lower Saving Throw ROLL results in being offender."
           Tie = default to the active party.

================================================================================

FILE: core/match.py
================================================================================

[BUG 7] BOT HAND WAS BEING DRAWN TWICE PER PLAY
  WHERE:  Main match loop, after user card input
  BEFORE: After smart_bot_logic() drew, analyzed, and recycled cards, the
          match loop drew AGAIN to rebuild groups. This burned the deck at
          2x rate and made the bot's played hand inconsistent.
  AFTER:  Match loop trusts smart_bot_logic's returns (b_suit, b_max,
          b_special) and constructs b_hand directly. Zero second draw.

[BUG 8] JKR STANDALONE INPUT CRASHED / DEFAULTED WRONG
  WHERE:  Card input parsing loop
  BEFORE: "JKR" split to ["JKR"], then raw[1] threw IndexError, caught by
          fallback: s="C", v="2". Typing JKR gave you Clubs 2.
  AFTER:  Explicit JKR check as first token:
            "JKR"     -> suit=JKR, val=15
            "JKR 15"  -> suit=JKR, val=15
            "D JKR"   -> suit=JKR, val=15

[BUG 9] NEUTRAL RESET (OOB / PENALTY FG) FLIPPED POSSESSION
  WHERE:  Possession update block after resolution
  BEFORE: new_driving=None was handled as "flip" (not u_driving).
  AFTER:  new_driving=None = NEUTRAL RESET. Possession stays with current
          driver. Next play starts from neutral snap, no turnover.
  DOC REF: Section 4 [2]: "OUT OF BOUNDS: Reset play to NEUTRAL."
           Reset ≠ flip.

================================================================================
 UNCHANGED FILES (verified against ROUGHBALL_DOC.md):
   roughball.py      — Entry point, menus, activities preview. Correct.
   core/teams.py     — All 16 teams, stats, tiers, save derivation. Correct.
   core/cards.py     — 54-card deck, Card class, draw/discard. Correct.
   core/dice.py      — D66, D4, D6, success windows. Correct.
   core/__init__.py  — Package exports. Correct.
================================================================================
