# Lucky Buck — shot mechanics, owner's restated spec (November 5, 2026)

**Status: NOTES ONLY. Not implemented. Do not change the live calculator until the owner says so.**
**Standing rule from the owner: never make code changes without explicit permission.** Build changes as a separate preview page first; nothing goes live until the owner approves.
**This file supersedes** `shot-mechanics-discussion-2026-11-05.md` and the shot sections of `lucky-buck-chance-of-streak.md` wherever they conflict. The owner set aside the earlier notes and the current code and described the mechanic from scratch. Latest update: 12:38 Central.

## How to win
- Three matching dollar numbers wins that amount. Ticket values: 0, 1, 5, 25.
- A number changing does nothing on its own. Only three matching non-zero numbers is a win.

## Shot accuracy zones (each shot's accuracy is 0–100%)
| Zone | Default | What happens |
|---|---|---|
| **Bullseye range** | exactly 100% (adjustable box, e.g. 90–100%) | Full bonus chance. Counts toward shot 3's requirement. |
| **Partial hit** | anything between the zones | **Scaled** bonus chance = accuracy × that shot's bonus. Example: 75% accuracy × 5% = 3.75%. |
| **No-bonus zone** | **off** (adjustable box, e.g. 5% accuracy or less = "95% off center") | No bonus and no penalty. |
| **Complete miss** | 0% | Missed-shot penalty roll. |

## Bonus chances, stacking and display
- Every shot's bonus starts at **5%** in its own dropdown, with the **stacked (boosted) chance shown next to it in green**, also editable:
  - **Shot 1:** 5%
  - **Shot 2:** 5% | **10%** (green)
  - **Shot 3:** 5% | **15%** (green)
- **Stacking only happens when the previous roll actually succeeds** — bullseyes included. A bullseye whose roll misses does not boost the next shot.
- A successful **partial** roll stacks **its own percentage** onto the next shot. Example: shot 1 at 75% accuracy succeeds at 3.75% → a shot 2 bullseye gets 5% + 3.75% = 8.75%.
- A **shotgun sound** plays whenever a bonus roll succeeds.

## Shot 1 bonus
- If it succeeds: balloon 2 changes to match balloon 1.
- Example: hidden 5, 1, 25 → **5, 5, 25** (still a loser).
- **Zero rule:** a bonus only ever helps. If balloon 1 is 0, it becomes 1 (the next prize level) **and** balloon 2 becomes 1, from one roll. Example: 0, 0, 5 → **1, 1, 5**.

## Shot 2 bonus
- If it succeeds: balloon 3 changes to match balloon 2.
- Examples: 5, 5, 25 → **5, 5, 5** ($5). 1, 1, 5 → **1, 1, 1** ($1).
- **Same zero rule:** if balloon 2 is 0, it becomes 1 and balloon 3 becomes 1, from one roll. Example: 1, 0, 25 (shot 1 missed) → **1, 1, 1** ($1).

## Shot 3 bonus — prize upgrade
- If it succeeds, a **winning** card moves up exactly one prize level: **1 → 5 → 25 → Grand Prize**.
- **Grand Prize:** its own dropdown next to shot 3's boxes, default **$50**, editable. ("Grand prize ($50)".)
- **Eligibility:** shots 1 **and** 2 must both land in the **bullseye range** **and** their rolls must **succeed**.
- Shot 3 itself gets the full chance on a bullseye, or a **scaled** chance on a partial hit.
- On a card that is **already a winner** (e.g. 1, 1, 1), shots 1 and 2 still roll and can succeed (and play the sound) even though nothing changes, so the card can still earn the upgrade: 1, 1, 1 → **5, 5, 5**.
- A **losing** card is never upgraded. Example: three successful bullseyes on 5, 5, 25 → stays a loser.

## Missed-shot penalty
- A **complete miss** (0% accuracy) rolls a chance that **the missed balloon turns to 0**.
- **One dropdown** for all misses on any balloon ("Missed shot penalty"), default **5%**.
- **Back-to-back misses stack:** 5%, then 10%, then 15%.
- Example: 5, 5, 5 winner, shot 2 misses and the penalty hits → **5, 0, 5** (loser).

## Popping order (owner, 17:24 Central)
- A ticket's three numbers are generated **at purchase** and live in the player's inventory until scratched.
- Numbers follow **popping order, not balloon position**: the first balloon popped (any of the three) shows the 1st number, the second popped shows the 2nd, the third shows the 3rd. The player doesn't need to know this.
- "Shot 1, 2, 3" always means the order shots are fired, so all bonus rules above are unchanged.
- The simulator keeps **left-to-right popping for now**; any-order popping comes with the future tap-to-shoot animation update. Code keeps the ticket's numbers separate from shot effects so it plugs in cleanly, and other tickets can reuse "1st revealed, 2nd revealed" the same way.

## How stacked chances are calculated in the v3.1 preview (confirm with owner)
- Each shot's own chance = its bonus × accuracy (100% for a bullseye; e.g. 75% accuracy → 75% of 5% = 3.75%).
- After a **successful bullseye**, the next shot adds the green boost (green minus that shot's own bonus): defaults give 10% on shot 2 and 15% on shot 3.
- After a **successful partial hit**, the next shot adds that partial chance (5% + 3.75% = 8.75%).
- A partial hit on shot 2 after a successful shot 1 bullseye: 3.75% + 5% boost = 8.75%. Shot 3 partial at 75%: 3.75% + 10% = 13.75%.
- Back-to-back misses stack on consecutive misses (5%, 10%, 15%) whether or not the earlier penalty roll hit.

## Double Down
- Stacks with the shot 3 upgrade. A Grand Prize ($50) that also hits Double Down pays **$100**.

## Worked examples from the owner
1. Hidden 5, 1, 25. Shot 1 bullseye succeeds → 5, 5, 25. Shot 2 bullseye succeeds → 5, 5, 5. **$5 winner.**
2. Hidden 0, 0, 5. Shot 1 bullseye succeeds → 1, 1, 5. Shot 2 bullseye succeeds → 1, 1, 1. Shot 3 bullseye succeeds → **5, 5, 5.**
3. Hidden 1, 0, 25. Shot 1 misses, shot 2 bullseye succeeds → **1, 1, 1.** No upgrade chance (shot 1 wasn't a successful bullseye).
4. 25, 25, 25 with three successful bullseye rolls → **$50 Grand Prize**; plus Double Down → **$100**.

## Possible future question (not raised by owner yet)
- The simulator never deals 0, 0, 0, and bonuses never spread zeros, but the **miss penalty can now create zeros**. Check with the owner whether any further zero handling is wanted.

## Next steps
1. **Done (owner approved, 17:33):** built as a separate preview page, `shots-preview.html` (v3.1 preview). Live `index.html` untouched. The preview keeps its own saved data, copied once from the live save.
2. Owner tests the preview on iPhone and gives feedback.
3. Only with explicit permission: make it live.

## Known gaps in the current code (v3.0) vs this spec
- Shots 1 and 2 share one effect rate; no separate or boosted dropdowns.
- Shot 3 does nothing; no Grand Prize.
- A bonus can copy a 0 forward (e.g. 0, 5, 25 → 0, 0, 25), which breaks the zero rule.
- Bullseye is fixed at exactly 100%; no bullseye range or no-bonus zone boxes.
- Stacking currently multiplies on consecutive 100% shots regardless of whether the roll succeeded.
- Current penalties scale for any shot below 50% and replace a matching number with a different non-zero value; spec wants penalties only on a complete miss, turning that balloon to 0.
