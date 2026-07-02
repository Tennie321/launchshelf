# Gumroad Setup Checklist

The landing page is ready — but these still need YOUR Gumroad account to go live:

## 1. Create Gumroad Products
Log into https://gumroad.com/ and create three products:

| Product | Price | Landing Page Link |
|---|---|---|
| LaunchShelf Starter | $29 | https://tennie321.gumroad.com/l/launchshelf-starter |
| LaunchShelf Complete | $49 | https://tennie321.gumroad.com/l/launchshelf-complete |
| LaunchShelf Author Pro | $99 | https://tennie321.gumroad.com/l/launchshelf-pro |

> **Replace `tennie321`** in the URLs above with your actual Gumroad username if different.
> After creating each product on Gumroad, replace the URLs in `index.html` with the actual links Gumroad gives you.

## 2. Create Formspree Form
1. Go to https://formspree.io/ and sign up
2. Create a new form (it will give you an ID like `xyzabc12`)
3. Replace `YOUR_FORM_ID` in `index.html` line 408:
   `<form action="https://formspree.io/f/xyzabc12" method="POST">`

## 3. Create Social Preview Image
The landing page references `social-preview.png` for Open Graph. Create a 1200×630px image with:
- Background: dark gradient (#0d1017 → #1a1f2e)
- Title: "LaunchShelf — Book Launch Kit"
- Text: "90-Day System • ARC Templates • KDP Prompts"
- Color accent: gold/orange (#f59e0b)

Save it as `~/Desktop/LaunchShelf/social-preview.png` and push to GitHub.

## 4. Deploy
After setting up Gumroad products and Formspree:
```bash
cd ~/Desktop/LaunchShelf
git add -A
git commit -m "Set up Gumroad links and Formspree"
git push
```
GitHub Pages will auto-deploy to https://tennie321.github.io/launchshelf/