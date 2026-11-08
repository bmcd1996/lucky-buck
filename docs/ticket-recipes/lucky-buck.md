# Ticket recipe: Lucky Buck ($1)

A one-page "recipe" that pins down everything that makes Lucky Buck what it is, so a future rebuild (for example in Godot for Scratch-Off Saga) can match it exactly.
**Status:** matches the live site as of v3.4.0 (November 8, 2026). Update this file whenever an owner-approved change goes live.

## Identity
- Name: Lucky Buck. Price: $1. Studio: Quill Productions.
- Art: the original Lucky Buck artwork, **untouched** (owner decision): deer hunter, antler logo, sunset lake, and a "MATCH 3 AMOUNTS TO WIN!" footer. Native size 680×1017.
- Front: a top-right flip badge (mirror of the $1 badge with a pixel arrow) flips the ticket.
- Back: the same base image plus a cream rules panel:
  - "$1 MATCH 3 AMOUNTS TO WIN!"
  - 1 SHOOT / 2 REVEAL / 3 WIN
  - **Buck's Secret** in red handwriting: "Word around the woods is hittin' a perfect bullseye can earn ya an extra buck or two..."
- Fonts: Lilita One for headings, Roboto Condensed Bold for rules, Annie Use Your Telescope for the secret, Press Start 2P for prize numbers.

## Balloons and aiming
- Three pixel-art balloons (red, blue, yellow; option D): round, glossy upper-left shine, black marker X.
  - Grid: 37×45 cells at 4 px. The centre cell (18,22) is the exact hit point.
  - The centre pixel is the balloon's own colour.
- Balloon width is 22.8% of the ticket × the balloon size setting (default 100%, range 70–130%).
- Balloons drift on gentle loops. Defaults: speed 1.6×, distance 100%.
- Crosshair: red "Hunter" pixel crosshair, 17 cells. Its cell size always equals the balloon cell size (it scales with balloon size).
  - It appears while the finger is held and floats 130 px above the finger.
  - It traces an infinity sign, then a figure 8, at 20 px pattern size, 2.4 s per shape.
  - Releasing fires.
- Pop: the balloon disappears completely, and its number bounces in with eight pixel stars.
  - Number colours: $25 gold, $5 green, $1 blue, $0 red.

## Modes (set by the calculator's Skill switch)
### Skill OFF (Luck / odds mode)
- Outcome is dealt from the calculator's lucky-buck prize odds plus its Luck level.
  - Default odds: lose 75%, $1 17%, $5 6.5%, $25 1.5%.
- A win needs three matching amounts. A losing deal never shows three of a kind.
- Unlimited misses.

### Skill ON
- One target grid for all three balloons, painted in the calculator.
  - Default: gold = the dead-centre pixel only, green to 6.5 px, yellow to 11.5 px, red elsewhere on the balloon.
  - Values: gold $25, green $5, yellow $1, red $0.
- A shot's number is the colour of the pixel under the crosshair's centre. Off the balloon = miss.
- **Prize = your worst shot** (5, 5, 1 pays $1; any $0 = no prize).
- **5 shells per ticket** (adjustable). Every shot uses one. Balloons left when you run out count as $0.
- The grid is **never visible to the player**.

## Buck's Secret
- The gold squares of the grid are Buck's Secret.
- Skill ON: a gold hit shows the gold prize ($25), with "BUCK'S SECRET!".
- Skill OFF: each gold hit pays +$1 on top of the ticket (even a loser), up to +$2 per ticket. Both amounts are adjustable.

## Not part of the ticket yet
- Rescue Bonus, Hot Streak, Double Down and special items (Trusty Shotgun) exist in the calculator only.
- Sounds are simple placeholders. Pixel sounds (ChipTone/jsfxr) are planned.

## Where it lives
- Ticket: `ticket-1.0.0.html` (identical copy: `playtest.html`).
- Calculator: `index.html`.
- Saved settings in the browser:
  - `lucky-buck-skill-v1`: Skill switch, grid, values, shells, play settings, Buck's Secret.
  - `quill-lucky-buck-v2`: calculator tickets and odds.
- Art scripts: `design/ticket-art-tools/`. Skill-mode build tools: `design/skill-mode-tools/`.
