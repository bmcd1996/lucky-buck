# Claude Code project instructions — Lucky Buck

## Version numbering (approved November 5, 2026)

Use three-part version numbers for the Lucky Buck calculator: **major.minor.patch** (for example, `v3.1.1`).

- **Patch (third number):** For tiny updates such as label/text changes, small cosmetic adjustments, minor UI fixes, or other narrowly scoped corrections, increase **only** the final number. Examples: `v3.1.1` → `v3.1.2` → `v3.1.3`. Do not call these `v3.2` or `v4.0`.
- **Minor (middle number):** Reserve for substantial new features or meaningful changes to the simulator, when the owner agrees the update is large enough. Example: `v3.1.x` → `v3.2.0`.
- **Major (first number):** Reserve for major overhauls, when explicitly agreed with the owner. Example: `v3.x.x` → `v4.0.0`.

For app releases, update the **visible version badge** so that it matches the release version. Always determine the current version before incrementing it. Keep tiny fixes narrowly scoped; do not alter shot odds, ticket mechanics, calculations, artwork, or unrelated UI for a text-only patch. Do not change the app's visible version solely because this instruction document changes.

**Current baseline:** `v3.4.0` — released November 8, 2026. Skill mode switch, balloon target-zone grid editor (one grid for all three balloons), Buck's Secret (gold squares), 5-shell and worst-shot rules in Skill mode, big playable ticket and play sliders in the calculator; the ticket (`ticket-1.0.0.html`/`playtest.html`) now reads the calculator's settings. Rollback branch: `backup/before-skill-mode-2026-11-08`. See `docs/release-notes/2026-11-08-v3.4.0-skill-mode.md` and the ticket recipe `docs/ticket-recipes/lucky-buck.md`.

**Previous baseline:** `v3.3.3` — committed November 6, 2026. Cosmetic/help patch: visible Momentum name becomes **Hot Streak 🔥**; rewritten and added contextual `?` explanations; tiny Original/Final labels in the individual ticket readout. All internal `momentum` save keys and calculation engine remain unchanged. Backup branch: `backup/pre-v3-3-3-2026-11-06`. Previous v3.3.2 was a Rescue Bonus label layout patch; v3.3.0 introduced the rescue-bonus mechanics. See `docs/release-notes/2026-11-06-v3.3.3-hot-streak-help.md`. The GitHub Pages/iPhone visual check is still outstanding.

**Earlier baseline:** `v3.2.2` — released November 6, 2026 (preset-only patch: Custom 1 became "Shooter Bonus", with one-time per-browser installation and backup of any prior Custom 1; no active ticket settings, past statistics, or Default/Custom 2/Custom 3 changes). Rollback branch: `backup/pre-shooter-bonus-preset-v3-2-2-2026-11-06`. Previous: `v3.2.1` (rollback `backup/pre-v3-2-1-2026-11-06`).

**Shooter Bonus preset (v3.2.2):** $1 ticket; Lose 76%, $1 21%, $5 2.5%, $25 0.5%; shot accuracies 70/75/65% as test defaults; bonuses 18/25/50%; stacking on; bullseye 95–100%; no-bonus 1–25%; miss penalty 8%; grand prize $30. Double Down 2/3 Default; Momentum 1/3 custom rates [12,25], [15,30], [18,36] at levels 1–3; Luck 1/3 custom rates at levels 1–3: [74,23,2.5,0.5], [72,25,2.5,0.5], [70,27,2.5,0.5]. Special item: Trusty Shotgun, 1 in 600, Pack. These numbers are a design experiment, not proven balance. Saved preset remains inactive until loaded. Browser Custom 1 previous content is backed up under `lucky-buck-custom1-pre-shooter-bonus-v1` on first load. Do not automatically overwrite user edits after that first migration.

These are the owner's versioning rules for future Lucky Buck updates.
