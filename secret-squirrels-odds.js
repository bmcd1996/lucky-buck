// Secret Squirrels ($2) — rules, odds and the ticket dealer.
// Owner-approved gameplay and Quill's odds handoff of 2026-11-24
// (project-quill: lucky-buck-notes/docs/ticket-recipes/secret-squirrels-gameplay-and-odds-2026-11-24.md).
// Plain data + one dealer function, shared by the ticket page and the offline simulation,
// so the Godot game can copy it exactly. Used in the browser as window.SS_ODDS, in Node via require().
(function (root) {
  'use strict';

  const RULES = {
    price: 2,
    // The 10 symbols, in the order of secret-squirrels-symbols.png.
    symbols: ['acorn', 'binoculars', 'oak-leaf', 'pinecone', 'sack-of-nuts', 'walkie-talkie', 'slingshot', 'walnut', 'squirrel-tail', 'tnt'],
    // Bonus sack values, in the order of secret-squirrels-sacks.png: empty, a few nuts, half full, overflowing.
    sackValues: [0, 1, 5, 10],
    matchPays: 1,          // every right-hand symbol that matches its own row's winning symbol pays $1
    // Whole-ticket prize table (% of tickets). Sums to 100 together with the jackpot.
    prizeTable: [
      [0, 25], [1, 24], [2, 26], [3, 2], [4, 2], [5, 1.5], [6, 1], [7, 0.75], [8, 0.5], [9, 0.25],
      [10, 2.5], [11, 2], [12, 1], [13, 0.01], [14, 0.01], [15, 4], [16, 2], [17, 1], [18, 0.01], [19, 0.01],
      [20, 2.55], [21, 1], [22, 0.01], [23, 0.01], [24, 0.01], [25, 0.75], [26, 0.01], [27, 0.01], [28, 0.01],
    ],
    // SUPER JACKPOT: all 9 matches AND both sacks overflowing ($10 + $10) pays $200 for the whole ticket (not $29, not $229).
    jackpot: { percent: 0.1, pays: 200 },
    // Share of each $1–$9 prize paid by the board alone (both sacks empty). 25/58 keeps
    // "two empty sacks" at exactly 50% of tickets: 25% $0 tickets + 25% board-only $1–$9 wins.
    // The rest of each $1–$9 prize, and every prize of $10+, is spread evenly over the ways the sacks can take part.
    boardOnlyShare: 25 / 58,
  };

  // Every bonus total two sacks can make, and the ordered sack pairs that make it.
  const SACK_PAIRS = {};
  for (const a of RULES.sackValues) for (const b of RULES.sackValues) (SACK_PAIRS[a + b] = SACK_PAIRS[a + b] || []).push([a, b]);
  const BONUS_TOTALS = Object.keys(SACK_PAIRS).map(Number).sort((x, y) => x - y);

  // Ways to pay a prize: [bonus total, number of board matches]. Never the jackpot pattern (9 matches + $20).
  function paths(total) {
    const out = [];
    for (const b of BONUS_TOTALS) { const m = total - b; if (m >= 0 && m <= 9 && !(m === 9 && b === 20)) out.push([b, m]); }
    return out;
  }

  const pick = (rand, list) => list[Math.floor(rand() * list.length)];

  // Deal one ticket. rand() must return a uniform number in [0, 1). The whole ticket is decided here, at purchase;
  // scratching only reveals it. Outcome first (weighted like a real print run), then a board and sacks that pay exactly it.
  function deal(rand) {
    let total = null, jackpot = false, r = rand() * 100;
    if ((r -= RULES.jackpot.percent) < 0) jackpot = true;
    else for (const [t, p] of RULES.prizeTable) { if ((r -= p) < 0) { total = t; break; } }
    if (!jackpot && total === null) total = RULES.prizeTable[RULES.prizeTable.length - 1][0];   // float round-off guard

    let bonus, matches;
    if (jackpot) { bonus = 20; matches = 9; }
    else if (total === 0) { bonus = 0; matches = 0; }
    else {
      const all = paths(total), withSacks = all.filter(([b]) => b > 0);
      const boardOnly = all.find(([b]) => b === 0);
      const choice = boardOnly && (withSacks.length === 0 || rand() < RULES.boardOnlyShare) ? boardOnly : pick(rand, withSacks);
      [bonus, matches] = choice;
    }
    const sacks = jackpot ? [10, 10] : pick(rand, SACK_PAIRS[bonus]).slice();

    // Board: a winning symbol per row; `matches` of the 9 right-hand spots copy their row's symbol, the rest never do.
    const S = RULES.symbols, winning = [0, 1, 2].map(() => pick(rand, S));
    const slots = [0, 1, 2, 3, 4, 5, 6, 7, 8];
    for (let i = slots.length - 1; i > 0; i--) { const j = Math.floor(rand() * (i + 1)); [slots[i], slots[j]] = [slots[j], slots[i]]; }
    const hit = new Set(slots.slice(0, matches));
    const yours = [0, 1, 2].map((row) => [0, 1, 2].map((col) => {
      const w = winning[row];
      return hit.has(row * 3 + col) ? w : pick(rand, S.filter((s) => s !== w));
    }));
    const ticket = { winning, yours, sacks, matches, bonus, jackpot, total: jackpot ? RULES.jackpot.pays : total };
    return ticket;
  }

  // Prize worked out again from what is printed on the ticket (independent check of deal()).
  function payoutOf(t) {
    let m = 0;
    t.yours.forEach((row, r) => row.forEach((s) => { if (s === t.winning[r]) m++; }));
    const bonus = t.sacks[0] + t.sacks[1];
    if (m === 9 && t.sacks[0] === 10 && t.sacks[1] === 10) return RULES.jackpot.pays;
    return m * RULES.matchPays + bonus;
  }

  const api = { RULES, deal, payoutOf, paths, SACK_PAIRS };
  if (typeof module === 'object' && module.exports) module.exports = api; else root.SS_ODDS = api;
})(typeof window !== 'undefined' ? window : this);
