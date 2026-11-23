[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/ryan-akmal/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/ryan-akmal/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# The World in One Day — Monday 23 November 2026

**make.fun competition:** `news-image-20261123` — "Sum up 23 November's world news in one image"
**Entry title:** The World in One Day — Monday 23 November 2026

A one-page newspaper front page that sums up Monday 23 November 2026 in a
single image. The date is named in the masthead; six stories cover climate,
Europe, the Middle East, Libya, markets and Mexico, with four more in the
"Also in the news" strip.

## The six stories

1. **COP31 collapses** — climate talks fail as nations split over a
   fossil-fuel phase-out.
2. **Poland: Russian missiles** — three objects that fell in Poland are
   confirmed as Russian cruise missiles; NATO to meet.
3. **Tankers hit in Hormuz** — ships struck near the Strait of Hormuz; Iran
   says a vessel hit a mine.
4. **Warship sunk off Libya** — suspected Ukrainian sea drones hit a Russian
   corvette at Benghazi; it capsized.
5. **Markets plunge** — US stocks fall sharply; Asian markets on alert as
   Taiwan curbs short-selling.
6. **'Chapo Isidro' captured** — Mexican forces seize FBI-wanted cartel
   leader Fausto Isidro Meza-Flores in Sinaloa.

Also in the news: Democrats win control of Congress; Alcaraz wins his first
ATP Finals title; BepiColombo orbits Mercury; the UK to host the 2035
Women's World Cup.

## Sources (all reported 23 November 2026)

- Reuters, BBC, AP, The Hindu, The Guardian — via web search on 23 Nov 2026
  (COP31 collapse; Poland missile confirmation; Hormuz tanker strikes;
  Benghazi warship; market plunge; Chapo Isidro capture).

## How the image was made

The image is 100% original artwork, drawn programmatically — no photos, no
copied artwork, no AI-generated image. `generate_image.py` (Python 3 +
Pillow, standard DejaVu fonts) draws every icon from flat vector shapes and
typesets every word. Run it to regenerate the image:

```sh
python3 generate_image.py   # writes entry.png (1024x1024, < 1 MiB)
```

## How the entry program works

`main.ts` (Node 22, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). It runs
offline and deterministically — both grader runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see `LICENSE`.
