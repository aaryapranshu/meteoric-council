---
name: weekly-review
description: The council's weekly report. All four department heads (CFO, CMO, Sales, Fulfilment) file their reports in parallel as sub-agents, each with one thing they learned and one piece of outside research, and the orchestrator compiles a one-screen CEO brief with the red board and the three decisions for the week. Use when Moksh says "weekly review", "weekly report", "how was the week", "department reports", "state of the business", or at the end of Sunday's EOD game.
---

> Meteoric Council · Weekly Review. Built for Moksh Vasant by Fulcrum Labs on FulcrumOS.

Once a week, every department head reports at the same time, and Moksh reads one page instead of chasing four people. Same orchestrator pattern as `/council`: brief once, dispatch in parallel, wait for all, synthesise.

Read `council/COUNCIL.md` and `council/config.md` first.

## Step 1: Brief once

Create `council/reports/<YYYY>-W<ww>/brief.md` with:

- **The week:** Monday to Sunday dates.
- **EOD totals:** sum the week's `council/games/eod/` records (calls by type, booked, showed, closed, cash collected, content shipped, reds raised and cleared, one-thing hit rate, average energy).
- **Money:** the latest `council/games/money/` record and fitness score.
- **Decisions this week:** every memo in `council/sessions/` dated this week, with its decision line.
- **Pointers per department:** the paths from `config.md` each head should open, and any connected-tool figures you pulled (pull them here, once).
- **Last week's review:** path to `council/reports/<last week>/review.md` so heads can compare.

## Step 2: Dispatch the four heads in parallel

One message, four sub-agent calls: `council-cfo`, `council-cmo`, `council-sales`, `council-fulfilment`. Prompt each:

```
Mode: report. Brief: council/reports/<…>/brief.md. research: true.
Return your section in exactly this format, 300 words max:

## <Department>
**Verdict:** <one line: better / worse / flat than last week, and why>
**Numbers:** <3–6 lines: the department's key numbers this week vs last week, each with its source>
**Red:** <anything red, one line each with the action that turns it yellow>
**Working:** <one thing to double down on, with the evidence>
**Stop:** <one thing to stop or fix>
**Learned:** <one thing this department learned this week from the data, in one line>
**Research:** <one outside finding relevant to Meteoric, with URL. CMO and Sales may search the web; CFO and Fulfilment use the advisor brains and the OS instead>
**Decision needed:** <the one decision this department needs from Moksh, or "none">
```

(If sub-agents aren't available, run each head yourself in turn following its agent file.)

The Fulfilment head also returns the **client board**: every active client, green / yellow / red, with one line for each yellow and red.

## Step 3: Compile the CEO brief

Write `council/reports/<YYYY>-W<ww>/review.md` and show it:

```markdown
# Week <ww> — Meteoric Boost
<dates> · Financial Fitness <score>/100 · EOD streak <n>

## The week in one line
<…>

## Scoreboard
| | this week | last week | |
|---|---|---|---|
| Booked / showed / closed | | | ▲▼ |
| Cash collected | | | |
| Content shipped | | | |
| Active clients (G/Y/R) | | | |
| Net margin | | | |

## The red board
- <every red across departments, one line, owner, action>

## Three decisions for this week
1. <decision> — from <department> — `/council <preset>` if it needs the room
2. ...
3. ...

## Department reports
<the four sections, as returned>

## What the council learned
- <the four "Learned" lines>
```

Keep the top half (down to the three decisions) to one screen. The department reports sit underneath for detail.

## Step 4: Close

1. Append each head's **Learned** line and **Numbers** to the `## Log` of its `council/memory/<seat>.md`, and refresh `## Current picture` where the numbers changed.
2. Ask: "Want the council on any of the three decisions now?" On a yes, run `/council` with this review's brief attached so the room starts with the week's numbers.

## Rules

- Same rules as `council/COUNCIL.md`: no invented numbers, missing data marked unknown, nothing sent outside the OS.
- Research findings are labelled as outside sources, never mixed into Moksh's own numbers.
