# Lucky Buck — shot mechanics design checkpoint (November 5, 2026)

**Status: NOTES ONLY. NOT IMPLEMENTED OR APPROVED FOR DEPLOYMENT.**
**Owner instruction:** Store decisions and open questions in GitHub, not exclusively in assistant memory. Keep the regular Lucky Buck calculator unchanged while this discussion is being preserved. Especially **do not finalize or change the third-shot rule yet**; the owner wants to revisit it.
**Source:** Live design discussion, November 5, 2026, approximately 06:13 Central. The transcript contains ongoing clarifications; later clarifications supersede earlier examples.

## Core mechanic and presentation already discussed
- Lucky Buck has three balloons, popped sequentially. Ticket outcomes/prizes are hidden until revealed; this calculator is a testing tool and can expose the original three gray numbers and final numbers (green only where a shot effect changed them), compactly within the existing Special Function box. Do not enlarge that box.
- The game-player experience need not disclose hidden original numbers; a short pixel shotgun-like sound should signal when an effect actually changes a number. Preserve the existing balloon-pop/purchase-sound concepts.
- Each balloon's **shot accuracy** is selectable independently, 0–100%, with 50% neutral, 100% bullseye and 0% miss. That accuracy setting is distinct from the chance that a special shot effect actually triggers.
- The owner requested separate **editable effect chance controls for each shot**, not one shared bullseye rate. Proposed default behavior: shot 1 positive effect 5% at 100% accuracy, shot 2 positive effect 5% base at 100% accuracy (consecutive 100% bullseyes stack so effective second chance could be 10% under the established stacking rule), and shot 3 special upgrade chance initially proposed at 5%, later preferred 10%. All effect chances should be configurable individually in the simulator, including a separate third-shot dropdown.
- Maintain distinct handling of negative/miss effects unless deliberately reviewed. All code, displayed odds, batch simulations, and exported game mechanics must agree; do not silently implement a different interpretation.

## NEW first-shot zero rule — confirmed in discussion
**Critical invariant:** A successful bullseye should not harm the player. Do not propagate a leading zero to the next balloon as the positive special effect.

Owner's exact clarified example:
1. Original hidden sequence: **0, 5, 25**.
2. Shot 1 is a bullseye, and its chance-based effect *triggers*.
3. **One atomic effect makes BOTH changes:** balloon 1 changes **0 → 1**, and balloon 2 changes **5 → 1**. Final state after first effect: **1, 1, 25**.
4. If this effect does **not** trigger, neither of those two changes happens. Do not roll two separate probabilities for the two adjustments.
5. Shot 2, when its effect triggers, can then make balloon 3 match the current number in balloon 2: **1, 1, 25 → 1, 1, 1** (a $1 winner).

**Superseded example:** Earlier the assistant suggested a zero should instead copy the following $5, yielding 5,5,25. The owner corrected that example to **0,5,25 → 1,1,25**, and confirmed both modifications happen together. Do not revert to the old assistant example.

## Shot 2 / third-balloon clarification
- Normal shot order: shot 1 affects the first/second number relationship; shot 2 affects the second/third number relationship.
- User began saying 'And then same for the third balloon. If its effect...' and agreed that a successful effect is one chance roll, not separate probability rolls for its constituent number changes.
- **Open detail:** How the zero exception generalizes when the second number is zero, and how to protect other possible cases while preserving payouts, has *not* been fully specified. Do not invent a generalized zero rule or implement it without checking the owner's intention.

## NEW third-shot prize upgrade concept — PROVISIONAL, ON HOLD
- Earlier there was no fourth number, so shot 3 had no effect. User proposed giving shot 3 a different special mechanic.
- Proposed eligibility: **all three shot accuracy selections must be 100% bullseyes**. A third bullseye by itself, after misses or inaccurate earlier shots, must not unlock it.
- Proposed effect: after first two shots have made their changes, if the ticket is already a paying match, shot 3's own probability roll can **upgrade the entire winning three-number match by exactly one tier**: **1,1,1 → 5,5,5**, **5,5,5 → 25,25,25**. No skipping a tier; **25,25,25** is capped at the top.
- Requested third-shot effect probability: **default 10%**, independently editable via its **own dropdown**. Three bullseyes only make the extra roll eligible; they do not guarantee activation unless the configurable chance is 100%.
- **Unresolved:** Should a **0,0,0** match qualify for upgrade to **1,1,1**? This was raised but not agreed; the newer no-harm-first-shot rule may make the situation less common. **Do not treat zero-to-one third-shot rescue as approved.**
- **Latest explicit instruction:** '**Let's not change the final one yet, but let's save everything that we're talking about right now.**' Thus preserve this third-shot design as an *idea/working draft*, not a finalized rule or authorization to edit the live app.

## Calculator requirements and testing
- Keep separate editable dropdown percentages for shots 1, 2 and 3 inside Lucky Buck's existing Special Function area, compact and explained by a tiny help '?'; never scatter help marks or enlarge panels.
- Preserve per-ticket odds, artwork, accumulated simulation history, saved presets and data. Changes to the math must be reflected consistently in the **batch simulations**, projected probabilities and expected payout, not just single-ticket visuals.
- The existing code may still contain the old shared shot-effect rate and nonfunctional third shot. Confirm actual implementation state before coding; the checkpoint is not proof the features have been deployed.
- **No code mutation, app deployment, or data reset is authorized by this checkpoint.** When user resumes, address unresolved mechanics first and obtain explicit permission before updating the live calculator.

## Next discussion checkpoint
Confirm the generalized 'bullseyes never hurt' treatment (especially shot 2 when its current number is zero); decide whether the final/third shot can upgrade 0,0,0; only then implement and validate the calculator.
