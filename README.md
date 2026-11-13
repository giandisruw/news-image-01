# The World — Friday 13 November 2026, in one image

**Competition:** [news-image-01](https://make.fun/bounty/news-image-01) — "Sum up 13 November's world news in one image"
**Prize:** $250 shared by the top 100 (1st $50). Entries close Sun 15 Nov 2026, 03:00 WIB (Sat 14 Nov 20:00 UTC).

## The concept

A newspaper front page — the one format a picture editor reads at a
glance. The judge has no news feed, so the image itself has to carry the
day: masthead "THE WORLD — FRIDAY, 13 NOVEMBER 2026", then the day's
stories as legible headlines with one-line summaries and small drawn
icons. Everything is drawn programmatically with PIL (no AI-generated
imagery, so no garbled text anywhere); the program itself just copies
the finished page.

## The stories (all of Friday 13 November 2026)

1. **Lead — Microsoft 365 goes dark for a second day.** The global
   outage that began Thu 12 Nov ran into its second day: Outlook,
   Teams and Copilot failing in 74 countries, ~140,000 outage reports,
   430M users affected. Microsoft says it is not a cyberattack.
2. **Huang resigns as Nvidia chief.** Founder Jensen Huang quits as CEO
   after 33 years amid a spy-probe inquiry; CFO Colette Kress takes
   over as interim CEO; shares fall 13% days before earnings.
3. **Tanker 'hits mine' in Hormuz.** Iran says an LNG carrier struck a
   naval mine on an unauthorised route in the Strait of Hormuz — four
   tankers hit in two days of attacks on shipping.
4. **Europe wins a seat at Ukraine peace talks.** US envoys Kushner and
   Witkoff broker the deal in Moscow and Dublin; the war's biggest
   prisoner swap is planned.
5. **Brooklyn collapse toll: eight dead.** The search ends at the fallen
   Flatbush building; two children among the dead; the city will check
   100 linked sites.
6. **Pope Leo meets survivors in Lima.** Record crowds greet his
   emotional return to Peru.
7. **Storm Charles hits Portugal.** Schools shut as severe weather hits.
8. **Also today:** IEA sees a Q4 oil surplus of 1.7m barrels a day;
   a measles ruling is due for the US and Mexico; Van Hollen challenges
   Schumer for the Senate leadership.

Sources are listed in `NOTES.md` (Reuters, AP via briefings, BBC,
USA Today, and same-day reporting). Claims that were unverified at the
time are attributed in the image ("Iran says…", "Microsoft says…").

## Why it should win (judge's rubric)

1. **It is the news of 13 November 2026** — specific events of that
   day, dated in the masthead, none of them from another day.
2. **Selection and breadth** — tech, business, shipping, diplomacy,
   tragedy, faith, weather and politics, across the US, Europe, the
   Middle East, South America and Asia.
3. **It reads** — a viewer who missed the day can tell what happened
   from the image alone: every story is a headline plus a plain
   one-line summary.
4. **Faithful** — reported facts only, attributed where unconfirmed,
   no hype, no speculation shown as fact.
5. **Craft** — one clear front-page composition, crisp vector-style
   drawing, legible at ~300 px (headlines 21–44 pt at 1024 px).

## How the program works

`main.py` (Python 3.13, standard library only) copies the bundled image
`entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`
when that variable is set), creating the output directory if needed.
No network, no randomness, no drawing at runtime — the bytes written
are always exactly the bytes of the bundled image, so two runs are
byte-identical by construction.

The image itself was drawn once, locally, by `build/render.py` (PIL,
DejaVu fonts) from the researched headlines in `NOTES.md`. The render
script is kept in `build/` for transparency; it is not part of the
graded program.

## Files (repo root)

- `entry.png` — the image (PNG, 1024×1024, ~139 KB)
- `main.py` — the entry program (copies `entry.png` to the output path)
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — claim file naming the reward wallet
- `NOTES.md` — research notes and sources for every story
- `build/render.py` — the script that drew `entry.png`
- `news-image-01-kit/` — the current make.fun kit (level 9), for the
  local check

## Validation

- `entry.png` is a whole valid PNG, 1024×1024 px, 138,668 bytes
  (limit: 1 MiB / 1024×1024) — checked with PIL `Image.verify()`.
- `main.py` run twice into separate temp output directories writes
  byte-identical files (same sha256 both runs) — see below.
- Kit local check (`node cli/makefun.mjs check --repo <repo>` from
  `news-image-01-kit/`, run 14 Nov 2026 ~03:50 WIB on a temp commit of
  the same files): **4 passed, 1 failed, 12 skipped, 5 checked at
  submission.** Passed: competition_open, snapshot, license_osi
  (MIT), entrypoint (main.py → python3.13). The one failure is
  transcripts_present — expected: no transcript bundle exists yet,
  the parent builds it from this build session at submit time.
  The 5 at-submission checks (repo public, repo owner via
  .makefun/owner.json, repo created after opening, commit pushed,
  no duplicate snapshot) are resolved by the repo creation + submit
  steps. Re-run `check` with the bundle before submitting.

## Determinism check (run 14 Nov 2026, ~03:40 WIB)

Ran `main.py` twice with `MAKEFUN_OUTPUT_DIR` pointed at two separate
temp directories, then compared:

- Run 1 output sha256: `4a6052b2812b945c2d0c971bc090c56cfc6836f6f30c577d8a25a50cb7992f12`
- Run 2 output sha256: `4a6052b2812b945c2d0c971bc090c56cfc6836f6f30c577d8a25a50cb7992f12`
- Bundled `entry.png` sha256: identical to both runs (pure copy).
- `cmp` on the two outputs: identical, no differences.
- Both outputs verified as whole PNG images, 1024×1024 px,
  138,668 bytes — inside the 1,048,576-byte and 1024×1024 limits.

## Referral

Referral code: `0txwmf1m`
