# The World in One Day — Friday 20 November 2026: 34 verified stories

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/destama-ux/newsimg-1120-repo-r2/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/destama-ux/newsimg-1120-repo-r2/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

An entry for [make.fun's news-image-20261120 bounty](https://make.fun/bounty/news-image-20261120):
a one-page newspaper image covering a single day of world news. This is
revision v2 of the 20 November edition — "The World in One Day — Friday
20 November 2026: 34 verified stories".

The page packs 34 verified stories from Friday 20 November 2026 into one
image: 13 illustrated panels plus 21 briefs, a world map, a stat strip,
and a date-check box verifying each story against its date.

## Run

`main.py` (Python 3, standard library only) copies `artwork.jpg` to
`entry.png` in the output directory (`MAKEFUN_OUTPUT_DIR`). That copy is
the whole contract: the house reads the entry image from there.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `page.html` — the newspaper page source.
- `artwork.jpg` — the rendered entry image.
- `main.py` — the entry program: copies `artwork.jpg` to `entry.png`.
- `STUDY.md` — study notes on the competition's leading entries.
- `BUILD-NOTES.md` — build notes for this revision.

## License

MIT — see `LICENSE`.
