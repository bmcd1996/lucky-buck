# Lucky Buck / Scratch-Off Saga — Design Recovery Notes
**Date:** 2026-11-06 (America/Chicago)  
**Status:** SAVED DESIGN DISCUSSION — NOT IMPLEMENTED  
**Purpose:** Preserve all relevant decisions, proposed changes, experimental balance settings, concerns and next steps from the Nov 6 conversation before a possible signal interruption. Do not treat experimental settings as approved production values.

## Critical latest direction (prioritize this on resumption)
The owner wants to **finish working on balancing Lucky Buck today**, not defer gameplay to a future session. They have pivoted away from forcing the existing Shot 1/2/3 upgrade mechanics to match extreme profit targets by manipulating base odds. The preferred design is a **rescue-bonus system** layered on top of normal ticket outcomes:
1. Every ticket first receives its outcome from its ordinary configured prize odds, whether automatically scratched or manually shot.
2. **Auto-scratch / skip shooting** must receive normal prize odds, with **no shooting penalty** or requirement to play the aiming minigame. This explicitly resolves the owner's worry that auto-scratching would be unfair under prior implementations.
3. Shooting manually provides an **additional upside**, principally a chance to convert an otherwise losing ticket into a paying ticket. Shooting should not quietly worsen an already winning ticket.
4. Shot 1, Shot 2 and Shot 3 become clearly labeled **rescue bonus** controls in the existing compact Lucky Buck **Shot Bonus Settings** popup. The owner likes the term **Rescue Bonus** (rather than “Save Chance”), and wants adjustable **dropdowns** to tune rescue probabilities independently.
5. **Shot 1 — Rescue Chance:** relatively small chance to rescue an underlying loser after an eligible bullseye.
6. **Shot 2 — Combo Rescue Chance:** stronger rescue opportunity for **two consecutive bullseyes**.
7. **Shot 3 — Triple Bullseye Rescue Chance:** major reward for **three consecutive bullseyes**. Owner tentatively favors a **guaranteed minimum $1 cash payout on a $1 losing ticket**, potentially 100% rescue chance by default, but expressly wants this adjustable and still wants to examine the calculator. Latest phrasing: three bullseyes should make the player **“almost guaranteed a winner.”** Thus do not regard the exact 100% rule as irrevocably finalized.
8. Already-winning tickets retain at least their original payout; a separate prize-upgrade chance to $5 or $25 is a **proposal**, not yet fully specified or approved. Do not silently use the same rescue probability as the upgrade probability.
9. The top achievement should be **three consecutive bullseyes**. One and two bullseyes can be beneficial but far less powerful. Beginner bullseyes should be hard; a skilled player, after mastering the aiming minigame, should be able to land three consistently. The proposed bullseye threshold is **95%–100%** accuracy.
10. Keep the **Trusty Shotgun special-item jackpot separate** from cash rewards, with its existing **one per 600-ticket pack** setting. Keep the ticket artwork/logo, underlying prize tiers, and other equipment modifiers intact unless explicitly discussed.
11. **Do not change the live calculator or presets as part of merely saving these notes.** The owner requested notes be saved immediately due to bad cell coverage.

## Current saved version and baseline before any mechanics change
- GitHub repository: `bmcd1996/lucky-buck`. The owner considered renaming it to `scratch-off-simulator` but **decided to leave the name**. Do not rename.
- GitHub Pages live URL: https://bmcd1996.github.io/lucky-buck/
- Last confirmed saved app version in conversation: **v3.2.2**, adding the **Shooter Bonus** preset as Custom 1; Default, Custom 2 and Custom 3 otherwise untouched.
- `Shooter Bonus` is an experimental preset, **not** a finalized in-game balance recommendation.
- Presets are stored in browser localStorage. Previous one-time Custom 1 replacement saved a separate backup and did not intentionally wipe statistics. Avoid changes to local storage migrations, histories, ticket purchase queues, data, and backups without careful review.
- The original Default configuration in `index.html` at last inspection: $1 ticket; normal prize distribution **44% lose / 32% $1 / 20% $5 / 4% $25**. Shot accuracy defaults **50/50/50**; Shot 1/2/3 bonus **5%/5%/5%**, stacking OFF, 5% miss penalty, bullseye at 100%, no-bonus zone OFF, grand prize $50; Luck/Momentum/Double Down each level 0. Trusty Shotgun special item on, 1 in 600 in pack mode.
- Saved Shooter Bonus initial configuration: $1 ticket; base chance **76% lose / 21% $1 / 2.5% $5 / 0.5% $25**. Luck level 1 custom effective rates **74/23/2.5/0.5**; Momentum level 1 custom 12% after one underlying top-prize win / 25% after two; Double Down level 2 with standard 14% top-prize doubling. Accuracy **70/75/65**, shot bonuses **18/25/50**, stacking ON, missed-shot penalty 8%, bullseye **95–100%**, no-bonus zone 1–25%, grand prize $30. Trusty Shotgun special item 1 in 600, pack mode.
- Negative “Luck” numbers seen in the UI are **not a bug**; e.g. Shooter Bonus Luck 1 takes Lose from 76% to 74% (−2 percentage points) and raises $1 from 21% to 23% (+2 percentage points). Momentum can similarly redistribute probability. The owner understands this and wants it left alone.

## Owner's long-run skill/reward targets (DESIGN TARGETS, not achieved or final code)
For **10,000 one-dollar tickets** ($10,000 cost):
- **All three shots miss:** lose almost the entire $10,000, with a very small payout.
- **One bullseye per ticket:** roughly **$10,000 total returned** / **break even**.
- **Two bullseyes per ticket:** about **$13,333 returned** / **$3,333 net profit**, extrapolated from the owner's $200 profit over 600 $1 tickets.
- **Three consecutive bullseyes per ticket:** about **$30,000 returned** / **$20,000 profit**, i.e. triple the $10,000 ticket cost.
These are aspirations for *long-run averages*; not guaranteed profits for any batch or prize on each individual scratch. A full three-bullseye streak need **not** guarantee a huge prize; however the owner leaned toward guaranteeing a small $1 rescue on an underlying loser. The owner wants the skill bonus, not Luck/Momentum/Double Down equipment, to account for most of the expert advantage. Layer equipment modifiers separately.

## Earlier experiments and findings — DO NOT deploy these numbers
- An initial **100-ticket Default** standalone test reportedly produced **61 cash winners, $237 cash returned, +$137 net**, and 1 Trusty Shotgun. The corresponding **Shooter Bonus at saved 70/75/65 accuracy** test reportedly produced **20 cash winners, $48 returned, −$52 net**, plus 1 Trusty Shotgun. These are individual randomized runs; do not present them as expected values.
- A separate **Shooter Bonus at 95/95/95 accuracy** 100-ticket experiment reportedly returned **$104, +$4 net, 23 cash winners, 7 third-shot upgrades** and 1 Trusty Shotgun. Owner considered this **terrible reward for perfect shooting**. Again, it was a run, not reliable long-run expected payout.
- An experimental custom balancing combination tried **99.5% lose / 0.4% $1 / 0.05% $5 / 0.05% $25**, with Shot 1 bonus 80%, Shot 2 bonus 3%, Shot 3 upgrade 100%, grand prize $250, miss penalty 8%, stacking OFF, equipment levels 0, Trusty Shotgun separate. It reportedly *modeled* 10,000-ticket payouts near **$111 (0 bullseyes), $10,075 (1), $13,483 (2), $29,767 (3)**, but was **explicitly rejected by owner as unnatural**: essentially every base ticket loses, bonuses are unbalanced by shot order, and rare $250 jackpots dominate payout volatility. **Do not use this as an implementation preset.**
- Default is immediately rewarding but unsustainably generous as a prospective game economy. Shooter Bonus with its existing approach is too unforgiving for average shooters and undervalues consistent triple bullseyes.
- An early thought was to keep Default as a reference and postpone balancing until Scratch-Off Saga gameplay. **Owner rejected postponement; explicitly wants to make progress today.**
- Keep the original `Default` preset intact as a benchmark. Retain `Shooter Bonus` as experimental until a new approach is approved and tested.

## Design and implementation details that matter
- The existing simulator's shooting mechanic is **sequential and order-sensitive**: first two shots can modify next balloon numbers; third shot upgrade currently requires successful previous bullseye bonus rolls and an already winning ticket. The owner initially liked sequential mechanics but has now prioritized a clearer rescue system with strong third consecutive bullseye payoff.
- Current app `index.html` code has functions such as `normalOdds`, `resolveShots`, `useShots`, `singleDraw`, `specialHit`, `shotExpected`, `simulate`. These should be carefully updated **in a separate preview first**, preserving normal auto-scratch odds and avoiding unexpected loss of existing tickets/history/artwork and modifier logic.
- Keep normal prize odds configurable. Owner floated both **25% overall chance to win** and **~50% losers**, but **neither is a committed final base win rate**. Avoid treating either as locked.
- Clarify how chance-to-rescue interacts with current accuracy percentages: qualifying as a bullseye at 95–100% should be **distinct** from the dropdown rescue probability; do not misrepresent “bullseye” as automatically meaning successful rescue unless the chosen chance is 100%.
- Consider whether the second dropdown applies an additional rescue roll after Shot 1 failure, or a single cumulative chance. This remains unresolved and must be specified before coding.
- Determine if three-bullseye rescue is only checked on originally losing tickets; preserve original cash wins and decide how prize upgrades to $5/$25 should work without double-counting payouts.
- Separate manual shooting, automatic scratching, batch simulation with random accuracies, miss behavior, and special-item pack bookkeeping. Test each path independently.
- For the 10k ticket target simulations, make sure special items are tracked separately from cash (specials currently replace a cash draw on their pack positions); report expected payout, profit, win rate, win-size distribution, and uncertainty. Test `0 / 1 / 2 / 3` consecutive bullseyes and some realistic average and expert-shot mixes.
- UI must remain compact, readable, mobile portrait one-handed, with no clipped/overlapping labels, and the actual Lucky Buck ticket art/logo preserved.
- Versioning preference from earlier discussion: small text/copy corrections use the patch digit; significant mechanics should use an appropriate version increment. No version agreed for this proposed redesign.
- User's standing workflow preference: **ask for specific authorization before modifying code or deploying**; avoid deletions/rollbacks. The current request authorizes **saving these design notes only**.

## Latest spoken exchange / handoff
Owner: “Yeah, okay, I like that. We'll change [the controls] to rescue bonus ... leave it an adjustable dropdown ... [with] normal ticket chances ... auto scratch [gets] normal chance of winning ... when you go to shoot, you're almost guaranteed a winner if you get three bullseyes ... beginner hard, skilled player learns to hit three bullseyes.”
Owner subsequently: “Hey. Save all of this to GitHub immediately, all of our notes. We're about to go through a bad service zone where you're likely to lose all of this info. Hurry up.”

**Follow-up after reconnection:** Confirm saved note, then continue designing rescue probability semantics and modeling an intuitive, skill-rewarding 10,000-ticket payout curve. No new mechanics have yet been implemented or deployed in connection with this design discussion.
