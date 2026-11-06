# Lucky Buck — session notes, Nov 5–6, 2026 (owner + Claude)

**Status at save (Nov 6, 01:00 Central): NOTHING pending is built.** Live = **v3.2.0**. Preview = **v3.2.1** (`v3-2-1-preview.html`, not live yet).
Standing rules: never change live code without the owner's go-ahead; preview first; keep changes narrowly scoped ("no crazy stuff"); ask when unclear.

## Released / built tonight
- **v3.1** shot rules → **v3.1.1** (labels) → **v3.2.0 live** (logo fix, ⚙ settings pop-up, one bonus per shot + Enable stacking, batch readout, Random accuracy, one Buy button with result labels + 24 shooting lines incl. featured "Take 'em out." at 10%, Trusty Shotgun special item, no "Show waiting ticket"). Rollback branches: `backup/pre-shot-rules-v3-0-2026-11-05`, `backup/pre-v3-2-0-2026-11-05`.
- **v3.2.1 preview** (see ledger for detail): compact modifier rows with ? popup; checkboxes replace Active Mods; straight odds rows; $0 dropdown on Lose; single "＋ Add row"; Jackpot rows removed (special item lives in ⚙ settings and as a synced ★ row in the odds editor, shown as % to nearest tenth; ✕ unchecks it in settings); Run multiple tickets under the ticket, Saved preset at top of Odds & Sims; Recent simulations under modifiers; gap fix; Shot bonus settings open as a pop-up box (3 shot boxes + shared row + red ✕); "Pop all three balloons" line removed; Luck/Momentum changes shown in parentheses beside each odds row (🐇 / 🍀, red/green). Odds/payout math unchanged from v3.2.0.

## Questions answered (no change)
- Natural 1,1,1 / 5,5,5 streaks: correct for current odds (Lose 44 / $1 32 / $5 20 / $25 4 → 56% natural winners, ~$2.32 returned per $1).
- Batch "57 triggers in 600": ~126 rolls succeed per 600 at those settings, but the readout only counts rolls that **changed a number**; ~47 expected. Correct.
- Shot 3 shows a chance even when shots 1–2 aren't bullseyes (upgrade impossible). Possible future fix: show "–". Not built.

## Tuning discussion (in progress — NOT built)
Owner goal: feels like losing ~75% normally; with 95–100% aim, win ~75%; "fun and addicting"; save as new default.
- **Inputs-only with $25 top:** hits the win rates (e.g. Lose 75 / $1 18 / $5 6 / $25 1, bonuses 80/80/30, bullseye 95–100) but pays ~**$7.28 per $1** at perfect aim — rescued losers often become $25 wins.
- **$10 top prize (tested in a copy):** Lose 75 / $1 17 / $5 6 / $10 2, bonuses 80/80/40 flat, bullseye 95–100, no-bonus ≤30%, Grand Prize $20:
  100% aim 78% wins $4.32/$1 · 60% aim 50% $1.73 · 25% aim 25% $0.67 · random Good 68% $2.66 · Poor 28% $0.82.
  Still generous because rescues pay the card's number (avg ~$4). Option discussed but **not chosen**: rescued tickets pay $1.
- **Owner decision (00:59):** change the ticket to a **$10 max** (balloons 0/1/5/10; shot-3 Grand Prize $20; Double Down unchanged, max $40). **Keep Double Down.** **Luck and Momentum stay listed but locked at 0/3** until a future rework (their tables were tuned for the old odds/$25).
- **Open confirms before building:** (1) switch the saved Lucky Buck to the new odds/settings (keep totals/history)? (2) version **v3.3.0**, including the v3.2.1 preview changes? (3) Trusty Shotgun stays 1 in 600 Pack? Also: whether to add "rescues pay $1" later.
- Modifier rework (Luck, Momentum) planned as a later step: measure win rate and payback per level and set new tables with the owner.
