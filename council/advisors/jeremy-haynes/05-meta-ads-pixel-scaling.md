# 05 — Meta ads, pixel conditioning and scaling spend

**Open this file when:** the question is about Meta (Facebook/Instagram) ads: lead quality swinging, which conversion event to optimize, DM ad setup, ad creative formats, testing structure, CPMs, retargeting pockets, or why ads "stopped working".
**His stance:** "If your Facebook ads aren't working, it's not Facebook, it's not Meta, it's not Zuckerberg, it's you" (m4wYl6hrFIg [00:00]). Two things control who you reach: messaging and pixel conditioning. "You got messaging and you got pixel conditioning" (IyhO7kcyVWU [02:39]).

---

### Pixel conditioning (his core ads concept)
**When to use:** lead quality is mixed or declining, the results column looks cheap but sales say leads are junk, or you're choosing the optimization event.
**The idea:** The pixel reports results, but more importantly, whoever reports to the event you optimize for decides who the ads find next. Pixels work off "recency bias" (KNIJal9GqGY [01:54]) and "prediction batches": the platform reaches only the slice of an audience most likely to convert, bucket by bucket. So never let unqualified people touch the results column. Before there's data, messaging (who it's for and not for) does the targeting.
**How to run it:**
1. Call funnels: optimize for Schedule or Complete Registration, not Lead. Fire it only for qualified bookings.
2. Unqualified answers go to a separate confirmation page that is **not pixeled** ("brokie bait", his term).
3. If sales say "qualified" leads are junk, stop firing the standard event from the page. Have reps move real qualified leads to a CRM stage that sends the event via the Conversions API, quickly, because an empty results column makes the algorithm rotate audiences (WEwwAvTY1B4 [04:40]–[06:17]).
4. Ride out the conditioning phase. Early buckets swing. Don't make reactive edits.
5. Recondition an existing pixel by adding qualifiers now rather than starting a new pixel, unless it's beyond saving ("the art of detachment").
**The numbers:** Pixels retain about 180 days of data (m4wYl6hrFIg [09:27]; QwZ3X7GGSVw [02:41]). Exit learning needs roughly 50 events per ad set per 7 days, sometimes slightly fewer for small TAMs (Zr8m8euJ3zw [37:34]). His sources conflict: WEwwAvTY1B4 [06:17] (2025) says "a couple people" is enough and 50–100 is "barbarian" thinking, while rL1FIHwg8PE [06:04] (Dec 2025) says exiting learning "makes a huge difference" and the old 50/week answer could be 5 or hundreds. Prefer the newer view: get enough events to exit learning, at the most downstream event you can afford. Reconditioning math: 100 results/day, 5 qualified, at $100/day looks like a $1 CPL but is really $20 per qualified result (KNIJal9GqGY [21:10]). One webinar client went from 1.6 to 3.4 ROAS within a week of adding one qualifying question to the opt-in [29:17]–[33:08].
**Mistakes they call out:**
- Optimizing call funnels for Lead.
- Reactive changes in the conditioning phase: "if you can't endure the conditioning phase you will never get to the glory" (KNIJal9GqGY [23:30]).
- Panicking when cost per result rises after filtering. That's your true cost per qualified result showing up.
- An agency pushing spend into a no-qualifier registration campaign to hit quotas, which made the pixel worse every week.
**Ask first:** What event are you optimizing for, and who fires it? What % of results are actually qualified?
**Source:** KNIJal9GqGY [01:54]–[33:54], WEwwAvTY1B4 [01:09]–[07:29], A7aqpkk57Ts [05:18]–[05:43], Zr8m8euJ3zw [36:06]–[41:50], IyhO7kcyVWU [02:39]–[05:39]

---

### Brokie bait (his term)
**When to use:** any opt-in or application where unqualified people are getting through to the pixel.
**The idea:** One or two qualifying questions with conditional logic split traffic. Qualified people reach a pixeled confirmation page. "Brokies" reach an identical but unpixeled page. You can track the brokie ratio with an unlinked custom conversion, but never optimize on it. If there are enough of them and they're "not horridly broke", turn their page into a down-sell to liquidate ad spend.
**How to run it:**
1. Add one honest qualifier. His webinar example: "we are going to make an offer in this webinar that costs a few thousand, are you open to spending that amount if the offer makes sense for you, yes or no" (KNIJal9GqGY [31:54]).
2. Duplicate the confirmation page: pixeled for qualified, unpixeled for the rest.
3. Optional down-sell for the unqualified, handled by trainee closers.
**The numbers:** Down-sell client: under-$150K/year earners get a $5K product via newest closers. The business spends $10–15K/day on ads, and the down-sell liquidates ~$30–50K of spend a week (KNIJal9GqGY [17:39]–[18:25]).
**Mistakes they call out:** Opt-ins with only name, email and phone, which means "optimizing for the result", not quality.
**Ask first:** What single question best separates buyers from non-buyers?
**Source:** KNIJal9GqGY [15:43]–[19:14], [28:31]–[33:08]

---

### DM ads: the two paths to conditioning on qualified people
**When to use:** running Instagram "DM us" or comment-to-DM ads.
**The idea:** Optimizing for "message sent" eventually means "all it takes is one donkey to kick the door in" (IyhO7kcyVWU [04:09]). You get waves of good and bad leads, then a steady decline, and relaunching resets it only briefly. So move the optimization event downstream to a qualified action. Judge on cost per qualified DM: "This is a hallucinated number. This number is not real" (IyhO7kcyVWU [06:50]), meaning the raw cost per DM. He still says he wouldn't encourage DM ads over more stable funnels.
**How to run it:**
- **Path 1, quiz bridge:** ad → simple page with 1–2 qualifiers → qualified people see a button that opens IG DMs with a trigger word unique to this funnel → setter or AI → booked call. A Lead/Schedule web event fires on the qualified page.
- **Path 2, lead campaign + Schedule:** campaign type Lead, ad set optimized for Schedule, creative says "DM us this word". The ad's destination URL is the same scheduler page setters send people to. The confirmation page fires Schedule (+ Conversions API). The results column now shows cost per qualified booked call.
**The numbers:** $10 per DM × 50 DMs with 10 qualified = $50 per qualified DM (IyhO7kcyVWU [06:25]–[06:50]). The aim is to flip from ~80% unqualified to 70–80%+ qualified [16:51].
**Mistakes they call out:** "Raw dogging" message optimization. Generic trigger words that can't separate paid from organic.
**Ask first:** What share of DMs become qualified booked calls? Is the trigger word unique to the ad?
**Source:** IyhO7kcyVWU [02:39]–[17:14]

---

### The algorithm swarms your leads (hyper sophisticated, hyperaware)
**When to use:** explaining why leads cool off between click and call, or why messaging that used to work no longer does.
**The idea:** Meta aims at what you're most likely to buy now. Once you click, it floods you with similar offers across placements for days until the category is exhausted (his "dart" model). So every lead becomes hyper sophisticated within a few scrolls. Building on Eugene Schwartz's market stages, he says buyers now need you to show your whole process, not just a claim or a mechanism. "Treat them like they are going to get swarmed or that they are already getting swarmed because you likely didn't reach them first" (kZmPPS4512I [14:03]).
**How to run it:**
1. Shorten every gap: promote webinars no more than ~72h out, book calls soon.
2. Start selling at the confirmation page. Sell against the other options and make your process known.
3. Hammer Them so you're part of the swarm (`03`).
4. Secret-shop from five perspectives: owner, marketer, customer ("matters more than yours"), AI models, and the algorithm via burner accounts that get targeted by your ads.
5. Price as the premium option rather than undercutting.
**The numbers:** He claims Meta holds ~52,000 data points per user on average (kZmPPS4512I [00:48]). That's his claim, unverified.
**Mistakes they call out:** "Hallucinating" who your competitors are. Being everywhere with junk content.
**Ask first:** What other offers does a lead see in the 48 hours after clicking yours?
**Source:** kZmPPS4512I [00:00]–[25:15], P1v-AN3So3A [09:20]–[19:47]

---

### Ad creative formats, ranked by how well they absorb spend
**When to use:** choosing what creative to produce, or why winners die when budgets rise.
**The idea:** Rank formats by whether they can take serious budget at stable cost, not by ROAS on small spend. Only a single-digit percentage of creatives become real winners, so favor formats you can produce in volume.
**How to run it:**
1. **S:** static reels (B-roll with native on-screen text, written as you'd say it) and talking heads (phone-shot, up to 2 min, ideally 30–60s, jump cuts and subtitles, but they need charisma).
2. **A:** static images (stable CPMs, but call-funnel leads arrive less informed, so add back-end systems), carousels (tweet-thread screenshots, reviews; S if built and tested properly), and short 2–5 min VSLs as ads.
3. **B:** organic posts run as ads, UGC (paid creators rarely sound sincere about high-ticket outcomes), testimonials, green screen.
4. **C:** full 10–20 min VSLs, podcasts as ads (unless cut to back-to-back epiphanies), memes (curiosity clicks, low intent), retargeting (high ROI but can't absorb budget).
5. AI-generated creative: "really close to being rated in S-tier", limited by prompting skill (4C-2ab6rD9M [11:14]).
6. Track creative success rate = winners ÷ total launched.
**The numbers:** Winners at scale are a single-digit % of creatives launched (4C-2ab6rD9M [09:03]). Positive ROAS on a $100 test doesn't count [08:41]. Video ads bring higher-intent leads, image ads cheaper but lower interest (P1v-AN3So3A [57:07]–[57:53]).
**Mistakes they call out:** Running one creative type. Long unsubtitled testimonial videos. Unedited ads (the only D/F).
**Ask first:** What's your creative success rate? Can the founder carry a talking head?
**Source:** 4C-2ab6rD9M [00:43]–[17:19], P1v-AN3So3A [54:47]–[1:02:52]

---

### Testing structure: ad matrix, Thunderdome, consolidation
**When to use:** setting up campaigns and ad sets, or untangling a messy account.
**The idea:** Test angles, not rewordings: "different reasons why somebody would convert". Keep accounts simple. Match testing volume to budget. Where something wins, it tends to keep winning, so scale it where it won.
**How to run it:**
1. Build 5 angles × 5 variations = 25 ads (P1v-AN3So3A [54:47]).
2. Structure: all ads in one ad set (his bias), one ad set per angle, or **Thunderdome** (his name): one ad per ad set with a 3-second view exclusion, forcing spend onto each creative. Use ad-set budgets, not CBO [1:01:21]–[1:02:52].
3. Low budget (a few hundred $/day): one broad cold ad group, 10–20 creatives max.
4. Audiences with more budget: broad, lookalike, interest stack, plus warm.
5. Don't move winners from a test campaign to a scale campaign.
6. Turn off Advantage+ creative enhancements and related-media toggles, except the highlighted positive-comment option (Zr8m8euJ3zw [44:02]).
**The numbers:** An account with 70+ active campaigns cut to 3 saw result cost drop and ROAS "damn near 4x'd" (m4wYl6hrFIg [12:40], client example). In one ad set, 1–3 creatives take the spend (P1v-AN3So3A [1:00:57]).
**Mistakes they call out:** Copying brands that launch hundreds of creatives a week on a small budget. Test-to-scale campaign structures. Judging scaling by a December dip.
**Ask first:** How many active campaigns and ad sets? What's the daily budget per ad set?
**Source:** P1v-AN3So3A [54:47]–[1:08:17], m4wYl6hrFIg [07:16]–[13:27], AAzziyOKCx8 [12:04]–[18:08]

---

### Pocket opportunities (his name): contextual if-this-then-that retargeting
**When to use:** the main funnel works and you want more revenue from the same traffic, or blended ROAS needs lifting.
**The idea:** Small, cheap campaigns, emails and sales actions triggered by what a lead did or didn't do. Each has a tiny budget but a very high return, and stacked they add a large share of revenue.
**How to run it:**
1. VSL non-players: retarget visitors who never pressed play to a long-form sales page that turns each VSL point into a section, still optimizing for calls. Start at $5/day and scale it with the main funnel.
2. Hook-rotation basket: 15-second viewers of your ads who didn't click (excluding web visitors) see new hooks or formats. "The unconverted non-click traffic does not mean that they weren't probable to convert, it just means those ads didn't land well with them" (4fae9a7mbp8 [14:24]).
3. Email by application data: segment sequences by tier (e.g. a wealth manager's $1M to $100M+ bands), each with its own objections and case studies.
4. Sales triggers: a lead who consumed the last ~20 emails gets a rep selfie video.
5. Triggers list: watched/clicked or not, played or not, applied but not booked, booked and opening emails or not, showed or no-showed, CRM objections.
**The numbers:** One VSL had a 19% play rate (81% never pressed play) (4fae9a7mbp8 [01:53]). Pockets at 10:1 to 100:1 ROAS could be ~30% of revenue at $1M/month alongside a ~4:1 main funnel. He puts the blend at "a good you know 10 to1" and says "that's not exact math" [09:25]. (His own figures blend closer to ~9:1.)
**Mistakes they call out:** One giant autoresponder for every lead regardless of application answers. 3-second view audiences for this purpose (use 15s).
**Ask first:** What % of page visitors never press play? Do you segment email by application answers?
**Source:** 4fae9a7mbp8 [00:22]–[20:52]

---

### High CPMs and "it stopped working" complaints
**When to use:** costs rose suddenly, a funnel that worked has decayed, or the team is blaming the algorithm.
**The idea:** Start with ownership: messaging, reputation, over-testing and account complexity usually explain it. A new pixel producing junk with the same ads proves the messaging was always weak and the pixel was carrying it. Ad fatigue often explains a sudden drop better than the page does.
**How to run it:**
1. Check the top of the data hierarchy (`06`), then the chain.
2. A sudden opt-in or CTR drop after working → relaunch fresh ads before redesigning pages (audiobook client: opt-in 28% → 5% → 25% after relaunching ads, P1v-AN3So3A [1:34:03]).
3. High CPMs → the Forester (`04`), better messaging, a cleaner domain.
4. Reputation check (`03`).
5. Consolidate the account.
**The numbers:** In one consult, CPM fell from ~$100–120 on an old GoHighLevel-hosted domain to ~$60–75 on a new clean domain (bZe1YnKTBCE [52:39], guest-reported). CPM range $30–80 is his normal (zyfpGi9uEUU [06:55]).
**Mistakes they call out:** Collecting articles about rising CPMs instead of fixing messaging. Treating a 6-year-old pixel as a trained asset. Messaging that relies on income claims.
**Ask first:** What changed in the 14 days before the drop: creative, offer, page, domain, reviews?
**Source:** m4wYl6hrFIg [00:00]–[13:27], P1v-AN3So3A [1:34:03]–[1:34:51], bZe1YnKTBCE [51:33]–[52:39]

---

### Ads are gambling with better odds
**When to use:** setting a test budget, or a founder is afraid to spend or wants to quit early.
**The idea:** "Ads are gambling, okay? It's just sophisticated gambling with better odds" (QwZ3X7GGSVw [30:01]). Walk into the "casino" with a defined budget and a time frame long enough to survive the dip. Bet enough to be slightly nervous, so you take it seriously, but not so much that desperation makes you short-term. Judge stakes per test (per webinar), not per month.
**How to run it:**
1. Model worst-case stats (`06`).
2. Set the gambling budget and the time frame before spending.
3. Size the bet so it's "slightly nerve-racking" but survivable (bPkM0TCGFQQ [1:04:30]–[1:05:38]).
4. If indecision blocks action, take the smaller bet or the easier funnel.
**The numbers:** A worked guest example: a 10K webinar at 3:1 returns 30K, at 5:1 returns 50K (bPkM0TCGFQQ [36:25]).
**Mistakes they call out:** Calling a validated offer "a test" and betting tiny. Marketers who don't model or set expectations are "donkeys" (QwZ3X7GGSVw [31:55]–[33:01]).
**Ask first:** How much can you lose and still come back next month?
**Source:** QwZ3X7GGSVw [30:01]–[37:09], bPkM0TCGFQQ [35:39]–[38:18], [1:04:08]–[1:08:09], rZCe1U3ME4E [18:49]–[19:35]
