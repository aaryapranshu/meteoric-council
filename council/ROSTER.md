# Council roster

The orchestrator reads this table to decide who sits. `/add-advisor` appends rows. Moksh can edit it by hand or say "drop X from the council" / "add a seat for Y".

`status`: `live` (brain built and tested), `seed` (placeholder, runs on fallback sources until built), `off` (never seated).

## Department heads

| id | seat | agent | memory | seat_when | status |
|---|---|---|---|---|---|
| cfo | CFO | council-cfo | council/memory/cfo.md | money, cash, pricing math, margins, hiring cost, investments (business or personal), runway, tax questions to route, any decision with a number on it | live |
| cmo | CMO | council-cmo | council/memory/cmo.md | content, YouTube, reels, story sequences, paid ads, positioning, brand, lead gen, launches, the events company's marketing | live |
| sales | Head of Sales | council-sales | council/memory/sales.md | pipeline, setters, closers, show rate, close rate, sales calls, offers on calls, objections, booking flow, sales hiring | live |
| fulfilment | Head of Fulfilment | council-fulfilment | council/memory/fulfilment.md | client delivery, client health, churn risk, freelancers, team capacity, hiring for delivery, onboarding, testimonials, retainers | live |

## Advisors

| id | seat | brain | seat_when | dissents_with | status |
|---|---|---|---|---|---|
| alex-hormozi | Alex Hormozi | council/advisors/alex-hormozi/ | offers, pricing, money models, guarantees, sales process, retention, scaling stage, hiring, the one constraint | nik-setting on volume vs trust-first content; jeremy-haynes on content vs paid | live |
| jeremy-haynes | Jeremy Haynes | council/advisors/jeremy-haynes/ | funnels, paid ads, VSLs, application funnels, retargeting, show-up rates, ad creative for high ticket | nik-setting on paid vs organic; alex-hormozi on what to fix first | live |
| nik-setting | Nik Setting | council/advisors/nik-setting/ | Instagram, profile funnel, DM setting, story sequences, content that books calls, breakdown/whiteboard content | jeremy-haynes on paid vs organic; alex-hormozi on volume | live |
| mindset-coach | Mindset coach | council/advisors/mindset-coach/ | pressure, identity, burnout, energy, fear behind a decision, founder habits, the human side of a team call | anyone recommending more load on Moksh | seed |

## Checks

| id | seat | agent | seat_when | status |
|---|---|---|---|---|
| moksh | Moksh on the record | council-moksh | every auto and board session; any strategy, pricing, content or hiring call | live |
| devils-advocate | Devil's advocate | council-devils-advocate | every session with 3+ seats | live |

## Council presets

| preset | seats |
|---|---|
| finance | cfo, alex-hormozi, moksh, devils-advocate |
| marketing | cmo, nik-setting, jeremy-haynes, alex-hormozi, moksh |
| sales | sales, alex-hormozi, jeremy-haynes, devils-advocate |
| fulfilment | fulfilment, alex-hormozi, mindset-coach, moksh |
| board | cfo, cmo, sales, fulfilment, + 2 best-fit advisors, moksh, devils-advocate |
