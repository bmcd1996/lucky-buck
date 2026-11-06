# Lucky Buck simulator — approved UI update ledger
**Updated:** November 4, 2026
**Live calculator:** https://bmcd1996.github.io/lucky-buck/
**Current checked baseline:** v2.7; index.html blob SHA d94e0b98a04986e7a7c0ef58a427934f3fc1811a; code commit 6d526dd902b87f7db62aada2e013dc185e20c99b.
**Project distinction:** Lucky Buck is the probability simulator for Quill Productions' Scratch-Off Saga game. The actual Godot game lives privately in bmcd1996/project-quill. Do not mix their data or design tasks.

## Existing implementation / accepted design
- Three level status indicators in ticket header: Double Down, Momentum, Luck, each 0–3.
- Saved presets: protected Default, Custom 1, Custom 2, Custom 3; user-saved settings live locally. Presets must not silently overwrite other slots.
- Remove old redundant "Momentum is off. Choose a level..." line from Equipped Modifiers.
- v2.7: compact top-right version badge; visible $ prefix on ticket price and cash-prize inputs; concise Shot Effect Rates explanation.
- Compact consistent typography, including labels, odds and values. Never enlarge existing boxes merely to make explanation text fit; prefer concise wording/wrapping.
- Shot effect rates should describe the percentage setting's influence on the NEXT balloon number (above 50% can turn losers into winners; below 50% can turn winners into losers; exactly 50% has no effect). Do not claim actual displayed pop/hit dynamically changes the next configured shot accuracy.

## Update 6 — APPROVED DESIGN, NOT IMPLEMENTED
- Replace confusing independent Add Ticket button / hidden ticket switching with a **single compact ticket selector** near the top.
- Dropdown must include all saved/created ticket names and prices and a **Create New Ticket** action at the bottom.
- Creating a ticket must not abruptly hide the previous ticket with no clear way back. Show one active ticket at a time; user can switch back in one simple dropdown.
- Switching preserves **per-ticket** price, name, prize rows, odds, modifiers, results, statistics, saved history and other independent state. No resets, data corruption or silent overwrites.
- User's hand-drawn image shows **space and placement**, not final styling: ticket title and selector side by side at top; **scratch-off prominently centered**; a very **small discreet preset selector** to the left; active modifiers aligned to the right. Keep the scratch ticket the visual star.
- No oversized preset toolbar or padded empty panel. Maintain compact font sizes, alignment, consistent dollar signs.
- Do not implement or push until user explicitly instructs. When implemented, version label should advance from v2.7 to next appropriate release; test multi-ticket switching with existing saved browser data.
- This ledger is independent of implementation and has no effect on the HTML, JS or live pages.

## Repository incident audit (November 4, 2026)
- On inspection, main branch tip was 6d526dd902b87f7db62aada2e013dc185e20c99b, v2.7; the other chat had **not** pushed a later main commit.
- Existing branches: backup/pre-layout-restore-v2-2-2026-11-04, backup/pre-shot-calculator-v2-2026-11-04, cardboard-to-cash-v2, feature/balloon-shot-calculator-v2-2; not evidence of a new rogue main update.
- One older open pull request (#4, "Cardboard to Cash v2 — all 12 approved Lucky Buck calculator upgrades") targets main from cardboard-to-cash-v2; **do not merge blindly** because it predates the newer main improvements.
- Successful GitHub Pages deployment for v2.7 commit, confirmed from Actions.
- Static JS syntax audit passed. No duplicate DOM element IDs and no missing literal document element ID references. Formula sanity checks passed: base EV $2.32; Luck level 3 EV $3.15; Momentum stage 1 top prize 20%; shot effects and state restore could be evaluated. This is **not** a complete interactive browser or device test.
- Do not roll back v2.7 without evidence of damage. No data-reset operations authorized.

## Owner's idea-preservation rule (November 4, 2026)
- Owner requests a **notes-only GitHub backup after each ten game-related user messages**. Ask ahead of checkpoint (around ninth message); if the user is away or doesn't respond, the user's standing permission allows saving the notes at the tenth unless they've explicitly vetoed it. Don't imply background monitoring or real-time tracking across separate chats.
- Canonical instruction: [Project Quill BACKUP_PROTOCOL.md](https://github.com/bmcd1996/project-quill/blob/main/BACKUP_PROTOCOL.md).
- When a checkpoint concerns Lucky Buck, append updates to this ledger. Preserve full creative ideas for Scratch-Off Saga separately in the private project's CREATIVE_ARCHIVE.md. Keep changes notes-only; do not deploy new calculator features merely to back up discussions.


## v2.8.2 — Prominent persistent scratch results (November 4, 2026)
- **User feedback:** Winning/losing result was hard to find. Popped numbers were faint and seemed to vanish too soon.
- **Root cause:** Global disabled button CSS set opacity to 40%, affecting popped balloons. Win/loss result was limited to a small text message.
- **Implemented:** Bold **WIN / NO WIN / ITEM JACKPOT** panel next to ticket art on wide displays, directly below on phones; payout plus all three final numbers. Revealed balloon numbers have full opacity and high contrast, with no fade.
- Last completed result (including numbers) is persisted **per ticket**, shown after refresh or ticket switching. During a new scratch, the older result is clearly labeled as previous and never spoils the new ticket. "Clear display" hides it temporarily but does not delete saved data; resetting results removes it.
- **Tests passed:** 26 in-memory JS/localStorage behavioral checks including win, loss, jackpot, three-number visibility, new ticket, clearing, refresh, and old save support. Syntax and duplicate-ID checks passed. **Actual iPhone visual test remains needed.**
- Released source commit: `8381f56dae6b91797bed88b729d8186c2e7b4f56`. Recovery branch: `backup/pre-outcome-readability-v2-8-1-2026-11-04`. Odds and underlying ticket mechanics unchanged.


## v2.9 — iPhone-first ergonomic flow (November 4, 2026)
- **Owner approved:** Reorganize the calculator around one-handed actual use: choose ticket → configure shots → buy → scratch → see persistent result → buy another → run optional batch simulations/statistics → open advanced settings.
- **Visible layout changes:** Existing ticket menu, compact presets and active modifiers remain near top. Shot Calculator moves *before* the primary Buy Ticket button, instead of blocking prize visibility below the scratch art. Shot-effect percentage controls collapse under **Advanced shot effect rates**, while the three balloon-accuracy inputs remain accessible.
- **Scratch flow:** Buy One is directly before the ticket. Artwork and high-contrast result follow; a **Buy next ticket** button appears beneath the completed result and returns the view to the artwork when used. Existing **Show waiting ticket** and **Clear display** remain accessible below. The next-ticket button is hidden while a new card is being revealed so it does not distract or spoil the result.
- **Reporting flow:** Batch simulation has been relocated to the section **Simulation & Statistics**, before Totals and Recent Runs; its IDs and behavior are preserved.
- **Advanced editing:** Price/name, modifier editors, odds table, calculations and backup/restore are now collected in a collapsed-by-default **Advanced Ticket Settings** panel. **Edit ticket settings** and **Edit modifiers** shortcuts open it before scrolling to relevant controls.
- Existing localStorage save keys, ticket settings, purchased-but-unrevealed tickets, historical results, odds engine, prize calculations and preset behavior are retained. No destructive migration, rollback or data reset.
- **Tests:** 23 JS/in-memory-DOM functional checks passed (purchase, three-balloon results, next-ticket visibility, scrolled return, simulation, old stored-result reload, advanced shortcuts, HTML nesting and source order). Source comparison verified 11 core ticket, odds and storage functions unchanged. Script parses correctly; no duplicate IDs or missing DOM references; CSS bracket counts balance.
- **Limit:** Real iPhone interactive visual layout remains to be validated by owner screenshot after GitHub Pages deployment.
- Released source commit: `3464b7f2b2e50c748d5bc0c8c498c09824770dc1`. Restore branch: `backup/pre-mobile-flow-v2-8-2-2026-11-04`.


## Creative/layout checkpoint — next multi-ticket design (November 4, 2026; DESIGNS ONLY, NOT IMPLEMENTED)
**Owner says explicitly:** Do not change the live calculator while discussing mockups. Circled numbers on their hand-drawn notebook sketch were **planning references only**, never UI decorations or tab numbering. The next ticket design will be discussed/created later today. Do not claim these specs are coded in v2.9.

### Latest preferred full-layout concept
- The layout is **two side-by-side, independently full iPhone-screen-width columns**. Normal-size mobile experience can scroll/swipe horizontally between them. Add a **Fit Both / zoom-out** way to view the *two complete columns together, proportionally scaled*, rather than reflowing all the cards into a skinny single-column list. Exact zoom method and touch controls need to be tested on the owner's iPhone.
- **Left column, in order:** branded ticket selector/header; prominent scratch-off artwork; **Buy One Ticket directly under the artwork inside the same scratch panel**; **compact 45–55px-ish result strip** beneath (e.g., WIN $5 | 5 · 5 · 5); Shot Calculator; active/equipped modifiers.
- **Right column:** **Prize Odds Editor starts at the very top, directly to the RIGHT of the scratch-off art**, not in a collapsed Advanced drawer and **not squeezed alongside the art inside the left column**. It is one of the most important interfaces. Simulation Totals, batch simulation, Live Calculations, and Recent Simulations follow in a useful order beneath. Treat these boxes as full iPhone-width in ordinary zoom.
- **Save & Transfer** spans both columns at the bottom in the fully zoomed-out desktop-like composition.
- Controls, small-result strip, sizes and positioning are evolving drafts; do not over-design or lock visual styles without feedback. An image mockup incorrectly placed editor beside ticket **within the left column**; owner wanted it **in the right column**.
- The older v2.9 page order (shots before Buy; odds editor in Advanced) is NOT the new approved visual direction. This is a future redesign proposal; preserve working v2.9 until authorized to implement.
- The header should use the **exact existing colorful outlined “Lucky Buck” logo from the scratch-ticket face**, not plain text, a generic different font or AI-recreated approximation.

### Important NEW rule: switching ticket switches ALL ticket-specific identity AND mechanics
- Selecting another ticket in the very prominent first-screen **Your Tickets** dropdown must load **that specific ticket's artwork/graphics and logo on the FRONT of the scratch-off**, not merely rename a shared static Lucky Buck image. The top page/header branding should also reflect the chosen ticket's own branding rather than stay stuck on Lucky Buck.
- The same selection must switch ticket name, price, unique prize amounts, prize odds/denominators, Jackpot item configuration, pack size, modifiers and rates, shot settings where applicable, calculations, purchased-but-unrevealed ticket state, completed result, statistics and history. Changing ticket A must never alter ticket B's figures, images, or history.
- For new ticket designs with no artwork yet, show a clearly labeled temporary placeholder until the owner supplies/approves its unique ticket art/logo; NEVER silently reuse Lucky Buck art as though it belongs to the new ticket. Art/branding must be associated with ticket IDs and persist after reloading or importing.
- Art references and ticket settings should be stored safely without excessive browser localStorage usage (asset strategy not decided). Switching must restore independent state on each ticket and not leak one ticket's graphics/odds into another.
- This is **approved functional intent for upcoming multi-ticket design**, not implementation authorization. Do not generate the next ticket design without owner direction.

### Idea-backup checkpoint
- Saved this current discussion to GitHub pursuant to the standing every-ten-game-messages notes-only protocol. No app code, styles, calculations or live page were changed. The most recent user emphasis is **ticket-specific front logo and complete per-ticket math/settings switching**.


## Foundational purpose — Lucky Buck is the game-ticket laboratory (November 4, 2026; DESIGN RULE)
**Owner clarification, high priority:** "The whole point of this program is to test test the tickets and get them perfect or at least as close as we can to working good so that we can add them directly to our game from there."

- **PRIMARY MISSION:** Lucky Buck is NOT a standalone novelty calculator. It is the authoritative **ticket-design, probability-testing and economic-balancing workbench** for scratch-off ticket types intended to ship in **Scratch-Off Saga**. Playtest, refine and approve tickets here so those finalized specs can be incorporated into the Godot game with minimal rework.
- Every ticket should become a self-contained, independently versioned **ticket definition**: stable ticket ID; display name; its **own front-logo and visual artwork references**; price; prize kinds/amounts; exact probabilities and denominator; any pack/item-jackpot rules; compatible shot/balloon mechanics and effect rates; modifier settings/rates; optional ticket-specific presentation/animation/audio information; and provenance/approval status.
- **Game production path:** design ticket and artwork → repeatedly simulate and examine RTP/EV, prize-frequency and economic impact → refine with owner → lock a reviewed ticket-definition version → export the specification and art references → import through Godot/GDScript adapter → parity tests confirm identical meaningful payout odds and rules → release ticket in appropriate game shop/district.
- **Separate TICKET SPECIFICATION from TEST RESULTS:** simulation totals, recent test history, saved custom test presets, and testing-only UI values should not accidentally change production payouts in the game. Do not rely on fragile browser localStorage copies as the only source of a finalized ticket.
- Plan a durable **versioned JSON (or similar agreed shared data schema) export**, and an explicit Godot importer/validator; preserve all numbers without rounding drift. Mark approved vs experimental tickets. Graphics must follow the selected ticket; never show the Lucky Buck deer art on another ticket by mistake.
- **Critical parity test:** the simulator's Javascript logic and Godot's GDScript code must produce statistically/analytically equivalent behavior for prize allocation, jackpot packs, modifier bonuses, balloon changes and payout computation. If an engine differs, resolve before shipping; don't merely copy a summary of percentages.
- "Directly to our game" is the intended streamlined workflow, **not a claim that export-to-Godot already works**. The current website is v2.9 and production/export conversion has NOT yet been implemented or approved for a code change.
- **HOLD:** User has explicitly requested continuing visual drafts and NO live-code changes while the two-iPhone-column layout and per-ticket art selection are discussed.


## November 5, 2026 — Shot-mechanic checkpoint (NOTES ONLY)
- Permanent discussion record: [Shot 1 and Shot 3 new rules](https://github.com/bmcd1996/lucky-buck/blob/main/design/shot-mechanics-discussion-2026-11-05.md).
- Confirmed: if shot 1 bullseye effect triggers on **0,5,25**, it atomically changes **both** first and second numbers to **1,1,25**. One trigger, not two separate odds rolls; a successful bullseye must not spread a zero and harm the result. A triggered second shot can produce **1,1,1**.
- Under discussion: each shot gets an independently adjustable effect chance. Triple-bullseye third shot potentially upgrades an existing winner exactly one tier at a default **10%** adjustable chance; no higher than $25. Whether zero can be rescued by shot 3 and how the zero exception generalizes are unresolved.
- **Owner explicitly requested no final decision or live change to third shot yet.** Preserve as design notes; do not deploy code on this checkpoint. Prior stored history and project files must remain intact.


## November 5, 2026 — Owner restated shot mechanics from scratch (NOTES ONLY)
- New source of truth: [Owner's shot-mechanics spec](https://github.com/bmcd1996/lucky-buck/blob/main/design/shot-mechanics-owner-spec-2026-11-05.md). It supersedes the earlier Nov 5 shot discussion where they conflict.
- Confirmed: separate default-5% dropdowns per shot; bullseyes never spread a zero (0 → 1 and the next balloon → 1, one roll) on shots 1 and 2; shot 3 upgrades all three numbers one prize level only if all three shots were bullseyes.
- Open questions and next steps are listed in that file. The live calculator is v3.0 (not v2.7 as noted above). No code changed.
- **Update, 12:38 Central:** spec now also covers accuracy zones (bullseye range, scaled partial hits, no-bonus zone), stacking only on successful rolls, shot 3 upgrade to an editable Grand Prize (default $50, stacks with Double Down), and a complete-miss penalty that turns the missed balloon to 0. **Standing rule: never change the calculator code without the owner's explicit permission.**

## v3.1 shot rules — PREVIEW ONLY (November 5, 2026, 17:33 Central)
- Owner approved building the Nov 5 shot spec as a preview. Page: `shots-preview.html` → https://bmcd1996.github.io/lucky-buck/shots-preview.html. **Live `index.html` (v3.0) unchanged.**
- Implemented: per-shot bonus dropdowns with green boosted chances; stacking only on successful rolls; zero rule; scaled partial hits; bullseye range and no-bonus range; shot 3 upgrade to an editable Grand Prize (default $50, Double Down can make it $100); missed-shot penalty turning a balloon to 0 (red in the readout); shotgun sound on each successful bonus roll; exact modeled odds and batch simulations follow the new rules. Upgraded numbers stay hidden until the last balloon pops. All new settings live in the existing collapsed "Shot bonus settings" panel; layout and sizes otherwise unchanged.
- Preview saves under its own keys (`quill-lucky-buck-shots-preview`, `lucky-buck-shots-preview-presets`), seeded once from the live save, so testing never touches live data.
- Tests: 36 rule/odds checks (all owner examples, zero rule, partial hits, ranges, penalty stacking, Grand Prize, exact model vs 1.5M-ticket simulations in four scenarios incl. Double Down 3) and 16 phone-size play-through checks (carry-over of saved history, dropdowns, no-spoiler upgrade reveal, penalty display, batch, refresh, live data untouched, no page errors). Owner's real-iPhone check still needed.

## v3.1 shot rules — LIVE (November 5, 2026, 17:44 Central)
- Owner tested the preview on iPhone ("I love it") and explicitly approved making it live.
- `index.html` is now v3.1: identical to `shots-preview.html` except it uses the real save keys (`quill-lucky-buck-v2`, `lucky-buck-setting-presets-v1`) and the badge reads v3.1.
- Owner confirmed the partial-after-bullseye stacking rule (e.g. 3.75% + 5% boost = 8.75%).
- **Rollback point:** branch `backup/pre-shot-rules-v3-0-2026-11-05` (live v3.0 at commit 32a5a65).
- Tests before release: 36/36 rule and odds checks on the live build; 9/9 upgrade checks on top of v3.0 saved data (stats, history, an unscratched ticket, shot settings and presets all carried over; old waiting ticket and new tickets play; no page errors).
- `shots-preview.html` remains as a sandbox with its own saved data.

## Planned: v3.2.0 and the next update (November 5, 2026, 21:59 Central) — NOTES ONLY
- Owner-approved list saved in [update plan](https://github.com/bmcd1996/lucky-buck/blob/main/design/update-plan-v3.2-and-next-2026-11-05.md): items 1–7 for v3.2.0 (logo fix, settings gear, one dropdown per shot + Enable stacking, batch readout, random accuracy, one buy button with result labels, special item setting) and items 8–11 for the following update.
- Nothing built yet; waiting for the owner's go-ahead. Live is v3.1.1.

## v3.2.0 — PREVIEW ONLY (November 5, 2026, 22:03 Central go-ahead)
- Page: `v3-2-preview.html` → https://bmcd1996.github.io/lucky-buck/v3-2-preview.html. **Live `index.html` (v3.1.1) unchanged.** Own saves (`quill-lucky-buck-v3-2-preview`, `lucky-buck-v3-2-preview-presets`), copied once from the live save.
- Built items 1–7 from the [update plan](https://github.com/bmcd1996/lucky-buck/blob/main/design/update-plan-v3.2-and-next-2026-11-05.md): logo fix (waits for decoded art, retries, falls back to the name); settings gear pops up Ticket setup in a box in front of everything, closed with a small red X in the top-right (owner request, 22:28); "Edit ticket settings" link opens it too; one bonus dropdown per shot + Enable stacking (off by default; on = a successful roll adds its chance to the next shot, shown as +x%=x%); batch readout (chances / times each shot changed a number / red miss zeros, saved per ticket); Random accuracy checkbox + Random/Good/Medium/Poor; one buy button (Buy 1 ticket $X → numbers while popping → WINNER!/JACKPOT!/SUPER JACKPOT!/!SPECIAL JACKPOT!/LOSER; cha-ching on each purchase; Clear button, Last revealed box and Buy-next button removed; back to Buy 1 ticket only after Clear totals); Special item setting (Trusty Shotgun, 1 in 600, Pack or Random chance; Pack = exactly X per Y shuffled).
- Saved shot bonuses carry over; the old green boost boxes are dropped and stacking starts off.
- Tests: 40/40 rule/label/special-item/random-accuracy/odds checks (incl. exact model vs 1M-ticket simulations in four scenarios) and 34/34 phone play-through checks (carry-over, gear, special item, stacking math, buy states, batch readout, random accuracy restores your dropdowns, refresh, Clear totals, live data untouched, no page errors). Owner's iPhone check still needed.
