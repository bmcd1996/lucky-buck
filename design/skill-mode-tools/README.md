# Skill mode build tools

These files built Lucky Buck v3.4.0 from the v3.3.3 calculator and the ticket at commit `6fce0c9`:

- `shared.js`: saved-settings format shared by the calculator and the ticket (key `lucky-buck-skill-v1`), the balloon pixel mask, and the default rings.
- `calc_skill.js` / `calc_skill.css`: calculator additions (Skill switch, big ticket, play sliders, zone painter, Buck's Secret box).
- `build.py`: patches the base files.

Usage: `python build.py <out-dir> <ticket-url> <calc-url> <version>`. Example: `python build.py live ticket-1.0.0.html index.html v3.4.0`.

**Run it only against the pre-3.4.0 files** (for example, `git show 6fce0c9:index.html`). The live files already contain these changes, so running it against them would apply the changes twice. For future edits, change the live files directly or rebase these tools first.
