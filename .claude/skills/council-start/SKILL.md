---
name: council-start
description: First launch of Moksh's Meteoric Council. Reads his whole OS, interviews him in a short guided conversation (what he wants from the council, the decision on his mind, his mindset coach, his CFO, his EOD, who else should sit), pulls his coach's session transcripts and starts building the coach's brain, runs a live demo, then presents a personalised welcome page in Meteoric's own brand colours as an artifact. Use right after the council is installed, when Moksh says "start my council", "set up my council", "onboard me to the council", or when council/onboarding.md doesn't exist yet and he asks for the council.
---

> Meteoric Council · First launch. Built for Moksh Vasant by Fulcrum Labs on FulcrumOS.

This is the moment Moksh meets his council. It should feel like a sharp chief of staff who has already read everything, asks only what it couldn't find, teaches him how to use the room as it goes, and ends by handing him a page that's clearly about him.

Read `council/COUNCIL.md`, `council/ROSTER.md` and `council/config.md` first.

## Tone

Warm, quick, confident. He talks casually (English with some Hindi); match him. **One question per message.** Every question offers the brain's best guesses from his OS as lettered options, so most answers are one letter. After each answer, give one line on how he'll use that part of the council. That's the guiding. Never lecture. The whole conversation should take about ten minutes.

## Step 1: Read everything first (silent)

Before the first message, build a profile of Moksh and his OS. Spend real effort here; it's what makes the rest feel personal.

1. **His OS.** `CLAUDE.md`, every top-level folder's index or README, priorities or goals, team, clients, finances, content, sales, the daily brain or wiki sync, the decision log, `grid.md` (or his tool registry) for what's connected.
2. **The public layer.** `context/moksh-vasant-public/MOKSH.md` (who he is, stated goals, the business) and `00-identity/influences.md` (the people he learns from, which become advisor suggestions).
3. **Call recordings.** Find where calls land: a Fathom connection in `grid.md` or available tools, a transcripts folder, call notes from the daily sync. List recent calls by title and participants. Look for recurring sessions that look like a **mindset coach** (titles or participants with words like coach, mindset, session, or a repeating 1:1 with the same person) and a **CFO** (finance, CFO, accounts, numbers). Moksh's coach may be called Alex or something close to it. Treat that as a hint to confirm, not a fact.
4. **Meteoric's brand.** The welcome page uses Meteoric's colours, and they live on his device. Search the OS for brand tokens: a brand or design file (`brand.md`, `design.md`, `style guide`), CSS variables or Tailwind config in any website or app folder (look for `--color-`, `colors:`, hex codes in a brand context), or a brand kit folder. Build the 13 page tokens from what you find (see Step 5). If nothing is found, the template already defaults to Meteoric's public site palette (obsidian, cream, Meteoric yellow, gold, sage, set in Inter), so use that and note it.
5. **Fill `council/config.md`** from what you found, if `STATUS` isn't already `mapped`: every context-map row a real path or `[Gap]`, goals, people.

Keep notes in `council/onboarding.md` as you go (template at the bottom).

## Step 2: The interview (one question per message)

Open with one line that shows you've done the reading, then the first question. For example:

> Read your OS, your public record and your calls from the last month. Your council's seated, ten seats. Eight quick questions so it works the way you do, most of them one letter.

Then ask these, in order. Skip any question the OS already answered beyond doubt; confirm it in one line instead ("Your CFO is Riya, Monday calls on Fathom. Right? `y`/fix").

1. **The 90-day goal.** "What do you want this council to get you in the next 90 days?" Offer three options from his priorities and public goals (for example: A) retainers, fewer and better clients, six figures a month recurring; B) the events company launched and profitable; C) paid ads as a second engine). He can pick, combine or type his own.
   *Guide line:* every memo the council writes gets measured against this.
2. **The decision on his mind.** "What's the one call you're sitting on right now?" Offer two or three open decisions found in his OS (decision log, recent chats, the daily sync).
   *Guide line:* that's the first thing we'll put to the room in a minute.
3. **His mindset coach.** "Who's your mindset coach?" If you found a likely coach in the calls, offer it: "A) Alex, the Thursday 1:1s on Fathom (12 sessions) B) someone else". Then: "Can I use those session recordings to build their seat?" (`y` / `n` / "only the last N").
   *Guide line:* the coach's seat will think the way your coach does, the questions they always ask you and the patterns they've named in you. Private to your OS.
4. **His CFO.** Name, which day the call is, and whether the calls are recorded. Offer what you found.
   *Guide line:* every CFO call you log teaches the CFO seat. Say "log my CFO call" after each one.
5. **His EOD.** "Where should your EOD go, and do you already have a form?" Offer the chats you found (WhatsApp groups, Slack channels) and "save only". If he has a form, ask him to paste it or point to it, and copy its fields into `config.md`.
   *Guide line:* after 7:30pm the OS will offer the EOD game once. Four minutes.
6. **Where his money lives.** Bank or accounting exports, a sheet, his CA's reports. Offer what's connected.
   *Guide line:* Monday's Money game reads from there, and the Fitness Score only counts what it can see.
7. **Who else should sit.** Offer three or four people from his influences file who aren't on the council yet: "Want any of these on your council? A) … B) … C) … or name someone."
   *Guide line:* any yes gets built by `/add-advisor` from their public work, same as Hormozi, Haynes and Nik.
8. **How the room talks to him.** "How blunt do you want them? A) brutal, B) direct but kind, C) gentle." And "English, or Hinglish fine?"
   *Guide line:* every seat follows this from now on.

Write each answer into `council/onboarding.md` and the right config file as you go: goal and people into `council/config.md`; the EOD and money blocks into `config.md`; the tone preference into `council/COUNCIL.md` under a new `## How Moksh wants to be spoken to` section (a short block, not a rewrite).

## Step 3: Start the coach's brain

If Moksh said yes in question 3:

1. Pull the session transcripts from wherever they are (the Fathom connection, the transcripts folder, or ask him to export them from Fathom if there's no other way). Save them to `~/.fulcrum/advisor-build/mindset-coach/`, outside the OS repo.
2. Run `/add-advisor` for slug `mindset-coach`, private, from that folder. This takes a while for a full build, so start it as a background sub-agent if this environment can, and keep going with the onboarding. Otherwise tell Moksh it will run right after the welcome page, and run it then.
3. Update the roster row from `seed` to `live` only once the brain has passed its three test questions.

Do the same for any advisor he said yes to in question 7, one at a time, after the coach.

## Step 4: A live demo

Put the decision from question 2 to the room, small and fast so he sees it work:

- Pick the one council preset that fits, and run it as a **quick council**: three seats in parallel (the department head plus two advisors, or the head plus one advisor plus devil's advocate), then a five-line mini-memo: the recommendation, the split, the biggest risk, the unknown, the next step.
- End with: "That was three seats. Say `/council` and the full room does this properly, with cross-examination."

If sub-agents can't run yet (the agents load on the next session), run the three seats yourself in turn, following their agent files, and say so in one line.

## Step 5: Build the welcome page

1. Write `council/welcome-data.json` with everything below, every line specific to Moksh. Nothing generic: a line that would fit any founder is a failed line.

```json
{
  "example": false,
  "councilName": "Meteoric Council",
  "owner": {"first": "Moksh", "business": "Meteoric Boost", "date": "<D Mon YYYY>"},
  "headline": "Moksh, your council <em>is seated.</em>",
  "lede": "<two sentences: what it read and what the room is now>",
  "goal": {"text": "<his 90-day goal in his words>", "number": "<the number that defines winning, or empty>", "why": "<where it came from>"},
  "seats": [
    {"group": "dept | adv | check", "name": "<seat>", "status": "live | seed | queued", "watching": "<one line: what this seat will watch for HIM, from his data>"}
  ],
  "asks": [
    {"council": "<council>", "prompt": "<a question written from his real context, ready to paste>", "why": "<one line>"}
  ],
  "rituals": [
    {"name": "EOD game", "when": "<from config>", "body": "<one line incl. where it posts>", "say": "EOD game"},
    {"name": "Money game", "when": "<from config>", "body": "<one line>", "say": "money game"},
    {"name": "Weekly review", "when": "Sundays · after the EOD", "body": "<one line>", "say": "weekly review"}
  ],
  "coach": {"name": "<coach>", "status": "Live | Building | Waiting for sessions", "summary": "<one line>", "steps": [{"text": "<step>", "done": true}], "next": "<what to say next, or empty>"},
  "gaps": [{"what": "<missing data>", "why": "<which seat needs it, for what>", "fix": "<what to say or do>"}],
  "answers": [{"q": "<question>", "a": "<his answer, short>"}],
  "councils": [{"name": "<council>", "seats": "<seats>", "try": "<a one-line example from his world>"}],
  "theme": {
    "source": "<where in the OS the brand came from, or 'meteoricboost.com default'>",
    "light": {"bg": "", "surface": "", "ink": "", "mute": "", "line": "", "panel": "", "on-panel": "", "on-panel-mute": "", "accent": "", "on-accent": "", "accent-ink": "", "seed": "", "warn": ""},
    "dark":  {"bg": "", "surface": "", "ink": "", "mute": "", "line": "", "panel": "", "on-panel": "", "on-panel-mute": "", "accent": "", "on-accent": "", "accent-ink": "", "seed": "", "warn": ""},
    "fonts": {"google": "family=<Family>:wght@400;600;800", "display": "\"<Family>\",Helvetica,Arial,sans-serif", "mono": "\"JetBrains Mono\",Menlo,monospace"}
  }
}
```

Sizes: 10 seats (all of them, coach and any queued advisors included), 5 asks across different councils, 3–6 gaps (most important first), the 8 answers, 6 council rows.

**Theme rules.** `light` is for the light theme and `dark` for the dark theme; both must be complete. `accent` is Meteoric's signature colour; `on-accent` is the text colour that reads on it; `accent-ink` is the accent colour for text on `bg` (darken it on a light background until it's readable). `panel` is the dark card colour in the light theme and a raised surface in the dark theme. Keep contrast readable: body text on `bg` and on `surface` should be clearly legible in both themes. If his brand only has a dark palette, build the light one from its cream or light neutrals. If the brand uses a font that isn't on Google Fonts, put it in `display` with a fallback stack and leave `google` as the nearest Google family. Omit `theme` entirely to keep the template's Meteoric default.

2. Build it: `python3 council/scripts/build_welcome.py council/welcome-data.json` writes `council/welcome.html`.
3. **Present it.**
   - If this session has the **Artifact** tool, publish `council/welcome.html` with it (`icon: "team"`, `description`: "Moksh's Meteoric Council: the seats, what each one watches, and what to ask first"). Artifacts start private to Moksh. Then open it for him.
   - If not, run `open council/welcome.html` (macOS) so it opens in his browser, and tell him where the file is.
4. Close with three lines: the link (or file), the one thing to do tonight (`EOD game`), and the one gap that matters most.

## Step 6: Finish

- `council/onboarding.md` is complete, and its first line says `STATUS: onboarded <date>`.
- `council/config.md` says `STATUS: mapped <date>`.
- Re-running this skill later refreshes the welcome page from the latest context without repeating answered questions (confirm them in one line each instead).

## `council/onboarding.md` template

```markdown
STATUS: in progress

# Council onboarding — Moksh

## What the OS told me before asking
- Goals: <…>
- Open decisions: <…>
- Calls found: <n> (coach-like: <…>, CFO-like: <…>)
- Brand found at: <path or "not found, using meteoricboost.com default">

## The interview
1. 90-day goal: <…>
2. Decision on his mind: <…>
3. Mindset coach: <name> · sessions: <where, how many> · build: <yes / no>
4. CFO: <name, day, recordings>
5. EOD: <destination, form, time>
6. Money lives in: <…>
7. New advisors: <names, or none>
8. Tone: <…>

## Demo
<the five-line mini-memo>

## Built
- Welcome page: <artifact link or file path>
- Coach brain: <status>
```

## Rules

- One question per message, with guesses. Never a form.
- Every guess comes from his OS or public record. Never invent a name, a client or a number; if you aren't sure, ask.
- Coach and CFO transcripts are private. They stay in the OS and the scratch build folder, never in anything public-facing.
- Nothing is sent outside the OS during onboarding. The EOD destination is only recorded, not tested with a real message, unless he asks.
