# Installing the Meteoric Council

These instructions are for the AI agent (Claude Code or similar) doing the install in Moksh's OS. Follow them in order. Re-running them later updates the council in place and never touches Moksh's data.

## 1. Find the workspace

The workspace is Moksh's OS folder: the directory this session is running in (it has a `CLAUDE.md`). Tell Moksh which folder you're installing into before changing anything. If the session isn't inside his OS folder, ask which folder to use.

## 2. Get the module

Keep one copy outside the workspace so it can be updated later: `~/.fulcrum/meteoric-council`.

- Not there yet: `git clone --depth 1 https://github.com/aaryapranshu/meteoric-council.git ~/.fulcrum/meteoric-council` (the repo is public; no login needed)
- If `git` isn't installed: download https://github.com/aaryapranshu/meteoric-council/archive/refs/heads/main.zip and unzip it there (its `meteoric-council-main` folder's contents are the module).
- Already there: `git -C ~/.fulcrum/meteoric-council pull --ff-only`. If the pull fails, delete the folder and clone again.

Never clone into the workspace itself, or into a cloud-synced folder (Desktop or Documents on iCloud).

## 3. Copy it in

```
bash ~/.fulcrum/meteoric-council/install.sh "<workspace>"
```

This puts:
- 6 skills in `.claude/skills/`: `council-start`, `council`, `eod-game`, `money-game`, `weekly-review`, `add-advisor`
- 7 seat agents in `.claude/agents/`: `council-cfo`, `council-cmo`, `council-sales`, `council-fulfilment`, `council-advisor`, `council-moksh`, `council-devils-advocate`
- `council/`: the constitution, roster, config, three advisor brains (Alex Hormozi, Jeremy Haynes, Nik Setting), the mindset-coach seed, the department memory files, a worked example session and the welcome-page template

**Name clashes.** If the OS already has a skill or agent with the same name that this module didn't install (most likely an older `council` skill), the script skips it and lists it. Show Moksh what the existing one does in two lines, and ask whether to replace it. Only on his yes, re-run with `--force`. That moves the old one to `vault/pre-council-<date>/` first, so nothing is lost.

## 4. Map his context (the important step)

The seats are only as good as what they can read. `council/config.md` is the bridge between the council and Moksh's existing OS. It points to his files and never copies them.

1. Read his `CLAUDE.md`, list the top-level folders, and read the index or README of each. Find his daily brain / wiki sync output, call notes (Fathom), team file, client list, goals or priorities, finances, content and ads data, sales pipeline, and decision log. Read `grid.md` (or his tool registry) for connected tools: calendar, WhatsApp, Slack, Sheets, Fathom.
2. Fill every row of the **Context map** in `council/config.md` with the real path or tool. Leave `[Gap]` where nothing exists. Never invent a path.
3. Fill **Goals** from his priorities file, and **People** from his team file.
4. Check the public-record layer is at `context/moksh-vasant-public/`. The `council-moksh` seat needs it. If it's missing, tell Moksh to run the public-layer install message he was sent on 20 Oct, and carry on.
5. Ask Moksh only what the files can't answer, in **one** message:
   - Where should the EOD go? (WhatsApp group, Slack channel, email, or save only) And does he have an existing EOD form whose fields we should copy?
   - His human CFO's name, and where the CFO call recordings land.
   - His mindset coach's name, and whether session recordings exist.
6. Write the answers in, then change the first line to `STATUS: mapped <date>`.

If the workspace is a git repo with a remote, tell Moksh that `council/finance/` and `council/games/money/` will hold confidential money data, and ask whether to add them to `.gitignore`.

## 5. Register the council in CLAUDE.md

Append this section to `<workspace>/CLAUDE.md`. If a section called "Meteoric Council" already exists, replace only that section. Leave the rest of the file exactly as it was. If the file already has an older council section from another module, ask Moksh before removing it.

```markdown
## Meteoric Council (by Fulcrum Labs)

An orchestrator with sub-agents: four department heads (CFO, CMO, Head of Sales, Head of Fulfilment), advisor brains (Alex Hormozi, Jeremy Haynes, Nik Setting, my mindset coach), and two checks (me-on-the-record, devil's advocate). Constitution: `council/COUNCIL.md`. Seats: `council/ROSTER.md`. My context map: `council/config.md`.

**Whenever I bring a decision (pricing, offers, hiring, spend, investments, content strategy, a client, the team), or say "council", "finance / marketing / sales / fulfilment council", "full board", or "what would <seat> say", invoke the `council` skill.** For a one-line factual answer, skip it.

| When I want to… | Skill |
|---|---|
| Set up the council, or refresh my welcome page | `council-start` |
| Decide something with the council, or ask one seat | `council` |
| Do my end-of-day update (as a game) | `eod-game` |
| Do my Monday finance hour, or log a CFO call | `money-game` |
| Get the weekly report from every department | `weekly-review` |
| Put someone new on the council (build their brain) | `add-advisor` |

**First launch:** if `council/onboarding.md` doesn't exist or doesn't start with `STATUS: onboarded`, the first time I mention the council, run `council-start` before anything else.

**Nudges (offer once per session, never push):**
- After 19:30 IST, if `council/games/eod/<today>.md` doesn't exist: "EOD game? 4 minutes."
- On Mondays, if `council/games/money/<today>.md` doesn't exist: "Money game today?"
- On Sundays after the EOD game: offer `weekly-review`.

**Memory:** after every council session, EOD game, Money game and weekly review, the department memory files in `council/memory/` are updated, so the seats get sharper every week. Use my existing context for current and private facts, the public-record layer for what I've said on the record, and `council/memory/` for what the council has learned.

To update the council: say "update the Meteoric Council".
```

## 6. Verify

Check each of these and fix anything that fails:

- `.claude/skills/{council-start,council,eod-game,money-game,weekly-review,add-advisor}/SKILL.md` exist (or were skipped for a clash and Moksh knows).
- `.claude/agents/council-*.md` (7 files) exist.
- `council/advisors/alex-hormozi/LENS.md`, `council/advisors/jeremy-haynes/LENS.md` and `council/advisors/nik-setting/LENS.md` exist.
- `council/config.md` starts with `STATUS: mapped`, and every `[Gap]` left is one the OS genuinely doesn't cover.
- `CLAUDE.md` has the Meteoric Council section and nothing else in it changed.

**Smoke test.** Dispatch one quick take through the `council-advisor` agent (`Mode: quick. advisor: alex-hormozi. Question: In one paragraph, what's the biggest lever on Meteoric Boost moving to retainers?`). It should name a framework and a file. If sub-agents can't be dispatched in this environment, say so: the council will run in single-agent mode, which works but is slower.

## 7. Report back, then launch the council

Tell Moksh, briefly:

- what was installed or updated, and anything skipped for a clash
- which context gaps are left in `council/config.md`

Then **start the first launch now, in this same session**: read `.claude/skills/council-start/SKILL.md` and follow it from Step 1. It interviews Moksh (his goal, the decision on his mind, his mindset coach, his CFO, his EOD), starts building his coach's brain from his session recordings, runs a short live demo, and ends with his personal welcome page as an artifact in Meteoric's colours.

The seat agents load properly in the next session, so the demo in this first session may run in single-agent mode; that's expected. Finish by telling him to start a new session and try `/council` on a real decision, and `EOD game` tonight.
