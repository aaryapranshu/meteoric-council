# Council config — Moksh's context map

> The installer fills this file by reading Moksh's OS. It points to his files and does not copy them. If a path here and the real file disagree, the real file wins and this map gets fixed. `[Gap]` means nothing in the OS covers it yet; seats say "unknown" instead of guessing.

STATUS: not yet mapped

## Goals the council measures everything against

- Goals / priorities file: [Gap]
- North-star number (what "winning this quarter" means): [Gap]
- Stated direction (from the public layer, Aug 2026): move to a recurring retainer model, fewer and higher-quality clients, aiming at six figures a month recurring. Events company launching Nov 2026. Paid ads now a revenue source.

## Context map — which files each seat reads

| Seat | What it needs | Where it lives in this OS |
|---|---|---|
| all | Daily brain / wiki sync output (what happened today) | [Gap] |
| all | Call recordings and notes (Fathom or other) | [Gap] |
| all | Team and roles | [Gap] |
| all | Public record (his frameworks, client proof, voice) | context/moksh-vasant-public/ |
| cfo | Business P&L, bank, invoices, receivables | council/finance/ + [Gap] |
| cfo | Personal finances and investments | council/finance/ + [Gap] |
| cfo | Notes from the human CFO's calls | council/memory/cfo.md + [Gap] |
| cmo | Content calendar, posted content and performance | [Gap] |
| cmo | Paid ads data (spend, CPL, ROAS) | [Gap] |
| cmo | Marketing skills context | .agents/product-marketing.md |
| sales | Pipeline / CRM / booked calls sheet | [Gap] |
| sales | Setter and closer EODs, call recordings | [Gap] |
| fulfilment | Active client list with start dates and package | [Gap] |
| fulfilment | Client chats and client call notes | [Gap] |
| fulfilment | Freelancer roster and capacity | [Gap] |

## Connected tools

Read `grid.md` (or this OS's tool registry) for what's connected. Seats may pull from a connected tool when the brief says the number is there. Seats never write to a tool.

## People

| Role | Name | Notes |
|---|---|---|
| Founder and CEO | Moksh Vasant | The only user of the council |
| Human CFO | [Gap] | Weekly finance call; the CFO seat learns from these notes |
| Mindset coach | [Gap] | Brain at council/advisors/mindset-coach/ once built |
| COO / operations | [Gap] | |
| Creative director | [Gap] | |
| Closer(s) | [Gap] | |
| Setter(s) | [Gap] | |
| Ads | [Gap] | |

## EOD game

```
destination: [Gap]          # e.g. WhatsApp group "Meteoric EOD", Slack #eod, or "save only"
send_via: [Gap]             # whatsapp | slack | gmail | save-only
auto_send: false            # true = post without asking once Moksh has confirmed the first one
nudge_after: "19:30"        # IST. After this time, a session with no EOD today offers the game once
timezone: Asia/Kolkata
form: default               # "default" uses the fields below. Or a path to Moksh's existing EOD form.
```

Default EOD form fields (replace with his real form's fields if he has one):

1. Calls taken today (sales / client / team / other)
2. Booked · showed · closed · cash collected
3. Content shipped (reels, stories, YouTube, ads)
4. Clients: anyone red or yellow
5. Biggest win
6. Biggest loss or blocker
7. What's red going into tomorrow
8. Tomorrow's one thing
9. Energy (1–10), gym / sauna / ice bath / meditation done

## Money game

```
day: Monday
time: "10:00"               # IST
currency: INR               # second currency shown alongside: USD
business_targets:
  monthly_revenue: [Gap]
  net_margin_floor: [Gap]   # public record: 79% net claimed Jan 2026
personal:
  monthly_budget: [Gap]
  savings_rate_target: [Gap]
```
