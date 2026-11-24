# Research — Seventeen Syllables of Debugging (v2 resubmission)

## Provenance

- Anchor line quoted from STEP 0: `makefun anchor eaf19b6ab5212bfaf3a720762029fd3c08619559 round 34237273`
- v1 text ("Green when it's alone / It passes when no one watches / It breaks once I look") was used for reference only. No wording, image or turn from it was reused; candidate 21 below was cut specifically for drifting toward it.
- Method: wrote 25 new candidates around single concrete debugging moments, counted syllables by mouth (not by spelling), scored each 1-5 on the five judge criteria (C1 form/haiku-about-debugging, C2 concrete and fresh picture, C3 turn lands and reframes, C4 no filler, C5 reads aloud cleanly), cut everything that failed form or whose last line explained instead of turning, then re-scored the top five and critiqued the top three from the judge's seat.

## All 25 candidates

| # | Haiku (5 / 7 / 5) | C1 | C2 | C3 | C4 | C5 | Total | Verdict / rejection reason |
|---|---|---|---|---|---|---|---|---|
| 1 | Cursor blinks at three / the only thing still awake / it blinks, I blink back | 5 | 4 | 5 | 4 | 5 | 23 | Cut: line 2 is a familiar "only one awake" sentiment; one generic line costs it criterion 4. |
| 2 | Red stack trace at dawn / forty lines of who called whom / the last name is mine | 5 | 5 | 5 | 5 | 5 | 25 | CHOSEN. |
| 3 | Breakpoint in the dark / the world freezes, not the bug / the bug keeps running | 5 | 4 | 4 | 4 | 4 | 21 | Cut: "bug" repeats in lines 2-3 and "world freezes" is a familiar move. |
| 4 | Stale cache, warm and smug / it keeps last week's truth alive / the past answers back | 5 | 4 | 4 | 4 | 4 | 21 | Cut: "warm and smug" tells rather than shows; "truth alive" is abstract. |
| 5 | Print lines like breadcrumbs / they lead me into the dark / the trail ends at me | 5 | 4 | 4 | 4 | 4 | 21 | Cut: breadcrumbs-in-the-dark is well-worn and the last line duplicates #2's move. |
| 6 | Green test, two-faced friend / run it twice, it passes twice / trust is the bug | 3 | 3 | 3 | 3 | 3 | 15 | Cut: last line is 4 syllables ("trust is the bug") — fails 5-7-5. |
| 7 | Null pointer, unseen / each guard I wrote lets it through / nothing, staring back | 5 | 5 | 5 | 4 | 5 | 24 | Top five, rank 3. "unseen" slightly anticipates "lets it through", costing one point on C4. |
| 8 | Two threads, one shared cup / both grab it at the same time / one drinks, one is air | 5 | 4 | 4 | 4 | 4 | 21 | Cut: "at the same time" is prosaic padding added for the count. |
| 9 | One fix, one new wound / I close the door on one bug / another kicks it in | 3 | 3 | 3 | 3 | 3 | 15 | Cut: last line is 6 syllables (an-oth-er kicks it in) — fails 5-7-5. |
| 10 | Step into the dark / line by line the truth gets worse / the answer is me | 5 | 3 | 4 | 4 | 4 | 20 | Cut: "into the dark" is a cliché and line 1 has no concrete debugging object. |
| 11 | Error: something broke / it will not say where or how / I hunt the whole stack | 5 | 3 | 3 | 4 | 4 | 19 | Cut: line 1 is prose, not a picture; the last line narrates the hunt instead of turning it. |
| 12 | Duck, my only peer / I explain it line by line / it nods, I solved it | 5 | 4 | 4 | 4 | 4 | 21 | Cut: the rubber duck is a familiar trope and "it nods" is too cute. |
| 13 | One line in the diff / I have stared for an hour straight / it stares back, unmoved | 5 | 4 | 4 | 4 | 4 | 21 | Cut: "stared"/"stares" repeats and the last line explains the staring rather than turning. |
| 14 | Lost semicolon / the whole page goes red at once / one dot would end this | 5 | 5 | 4 | 5 | 5 | 24 | Top five, rank 4. Last line is close to an explanation, so C3 loses a point. |
| 15 | Loop without a door / it circles the same three lines / each lap gets warmer | 5 | 4 | 4 | 5 | 5 | 23 | Cut: "loop without a door" is a metaphor, not a picture. |
| 16 | Log line, smooth liar / it swears the value is fine / the crash disagrees | 5 | 5 | 5 | 5 | 5 | 25 | Top five, rank 2 — runner-up. |
| 17 | Memory, slow tide / it rises an inch a day / the fan learns my name | 5 | 4 | 5 | 5 | 5 | 24 | Top five, rank 5. "slow tide" is a comparison rather than the concrete object itself. |
| 18 | Warning in yellow / I keep scrolling past it, blind / it was the answer | 5 | 4 | 5 | 4 | 5 | 23 | Cut: "in yellow" is a weak modifier and "I keep scrolling past it" is plain prose. |
| 19 | Works on my machine / the server greets me with red / my machine sleeps, smug | 5 | 4 | 4 | 4 | 5 | 22 | Cut: line 1 is a programmer cliché, not a fresh picture. |
| 20 | Breakpoint, stubborn stone / it sits on the line I trust / it never stops there | 5 | 4 | 5 | 4 | 4 | 22 | Cut: "stubborn stone" is a stock comparison and "it" opens two consecutive lines. |
| 21 | Add a print, bug gone / remove it, the bug comes home / it knows when I look | 5 | 4 | 4 | 4 | 4 | 21 | Cut on originality: "it knows when I look" drifts toward v1's "It breaks once I look". |
| 22 | Midnight, wrong timezone / the timestamp swears it is noon / the clock lies to us both | 3 | 4 | 4 | 4 | 4 | 19 | Cut: last line is 6 syllables (the clock lies to us both) — fails 5-7-5. |
| 23 | Debug mode, left on / it whispers into the log / our names, one by one | 5 | 4 | 4 | 4 | 4 | 21 | Cut: "our names" is vague; no single sharp image at the centre. |
| 24 | Off by one again / the loop stops one step early / the last one is gone | 5 | 3 | 4 | 4 | 4 | 20 | Cut: line 1 is a statement, not an image; "gone" states the absence instead of showing it. |
| 25 | Stack trace, three a.m. / the messages climb the screen / I am the last frame | 5 | 4 | 4 | 4 | 4 | 21 | Cut: too close to #2 in subject and last-line move; #2 says it with less. |

## Top five, re-scored

1. **#2 — 25** (5/5/5/5/5). Mouth count: Red(1) stack(1) trace(1) at(1) dawn(1) / for-ty(2) lines(1) of(1) who(1) called(1) whom(1) / the(1) last(1) name(1) is(1) mine(1).
2. **#16 — 25** (5/5/5/5/5). Log(1) line(1) smooth(1) li-ar(2) / it(1) swears(1) the(1) val-ue(2) is(1) fine(1) / the(1) crash(1) dis-a-grees(3).
3. **#7 — 24** (5/5/5/4/5). Null(1) point-er(2) un-seen(2) / each(1) guard(1) I(1) wrote(1) lets(1) it(1) through(1) / noth-ing(2) star-ing(2) back(1).
4. **#14 — 24** (5/5/4/5/5). Lost(1) sem-i-co-lon(4) / the(1) whole(1) page(1) goes(1) red(1) at(1) once(1) / one(1) dot(1) would(1) end(1) this(1).
5. **#17 — 24** (5/4/5/5/5). Mem-o-ry(3) slow(1) tide(1) / it(1) ris-es(2) an(1) inch(1) a(1) day(1) / the(1) fan(1) learns(1) my(1) name(1).

#2 and #16 tie on the raw sum. The tie is broken on the judge's own ordering: #2 leads on criteria 2-4 (see the judge-seat critique), which are the first points of difference.

## Judge-seat critique of the top three

Read as if comparing two entries at a time, going through the criteria in order and stopping at the first real difference.

- **#2 vs #16.** Criterion 1: both are clean 5-7-5 debugging haiku, no difference. Criterion 2: #2 gives a colour, a time and an object in "Red stack trace at dawn", then scale in "forty lines"; #16 offers a personified abstraction, "smooth liar", where a photograph could be. #2 wins here. Criterion 3: #16's "the crash disagrees" is a sharp contradiction but only answers line 2; #2's "the last name is mine" retroactively converts "who called whom" into an accusation that points at the reader, so the whole poem changes meaning on the last line. #2 wins again. Criterion 4: "forty lines of who called whom" carries scale, specificity and the idea of a call chain in seven syllables, with nothing spare. #2 wins. #16 would take a quick verdict on punchiness, but on the published weighting #2 is the stronger poem.
- **#2 vs #7.** Both hit criterion 1 and both have a strong C2 image. Criterion 3 separates them: "nothing, staring back" makes an absence into a watcher, which is a fine jolt, but it mostly extends the null image rather than reframing "each guard I wrote lets it through" as an accusation. #2's turn reorganises the preceding line. Criterion 4 also favours #2: #7's "unseen" in line 1 partly pre-empts what lines 2-3 reveal.
- **#7 vs #16.** #16 wins on C4 and C5 — every word is load-bearing and the three lines fall into speech rhythm — while #7 spends a syllable on "unseen" that the rest of the poem already implies. #16 is the runner-up.

## Choice

**Chosen: #2** — `Red stack trace at dawn / forty lines of who called whom / the last name is mine` (76 characters, 76 UTF-8 bytes, three lines, no trailing newline).

It beats the runner-up (#16) on criteria 2-4 because its first line gives a visible colour, hour and object instead of a personified abstraction, its last line turns the whole call chain from a neutral "who called whom" into a verdict aimed at the reader rather than merely contradicting a lying log, and its middle line packs scale and specificity into seven syllables without a single spare word.

## Declarations

thinking_own_work: true
originality: own wording, no copied winner/reference text
