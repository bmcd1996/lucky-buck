# Lucky Buck — planned updates (owner-approved list, November 5, 2026)

**Status: NOTES ONLY. Nothing here is built yet.** Owner said "not yet" to building; Claude may choose the build order when the owner says go.
**Rules:** never change calculator code without the owner's explicit go-ahead; build as a preview page first; live only after the owner approves. Follow `CLAUDE.md` versioning. Current live: **v3.2.1** (items 1–11 done).

## v3.2.0 — DONE, live November 5, 2026 (see ledger for the extra owner tweaks made during preview)

1. **Logo fix.** The Lucky Buck heading logo is cut out of the ticket art at load; on iPhone it sometimes comes out as a black silhouette (art not decoded yet). Wait until the art is fully ready before cutting it out; if the cutout is still blank, show the "Lucky Buck" name instead. Owner wants this fixed even though a refresh clears it.

2. **Settings gear.** The whole **Ticket setup** section (logo & artwork, ticket name, item-jackpot pack size, luck curve, plus the new Special item setting) is hidden behind a **small gear** (about the size of a close "X") in the **top-left corner of the "Scratch a ticket" area, by the heading — not on the ticket itself**. Tapping it opens Ticket setup.

3. **One dropdown per shot + "Enable stacking" checkbox.**
   - Shots 1, 2, 3 each have **one** bonus dropdown (no separate green boost boxes).
   - **Enable stacking** checkbox, **unchecked by default**.
   - Unchecked: each shot uses only its own chance.
   - Checked: after a successful roll, the next shot adds that roll's chance. Shots 2 and 3 display as **x% + x% = x%** (e.g. 20% + 20% = 40%; 20% + 40% = 60%); the middle number is **automatic, not editable**; total shown in green. Same space as now.
   - Shot 3 upgrade still requires successful bullseyes on shots 1 and 2, with or without stacking.

4. **Batch readout** (after running multiple tickets), same box style as the single-ticket readout:
   - Row 1 (green): each shot's chance.
   - Row 2: how many times each shot's effect **actually changed a number**, out of Y tickets run.
   - Row 3 (red): how many times a miss turned that balloon to 0. Always shown.

5. **Random accuracy** checkbox next to "Run tickets". When checked, an **Accuracy level** dropdown appears and batch tickets roll their own accuracy per shot instead of using the shot dropdowns:
   - **Random:** any whole number 0–100%
   - **Good:** 25% bullseye, 2% miss, otherwise 70–99%
   - **Medium:** 10% bullseye, 8% miss, otherwise 40–80%
   - **Poor:** 3% bullseye, 25% miss, otherwise 1–50%
   (Owner approved these as "perfect".)

6. **One buy button.**
   - Reads **Buy 1 ticket $1**. A **cha-ching** (cash register) sound plays on every purchase.
   - Balloons are still popped by hand. While popping, the button shows numbers as revealed: `5 · ? · ?` → `5 · 5 · ?`; it can't be tapped until all three are popped.
   - After the last pop the button shows the result (no parentheses):
     - **WINNER! $1** / **WINNER! $5** — green
     - **JACKPOT! $25** — green
     - **SUPER JACKPOT! $50 / $100** — gold (any cash win above $25: Double Down $50, $50 Grand Prize, $100)
     - **!SPECIAL JACKPOT!** with the item name underneath, e.g. **Trusty Shotgun** — gold
     - **LOSER** — red
   - Tapping it again buys the next ticket (cha-ching). Every ticket still logs into the simulation totals.
   - The **Clear** button and the **Last revealed ticket** box are removed.
   - The button returns to **Buy 1 ticket $1** only when totals are cleared in the Run tickets tab.

7. **Special item setting** in Ticket settings: **Special item: [Trusty Shotgun]  Odds: [1] in [600]** — name and both numbers editable, plus **Odds type**:
   - **Pack:** exactly X per Y tickets, guaranteed (how item jackpots work now). Default for Trusty Shotgun.
   - **Random chance:** each ticket has an X-in-Y chance; streaks and droughts possible.
   - Trusty Shotgun starts as **Pack, 1 in 600**.

## Next update (after v3.2.0)

8. **Compact modifier rows.** Each modifier is one row: **Name ⓘ  [level 0/3] [Default]** — level and Default dropdowns side by side on the right. The long description and the "Double Down — Level 0" level-detail boxes move into the **?** popup.

9. **Checkboxes replace Active Mods.** Remove the Active Mods box; each modifier row gets a checkbox. Unchecked = row slightly gray and the modifier is off (its level stays saved). Also remove the summary line above the ticket ("Double Down 0/3 · Momentum 0/3 · Luck 0/3").

10. **Clean up the Prize odds editor.** Each prize on one straight row: **[Cash ▾] [$ 5]  [20 %]  +0%  ✕**. Remove the **/600 probability column** (it duplicated the percentage).

11. **Move the Run multiple tickets box above the Prize odds editor** (batch readout and random accuracy move with it).

## Future idea (not scheduled)
- In the game, a **set number of tickets sold across the whole world**; top jackpots dealt from that supply (Pack style), lesser jackpots possibly Random chance.
- Tap-to-shoot balloons in any order with animation (numbers follow popping order, per the shot spec).


## Next update notes — post-v3.3.2 (added November 6, 2026; NOTES ONLY)

- **Lucky Buck Special Function / individual-ticket six-box readout:** Preserve the existing two rows of three boxes and their behavior. Add tiny, unobtrusive row labels **Original** (the three originally drawn numbers, currently shown as dashes before a ticket is available) and **Final** (the three revealed numbers, initially question marks). Green still highlights numbers changed by the rescue/upgrade mechanic. Keep the panel compact on iPhone; labels must not enlarge it significantly, overlap, or push boxes out of alignment. Do **not** replace this with the separate batch-statistics readout. This is a requested future UI improvement, **not yet implemented**. No changes to the shot rules or payout odds are requested here.
