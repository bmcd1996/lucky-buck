# Claude Code project instructions — Lucky Buck

## Version numbering (approved November 5, 2026)

Use three-part version numbers for the Lucky Buck calculator: **major.minor.patch** (for example, `v3.1.1`).

- **Patch (third number):** For tiny updates such as label/text changes, small cosmetic adjustments, minor UI fixes, or other narrowly scoped corrections, increase **only** the final number. Examples: `v3.1.1` → `v3.1.2` → `v3.1.3`. Do not call these `v3.2` or `v4.0`.
- **Minor (middle number):** Reserve for substantial new features or meaningful changes to the simulator, when the owner agrees the update is large enough. Example: `v3.1.x` → `v3.2.0`.
- **Major (first number):** Reserve for major overhauls, when explicitly agreed with the owner. Example: `v3.x.x` → `v4.0.0`.

For app releases, update the **visible version badge** so that it matches the release version. Always determine the current version before incrementing it. Keep tiny fixes narrowly scoped; do not alter shot odds, ticket mechanics, calculations, artwork, or unrelated UI for a text-only patch. Do not change the app's visible version solely because this instruction document changes.

**Current baseline:** `v3.1.1` — the three main accuracy control labels were renamed from “Balloon 1/2/3” to “Shot 1/2/3”, with no mechanic changes.

These are the owner's versioning rules for future Lucky Buck updates.
