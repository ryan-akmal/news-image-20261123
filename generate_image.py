#!/usr/bin/env python3
"""Draw the 23 November 2026 world-news front page (1024x1024 PNG).

Original artwork: every icon is drawn from flat vector shapes with Pillow,
every word is typeset with DejaVu. No photo, no copied artwork, no network.
Run:  python3 generate_image.py   (writes entry.png next to this file)
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (20, 28, 44)
NAVY = (20, 33, 61)
GOLD = (233, 196, 106)
RED = (178, 34, 34)
GREY = (90, 90, 90)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading):
    lines = wrap(draw, text, fnt, max_w)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


# ---------- icons, each drawn inside a 140x140 box at (x, y) ----------
def icon_globe(d, x, y):
    cx, cy, r = x + 70, y + 70, 58
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(43, 122, 185),
              outline=NAVY, width=4)
    d.ellipse([cx - 42, cy - 30, cx - 2, cy + 2], fill=(46, 160, 90))
    d.ellipse([cx + 8, cy + 12, cx + 44, cy + 42], fill=(46, 160, 90))
    d.ellipse([cx + 18, cy - 44, cx + 48, cy - 14], fill=(46, 160, 90))
    d.line([(cx - 18, cy - 52), (cx - 2, cy - 20), (cx - 20, cy + 8),
            (cx + 4, cy + 34), (cx - 8, cy + 56)], fill=RED, width=6)


def icon_missile(d, x, y):
    d.ellipse([x + 8, y + 8, x + 132, y + 132], outline=(200, 200, 200), width=2)
    d.arc([x + 28, y + 28, x + 112, y + 112], 200, 340, fill=GREY, width=3)
    d.arc([x + 48, y + 48, x + 92, y + 92], 200, 340, fill=GREY, width=3)
    d.polygon([(x + 92, y + 22), (x + 118, y + 48), (x + 96, y + 62),
               (x + 78, y + 44)], fill=(120, 120, 120))
    d.polygon([(x + 30, y + 96), (x + 56, y + 78), (x + 70, y + 100),
               (x + 44, y + 116)], fill=(120, 120, 120))
    d.line([(x + 44, y + 96), (x + 96, y + 44)], fill=(70, 70, 70), width=16)
    d.polygon([(x + 22, y + 104), (x + 34, y + 92), (x + 44, y + 112),
               (x + 30, y + 122)], fill=(230, 126, 34))
    d.polygon([(x + 96, y + 22), (x + 110, y + 34), (x + 100, y + 46),
               (x + 88, y + 32)], fill=RED)


def icon_tanker(d, x, y):
    for i, c in enumerate([(214, 48, 49), (230, 126, 34), (43, 122, 185)]):
        d.rectangle([x + 14 + i * 38, y + 30, x + 46 + i * 38, y + 62],
                    fill=c, outline=NAVY, width=2)
    d.polygon([(x + 8, y + 64), (x + 132, y + 64), (x + 120, y + 96),
               (x + 20, y + 96)], fill=(40, 48, 64))
    d.rectangle([x + 104, y + 40, x + 128, y + 64], fill=(240, 240, 240),
                outline=NAVY, width=2)
    d.line([(x + 10, y + 106), (x + 40, y + 106), (x + 55, y + 100),
            (x + 85, y + 106), (x + 100, y + 100), (x + 130, y + 106)],
           fill=(43, 122, 185), width=4)
    cx, cy = x + 70, y + 18
    for ang in range(0, 360, 45):
        a = math.radians(ang)
        d.line([(cx, cy), (cx + 16 * math.cos(a), cy + 16 * math.sin(a))],
               fill=(230, 126, 34), width=5)


def icon_warship(d, x, y):
    d.polygon([(x + 18, y + 78), (x + 96, y + 56), (x + 122, y + 66),
               (x + 108, y + 92), (x + 30, y + 104)], fill=(90, 100, 116),
              outline=NAVY)
    d.rectangle([x + 62, y + 34, x + 72, y + 60], fill=(70, 78, 92))
    d.line([(x + 67, y + 34), (x + 67, y + 18)], fill=NAVY, width=4)
    d.ellipse([x + 62, y + 12, x + 72, y + 22], fill=RED)
    d.line([(x + 10, y + 116), (x + 40, y + 110), (x + 70, y + 116),
            (x + 100, y + 110), (x + 130, y + 116)], fill=(43, 122, 185),
           width=5)
    d.line([(x + 10, y + 128), (x + 40, y + 122), (x + 70, y + 128),
            (x + 100, y + 122), (x + 130, y + 128)], fill=(43, 122, 185),
           width=4)
    d.ellipse([x + 100, y + 14, x + 118, y + 32], fill=(60, 60, 60))
    d.line([(x + 104, y + 14), (x + 98, y + 8)], fill=(60, 60, 60), width=3)
    d.line([(x + 114, y + 14), (x + 120, y + 8)], fill=(60, 60, 60), width=3)


def icon_chart(d, x, y):
    d.line([(x + 18, y + 20), (x + 18, y + 118)], fill=INK, width=4)
    d.line([(x + 18, y + 118), (x + 126, y + 118)], fill=INK, width=4)
    pts = [(x + 24, y + 34), (x + 48, y + 52), (x + 70, y + 48),
           (x + 92, y + 82), (x + 116, y + 104)]
    d.line(pts, fill=RED, width=6, joint="curve")
    d.polygon([(x + 116, y + 104), (x + 100, y + 98), (x + 110, y + 116)],
              fill=RED)
    for p in pts:
        d.ellipse([p[0] - 4, p[1] - 4, p[0] + 4, p[1] + 4], fill=RED)


def icon_cuffs(d, x, y):
    d.ellipse([x + 16, y + 52, x + 66, y + 102], outline=NAVY, width=10)
    d.ellipse([x + 74, y + 52, x + 124, y + 102], outline=NAVY, width=10)
    d.line([(x + 58, y + 62), (x + 82, y + 62)], fill=NAVY, width=8)
    d.line([(x + 64, y + 52), (x + 76, y + 40)], fill=NAVY, width=6)
    d.ellipse([x + 66, y + 28, x + 86, y + 48], outline=NAVY, width=5)
    d.text((x + 44, y + 104), "$5m", font=font(SANS_B, 22), fill=RED)


ICONS = [icon_globe, icon_missile, icon_tanker,
         icon_warship, icon_chart, icon_cuffs]

STORIES = [
    ("CLIMATE", (42, 157, 143), "COP31 COLLAPSES",
     "Climate talks fail as nations split over a fossil-fuel phase-out."),
    ("EUROPE", (178, 34, 34), "POLAND: RUSSIAN MISSILES",
     "Three objects that fell in Poland confirmed as Russian cruise "
     "missiles; NATO to meet."),
    ("MIDDLE EAST", (214, 111, 51), "TANKERS HIT IN HORMUZ",
     "Ships struck near the Strait of Hormuz; Iran says a vessel hit a mine."),
    ("LIBYA", (29, 53, 87), "WARSHIP SUNK OFF LIBYA",
     "Suspected Ukrainian sea drones hit a Russian corvette at Benghazi; "
     "it capsized."),
    ("MARKETS", (155, 34, 38), "MARKETS PLUNGE",
     "US stocks fall sharply; Asian markets on alert as Taiwan curbs "
     "short-selling."),
    ("MEXICO", (106, 76, 147), "\u2018CHAPO ISIDRO\u2019 CAPTURED",
     "Mexican forces seize FBI-wanted cartel leader Fausto Isidro "
     "Meza-Flores in Sinaloa."),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.text((W // 2, 18), "THE WORLD IN ONE DAY", font=font(SERIF_B, 58),
           fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 92), "MONDAY  \u2022  23 NOVEMBER 2026",
           font=font(SANS_B, 34), fill=GOLD, anchor="ma")
    d.rectangle([0, 148, W, 154], fill=GOLD)

    # Standfirst
    y = text_block(d, 28, 168,
                   "Six stories that defined the day: climate talks collapse, "
                   "missiles over Poland, tankers hit in the Gulf, a warship "
                   "sunk off Libya, markets plunge \u2014 and a cartel kingpin "
                   "is captured.",
                   font(SANS, 21), INK, W - 56, 28)

    # Story grid: 2 columns x 3 rows
    gx, gy = 24, 232
    pw, ph, gap = 480, 218, 16
    for i, (tag, accent, head, cap) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x0 = gx + col * (pw + gap)
        y0 = gy + row * (ph + gap)
        d.rectangle([x0, y0, x0 + pw, y0 + ph], fill=(255, 255, 255),
                    outline=(200, 195, 185), width=2)
        d.rectangle([x0, y0, x0 + pw, y0 + 34], fill=accent)
        d.text((x0 + 14, y0 + 5), tag, font=font(SANS_B, 20),
               fill=(255, 255, 255))
        ICONS[i](d, x0 + 12, y0 + 48)
        tx = x0 + 168
        text_block(d, tx, y0 + 50, head, font(SANS_B, 27), INK, pw - 184, 33)
        text_block(d, tx, y0 + 122, cap, font(SANS, 19), (60, 60, 60),
                   pw - 184, 25)

    # Also-in-the-news strip
    by = gy + 3 * ph + 2 * gap + 14
    d.rectangle([24, by, W - 24, by + 64], fill=(232, 226, 212),
                outline=(200, 195, 185), width=2)
    text_block(d, 40, by + 8,
               "ALSO IN THE NEWS:  Democrats win control of Congress  \u2022  "
               "Alcaraz wins his first ATP Finals title  \u2022  BepiColombo "
               "orbits Mercury  \u2022  UK to host the 2035 Women\u2019s World Cup",
               font(SANS_B, 18), INK, W - 80, 24)

    # Footer
    d.text((W // 2, H - 26),
           "Sources: Reuters, BBC, AP, The Hindu, The Guardian \u2014 "
           "reported 23 November 2026",
           font=font(SANS, 15), fill=GREY, anchor="ma")

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
