# Lucky Buck — Accuracy-Driven "Chance of Streak" (confirmed concept)

**Status:** Designer confirmed this is the intended mechanic on November 4, 2026. **Design note only. Do not change the live calculator/app without explicit permission.**

## Ticket and presentation
- Lucky Buck is a $1 pixel-art ticket featuring a deer/buck dressed for hunting and aiming at three balloons.
- Balloons have **hidden target centers**. The player shoots or swipes/taps to pop each balloon, with an 8-bit pop sound; balloon reveals its number.
- The base ticket's three numbers are **predetermined** before the interaction. Values on the Lucky Buck ticket: 0, 1, 5, 25. Three matching numbers constitute a cash winner (0 means no payout).
- Higher accuracy = a better *chance*, not a guarantee, to alter the **next unrevealed balloon's number** to match the balloon just hit. Exact accuracy bands and bonuses remain to be balanced.
- **Confirmed perfect-center example:** Initially the ticket is **1, 1, 5**, a loser.
  1. Player hits balloon #1 dead center, producing a chance to make balloon #2 match 1. It already does, so there is no need to change it.
  2. Player hits balloon #2 dead center. It currently reveals 1; balloon #3 is predetermined to reveal 5.
  3. A **hidden 10% roll** now decides whether balloon #3 changes from 5 to 1.
  4. If the roll succeeds, the final displayed numbers are **1, 1, 1** and the player wins **$1**. Otherwise, numbers remain **1, 1, 5** and the ticket loses.
- This changes a **losing, predetermined** ticket into a potential **winner** based on shooting accuracy plus a hidden dice roll. It does NOT merely reroll the ticket at purchase or change the base purchase odds in advance.
- A perfect hit does NOT guarantee the number changes; it supplies a percentage chance. The 10% figure above is the confirmed example for a dead-center second hit. Rates for off-center shots and other cases have not been approved.

## Important implementation/economy boundaries
- **Keep the current Cardboard to Cash calculator unchanged.** The new real gameplay mechanic is for the later full game, not the calculator's visual prototype.
- If implemented later, use a fixed base ticket and a separate, auditable skill-triggered mutation roll before the next balloon reveals; keep base numbers vs final presented numbers separate in the data model and avoid duplication or other accidental changes.
- Accuracy-based conversions raise the overall payout rate relative to predetermined base-ticket odds. Model and test these effects alongside Luck, Momentum and Double Down instead of claiming the overall odds are unchanged. Do not silently change their established, approved tables.
- No change to rare item jackpot rules without explicit designer approval.
- Not yet decided: precise target radius/accuracy tiers, probability curve for near-center shots, what happens if previous balloons do not match, whether 0 may be changed or matched, and limits to how many conversions a ticket may receive.

## Preservation
This note captures the confirmed concept and specific 1-1-5 example from the conversation. It is not authorization to implement the mechanic or modify index.html.
