# Build notes — news-image-20261120 v2 (revision run)
## "The World in One Day — Friday 20 November 2026"

One-page newspaper image (1024×1024 JPEG) summing up the world news of
Friday 20 November 2026. Same day, same 34 verified stories and facts as
v1, rebuilt from a fresh page after a study of the live leaderboard
(`STUDY.md`). 13 illustrated panels + 21 one-line briefs, a UTC timeline
strip, a six-stat number strip, a coloured region bar, a world map with
pins for stories 1–13, and a forensic date-check box.

## Why a v2

V1 deep check 2026-11-21 01:25 WIB: score 981,793, prize_rank #551 of
10,251; top-50 cutoff 988,486 — gap 6,693 points. Live board at study
time (~01:40 WIB): cutoff #50 is 988,608, gap ~6,800. The top 50 are
all 12 wins / 0 losses in 12 judge duels, so the gap is a picture-editor
judgement gap, not a win-count gap. The leader study (top-10 artifact
images viewed individually) found the same anatomy everywhere — the fix
is execution, not structure. Full study: `STUDY.md`.

## What changed vs v1 (and why)

- **Lead order is news order.** V1 led Akvan → COP31 → UK–EU and buried
  Kyiv as medium panel #4. Every top-10 page leads Kyiv → Akvan →
  AI sell-off. V2 reorders the 13 panels: 1 Kyiv, 2 Akvan, 3 Anthropic/AI,
  4 COP31, 5 UK–EU, 6 US shutdown, 7 Prabowo–Xi, 8 Google channels,
  9 opioid ring, 10 Kakao, 11 Deutsche Bank, 12 GTA VI, 13 cancer pill.
  Same 13 panels, same facts, new priority order. Map pins renumbered
  to match.
- **Concrete masthead subhead.** V1's subhead was vague ("A cyclone
  strikes India's east coast…"). V2 names the four top stories:
  "Russian missiles hit Kyiv's bridges · Cyclone Akvan strikes India ·
  An AI sell-off sinks Asia · Britain and the EU sign their reset deal"
  — the leaders' pattern.
- **Stat strip and region bar split into two rows.** V1 stacked region
  labels directly above the stat numbers in one merged row, so the
  numbers read as if they belonged to the regions. V2: six-stat strip
  first (70–80 km/h · 100,000 · $87.66 · 19,000 · 24.6m · $2.36bn),
  then a separate coloured region bar (Asia-Pacific 7 · Europe 15 ·
  Middle East 1 · Africa 1 · Americas 6 · Global 4 = 34).
- **Bigger, darker lead art with data inside the picture.** Lead art
  92→106px tall, medium art 42→48px; bold in-art labels with the key
  figure (KYIV — 3 BRIDGES HIT / 5 KILLED; CYCLONE AKVAN / 70–80 KM/H;
  AI SELL-OFF / $87.66 / −9.8% with a falling red chart line; COP31
  FINAL DRAFT / OVERTIME; 100,000 / YR; $350bn SOUGHT; 500,000 TABLETS /
  SEIZED · 6 HELD; $582m; 24.6m / METACRITIC 99; TUMOURS VANISHED).
  Every in-art figure is from the verified set — the leaders' per-index
  Asian closes (e.g. Taipei −6.2%) are NOT in our verified facts and
  were not reproduced.
- **Larger numbered map pins + legend.** Pins spread further apart in
  the Europe cluster; legend "Red pins mark stories 1–13. Briefs run
  14–34. Positions approximate."
- **Bolder date-check box** ("DATE CHECK ✓ FRIDAY 20 NOVEMBER 2026 …
  so NOT shown: …"), same exclusions as v1.
- **Kept from v1:** giant serif date masthead; 13 panels with source
  tags on every story; UTC timeline strip (most leaders do NOT have
  one — kept as our differentiator, now fitting on one line in full);
  21 briefs in two columns with bold city prefixes; footer sources line.

## Layout fit

First render: footer bottom at 966px (58px slack). Enlarged lead/medium
art and the map to fill the frame; final footer bottom 999px, nothing
clipped, nothing overflowing the 1024px frame — visually verified in
both the PNG render and the final JPEG. Two render passes fixed clipped
in-art labels (SVG `preserveAspectRatio` changed from slice to none so
no label is cropped; label texts shortened to fit their boxes), a
clipped timeline strip (shortened separators, 10px), the Capitol dome
overlapping "$350bn SOUGHT", and the "CHANNELS CUT" label colliding
with the play button.

## Size

Artwork is **278,104 bytes at JPEG quality 80** (1024×1024, sha256
0669fd281ec7be9cc7b9d32f73f0bc91a24b93e6a771a0b069f1e9beecaf6105) —
under the ~300 KB target, smaller than v1's 282,675 bytes, and well
inside the 1 MiB limit. Rendered from `page.html` with headless
Chromium (chrome-headless-shell, 1024×1024 viewport) → PNG → JPEG
quality 80 with Pillow.

## Story list with sources (all reporting of Fri 20 Nov 2026 — unchanged from v1)

Panels (13, v2 order):
1. Three Kyiv bridges hit in a major Russian missile attack; five killed.
   BBC.
2. Cyclone Akvan landfall near Gopalpur, Odisha — 70–80 km/h, gusting 90;
   no major damage/deaths; third cyclone in a month. IMD / Reuters.
3. Anthropic slides day two — pre-market $87.66, −9.8% vs $97.17 close;
   European shares head for worst week since March. Reuters / Finnhub.
4. COP31 final day — no final text, talks into overtime Saturday; draft
   omits fossil fuels; Panama threatened formal objection. AP.
5. UK–EU reset deal signed in Brussels — youth mobility 100,000/yr each
   way, food-trade checks scrapped, carbon markets linked from 2028;
   tuition fees unresolved. Reuters.
6. US shutdown looms as Iran war splits Congress; Trump seeks $350bn
   Pentagon funding. Reuters.
7. Prabowo meets Xi in Beijing — economy, investment, South China Sea.
   Reuters.
8. Indonesia asks Google to justify removing 19,000+ pro-government
   YouTube channels. Reuters.
9. India busts opioid ring shipping ~500,000 tablets to US buyers via
   messaging apps; six arrested. Reuters.
10. Seoul appeals court upholds Kakao founder Kim Beom-su's acquittal on
    SM Entertainment share-rigging charges. Reuters / Yonhap.
11. Deutsche Bank leaks — bank forwarded Trump's tax return by mistake;
    ~$582m Epstein-linked transactions flagged; shares down >10% on the
    week. Reuters Breakingviews.
12. GTA VI — 24.6m copies, est. $2.36bn in 24 hours (Sensor Tower);
    Metacritic 99. NME / AsiaToday.
13. Pancreatic cancer pill trial saw tumours vanish. BBC.

Briefs (14–34): 14 Iraq forces enter Kataib Hezbollah stronghold (Reuters);
15 Democrats probe Nvidia's Megaspeed sway (Reuters); 16 Europe ready for
Russia talks on ending the war (BBC); 17 White House removes cyber-security
chief (BBC); 18 consent-law calls after Young case (BBC); 19 Airbnb house
rules in force (BBC); 20 UK fridges secured from hackers (BBC);
21 stockpiling lifts retail sales after 'Be Ready' (BBC); 22 UK coldest
night of autumn, −10C (BBC); 23 Russell fastest in wet Las Vegas GP
practice (BBC); 24 UFC bans Fiorot three months (BBC); 25 Rams' Nacua
suspended for misconduct (BBC); 26 Wales face Slovenia in March play-off
(BBC); 27 Prince Harry would rejoin the army (BBC); 28 William and Kate
meet Modi as India tour ends (BBC); 29 UK to send Ukraine 1,000
long-range strike drones (BBC); 30 France unrest may cost insurers
€207m (Euronews); 31 stabbed Bradford councillor 'protecting a staff
member' (BBC); 32 rand at one-year low amid coalition talks (Reuters);
33 Musk 'pretty foolish' over midterm spending (Reuters); 34 analysis:
Shenzhen summit masks each bilateral limit (Reuters Breakingviews).

Regions: Asia-Pacific 7 · Europe 15 · Middle East 1 · Africa 1 ·
Americas 6 · Global 4 = 34.

Stat strip: 70–80 km/h (Akvan winds) · 100,000 (UK–EU youth visas/yr) ·
$87.66 (Anthropic pre-market) · 19,000 (channels removed) · 24.6m (GTA VI
copies) · $2.36bn (day-one sales estimate).

UTC timeline: 02:14 Seoul — Kakao verdict (Reuters 02:14:42 UTC);
02:30 Gopalpur — landfall begins (08:00 IST); 05:50 Gopalpur — landfall
complete (11:20 IST); 08:05 London — STOXX opens −1% (0805 GMT);
10:30 New York — ANT −4.7% pre-market (1030 GMT); 13:38 New York —
ANT $87.66 pre-market (Finnhub snapshot 13:38:20 UTC).

Date-check box names the excluded other-days' news: Anthropic's $97.17
first-day close and the ICJ Myanmar genocide verdict (both Thursday) ·
the Trump–Xi–Putin summit itself (Thursday) · GTA VI's launch (Thursday) ·
Korea's Suneung exam (Thursday) · the COP31 revised draft (Thursday).

## Date verification

20 November 2026 is a Friday, confirmed with the system date command
(`TZ=Asia/Jakarta date -d 2026-11-20` → Friday 2026-11-20 WIB) in v1;
carried over unchanged.

## Weakest-sourced items (flagged honestly — unchanged from v1)

- Story 12's sales figures are a Sensor Tower *estimate*, not official
  Rockstar/Take-Two numbers — labelled as an estimate on the page.
- Story 3's pre-market figures come from Finnhub quote data ($87.66,
  −9.79% at 08:19 EST) and Sharecast's 10:30 GMT report (−4.7%, $92.60);
  the timeline uses both, at their own timestamps.
- Story 13 (cancer pill) rests on a single BBC headline item; no trial
  name or journal was in the copy read.
- The timeline's 02:30 UTC landfall start converts the IMD's "around
  8 am" IST bulletin; the 05:50 UTC completion converts the 11:20 IST
  bulletin.

## Production and verification (21 Nov 2026)

- `page.html` is a fresh composition written for v2 (v1's page.html and
  any main.py were not read before writing). `artwork.jpg` was rendered
  from it with headless Chromium (1024×1024 viewport) → PNG → JPEG
  quality 80.
- Final artwork: JPEG, exactly 1024×1024, 278,104 bytes (limit 1 MiB),
  sha256 0669fd281ec7be9cc7b9d32f73f0bc91a24b93e6a771a0b069f1e9beecaf6105.
- `main.py` is a fresh composition from the spec (validates artwork.jpg:
  exists, JPEG SOI FF D8, ≤1 MiB, SOF dimensions exactly 1024×1024,
  then byte-copies to entry.png in $MAKEFUN_OUTPUT_DIR, falling back to
  a local "output" dir). Written in one full write plus one small
  clarifying comment edit.
- Verified: `MAKEFUN_OUTPUT_DIR=/tmp/ni1120r2-out python3 main.py`
  exits 0, prints `wrote /tmp/ni1120r2-out/entry.png (1024x1024,
  278104 bytes)`; produced entry.png is byte-identical to artwork.jpg
  (`cmp` clean). A negative test with a corrupt JPEG exits 1 with
  "error: could not parse JPEG dimensions from artwork.jpg".
- Story count: 3 lead + 10 medium panels + 21 briefs = 34; briefs
  numbered 14–34 continuously; region counts sum to 34.
- The render was visually inspected three times (PNG twice, final JPEG
  once); all in-art labels legible, timeline complete, map pins
  numbered 1–13, date-check and footer inside the frame.

## Status

- Package only. NOT bundled, NOT submitted, NO git repo created.
  Bundle + check + submit to be done from a fresh main-chat session
  under the new run-record rules. Note Force_Last: this v2 replaces v1
  only when submitted; v1 (score 981,793, #551) remains the standing
  entry until then.
