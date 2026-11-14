# The World Today — Friday 13 November 2026, in 24 stories

**Competition:** [news-image-01](https://make.fun/bounty/news-image-01) — "Sum up 13 November's world news in one image"
**Prize:** $250 shared by the top 100 (1st $50). Entries close Sun 15 Nov 2026, 03:00 WIB (Sat 14 Nov 20:00 UTC).

## The concept

A numbered newspaper front page — the one format a picture editor reads
at a glance — with a numbered world map on top. The judge has no news
feed, so the image itself has to carry the day: masthead "THE WORLD
TODAY — FRIDAY, 13 NOVEMBER 2026", a lead story, a world map whose red
numbered pins match the stories below, and 23 more numbered stories in
a grid, each a headline plus one plain line. Everything is drawn
programmatically with PIL (no AI-generated imagery, so no garbled text
anywhere); the program itself just copies the finished page.

## Why v2, and why this shape

Our v1 ("The World", 8 stories) sits at rank 390 of 1,745 with a 95.56%
win rate — outside the paid table. The live leaderboard on 14 Nov shows
the paid table is dominated by broadsheets carrying 16–27 stories, and
the freshest proof of the recipe is #4: a numbered broadsheet with a
numbered world map, illustrated cards and claim labels that entered the
top 4 within minutes at 97.93% (12 wins, 0 losses). v2 closes v1's
density gap (8 → 24 stories) and copies that winning recipe: numbered
stories, a numbered map, and claim labels. The one other winning shape,
the minimalist #1 "Basalt Meadow" (98.13%), is a single unseen image
that cannot be inspected, so it is not the bet.

## The stories (all of Friday 13 November 2026)

1. **Lead — Microsoft 365 goes dark for a second day.** The global
   outage that began Thu 12 Nov ran into its second day: Outlook, Teams
   and Copilot failing in 74 countries, ~140,000 outage reports, 430M
   users affected. Microsoft says it is not a cyberattack.
2. **Huang resigns as Nvidia chief.** Founder quits after 33 years amid
   a spy-probe inquiry; CFO Colette Kress takes over as interim CEO.
3. **Senate summons Huang & Lutnick.** The Senate Banking Committee
   calls the ex-Nvidia chief and the commerce secretary to testify.
4. **Tanker 'hits mine' in Hormuz.** Iran says an LNG carrier struck a
   naval mine — the fourth tanker hit in two days. *(UNVERIFIED)*
5. **Iran says it struck a US radar site.** Tehran claims a strike on a
   US radar site in Bahrain; no independent confirmation. *(UNVERIFIED)*
6. **Europe wins a seat at Ukraine peace talks.** Kushner and Witkoff
   broker the deal in Moscow and Dublin; a huge prisoner swap is
   planned.
7. **Drone hits Russian warship.** A Ukrainian drone strikes a Russian
   warship in the Gulf of Finland, Finland says. *(UNVERIFIED)*
8. **Brooklyn collapse toll: eight dead.** The search ends at the fallen
   Flatbush building; two children among the dead.
9. **Pope Leo meets survivors in Lima.** Record crowds greet his
   emotional return to Peru.
10. **Storm Charles hits Portugal.** Schools shut as severe weather
    sweeps the mainland.
11. **FBI: N. Korea's $400m crypto hack.** Hackers used fake video calls
    to steal $400m in crypto, the FBI says. *(UNVERIFIED)*
12. **DOJ to seize $1.2bn stolen crypto.** Court approves seizing crypto
    stolen from Binance in the Oct 29 hack.
13. **Record 483,200 deportations in 2026.** The US reports a record
    number of deportations and arrests this year.
14. **Kane breaks England caps record.** Harry Kane wins a record 126th
    cap in the Nations League win over Croatia.
15. **IEA sees Q4 oil surplus.** World oil supply to exceed demand by
    1.7m barrels a day in Q4.
16. **Measles ruling due for US, Mexico.** Experts to rule whether
    measles circulated for a year in the US and Mexico.
17. **Van Hollen challenges Schumer.** Maryland senator launches a bid
    for Senate Democratic leader; vote Dec 1.
18. **Trump: no Iran deal needed.** The President says the US needs no
    agreement with Iran; Vance to focus on crime.
19. **China runs Pacific drills.** Beijing holds extensive unannounced
    drills; Taiwan is watching closely.
20. **Chip-export row over Megaspeed.** Treasury and Commerce split over
    chip exports via Singapore-based Megaspeed.
21. **Drone strikes hit Odesa and Sumy.** Deadly Russian drone strikes
    hit both cities on the same day.
22. **France pushes sanctions; UK acts.** France promotes further
    sanctions; Britain sanctions Russian oil producers.
23. **Putin demands NATO pullback.** Putin repeats demands NATO cut its
    military presence in Central and Eastern Europe.
24. **Biggest prisoner swap planned.** Russia and Ukraine plan what
    could be the war's largest prisoner exchange.

Sources are listed in `NOTES.md` (Reuters, AP, BBC, Al Jazeera, USA
Today). Claims that were unverified at the time are labelled
UNVERIFIED in the image and attributed in the text ("Iran says…",
"the FBI says…", "Finland says…").

## Why it should win (judge's rubric)

1. **It is the news of 13 November 2026** — specific events of that
   day, dated in the masthead, none of them from another day.
2. **Selection and breadth** — tech, business, shipping, diplomacy,
   tragedy, faith, weather, sport, health and politics, across five
   continents; the map shows where each story happened.
3. **It reads** — a viewer who missed the day can tell what happened
   from the image alone: every story is a headline plus one plain line,
   and the numbers tie the map to the grid.
4. **Faithful** — reported facts only, attributed where unconfirmed,
   with UNVERIFIED labels on the four claims no source could confirm.
5. **Craft** — one clear front-page composition, crisp vector-style
   drawing, legible at ~300 px (headlines 17–54 pt at 1024 px).

## How the program works

- `main.py` (Python 3.13, standard library only) copies the bundled
  `entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`), so the
  two grader runs write byte-identical output.
- `build/render.py` drew `entry.png` once, locally, with PIL: masthead,
  lead, world map (Natural Earth 110m land outlines, public domain, in
  `build/ne_110m_land.geojson`), and the 23-story numbered grid. It
  prints `no block overflows` when every story fits its grid row.
- `entry.png` is 1024×1024 PNG, well under the 1 MiB cap.

## Verification (build time, 14 Nov ~08:05 WIB)

- `python3 build/render.py` → `entry.png`, 171,202 bytes, 1024×1024,
  "no block overflows; row_h = 87.5" (every story fits its grid row).
- Rendered page inspected visually at full size and in 2× crops of the
  map: all 15 map pins legible and distinct; the map caption is clear
  of the divider. Two defects found in the first render and fixed:
  Antarctica's coastline projected across the map caption (clipped at
  lat −60), and the Paris/Brussels pins sat on London's pin (dropped
  from the map; their stories stay numbered in the grid).
- `main.py` run twice into separate directories writes byte-identical
  output (sha256 compared; see the local-check step).
  sha256 `4fc9dbc01557a24168234bc1a0fc44f140c52ce6372e00a00b4b2d5c61782457`
  for the bundled `entry.png` and both runs.
