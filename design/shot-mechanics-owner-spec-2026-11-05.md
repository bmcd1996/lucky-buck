# Lucky Buck — shot mechanics, owner's restated spec (November 5, 2026)

**Status: NOTES ONLY. Not implemented. Do not change the live calculator until the owner says so.**
**This file supersedes** `shot-mechanics-discussion-2026-11-05.md` and the shot sections of `lucky-buck-chance-of-streak.md` wherever they conflict. The owner asked to set aside the earlier notes and the current code and describe the mechanic from scratch.

## How to win
- Three matching dollar numbers wins that amount. Values on the ticket: 0, 1, 5, 25.
- A number changing does nothing on its own. Only three matching non-zero numbers is a win.

## Special feature
- The player shoots three balloons in order. A **bullseye** gives a chance at a bonus.
- Each shot's bonus chance is a separate setting: **default 5%**, adjustable in its own dropdown.

## Shot 1 (bullseye)
- 5% chance that balloon 2 changes to match balloon 1.
- Example: hidden 5, 1, 25 → **5, 5, 25** (still a loser).
- **Zero rule:** a bullseye only ever helps. If balloon 1 is 0, the 0 becomes 1 (the next prize level) **and** balloon 2 becomes 1. One roll covers both changes.
- Example: hidden 0, 0, 5 → **1, 1, 5**.

## Shot 2 (bullseye)
- 5% chance that balloon 3 changes to match balloon 2.
- Example: 5, 5, 25 → **5, 5, 5** ($5 winner). 1, 1, 5 → **1, 1, 1** ($1 winner).
- **Same zero rule:** if balloon 2 is 0, it becomes 1 and balloon 3 becomes 1, from one roll.
- Example: hidden 1, 0, 25, shot 1 misses, shot 2 bullseye triggers → **1, 1, 1** ($1 winner).

## Shot 3 (bullseye) — prize upgrade
- 5% chance (own dropdown) that all three numbers move up one prize level.
- Example: 1, 1, 1 → **5, 5, 5**.
- **Catch (confirmed):** shots 1, 2 **and** 3 must all be bullseyes. In the 1, 0, 25 example above, shot 1 missed, so the ticket ends at 1, 1, 1 — no upgrade chance.

## Full worked examples from the owner
1. Hidden 5, 1, 25. Shot 1 bullseye triggers → 5, 5, 25. Shot 2 bullseye triggers → 5, 5, 5. Shot 3 reveals 5. **$5 winner.**
2. Hidden 0, 0, 5. Shot 1 bullseye triggers → 1, 1, 5. Shot 2 bullseye triggers → 1, 1, 1. Shot 3 bullseye (all three bullseyes) triggers → **5, 5, 5.**

## Still open — ask the owner before coding
1. **Shot 2's chance:** flat 5% in its own dropdown, or does it stack (e.g. 10%) after a shot 1 bullseye, as older notes described?
2. **Shot 3 on a losing card:** assumed it only upgrades a card that is already a winner, and 25, 25, 25 is the top (no further upgrade). Confirm.
3. **Shot 3's catch:** do shots 1 and 2 only need to be bullseyes, or must their 5% rolls also have succeeded?
4. **Non-bullseyes:** assumed anything other than a bullseye does nothing (dropping the current partial-accuracy bonuses and miss penalties that can turn winners into losers). Confirm.
5. **0, 0, 0:** the simulator never deals 0, 0, 0, and under these rules zeros never spread, so shot 3 never needs to handle it — unless the owner wants 0, 0, 0 to exist as a losing ticket in the game.

## Next steps
- Owner will next describe **how this should be displayed** in the calculator.
- Then: test the current calculator against this spec and report where it matches and where it doesn't.

## Known gaps in the current code (v3.0) vs this spec
- Shots 1 and 2 share one effect rate; no separate dropdowns.
- Shot 3 does nothing.
- A bullseye can copy a 0 forward (e.g. 0, 5, 25 → 0, 0, 25), which breaks the zero rule.
- Partial accuracy and miss penalties exist that this spec may remove (open question 4).
