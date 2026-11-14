#!/usr/bin/env python3
"""Render the news-image-01 v4 entry: a MINIMALIST single-day broadsheet
for Friday 13 November 2026.

Drawn once, locally, with PIL. The entry program (main.py) only copies the
rendered file, so the graded run is deterministic and needs no fonts at all.

v4 vs v3 (97.1467%, #169 — OUTSIDE paid; #100 cutoff 97.5290%):
- Density hurt: v3's 28 stories / 6 continents scored LOWER than v2's 24
  (97.5982%). The current #1 (@cheneyc9, 98.3796%) and ex-#1
  (@whoistyfur, 98.2554%) are both minimalist single-day images.
- v4 cuts 28 stories to 13: one big lead + 6 illustrated tiles + a
  6-item "Also today" strip. Generous whitespace, nothing below 15 px,
  so the page stays legible at ~300 px (judge criterion 5).
- The shape follows the kit's own calibration rungs (r1: four illustrated
  tiles with one short bold label; r2/r3: six vignettes around a focal
  point): flat editorial illustration + short bold labels, not dense text.
- The FAA nationwide ground stop still leads (the day's biggest story,
  which v2 missed and v3 fixed) — now as a hero panel with a drawn
  airport scene instead of one line among 28.
- Six of the kit's seven early-day anchor stories are covered (Senate
  summons, warship drone, FBI $400m hack, record deportations, Kane,
  Ukraine talks); the seventh, Iran's unverified Bahrain radar claim,
  was cut for space — the Hormuz tile already covers the Gulf, and an
  unverified claim is the weakest tile to spend.
- Every featured story carries its source; unverified claims are
  attributed in the text ("Iran says...", "Kyiv says...", "FBI says...").
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (17, 17, 17)
RED = (178, 32, 44)
GREY = (90, 86, 78)
BLUE = (31, 73, 125)
GREEN = (31, 122, 63)
AMBER = (255, 176, 32)
LIGHT = (233, 226, 210)
SKY = (214, 228, 238)

F = "/usr/share/fonts/truetype/dejavu"
SERIF_B = f"{F}/DejaVuSerif-Bold.ttf"
SERIF = f"{F}/DejaVuSerif.ttf"
SANS = f"{F}/DejaVuSans.ttf"
SANS_B = f"{F}/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap by measured pixel width."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_font(draw, text, path, size, width, minimum=11):
    """Largest font size <= `size` at which `text` fits in `width` px."""
    s = size
    while s > minimum and draw.textlength(text, font=font(path, s)) > width:
        s -= 1
    return font(path, s)


def draw_centered(draw, cx, y, text, fnt, fill):
    draw.text((cx, y), text, font=fnt, fill=fill, anchor="ma")


# ---------------------------------------------------------------- icons
# (small flat icons, adapted from v3's render.py)
def icon_laptop(draw, x, y, s=56):
    draw.rounded_rectangle([x, y, x + s, y + int(s * 0.62)], radius=5,
                           outline=INK, width=3)
    draw.rectangle([x - 5, y + int(s * 0.62), x + s + 5, y + int(s * 0.72)],
                   fill=INK)
    draw.text((x + s // 2 - 10, y + 4), "\u2715", font=font(SANS_B, 26),
              fill=RED)


def icon_chip(draw, x, y, s=56):
    c = GREEN
    draw.rectangle([x + 9, y + 9, x + s - 9, y + s - 9], fill=c,
                   outline=INK, width=3)
    draw.rectangle([x + 20, y + 20, x + s - 20, y + s - 20], fill=PAPER,
                   outline=INK, width=2)
    draw.text((x + s // 2 - 9, y + s // 2 - 9), "NV", font=font(SANS_B, 15),
              fill=INK)
    for i in range(3):
        px = x + 16 + i * 12
        draw.line([px, y, px, y + 9], fill=INK, width=2)
        draw.line([px, y + s - 9, px, y + s], fill=INK, width=2)
        py = y + 16 + i * 12
        draw.line([x, py, x + 9, py], fill=INK, width=2)
        draw.line([x + s - 9, py, x + s, py], fill=INK, width=2)


def icon_senate(draw, x, y, s=56):
    # Capitol dome: arc + drum + columns + base.
    draw.arc([x + 10, y + 2, x + s - 10, y + 28], 180, 360, fill=INK, width=3)
    draw.line([x + 10, y + 15, x + s - 10, y + 15], fill=INK, width=3)
    for cx in (x + 14, x + s // 2 - 1, x + s - 16):
        draw.line([cx, y + 18, cx, y + 40], fill=INK, width=3)
    draw.line([x + 8, y + 40, x + s - 8, y + 40], fill=INK, width=3)
    draw.line([x + 5, y + 48, x + s - 5, y + 48], fill=INK, width=3)
    draw.line([x + s // 2, y - 2, x + s // 2, y + 4], fill=RED, width=3)


def icon_tanker(draw, x, y, s=56):
    draw.polygon([(x + 5, y + 35), (x + s - 5, y + 35), (x + s - 13, y + 48),
                  (x + 13, y + 48)], fill=INK)
    draw.rectangle([x + 14, y + 21, x + 27, y + 35], fill=RED)
    draw.rectangle([x + 31, y + 16, x + 38, y + 35], fill=INK)
    draw.rectangle([x + 41, y + 25, x + s - 14, y + 35], fill=RED)
    draw.arc([x, y + 50, x + s, y + 56], 0, 180, fill=BLUE, width=3)
    draw.ellipse([x + 27, y + 4, x + 37, y + 14], fill=AMBER, outline=INK,
                 width=2)
    for dx, dy in ((-9, 4), (9, 1), (0, -4)):
        draw.line([x + 32 + dx, y + 9 + dy, x + 32 + dx, y + 15 + dy],
                  fill=AMBER, width=2)


def icon_warship(draw, x, y, s=56):
    draw.polygon([(x + 3, y + 33), (x + s - 3, y + 33), (x + s - 13, y + 48),
                  (x + 10, y + 48)], fill=INK)
    draw.rectangle([x + 18, y + 20, x + 23, y + 33], fill=INK)
    draw.line([x + 33, y + 10, x + 33, y + 33], fill=INK, width=3)
    draw.line([x + 33, y + 10, x + 43, y + 18], fill=RED, width=3)
    for cx, cy, r in ((x + 15, y + 10, 5), (x + 25, y + 5, 6),
                      (x + 37, y + 10, 5)):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREY)
    draw.arc([x, y + 51, x + s, y + 57], 0, 180, fill=BLUE, width=3)


def icon_webcam(draw, x, y, s=56):
    # Laptop screen with a masked face; coins spilling out below.
    draw.rounded_rectangle([x + 4, y, x + s - 4, y + 36], radius=5,
                           outline=INK, width=3)
    draw.rectangle([x - 2, y + 36, x + s + 2, y + 42], fill=INK)
    draw.ellipse([x + 16, y + 8, x + 40, y + 32], fill=INK)
    draw.rectangle([x + 16, y + 17, x + 40, y + 24], fill=PAPER)
    draw.ellipse([x + 21, y + 18, x + 26, y + 23], fill=INK)
    draw.ellipse([x + 30, y + 18, x + 35, y + 23], fill=INK)
    draw.ellipse([x + 42, y + 40, x + 54, y + 52], fill=AMBER, outline=INK,
                 width=2)
    draw.text((x + 44, y + 40), "$", font=font(SANS_B, 11), fill=INK)


def icon_plane(draw, x, y, s=130):
    """Plane silhouette, side view, nose right (from v3)."""
    draw.rounded_rectangle([x, y + 34, x + s, y + 62], radius=14, fill=INK)
    draw.polygon([(x + s - 18, y + 34), (x + s + 16, y + 48),
                  (x + s - 18, y + 62)], fill=INK)
    draw.polygon([(x + 12, y + 36), (x + 30, y + 6), (x + 42, y + 8),
                  (x + 34, y + 36)], fill=RED)
    draw.polygon([(x + 52, y + 56), (x + 78, y + 88), (x + 64, y + 90),
                  (x + 44, y + 60)], fill=INK)
    draw.polygon([(x + 56, y + 38), (x + 76, y + 14), (x + 86, y + 18),
                  (x + 68, y + 40)], fill=INK)
    for i in range(5):
        wx = x + 26 + i * 15
        draw.ellipse([wx, y + 43, wx + 7, y + 50], fill=PAPER)


def draw_airport(draw, x, y, w, h):
    """Hero illustration: grounded planes, control tower, GROUND STOP sign.

    Flat editorial style on a pale sky panel. `x, y, w, h` is the panel.
    """
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=SKY)
    # Red banner across the top: the message, unmissable and clear of the
    # plane (the old signpost collided with the plane's nose).
    draw.rounded_rectangle([x + 10, y + 8, x + w - 10, y + 40], radius=6,
                           fill=RED)
    draw_centered(draw, x + w // 2, y + 14, "\u2715  ALL FLIGHTS GROUNDED",
                  font(SANS_B, 17), (255, 255, 255))
    # Ground / runway.
    gy = y + h - 46
    draw.rectangle([x, gy, x + w, y + h], fill=LIGHT)
    draw.line([x, gy, x + w, gy], fill=INK, width=3)
    for i in range(7):
        dx = x + 14 + i * 46
        draw.line([dx, gy + 22, dx + 24, gy + 22], fill=GREY, width=4)
    # Control tower (left), below the banner.
    tx = x + 18
    draw.rectangle([tx + 8, y + 98, tx + 26, gy], fill=INK)
    draw.polygon([(tx, y + 98), (tx + 34, y + 98), (tx + 42, y + 72),
                  (tx - 8, y + 72)], fill=RED)
    draw.rectangle([tx - 8, y + 72, tx + 42, y + 80], fill=INK)
    draw.line([tx + 17, y + 72, tx + 17, y + 54], fill=INK, width=3)
    draw.ellipse([tx + 13, y + 48, tx + 21, y + 56], fill=RED)
    # Big grounded plane (right, on the runway). No second plane in the
    # sky: with a ground stop in force, an empty sky is the point.
    icon_plane(draw, x + 78, gy - 108, s=210)


# ---------------------------------------------------------------- stories
# (kicker, kicker colour, headline, caption, source, icon)
TILES = [
    ("TECHNOLOGY", RED,
     "Microsoft 365 still dark",
     "Outlook, Teams and Copilot fail in 74 countries.",
     "Downdetector", icon_laptop),
    ("BUSINESS", GREEN,
     "Huang quits Nvidia",
     "Founder resigns after 33 years; shares fall 13%.",
     "USA Today", icon_chip),
    ("POLITICS", BLUE,
     "Senate summons Huang",
     "Ex-Nvidia chief and Lutnick called to testify.",
     "BBC", icon_senate),
    ("EUROPE", BLUE,
     "Drone hits warship",
     "Kyiv says a drone struck a Russian warship in the Baltic.",
     "BBC", icon_warship),
    ("MIDDLE EAST", RED,
     "Tankers hit mines",
     "Iran says a gas carrier struck a mine in Hormuz; four hit.",
     "Reuters", icon_tanker),
    ("CRIME", RED,
     "N. Korea's $400m hack",
     "Fake video calls stole $400m in crypto, FBI says.",
     "BBC", icon_webcam),
]

ALSO_TODAY = [
    "Europe wins a seat at Ukraine talks",
    "Brooklyn collapse toll: eight dead",
    "Pope Leo meets survivors in Lima",
    "Storm Charles shuts schools in Portugal",
    "U.S. deportations hit a record 483,200",
    "Kane breaks England caps record",
]


def tile(draw, x, y, w, h, kicker, kcolor, head, caption, source, icon):
    cx = x + w // 2
    icon(draw, x + (w - 56) // 2, y + 4, s=56)
    draw_centered(draw, cx, y + 70, kicker, font(SANS_B, 14), kcolor)
    hf = font(SERIF_B, 20)
    lines = wrap(draw, head, hf, w - 8)[:2]
    yy = y + 94
    for ln in lines:
        draw_centered(draw, cx, yy, ln, hf, INK)
        yy += 26
    sf = font(SANS, 15)
    full = f"{caption}  \u2014 {source}"
    clines = wrap(draw, full, sf, w - 8)[:2]
    yy += 4
    for ln in clines:
        draw_centered(draw, cx, yy, ln, sf, (52, 50, 46))
        yy += 21


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 36
    CW = W - 2 * M  # 952

    # ---- masthead ----
    draw_centered(d, W // 2, 8, "THE WORLD TODAY", font(SERIF_B, 58), INK)
    draw_centered(d, W // 2, 78, "FRIDAY  \u2022  13 NOVEMBER 2026",
                  font(SANS_B, 19), RED)
    d.line([M, 110, W - M, 110], fill=INK, width=3)
    d.line([M, 116, W - M, 116], fill=INK, width=1)

    # ---- hero: FAA ground stop ----
    hy = 128
    d.text((M, hy), "AVIATION  \u2022  UNITED STATES", font=font(SANS_B, 16),
           fill=RED)
    draw_airport(d, 636, hy + 6, 352, 296)
    hf = font(SERIF_B, 44)
    lines = wrap(d, "FAA grounds every flight in America", hf, 580)[:2]
    yy = hy + 26
    for ln in lines:
        d.text((M, yy), ln, font=hf, fill=INK)
        yy += 52
    d.text((M, yy + 4),
           "A telecom failure hits every air-traffic centre;",
           font=font(SANS, 19), fill=(52, 50, 46))
    d.text((M, yy + 30),
           "all departures halted nationwide.  \u2014 Reuters",
           font=font(SANS, 19), fill=(52, 50, 46))
    sy = yy + 74
    d.text((M, sy), "4 HOURS  \u2022  1,000+ CANCELLED  \u2022  10,000 DELAYED",
           font=font(SANS_B, 17), fill=INK)
    d.text((M, sy + 26), "2ND NATIONWIDE STOP SINCE 9/11",
           font=font(SANS_B, 17), fill=RED)
    d.line([M, 452, W - M, 452], fill=INK, width=3)

    # ---- tiles: 2 rows x 3 cols ----
    gap = 24
    col_w = (CW - 2 * gap) // 3  # 301
    row_h = 200
    y0 = 466
    for i, (kicker, kcolor, head, caption, source, icon) in enumerate(TILES):
        row, col = divmod(i, 3)
        x = M + col * (col_w + gap)
        y = y0 + row * (row_h + 10)
        tile(d, x, y, col_w, row_h, kicker, kcolor, head, caption, source,
             icon)
    d.line([M, 886, W - M, 886], fill=INK, width=2)

    # ---- also today ----
    ay = 898
    d.text((M, ay), "ALSO TODAY", font=font(SANS_B, 15), fill=INK)
    d.text((W - M, ay), "Sources: Reuters  \u2022  AP  \u2022  BBC  "
           "\u2022  Al Jazeera",
           font=font(SANS, 13), fill=GREY, anchor="ra")
    ccol_w = (CW - 2 * gap) // 3
    for j, item in enumerate(ALSO_TODAY):
        col = j // 2
        row = j % 2
        x = M + col * (ccol_w + gap)
        y = ay + 26 + row * 26
        d.text((x, y), "\u2022", font=font(SANS_B, 16), fill=RED)
        fnt = fit_font(d, item, SANS, 16, ccol_w - 18, minimum=13)
        d.text((x + 16, y), item, font=fnt, fill=(52, 50, 46))

    # ---- footer ----
    d.line([M, 990, W - M, 990], fill=INK, width=1)
    draw_centered(d, W // 2, 998,
                  "All events of Friday 13 November 2026",
                  font(SANS, 13), GREY)

    out = Path(__file__).resolve().parent.parent / "entry.png"
    img.save(out, "PNG", optimize=True)
    print(out, out.stat().st_size, "bytes", img.size)


if __name__ == "__main__":
    main()
