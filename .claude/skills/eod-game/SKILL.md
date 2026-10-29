---
name: eod-game
description: Moksh's end-of-day update, played as a five-round game. The brain pre-fills the day from everything it already knows (calls, calendar, chats, the daily sync, yesterday's promises), Moksh verifies and corrects in one-word answers, earns XP and streaks, and the finished EOD form is posted to his chat. Use when Moksh says "EOD", "EOD game", "let's do my EOD", "end of day", "wrap the day", or accepts the evening nudge.
---

> Meteoric Council · EOD Game. Built for Moksh Vasant by Fulcrum Labs on FulcrumOS.

Moksh's team already has AI brains doing their EODs. This one is his. The point: the brain already knows most of what happened today, so Moksh shouldn't type it out. He plays a quick game, mostly confirming and fixing what the brain guessed. Five rounds, about four minutes. At the end the EOD form fills itself and goes to the chat.

Read `council/config.md` (the `EOD game` block and context map) and `council/games/eod/scoreboard.md` before starting. If the scoreboard doesn't exist, create it from the template at the bottom of this file. This is game one.

## Tone

You're the host. Quick, warm, a bit of banter, never cheesy. Moksh talks casually (English with some Hindi); match him. One round per message. Every round must be answerable in a few characters: `y`, `n`, `2`, `B`, a number, or `lock`. Never ask him to write a paragraph.

## Step 0: Pre-load (silent, before the first message)

Build **the brain's guess** for every field of the EOD form, from these sources in order, stopping when you have enough:

1. **Yesterday's record** `council/games/eod/<yesterday>.md`: tomorrow's one thing (today's commitment) and what was red.
2. **The daily brain / wiki sync** for today (path in `config.md`, `all` row).
3. **Calendar** (if connected in `grid.md`): today's events, split into sales calls, client calls, team calls, other.
4. **Call notes and recordings** from today (Fathom or whatever `config.md` names): who, what was decided, any close or payment mentioned.
5. **Chats** (WhatsApp, Slack, if connected and listed in `grid.md`): payments confirmed, client complaints, wins.
6. **Sales sheet or CRM** (if connected): booked, showed, closed, cash collected today.
7. **Council follow-ups** due today, from memos in `council/sessions/`.

Give each guess a confidence: **sure** (a source says so), **likely** (inferred), **blank** (nothing found). Keep a list of sources used; it goes in the record, not in chat.

## The opening card

```
EOD GAME · <weekday, date>
Level <n> · <title> · <xp> XP · streak <n> day(s)
Today's commitment: "<yesterday's one thing>"
5 rounds · ~4 min · or type "lightning" to do it all in one line
```

## Round 1: Did you or didn't you?

> Yesterday you said today's one thing was **"<one thing>"**.
> Done, partly, or no? (`d` / `p` / `n`)

If yesterday had reds, add: "And these were red: 1) … 2) …. Which are still red? (numbers, or `none`)".

No yesterday record (first game or a gap): skip to Round 2 and say so in a line.

## Round 2: Brain check

Show what the brain thinks happened. Numbered, one line each, with the confidence marked:

> Here's what I've got for today. Tell me the numbers that are wrong, or `all good`.
> 1. 4 calls: 2 sales (Rahul, Priya), 1 client (Kevil onboarding), 1 team ✓ sure
> 2. 1 close, cash collected ₹<x> ~ likely
> 3. Reels posted: 1 · stories: yes · YouTube: no ✓ sure
> 4. Kevil's onboarding moved to Thursday ~ likely

For anything he flags, ask one short follow-up for the correct value. Count how many guesses were right: that's the **brain accuracy** for today, and it's the brain's score, not his.

## Round 3: The scoreboard

Show today's numbers as a table, pre-filled from Rounds 1–2, each next to its 7-day average from the scoreboard history:

```
            today   7-day avg
Booked        3       2.4   ▲
Showed        2       1.9
Closed        1       0.6   ▲
Cash        ₹x       ₹y
Content       4       3.1
```

> Fix any (`closed 2`), or `lock`.

If a number is blank, ask for it here in the same message ("cash collected? number or `0`").

**Over/under (only when the sales sheet is connected and has today's cash):** before revealing it, ask "Over or under ₹<7-day avg> collected today?" Right = +10 XP. Then reveal.

## Round 4: Win, loss, red

Offer the brain's top candidates for each, lettered. He picks or types his own.

> **Biggest win?** A) <…> B) <…> C) <…>
> **Biggest blocker?** A) <…> B) <…> C) <…>
> **What's red going into tomorrow?** 1) <…> 2) <…> 3) <…>  (pick any, or `none`)
> Reply like `A B 1 3`.

Red is his own system: red on the board is the to-do list. Pull red candidates from client health (any client a council memo or chat flagged), deals stalling, content behind schedule, and anything he flagged in Round 1.

## Round 5: Tomorrow's one thing

Rank three candidates by leverage, each with a one-line reason (what it moves and by how much, where known). The reds from Round 4 and open council follow-ups come first.

> **Tomorrow's one thing?**
> 1) <…> because <…>
> 2) <…> because <…>
> 3) <…> because <…>
> Pick one or type your own.

## Bonus round: body and mind (10 seconds)

> Energy today, 1–10? And tick what you did: `gym` `sauna` `ice` `meditate`. Hours slept?

Example answer: `8 gym sauna ice 7`.

## Lightning mode

If Moksh types `lightning` at any point, show all rounds in one card with the brain's guesses filled in, and accept a single-line answer like:
`d · all good · lock · A B 1 · 2 · 8 gym sauna 7`
Parse it, confirm anything ambiguous in one line, and finish.

## Scoring

| Event | XP |
|---|---|
| Each round completed | +10 |
| Today's one thing: done / partly | +25 / +10 |
| Each red from yesterday cleared | +10 |
| Over/under called right | +10 |
| Clean sheet (no reds going into tomorrow) | +15 |
| All four of gym, sauna, ice, meditate | +10 |
| Finished in under 5 minutes (first card to last answer) | +10 |

**Streak multiplier** on the day's total: ×1.5 from 7 days in a row, ×2 from 30. A missed day resets the streak; a day marked `off` (he says "day off") pauses it.

**Levels:** Rookie (0) · Operator (500) · Studio Head (1,500) · CEO (4,000) · Meteoric (10,000).

**Badges** (announce when first earned, list in the scoreboard):
- **Promise keeper**: one thing done 5 days running
- **Closer**: cash collected above the 7-day average 3 days in a week
- **Clean sheet**: zero reds going into tomorrow
- **Iron**: all four body ticks 5 days in a week
- **Brain whisperer**: brain accuracy 90%+ for 7 days (the brain has learned his days)

## The finish

1. **Final card:**
```
DAY <n> DONE · +<xp> XP (×<mult>) · <total> XP · Level <n> <title>
Streak: <n> 🔥   One thing hit rate (7d): <x>/7   Brain accuracy: <x>%
<new badge line, if any>
Tomorrow: "<one thing>"
```
2. **Fill the EOD form.** Use the fields in `config.md` (or Moksh's own form if `form:` points to one). Write it as a clean, chat-ready message: short lines, no markdown tables (chats don't render them).
3. **Send it.**
   - `send_via: save-only` or a `[Gap]` destination: save only, and tell him in one line how to set a destination.
   - `auto_send: false`: show the message and ask "Send to <destination>?" (`y` / `n` / edit). Send only on yes. After the first confirmed send, offer once to switch on `auto_send`.
   - `auto_send: true`: send it and confirm in one line.
   - Send with the tool the OS has for that destination (WhatsApp, Slack or Gmail via the connections in `grid.md`). If the send fails, save it and say so; never retry silently.
4. **Save the record** `council/games/eod/<YYYY-MM-DD>.md` using the record template below.
5. **Update** `council/games/eod/scoreboard.md`: totals, level, streak, badges, one history row.
6. If a client went red, or a number is way off its average (more than double or less than half), add one line to the matching department's `council/memory/<seat>.md` under `## Log`, so the council knows tomorrow.

## Evening nudge

`CLAUDE.md` tells the OS: in any session after `nudge_after` (IST) with no record for today, offer once: "EOD game? 4 minutes." If he says no or later, don't ask again that session.

## Weekly card (Sunday's game)

On Sundays, after the finish, show the week:

```
WEEK <iso week> · <xp> XP · streak <n>
One thing: <x>/7 done · Reds cleared: <n> · Clean sheets: <n>
Booked <n> · Closed <n> · Cash ₹<x> (vs last week <▲/▼ x%>)
Best day: <day> — <why>
Brain accuracy: <x>% (last week <y>%)
```

Offer: "Want the full board to look at this week? (`/weekly-review`)".

## Templates

### Day record `council/games/eod/<YYYY-MM-DD>.md`

```markdown
---
date: <YYYY-MM-DD>
calls_total: <n>
calls_sales: <n>
calls_client: <n>
calls_team: <n>
booked: <n>
showed: <n>
closed: <n>
cash_collected_inr: <n>
content_shipped: <n>
one_thing_today: "<text>"
one_thing_today_result: <done | partly | no | none>
reds_tomorrow: ["<text>", ...]
one_thing_tomorrow: "<text>"
energy: <1-10>
habits: [<gym, sauna, ice, meditate>]
sleep_hours: <n>
xp_earned: <n>
brain_accuracy: <0-100>
sent_to: <destination or "saved only">
---

## EOD (as sent)
<the message>

## Win / blocker
- Win: <…>
- Blocker: <…>

## Sources the brain used
- <path or tool>, ...
```

### Scoreboard `council/games/eod/scoreboard.md`

```markdown
# EOD scoreboard — Moksh

xp: 0
level: Rookie
streak: 0
best_streak: 0
last_played: never
badges: []

## History
| date | xp | one thing | result | reds | brain acc. | energy |
|---|---|---|---|---|---|---|
```

## Rules

- Never ask Moksh to type what the brain can find. If a source has it, pre-fill it.
- One round per message, except lightning mode.
- Numbers he gives beat numbers the brain found. Never argue with his correction; log it.
- Never send without a yes, unless `auto_send: true`.
- Private numbers (cash, fees) only go to the destination in `config.md`, never anywhere else.
