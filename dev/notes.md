# Working notes — gta6-meme-x-01

## The meme
- Base scene: AI-generated Vice City-style neon sunset street (dev/base-scene.png),
  an original couple seen from behind looking up at a blank billboard. No
  Rockstar artwork, no real people, no official logos.
- `dev/compose_meme.py` warps "WAITED 13 YEARS / FOR GTA 6." onto the
  billboard in perspective, pastes the real make.fun ghost mark
  (assets/makefun-mark-1024.png, from https://make.fun/press/) standing on
  the street, and adds the bottom punchline bar: "MY AI AGENT MADE $500 /
  ON MAKE.FUN WHILE I WAITED."
- First composite: billboard text overflowed the billboard's right edge.
  Fixed by shrinking the text (fit width 660 -> 520, start size 100 -> 88)
  and widening the quad inset (0.10 -> 0.18); ghost moved slightly and
  shrunk 215 -> 190 px. Re-checked at 1024 and at 480x480 (the judge's
  size): all text readable, ghost recognisable, nothing cut off.

## The post (parent posts it; draft in dev/post_text.txt)
- X account: @Ahmadabbabsg (public). Play code n=0:
  makefun-dragon-trinket-ferret. Contains the bounty link, @makefunai,
  the play code, and the earn-real-money pitch. 301 bytes, under the
  ~1,100-byte judge read limit.

## Repo
- main.ts written fresh (own structure + JSON validation + clear errors);
  copies POST.json to $MAKEFUN_OUTPUT_DIR/POST.json, prints nothing.
- POST.json still holds the starter placeholder — the parent updates it
  with the real post URL after posting.
- README uses the live badge template from requirements.json
  (owner czechion-cpu, repo gta6-meme-x-01, referral g437m30w).
- LICENSE is MIT with an SPDX-License-Identifier: MIT line.
- .makefun/owner.json names wallet
  8SdQwmvef5amFrDNpB59iPsf75BeGh9QR5BYHT7feiJX.

## Still to do (parent)
- Post meme.png from @Ahmadabbabsg with the draft text, get the post URL,
  update POST.json, commit, push to new public GitHub repo czechion-cpu/
  gta6-meme-x-01, set repo About (homepage + topics), bundle this session
  and submit before 2026-11-23T14:00:00Z.
