# Meteoric Council

**A board of AI advisors for Moksh Vasant's OS.** Built by Fulcrum Labs on FulcrumOS.

> Proprietary. © 2026 Fulcrum Labs Technologies Private Limited. Licensed to Moksh Vasant, Meteoric Boost. See `LICENSE`.

## What it is

One AI with everything in its head gets worse the more you give it. So the council works the way Anthropic runs its own work: an **orchestrator** on top, and **sub-agents** underneath, each with its own brain, memory, context and tools.

You ask the orchestrator. It works out which experts the question needs, briefs them once, sends them out in parallel, waits for every one, makes the disagreements fight it out, and hands you one memo measured against your goals. You decide.

```
                              YOU
                               │
                        ORCHESTRATOR
        ┌──────────────┬───────┴───────┬───────────────────┐
   DEPARTMENTS                    ADVISORS                CHECKS
   CFO · CMO · Sales · Fulfilment   Hormozi · Haynes ·      You-on-the-record ·
   (each learns every week)         Nik Setting · Coach     Devil's advocate
```

## What's inside

| | What it does | Say |
|---|---|---|
| **The council** | Four department councils (finance, marketing, sales, fulfilment), the full board, or auto. Parallel sub-agents, a cross-examination round, one memo. | `/council <decision>` · "marketing council: …" · "what would Hormozi say about…" |
| **EOD game** | Your end of day in five quick rounds. The brain pre-fills the day, you confirm in one word, earn XP and streaks, and the EOD form posts itself to the chat. | "EOD game" |
| **Money game** | Your Monday finance hour with the CFO seat. Guess-the-number, cash, leaks, margins, personal money, investments, CFO prep. Ends in a Financial Fitness Score out of 100. | "money game" · "log my CFO call" |
| **Weekly review** | All four department heads report at once. One page: scoreboard, the red board, three decisions for the week. | "weekly review" |
| **First launch** | Reads your whole OS, interviews you in about ten minutes (your goal, the call you're sitting on, your mindset coach, your CFO, your EOD), starts building your coach's brain from your sessions, runs a live demo, and opens your welcome page in Meteoric's colours. | "start my council" |
| **Add advisor** | Put anyone on the council. Builds their brain from their YouTube, podcasts or books, or from your own sessions with them (your mindset coach). | "add <name> to my council" |

Advisor brains shipped: **Alex Hormozi** (offers, money models, scaling), **Jeremy Haynes** (funnels, paid, VSLs), **Nik Setting** (Instagram content to leads, profile funnel). **Mindset coach** is a seed you build from your own sessions.

Every advisor is an unofficial simulation built from public work, not the real person.

## Install

In a new chat inside your OS, paste:

```
Install the Meteoric Council into my OS. Follow https://github.com/aaryapranshu/meteoric-council/blob/main/INSTALL.md step by step, then start my council.
```

## Layout

```
.claude/skills/   council-start · council · eod-game · money-game · weekly-review · add-advisor
.claude/agents/   council-cfo · council-cmo · council-sales · council-fulfilment
                  council-advisor · council-moksh · council-devils-advocate
council/          COUNCIL.md (constitution) · ROSTER.md · config.md (your context map)
                  advisors/ · memory/ · docs/ · scripts/ · templates/ · examples/
install.sh        safe to re-run; never overwrites your data
INSTALL.md        what your OS's agent follows
```
