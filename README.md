# Wednesday 25 November 2026 — 37 stories, 7 regions: Kyiv hits Russian ship, Houthis strike Riyadh tower, Asian stocks tumble

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/mattthaphap-tech/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/mattthaphap-tech/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

make.fun bounty entry — "Wednesday 25 November 2026 — 37 stories, 7 regions: Kyiv hits Russian ship, Houthis strike Riyadh tower, Asian stocks tumble"
($100, ends 27 Nov 2026 07:00 WIB). Bounty: https://make.fun/bounty/news-image-20261125

## The image

`entry.png` — a 1024×1024 dense front page summarising Wednesday
25 November 2026 in **37 stories**, built the way the previous daily
winners are built (18 Nov: 51 stories, 1st place; 19 Nov: 37 stories,
1st place; 22 Nov v5: 37 stories, 97.1% dev-board win rate): a masthead with the date
prominent, a numbers strip, 3 illustrated leads, 10 richly illustrated
minis, 24 one-line briefs, a date-check box and a sources footer. Every
story carries a region tag and a CONFIRMED / REPORTED status.

**The recipe decision.** The 24 Nov entry tested the 25-story experiment:
round 1 rank 397/7,302, round 2 rank 132/9,063 — but those scores are raw
judge win-counts, not a percentage, so ">= 97.1%" against the 22 Nov v5
benchmark could not be confirmed. Per the standing rule, this edition
reverts to the proven 37-story v5 recipe: briefs 19px, lead headlines
22px, lead summaries 16px, mini headlines 16px. The world map stays
dropped — at phone width it was an unreadable beige blob — and the briefs
take the full width. Verified legible at 400px and 390px wide, every
brief, lead headline and mini headline read by eye at both widths. QC at
full size found and fixed: seven briefs overflowing their columns at 19px
(shortened); the numbers-strip label wrapping into the lead images
(shortened to one line); three-line mini headlines pushing their
status tags over the next row (shortened to two lines); the date-check
box text running past its right edge (max-width corrected, font 14px so
the full text fits two lines); and the second lead's tag running 364px
in a 316px column (source shortened to "SAUDI").

- **The day in numbers:** 11 wounded in the Riyadh tower strike · 60 km
  Houthis from Aden · −5.3% Korean shares · $54.94bn Dell Q3 revenue ·
  74,746 Gaza death toll · 266m facing acute hunger
- **Leads:** Zelenskiy confirms Kyiv hit a Russian ship in the Gulf of
  Finland · Houthis hit Riyadh's tallest tower, 11 wounded · Asian stocks
  tumble as US tariff threats return
- **Minis:** CIA and ODNI hit by cyber breach · NATO to send jets to
  Poland · Huawei guilty of trade-secret theft · Dell lifts outlook on AI
  server boom · Nvidia falls about 6% after surge · Gaza death toll
  reaches 74,746 · Trump gives Giuliani Medal of Freedom · EU announces
  new sanctions on Russia · BJP, Akali Dal reunite for Punjab 2027 · US
  envoy unsure Israel aid ends
- **Briefs (24):** Russia–Ukraine spar at the UN · Iran suspected in
  tanker cyberattacks · Fort Hood gunman seeks stay of execution ·
  Houthis 60 km from Aden · O'Hare radar fault · US core PCE due ·
  Trump spares Thanksgiving turkeys · Bitcoin $59,258 · Australia
  inflation 3.8% · Brent $90.97 · Shein $100m FTC settlement · Netflix
  buys Radford Studio Center · Iraq rejects OPEC+ assessment · England
  beat Australia in 2nd T20I · India women beat Indonesia 17-1 in hockey
  · 266m face acute food insecurity · 700,000+ Russian troops killed ·
  Banten fire search goes on · Indonesia seeks ASEAN grid safeguards ·
  Man Utd fury at Yoro red card · Army to detonate lead azide in Iowa ·
  Venezuela debt $237.5bn · India manufacturing nine-month high · Wall
  Street mixed

## How it is built

`build_25nov.py` draws `entry.png` with PIL only — deterministic, no
network. `main.py` copies the bundled image to `/output/entry.png` and
verifies the copy (size and sha256). `research.md` is the locked, verified
story list with sources and date-discipline notes.

## Date discipline

Every story happened, or was first reported, on Wednesday 25 November
2026. The date-check box on the page lists what was deliberately left out
because it was first reported earlier (COP31 ending Sunday, the
Sanofi–Insmed $41bn deal Monday, Nvidia's +31% surge Monday, Prabowo
naming VP nominees Monday, MSCI's Indonesia word Tuesday, GTA VI
launching 19 Nov).

## License

MIT — see `LICENSE`.
