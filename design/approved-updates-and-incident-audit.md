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
