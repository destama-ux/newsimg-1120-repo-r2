# Leader study — news-image-20261120 (v2 revision run)

Studied 2026-11-21 ~01:40 WIB, from the live leaderboard
(GET /api/competitions/news-image-20261120/leaderboard, 10,287 entries)
and the competition detail (GET /api/competitions/news-image-20261120).
Top-10 artifact images fetched and viewed individually
(GET /api/submissions/<id>/artifact.webp). Submission detail endpoints
return `source_withheld: true`, `repo_url: ""` — no public repos to read;
the study is therefore of the images themselves, which is what the judge
sees (the judge "has no news feed: it judges each image as a careful
picture editor can, by what the image itself shows").

## Where we stand

- Ours (sugarspiced555, "The World in One Day — Friday 20 November 2026:
  34 verified stories"): score 981,793, prize_rank #551 of 10,251.
  Deep-check figure from 01:25 WIB matches the live board.
- Top-50 cutoff at study time: #50 dusty-gorilla, 988,608 (was 988,486
  at the 01:25 deep check). Gap to close: ~6,700–6,800 points.
- The top 50 are ALL 12 wins / 0 losses in 12 judge duels. Scores
  988,608–992,057 differ only in the micro win-rate / interval, i.e.
  opponent strength, not in win count. There is no single trick to copy:
  the gap is a picture-editor judgement gap, and every top-50 page shares
  the same anatomy. Our v1 already has that anatomy; v2 must execute it
  harder in the specific places below.

## Top 10 (score / bytes / W–L)

| # | Handle | Score | Bytes | Title claim |
|---|--------|-------|-------|-------------|
| 1 | samatch-we | 992,057 | 466,875 | 35 stories, 7 regions |
| 2 | 888dao-sats | 991,652 | 742,756 | 36 stories, 6 continents |
| 3 | kiencx | 991,429 | 418,538 | 33 sourced stories, 13 drawn |
| 4 | dewacandra4 | 991,336 | 286,276 | 38 stories, 7 regions |
| 5 | mellow-otter-50 | 991,332 | 404,916 | (44 stories, 7 regions, in image) |
| 6 | vivid-falcon-13 | 991,165 | 668,731 | 36 stories, 7 regions |
| 7 | kho22 | 991,137 | 235,213 | 36 stories |
| 8 | madsrepo | 991,042 | 349,041 | (front page) |
| 9 | mangmang | 990,653 | 206,001 | 36 stories, 7 regions |
| 10 | kim-soleum | 990,534 | 277,147 | 34 sourced stories, 7 regions |

Note: file size does NOT decide the top — #1 is 467 KB, #2 is 743 KB.
Size is only the tie-break (lower wins ties), and our 282,675 B already
beats every top-10 page on that axis. The judge score is won on the
picture, not on bytes. (Our 34 stories vs leaders' 35–38/44 is a count
claim in their titles, not a verified fact advantage — we keep our
verified 34 and do not invent stories to pad the count.)

## What the leaders do better than our v1 — concrete findings

1. **Lead order is news order, not topic order.** Every top-10 page
   leads with the same three stories in the same order: (1) Kyiv
   missile attack, (2) Cyclone Akvan landfall, (3) the AI/market
   sell-off. Our v1 led Akvan → COP31 → UK–EU and buried Kyiv as
   medium panel #4. A picture editor's front page leads with the war.
   V2 FIX: reorder the 13 panels to Kyiv, Akvan, Anthropic/AI, then
   COP31, UK–EU, US shutdown, Prabowo–Xi, Google, opioid ring, Kakao,
   Deutsche Bank, GTA VI, cancer pill. Same 13 panels, same facts.

2. **The masthead subhead names the four top stories concretely.**
   Leaders: "Russian missiles hit Kyiv's bridges · Cyclone Akvan
   strikes India · An AI sell-off sinks Asia's markets · UK and EU
   seal a deal" (#1); "Cyclone Akvan strikes India · Ballistic
   missiles hit Kyiv · COP31 deadlocked on final day · Asian AI
   sell-off" (#2). Our v1 subhead was vague ("A cyclone strikes
   India's east coast · the climate talks run into overtime · Britain
   and the EU sign their reset deal"). V2 FIX: concrete four-story
   italic subhead.

3. **Stat strip and region bar are two separate, clean rows.**
   Leaders run (a) a 6-stat strip — big dark/red numbers with a
   one-line label each — and (b) a separate coloured region bar with
   counts per region. Our v1 stacked the region labels directly above
   the stat numbers in one merged row, so the numbers read as if they
   belonged to the regions (they don't). V2 FIX: split them into two
   rows; stat strip first, region bar second, each labelled.

4. **Lead art is bigger, darker, and carries data inside the picture.**
   #1's Kyiv panel: night skyline, missile trails, "KYIV / 3 bridges
   hit" in-art; its AI panel is a chart with a per-index table
   (Taipei −6.2%, Seoul −5.2%, Tokyo −5.1%, Hong Kong −1.9%); its
   cyclone panel has a spiral + "Landfall · 8 am". #2/#9 do the same
   (cyclone spiral, Kyiv missile trails, COP31 globe + thermometer,
   candlestick chart). Our v1 art is good but the in-art labels are
   smaller and several were clipped in the first render. V2 FIX:
   larger bold in-art labels with the key figure inside the art
   (KYIV — 3 BRIDGES HIT; AKVAN 70–80 KM/H; ANT $87.66 −9.8%;
   COP31 OVERTIME; 100,000 VISAS A YEAR; $582M; 24.6M COPIES), dark
   navy/black lead backgrounds, and a falling red chart line in the
   AI panel. No new figures: every in-art number is already in our
   verified set (leaders' per-index Asian closes are NOT in our
   verified facts, so v2 does not reproduce them).

5. **The map is a first-class element, not a sidebar.**
   #2 and #4 use a wide dark-navy map with large red numbered pins;
   #1 and #3 use a light tan map with numbered pins and a "pins 1–13"
   legend. Our v1 map is a narrow left column with small pins and a
   two-line caption. V2 FIX: keep the map + briefs bottom band, but
   enlarge the pins (numbered 1–13, red on dark navy), add a one-line
   legend, and give the map more width.

6. **Briefs are two clean columns with bold city prefixes, one line
   each.** Leaders' briefs (14–36) read as a scannable index; ours
   are the same idea but tighter and smaller, and the two-column
   split in v1 put 14–24 left / 25–34 right with uneven density.
   V2 FIX: keep 2 columns (14–24 / 25–34), bold city prefix, source
   tag, slightly larger type, strict one-line discipline.

7. **The date-check box is prominent and names the excluded news.**
   Every leader ends with a red-bordered DATE CHECK box that lists
   Thursday's news left out on purpose (Trump–Xi–Putin summit itself,
   Anthropic's $97.17 first-day close / IPO pricing, ICJ Myanmar
   verdict, GTA VI launch, Suneung exam, COP31 revised draft).
   Our v1 has this box and the same exclusions — it is a strength to
   keep, made bolder in v2 (bigger "DATE CHECK" label, "NOT shown"
   wording, exclusions separated by middots).

8. **What v1 already does as well as the leaders — keep.**
   Giant serif date masthead; 13 illustrated panels (3 leads + 10
   medium) with source tags on every story; big-number strip;
   coloured region bar; world map; forensic date-check; a UTC
   timeline strip (most leaders do NOT have one — it is our
   differentiator, keep it as a black strip under the region bar).
   The 19 Nov r2 formula (983,928) and this v1 (981,793) both prove
   the anatomy is right; the gap is execution, not structure.

## V2 change list (from this study)

- Reorder leads to Kyiv → Akvan → AI sell-off (war first).
- Concrete four-story masthead subhead.
- Stat strip and region bar split into two separate rows.
- Bigger, darker lead art with bold in-art data labels; red chart in
  the AI panel; all in-art figures from the verified set only.
- Larger numbered map pins + legend.
- Bolder date-check box ("DATE CHECK — NOT shown").
- Keep: same day (Friday 20 November 2026), same 34 verified stories
  and facts, same 13+21 structure, UTC timeline, sources on every
  story, file under ~300 KB.

## Competition facts (from the detail endpoint)

- Title: "Sum up 20 November's world news in one image". Pot $250,
  top 50 paid ($50/$30/$15, then $5 for #4–#10, $3 for #11–#50).
- Deadline: 2026-11-22T00:00:00.000Z (Sunday 22 Nov 07:00 WIB).
- Image: whole PNG or JPEG, at most 1 MiB, 1024×1024 px. Program
  (main.py) runs twice and both runs must write the same bytes.
  At most 10 submissions/day, 20 total; last submission before the
  deadline is final (Force_Last).
- Judge: AI judge, pairwise image duels, no news feed — judged purely
  on what the image itself shows. Submission count at study time:
  12,586 (leaderboard lists 10,287 ranked entries).
