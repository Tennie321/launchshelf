# 30-Day Launch Plan — LaunchShelf

Legend: 🧑 = you must do it manually · 🤖 = Claude/scripts do it (you review) · ⏱ = est. time

## Week 1 — Ship the storefront

| Day | Task | Who | ⏱ |
|---|---|---|---|
| 1 | Create Gumroad account, verify email, connect bank/PayPal for payouts | 🧑 | 20m |
| 1 | Review the 5 product modules (product/ folder); personalize the author voice | 🧑+🤖 | 1h |
| 2 | Export modules to PDF (I can do this), zip Starter/Complete/Pro bundles | 🤖 | — |
| 2 | Create Gumroad product + variants; paste everything from gumroad-listing.md | 🧑 | 40m |
| 3 | Make cover image in Canva (spec in gumroad-listing.md); upload | 🧑 | 30m |
| 3 | Create free Formspree account, copy form ID into index.html | 🧑 | 10m |
| 3 | Replace all placeholder URLs in index.html (Gumroad links, email) | 🤖 | — |
| 4 | Create GitHub account (if none) → deploy index.html to GitHub Pages, or `npx surge` | 🧑 | 30m |
| 4 | Buy domain (~$12, optional) and point it at the page | 🧑 | 20m |
| 5 | I generate the free Launch Week Checklist PDF (lead magnet) | 🤖 | — |
| 5 | Test end-to-end: visit page → buy with Gumroad test mode → email capture | 🧑 | 30m |
| 6–7 | Give 5–10 free copies to authors in communities for honest reviews/testimonials | 🧑 | 1h |

**Week 1 exit criteria:** product purchasable, page live, lead magnet flowing, 5+ review copies seeded.

## Week 2 — First traffic

| Day | Task | Who | ⏱ |
|---|---|---|---|
| 8 | Run `lead-scraper.py` → review leads.csv, shortlist 15 partnership targets | 🤖 then 🧑 | 30m |
| 8 | Post Reddit 1 (pure value post) in r/selfpublish | 🧑 posts, 🤖 drafts | 20m |
| 9 | Send outreach Email 1 to first 5 targets (personalized) | 🧑 sends, 🤖 drafts | 40m |
| 10 | Post X Thread 1 | 🧑 | 10m |
| 11 | Outreach Email 1 to next 5 targets; Email 2 to day-8 batch | 🧑 | 40m |
| 12 | Post Reddit 2 (ARC templates giveaway) | 🧑 | 20m |
| 13 | Collect testimonials from week-1 review copies → replace placeholders in index.html | 🧑+🤖 | 30m |
| 14 | Weekly review: run analytics.py / check Gumroad dashboard; log numbers | 🤖 | 15m |

## Week 3 — Compound

| Day | Task | Who | ⏱ |
|---|---|---|---|
| 15 | Post LinkedIn 1; X Thread 2 | 🧑 | 20m |
| 16 | Outreach Emails 3 to earlier batches; onboard any affiliates who said yes (Gumroad affiliate settings, 40%) | 🧑 | 45m |
| 17 | Reddit 3 — free blurb-teardown day (highest-effort, highest-payoff post) | 🧑 | 2h |
| 18 | Set up cron for onboarding.py (daily lead-magnet delivery) | 🧑 once | 15m |
| 19 | X Thread 3; engage every reply within 24h | 🧑 | 30m |
| 20 | Outreach Email 4; follow up with warm affiliate leads personally | 🧑 | 30m |
| 21 | Weekly review + first price/copy tweak based on data (e.g., if CTR high but sales low → listing problem) | 🧑+🤖 | 30m |

## Week 4 — Review and double down

| Day | Task | Who | ⏱ |
|---|---|---|---|
| 22 | Post Reddit 5 in weekly promo threads (free checklist) | 🧑 | 15m |
| 23 | Outreach Email 5 (graceful close) to non-responders; tally affiliate roster | 🧑 | 30m |
| 24 | Post Reddit 4 + LinkedIn 2 (honest month-1 numbers — these perform) | 🧑 | 30m |
| 25–26 | Kill what didn't work, double what did (data from analytics + Gumroad) | 🧑+🤖 | 1h |
| 27 | Draft month 2 calendar: repeat winners weekly; I draft all posts in advance | 🤖 | — |
| 28 | Ask every buyer so far for a Gumroad rating (short friendly email) | 🧑+🤖 | 20m |
| 29 | Decide first extension product (order bump / genre pack) based on buyer questions | 🧑+🤖 | 30m |
| 30 | Month-1 retro: revenue, list size, affiliate count vs. business-model.md base case | 🧑+🤖 | 30m |

## What runs autonomously vs. what needs you

**Fully autonomous (scripts/cron):** lead scraping, analytics reports, lead-magnet email delivery, sent-log dedup.

**AI does the work, you press send (~80% of the labor):** all Reddit/X/LinkedIn drafts, all outreach emails, testimonial swaps into the page, monthly retros, product updates, new modules.

**Only you can do (~3–5 hrs/week):** creating accounts (Gumroad, Formspree, GitHub, domain — platforms require a human and it's your money/identity), posting under your name, sending outreach from your inbox, replying to customers, approving refunds.

Anything posted under your name should be read by you first — communities detect and punish unreviewed AI content, and it's your reputation.
