# LaunchShelf — Complete Business Package

A digital product business selling a book-launch kit to self-published authors. Built July 2026.

## What's in this folder

```
launchshelf/
├── index.html                    ← Landing page (deploy to GitHub Pages/Surge/Vercel)
├── gumroad-listing.md            ← Paste into Gumroad product editor
├── outreach-sequence.md          ← 5-email affiliate/partnership sequence
├── social-promo-kit.md           ← 3 X threads, 2 LinkedIn posts, 5 Reddit posts
├── business-model.md             ← Costs, pricing, honest revenue projections
├── 30-day-launch-plan.md         ← Your day-by-day execution checklist
├── competitor-analysis.md        ← Landscape + positioning
├── product/                      ← THE ACTUAL PRODUCT YOU SELL (5 modules)
│   ├── 01-90-day-launch-plan.md
│   ├── 02-arc-outreach-templates.md
│   ├── 03-kdp-listing-prompts.md
│   ├── 04-reader-email-sequences.md
│   └── 05-social-promo-calendar.md
└── automation/
    ├── lead-scraper.py           ← Finds partnership leads (HN + Reddit APIs)
    ├── analytics.py              ← Traffic reports from server logs
    └── onboarding.py             ← Emails the free checklist to subscribers
```

## What YOU must do manually (platforms require a human — ~4 hours total setup)

1. **Gumroad account** — sign up, verify identity, connect bank/PayPal. Create product + 3 variants from `gumroad-listing.md`. Upload zipped `product/` bundles.
2. **Formspree account** (free) — create a form, copy the form ID into `index.html` (search `YOUR_FORM_ID`).
3. **Hosting** — GitHub Pages (free): create repo → upload `index.html` → Settings → Pages. Or `npx surge` from this folder.
4. **Replace placeholders in `index.html`** — search for `YOURNAME` (Gumroad links) and `yourdomain.com` (email). Ask me and I'll do the edits once you have the real URLs.
5. **Cover image** — Canva free tier, spec in `gumroad-listing.md`.
6. **Domain** (~$12/yr, optional but recommended).
7. **All posting and outreach happens under your name** — I draft everything; you review and press send. Communities ban unreviewed AI spam, and they're right to.
8. **Testimonials** — seed 5–10 free copies for honest reviews; replace the placeholders in `index.html`. Never fabricate.

## What runs autonomously

- `lead-scraper.py` — weekly via cron; outputs ranked `leads.csv`
- `onboarding.py` — daily via cron; sends the lead magnet to new signups exactly once (needs Gmail app password, see file docstring)
- `analytics.py` — on demand or weekly; funnel report (visits → Gumroad clicks)
- Gumroad itself — paid delivery, receipts, refunds, affiliate payouts: all automatic

## Honest expectations

Realistic base case (from `business-model.md`): **$0–400 in month 1, $400–800/mo by month 3** with 5–10 hrs/week of consistent marketing. The product is finished; from here, revenue is a function of distribution work actually happening. There is no version of this that makes money while nobody markets it.

## First three actions (today)

1. Create the Gumroad account (20 min).
2. Read the 5 product modules and adjust anything to your taste (1 hr) — it's your name on it.
3. Tell me when the Gumroad URLs exist and I'll wire them into the landing page and generate the checklist PDF.
