# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/0xzunid/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/0xzunid/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One picture, one day of world news. This entry renders Tuesday 24 November 2026 as a single 1024×1024 newspaper front page: the masthead, a lead story, four more stories in two columns, and an "Also today" strip — all of it drawn in code with Pillow, so every headline is sharp, baked-in text instead of AI-generated lettering.

What made the page:

- **Nvidia's U-turn** — Jensen Huang is back as CEO 11 days after resigning, after President Trump called the board directly; shares jumped 31% and the Nasdaq 6%.
- **Poland** — NATO is sending an AWACS early-warning aircraft after three Russian Kh-101 cruise missiles came down on Friday.
- **The Gulf** — the US sanctioned nearly 30 Iran-linked shadow-banking houses while Secretary of State Rubio met Qatar's prime minister.
- **Ukraine** — naval drones sank a Russian corvette off Libya, and 11 bodies were recovered from a drone-hit block of flats near Kyiv.
- **Indonesia** — the Java candy-factory fire toll is confirmed at 24 dead, with about 30 workers still missing.
- **Also today** — strikes in Gaza, the COP31 collapse, Congo halting cobalt exports, and a record-equalling 9-1 Champions League night for Como.

## How to run it

```sh
python3 main.py
```

`main.py` copies `entry.png` into `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`) and checks the copy twice: its SHA-256 must match the pinned digest of the bundled image, and its PNG header must say 1024×1024. The front page itself is produced by `news-image-gen-20261124.py`, which lives outside this repo — it draws the page with Pillow and DejaVu fonts and nothing else, no network, no randomness.

Verified on 2026-11-24: `entry.png` is 182,170 bytes with sha256 `f41552452cea0afaf7da913a8eca2565224f8eaec0ceb44a2a451280a6fbb4ec`. `main.py` was written fresh on 2026-11-24 and run twice with `python3 -P -s` — exit 0 both times, byte-identical output, dimensions confirmed 1024×1024.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1q7g6m7h&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
