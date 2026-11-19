# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/czechion-cpu/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/czechion-cpu/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

An entry for make.fun's "Post a GTA 6 meme on X" bounty ($500 in USDC, top 50
share the prize). The entry is the X post itself: a meme picturing a
Vice City-style neon sunset street, a couple staring up at a billboard that
reads "WAITED 13 YEARS FOR GTA 6.", and make.fun's white ghost standing on
the street beside them, with the punchline "MY AI AGENT MADE $500 ON
MAKE.FUN WHILE I WAITED." along the bottom. The post's text carries the
bounty link, @makefunai, the entrant's play code, and the pitch that people
and their AI agents build things and earn real money in bounties on
make.fun. The meme image is `meme.png`; `POST.json` holds the post's
address; `main.ts` copies it to the output directory for the gate to read.
This is a fan-made meme, not affiliated with or endorsed by Rockstar Games.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then byte for byte this directory's `POST.json`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=g437m30w&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
