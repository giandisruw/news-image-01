#!/usr/bin/env python3
"""Render the news-image-01 v3 entry: a late-edition newspaper front page
for Friday 13 November 2026 — 28 stories, 6 continents, numbered world map.

Drawn once, locally, with PIL. The entry program (main.py) only copies the
rendered file, so the graded run is deterministic and needs no fonts at all.

v3 vs v2 (97.5982%, peaked #43, slipped to #61):
- LEAD is the FAA nationwide ground stop (the day's biggest story; v2
  missed it — it happened after v2's research). Top entries all lead it.
- 28 stories (was 24), 6 continents, incl. the kit's own early-day
  stories (Senate summons, Baltic warship, Bahrain radar, deportations).
- A labelled world-map strip with 10 story dots.
- A source on every featured story + a sources line over the compact list.
- "LATE EDITION" masthead flag.
"""
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (17, 17, 17)
RED = (178, 32, 44)
GREY = (90, 86, 78)
BLUE = (31, 73, 125)
GREEN = (31, 122, 63)
LIGHT = (233, 226, 210)
MAPSEA = (232, 238, 242)
MAPLAND = (168, 196, 214)

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


def draw_text_fit(draw, xy, text, path, size, width, fill, minimum=11):
    fnt = fit_font(draw, text, path, size, width, minimum)
    draw.text(xy, text, font=fnt, fill=fill)
    return fnt


# ---------------------------------------------------------------- icons
def icon_laptop(draw, x, y, s=44):
    draw.rounded_rectangle([x, y, x + s, y + int(s * 0.62)], radius=4,
                           outline=INK, width=3)
    draw.rectangle([x - 4, y + int(s * 0.62), x + s + 4, y + int(s * 0.72)],
                   fill=INK)
    draw.text((x + s // 2 - 8, y + 3), "✕", font=font(SANS_B, 21), fill=RED)


def icon_chip(draw, x, y, s=44):
    c = GREEN
    draw.rectangle([x + 7, y + 7, x + s - 7, y + s - 7], fill=c,
                   outline=INK, width=2)
    draw.rectangle([x + 16, y + 16, x + s - 16, y + s - 16], fill=PAPER,
                   outline=INK, width=2)
    draw.text((x + s // 2 - 7, y + s // 2 - 7), "NV", font=font(SANS_B, 12),
              fill=INK)
    for i in range(3):
        px = x + 13 + i * 9
        draw.line([px, y, px, y + 7], fill=INK, width=2)
        draw.line([px, y + s - 7, px, y + s], fill=INK, width=2)
        py = y + 13 + i * 9
        draw.line([x, py, x + 7, py], fill=INK, width=2)
        draw.line([x + s - 7, py, x + s, py], fill=INK, width=2)


def icon_senate(draw, x, y, s=44):
    # Capitol dome: arc + drum + columns + base.
    draw.arc([x + 8, y + 2, x + s - 8, y + 22], 180, 360, fill=INK, width=3)
    draw.line([x + 8, y + 12, x + s - 8, y + 12], fill=INK, width=3)
    for cx in (x + 11, x + s // 2 - 1, x + s - 13):
        draw.line([cx, y + 14, cx, y + 32], fill=INK, width=3)
    draw.line([x + 6, y + 32, x + s - 6, y + 32], fill=INK, width=3)
    draw.line([x + 4, y + 38, x + s - 4, y + 38], fill=INK, width=3)
    draw.line([x + s // 2, y - 2, x + s // 2, y + 3], fill=RED, width=3)


def icon_tanker(draw, x, y, s=44):
    draw.polygon([(x + 4, y + 28), (x + s - 4, y + 28), (x + s - 10, y + 38),
                  (x + 10, y + 38)], fill=INK)
    draw.rectangle([x + 11, y + 17, x + 21, y + 28], fill=RED)
    draw.rectangle([x + 24, y + 13, x + 30, y + 28], fill=INK)
    draw.rectangle([x + 32, y + 20, x + s - 11, y + 28], fill=RED)
    for wy in (41,):
        draw.arc([x, y + wy - 3, x + s, y + wy + 3], 0, 180, fill=BLUE,
                 width=2)
    draw.ellipse([x + 22, y + 4, x + 30, y + 12], fill=(255, 176, 32))
    for dx, dy in ((-7, 3), (7, 1), (0, -3)):
        draw.line([x + 26 + dx, y + 8 + dy, x + 26 + dx, y + 13 + dy],
                  fill=(255, 176, 32), width=2)


def icon_radar(draw, x, y, s=44):
    draw.arc([x + 4, y + 10, x + s - 4, y + 40], 180, 360, fill=INK, width=3)
    draw.line([x + 4, y + 25, x + s - 4, y + 25], fill=INK, width=3)
    draw.line([x + s // 2, y + 10, x + s // 2, y + 25], fill=INK, width=2)
    draw.line([x + s // 2, y + 10, x + s - 8, y + 16], fill=RED, width=3)
    draw.ellipse([x + s - 11, y + 13, x + s - 5, y + 19], fill=RED)
    draw.line([x + 10, y + 38, x + s - 10, y + 38], fill=INK, width=3)
    draw.line([x + 14, y + 42, x + s - 14, y + 42], fill=INK, width=2)


def icon_talks(draw, x, y, s=44):
    draw.rounded_rectangle([x + 3, y + 8, x + 28, y + 25], radius=5,
                           outline=BLUE, width=3)
    draw.polygon([(x + 9, y + 25), (x + 15, y + 25), (x + 9, y + 32)],
                 fill=BLUE)
    draw.rounded_rectangle([x + 19, y + 18, x + s - 2, y + 35], radius=5,
                           outline=INK, width=3)
    draw.polygon([(x + s - 12, y + 35), (x + s - 18, y + 35),
                  (x + s - 12, y + 42)], fill=INK)
    for yy in (14, 20):
        draw.line([x + 9, y + yy, x + 22, y + yy], fill=BLUE, width=2)
    for yy in (24, 30):
        draw.line([x + 25, y + yy, x + s - 8, y + yy], fill=INK, width=2)


def icon_warship(draw, x, y, s=44):
    draw.polygon([(x + 2, y + 26), (x + s - 2, y + 26), (x + s - 10, y + 38),
                  (x + 8, y + 38)], fill=INK)
    draw.rectangle([x + 14, y + 16, x + 18, y + 26], fill=INK)
    draw.line([x + 26, y + 8, x + 26, y + 26], fill=INK, width=3)
    draw.line([x + 26, y + 8, x + 34, y + 14], fill=RED, width=3)
    for cx, cy, r in ((x + 12, y + 8, 4), (x + 20, y + 4, 5),
                      (x + 29, y + 8, 4)):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREY)
    draw.arc([x, y + 40, x + s, y + 44], 0, 180, fill=BLUE, width=2)


def icon_building(draw, x, y, s=44):
    draw.rectangle([x + 8, y + 5, x + s - 8, y + 40], outline=INK, width=3)
    draw.line([x + 17, y + 5, x + 23, y + 17, x + 19, y + 26, x + 26, y + 40],
              fill=RED, width=3)
    for r in range(3):
        for c in range(3):
            wx = x + 13 + c * 10
            wy = y + 10 + r * 10
            if (r, c) != (1, 1):
                draw.rectangle([wx, wy, wx + 5, wy + 5], fill=INK)


def icon_crypto(draw, x, y, s=44):
    draw.ellipse([x + 4, y + 4, x + s - 4, y + s - 4], outline=INK, width=3)
    draw.text((x + s // 2 - 7, y + 10), "$", font=font(SANS_B, 22),
              fill=GREEN)
    draw.ellipse([x + s - 14, y + s - 14, x + s - 4, y + s - 4],
                 fill=(255, 176, 32), outline=INK, width=2)
    draw.text((x + s - 12, y + s - 14), "$", font=font(SANS_B, 9), fill=INK)


def icon_deport(draw, x, y, s=44):
    # Small plane + down arrow.
    draw.polygon([(x + 6, y + 16), (x + 38, y + 16), (x + 30, y + 22),
                  (x + 12, y + 22)], fill=INK)
    draw.polygon([(x + 20, y + 8), (x + 26, y + 8), (x + 24, y + 16),
                  (x + 21, y + 16)], fill=INK)
    draw.polygon([(x + 30, y + 18), (x + 40, y + 22), (x + 30, y + 24)],
                 fill=RED)
    draw.line([x + s // 2, y + 28, x + s // 2, y + 40], fill=RED, width=3)
    draw.polygon([(x + s // 2 - 5, y + 35), (x + s // 2 + 5, y + 35),
                  (x + s // 2, y + 42)], fill=RED)


def icon_plane(draw, x, y, s=130):
    """Large plane silhouette for the lead story (side view, nose right)."""
    # Fuselage
    draw.rounded_rectangle([x, y + 34, x + s, y + 62], radius=14, fill=INK)
    draw.polygon([(x + s - 18, y + 34), (x + s + 16, y + 48),
                  (x + s - 18, y + 62)], fill=INK)
    # Tail fin
    draw.polygon([(x + 12, y + 36), (x + 30, y + 6), (x + 42, y + 8),
                  (x + 34, y + 36)], fill=RED)
    # Wings
    draw.polygon([(x + 52, y + 56), (x + 78, y + 88), (x + 64, y + 90),
                  (x + 44, y + 60)], fill=INK)
    draw.polygon([(x + 56, y + 38), (x + 76, y + 14), (x + 86, y + 18),
                  (x + 68, y + 40)], fill=INK)
    # Windows
    for i in range(5):
        wx = x + 26 + i * 15
        draw.ellipse([wx, y + 43, wx + 7, y + 50], fill=PAPER)

# ---------------------------------------------------------------- world map
# Rough equirectangular continent outlines (lon, lat). Stylised on purpose:
# flat blobs, no coast detail — readable as a world map at a glance.
NORTH_AMERICA = [(-168, 66), (-145, 70), (-125, 71), (-110, 68), (-95, 69),
                 (-85, 66), (-80, 73), (-65, 60), (-55, 52), (-60, 46),
                 (-70, 42), (-75, 36), (-81, 26), (-84, 30), (-90, 21),
                 (-97, 16), (-94, 17), (-104, 23), (-110, 24), (-114, 29),
                 (-120, 34), (-124, 42), (-124, 48), (-135, 58),
                 (-155, 58), (-165, 60)]
SOUTH_AMERICA = [(-79, 9), (-72, 11), (-62, 9), (-52, 5), (-50, 0),
                 (-44, -3), (-35, -8), (-38, -15), (-41, -23), (-48, -28),
                 (-57, -35), (-65, -41), (-68, -50), (-70, -54), (-73, -44),
                 (-73, -33), (-71, -20), (-77, -12), (-81, -5), (-80, 1)]
AFRICA = [(-17, 15), (-16, 21), (-10, 31), (-6, 35), (0, 36), (10, 37),
          (20, 32), (30, 31), (34, 28), (37, 22), (39, 18), (43, 12),
          (51, 11), (48, 2), (41, -4), (40, -15), (36, -22), (32, -29),
          (28, -33), (20, -35), (17, -29), (13, -18), (12, -6), (9, 4),
          (4, 6), (-8, 5), (-13, 8)]
EUROPE = [(-10, 36), (-9, 38), (-9, 43), (-2, 44), (-1, 46), (3, 43),
          (7, 44), (10, 44), (12, 42), (16, 40), (19, 42), (23, 40),
          (26, 38), (28, 41), (30, 36), (27, 37), (23, 36), (19, 45),
          (14, 45), (8, 44), (3, 42), (-2, 48), (-5, 48), (-1, 50),
          (2, 51), (5, 53), (8, 55), (10, 57), (12, 55), (18, 56),
          (21, 55), (24, 58), (28, 60), (30, 62), (32, 66), (30, 69),
          (25, 71), (18, 70), (14, 67), (12, 64), (8, 63), (5, 59),
          (5, 58), (-2, 57), (-6, 55), (-10, 54), (-10, 51), (-6, 49)]
ASIA = [(30, 36), (33, 36), (36, 36), (40, 38), (44, 39), (48, 38),
        (50, 37), (54, 37), (57, 38), (60, 38), (62, 40), (65, 42),
        (68, 44), (70, 46), (72, 48), (75, 50), (78, 52), (80, 55),
        (83, 58), (85, 60), (88, 62), (90, 65), (92, 68), (95, 70),
        (98, 70), (100, 69), (105, 70), (110, 70), (115, 70), (120, 70),
        (125, 70), (130, 70), (135, 70), (140, 70), (145, 70), (150, 70),
        (155, 70), (160, 68), (162, 65), (165, 62), (168, 60), (170, 60),
        (170, 62), (165, 66), (160, 66), (158, 62), (155, 59), (150, 60),
        (145, 58), (142, 55), (140, 52), (138, 48), (135, 44), (132, 42),
        (130, 38), (127, 35), (126, 33), (122, 32), (120, 28), (118, 25),
        (115, 22), (112, 20), (110, 18), (108, 15), (105, 10), (103, 8),
        (100, 6), (98, 10), (96, 15), (94, 17), (92, 20), (90, 22),
        (88, 22), (86, 20), (84, 18), (82, 16), (80, 14), (78, 10),
        (76, 10), (74, 14), (72, 18), (70, 20), (68, 22), (66, 25),
        (64, 25), (62, 25), (60, 25), (58, 26), (56, 27), (54, 28),
        (52, 29), (50, 30), (48, 30), (46, 30), (44, 29), (42, 28),
        (40, 30), (38, 32), (36, 36)]
AUSTRALIA = [(113, -22), (114, -28), (115, -33), (118, -35), (124, -33),
             (129, -32), (132, -32), (135, -35), (138, -35), (140, -38),
             (145, -38), (150, -37), (153, -32), (153, -27), (150, -22),
             (146, -19), (142, -11), (140, -17), (136, -12), (132, -12),
             (130, -13), (126, -14), (122, -17), (118, -20)]
CONTINENTS = [NORTH_AMERICA, SOUTH_AMERICA, AFRICA, EUROPE, ASIA, AUSTRALIA]

# (lon, lat, label, label dx, label dy) — dx/dy in px from the dot.
MAP_DOTS = [
    (-77, 39, "WASHINGTON", 10, -6),
    (-126, 49, "SEATTLE", -58, -6),
    (-118, 35, "SILICON VALLEY", 10, 8),
    (57.5, 25, "HORMUZ", 10, 8),
    (50, 27.5, "BAHRAIN", -24, -18),
    (30.5, 50.5, "KYIV", 10, -6),
    (23, 59.5, "BALTIC SEA", -66, -14),
    (-77, -12, "LIMA", -40, -6),
    (-9, 38.7, "LISBON", 10, -6),
    (34.5, 31.5, "GAZA", 10, 8),
]

MAP_X0, MAP_X1 = 152, 872      # lon -170 .. 190 at 2.0 px/deg
MAP_Y0, MAP_Y1 = 266, 400      # lat 70 .. -55
LAT_TOP, LAT_BOT = 70, -55


def map_xy(lon, lat):
    x = MAP_X0 + (lon + 170) * (MAP_X1 - MAP_X0) / 360.0
    y = MAP_Y0 + (LAT_TOP - lat) * (MAP_Y1 - MAP_Y0) / (LAT_TOP - LAT_BOT)
    return x, y


def draw_map(draw):
    for poly in CONTINENTS:
        pts = [map_xy(lon, lat) for lon, lat in poly]
        draw.polygon(pts, fill=MAPLAND)
    lf = font(SANS_B, 11)
    for lon, lat, label, dx, dy in MAP_DOTS:
        x, y = map_xy(lon, lat)
        draw.ellipse([x - 7, y - 7, x + 7, y + 7], fill=RED,
                     outline=(255, 255, 255), width=2)
        draw.text((x + dx, y + dy), label, font=lf, fill=INK)


# ---------------------------------------------------------------- stories
# (kicker, kicker colour, headline, summary, source, icon)
FEATURED = [
    ("TECHNOLOGY  •  GLOBAL OUTAGE", RED,
     "Microsoft 365 dark for a second day",
     "Outlook, Teams and Copilot fail in 74 countries.",
     "Downdetector", icon_laptop),
    ("BUSINESS  •  CHIPS", GREEN,
     "Huang resigns as Nvidia chief",
     "Founder quits after 33 years; Kress takes over, shares fall 13%.",
     "USA Today", icon_chip),
    ("POLITICS  •  UNITED STATES", BLUE,
     "Senate summons Huang and Lutnick",
     "Huang and Lutnick called to testify on chips and China.",
     "BBC", icon_senate),
    ("MIDDLE EAST  •  SHIPPING", RED,
     "Tankers \u2018hit mines\u2019 in Hormuz",
     "Iran says a gas carrier hit a mine; four tankers hit in two days.",
     "Reuters", icon_tanker),
    ("MIDDLE EAST  •  GULF", RED,
     "Iran claims radar strike in Bahrain",
     "Tehran claims it struck a U.S. radar site; no confirmation.",
     "Al Jazeera", icon_radar),
    ("EUROPE  •  WAR & DIPLOMACY", BLUE,
     "Europe wins a seat at Ukraine talks",
     "Kushner and Witkoff broker the deal; Europe joins the next round.",
     "AP", icon_talks),
    ("EUROPE  •  BALTIC SEA", BLUE,
     "Drone hits Russian warship",
     "Kyiv says a drone struck a Russian warship in the Baltic Sea.",
     "BBC", icon_warship),
    ("UNITED STATES  •  TRAGEDY", RED,
     "Brooklyn collapse toll: eight dead",
     "Search ends; eight dead, two of them children. DA opens inquiry.",
     "AP", icon_building),
    ("UNITED STATES  •  CRIME", RED,
     "N. Korea crypto crackdown: $1.2bn seized",
     "DOJ wins a $1.2bn seizure order; FBI shuts a $400m video scam.",
     "DOJ", icon_crypto),
    ("UNITED STATES  •  IMMIGRATION", BLUE,
     "U.S. deportations hit a record 483,200",
     "A record 483,200 deportations in 2026, the most ever recorded.",
     "Al Jazeera", icon_deport),
]

COMPACT = [
    "Pope Leo meets survivors in Lima",
    "Storm Charles shuts schools in Portugal",
    "Kane breaks England caps record",
    "Salah breaks Egypt scoring record",
    "Pochettino named Man Utd manager",
    "COP31: UN chief urges deep emissions cuts",
    "UN extends Abyei peacekeeping mandate",
    "Mekelle falls to Ethiopian forces",
    "T\u00fcrkiye, Qatar sign defence pact",
    "Pakistan raids kill 74 militants",
    "Houthis claim Riyadh airport strike",
    "Gaza hospital strike kills six",
    "Nairobi building collapse kills six",
    "Kaziranga bus crash kills at least 24",
    "7,400 reach Canary Islands in 10 days",
    "NZ suspends visa processing in outage",
    "IEA sees Q4 oil surplus of 1.7m b/d",
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 32  # margin
    CW = W - 2 * M  # 960

    # ---- masthead ----
    d.text((W // 2, 4), "THE WORLD TODAY", font=font(SERIF_B, 64), fill=INK,
           anchor="ma")
    d.text((W // 2, 76),
           "FRIDAY  \u2022  13 NOVEMBER 2026  \u2022  LATE EDITION  \u2022  "
           "28 STORIES  \u2022  6 CONTINENTS",
           font=font(SANS_B, 19), fill=RED, anchor="ma")
    d.line([M, 102, W - M, 102], fill=INK, width=4)
    d.line([M, 108, W - M, 108], fill=INK, width=1)

    # ---- lead: FAA ground stop ----
    ly = 118
    d.text((M, ly), "AVIATION  \u2022  UNITED STATES", font=font(SANS_B, 17),
           fill=RED)
    icon_plane(d, W - M - 150, ly + 4, s=130)
    d.text((M, ly + 26), "FAA grounds every flight in America",
           font=font(SERIF_B, 38), fill=INK)
    lead_sum = ("A telecom failure hits every air-traffic centre; all "
                "departures halted nationwide.")
    lsf = fit_font(d, lead_sum + "  \u2014 Reuters", SANS, 17, 790,
                   minimum=15)
    d.text((M, ly + 76), lead_sum, font=lsf, fill=(52, 50, 46))
    d.text((M + d.textlength(lead_sum, font=lsf), ly + 76),
           "  \u2014 Reuters", font=lsf, fill=GREY)
    d.text((M, ly + 102),
           "4 HOURS  \u2022  1,000+ CANCELLED  \u2022  10,000 DELAYED"
           "  \u2022  2ND STOP SINCE 9/11",
           font=font(SANS_B, 16), fill=INK)
    d.line([M, 240, W - M, 240], fill=INK, width=3)

    # ---- map strip ----
    d.text((M, 248), "THE DAY ON THE MAP", font=font(SANS_B, 14), fill=INK)
    d.text((W - M, 248), "10 places where the day happened",
           font=font(SANS, 14), fill=GREY, anchor="ra")
    d.rectangle([M, 264, W - M, 404], fill=MAPSEA)
    draw_map(d)
    d.line([M, 412, W - M, 412], fill=INK, width=2)

    # ---- featured grid: 10 stories, 2 cols x 5 rows ----
    col_w = (CW - 24) // 2  # 468
    row_h = 76
    y0 = 420
    for i, (kicker, kcolor, head, summ, source, icon) in enumerate(FEATURED):
        row, col = divmod(i, 2)
        x = M + col * (col_w + 24)
        y = y0 + row * row_h
        text_w = col_w - 56
        d.text((x, y), kicker, font=font(SANS_B, 15), fill=kcolor)
        draw_text_fit(d, (x, y + 19), head, SERIF_B, 21, text_w, INK)
        # summary + source tag, auto-fit together
        full = f"{summ}  \u2014 {source}"
        sf = fit_font(d, full, SANS, 14, text_w, minimum=12)
        d.text((x, y + 47), summ, font=sf, fill=(52, 50, 46))
        sw = d.textlength(summ, font=sf)
        d.text((x + sw, y + 47), f"  \u2014 {source}", font=sf, fill=GREY)
        icon(d, x + col_w - 46, y + 6, s=44)
    d.line([M, y0 + 5 * row_h + 6, W - M, y0 + 5 * row_h + 6], fill=INK,
           width=2)

    # ---- compact list: 17 more stories, 3 cols ----
    cy = y0 + 5 * row_h + 16  # 812
    d.text((M, cy), "ALSO TODAY  \u2014  17 MORE STORIES",
           font=font(SANS_B, 15), fill=INK)
    d.text((W - M, cy), "Sources: Reuters  \u2022  AP  \u2022  BBC  "
           "\u2022  Al Jazeera",
           font=font(SANS, 13), fill=GREY, anchor="ra")
    ccol_w = (CW - 48) // 3  # 304
    iy = cy + 26
    for j, item in enumerate(COMPACT):
        col = j // 6
        row = j % 6
        x = M + col * (ccol_w + 24)
        y = iy + row * 24
        d.text((x, y), "\u2022", font=font(SANS_B, 14), fill=RED)
        draw_text_fit(d, (x + 14, y), item, SANS, 14, ccol_w - 14,
                      (52, 50, 46), minimum=12)

    # ---- footer ----
    d.line([M, 992, W - M, 992], fill=INK, width=1)
    d.text((W // 2, 1000),
           "All events of Friday 13 November 2026  \u2022  Reported by "
           "Reuters, AP, BBC, Al Jazeera and USA Today",
           font=font(SANS, 13), fill=GREY, anchor="ma")

    out = Path(__file__).resolve().parent.parent / "entry.png"
    img.save(out, "PNG", optimize=True)
    print(out, out.stat().st_size, "bytes", img.size)


if __name__ == "__main__":
    main()
