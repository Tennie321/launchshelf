#!/usr/bin/env python3
"""
Lead Scraper — Find potential affiliate partners and customers.

Scrapes public sources for newsletter writers, podcasters, and bloggers
in the writing/publishing niche. Outputs a CSV of leads.

Usage:
    python3 lead-scraper.py
"""

import csv
import json
import re
import time
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.error import HTTPError

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; LeadScraper/1.0)"
}

SOURCES = [
    # HN — self-publishing / book launch / indie author discussions
    {
        "name": "HN Self-Publishing & Book Launch",
        "url": "https://hn.algolia.com/api/v1/search?query=self-publishing+book+launch+indie+author&tags=story&hitsPerPage=50",
        "type": "api"
    },
    # HN — ARC readers / book reviews / marketing
    {
        "name": "HN Book Marketing & Reviews",
        "url": "https://hn.algolia.com/api/v1/search?query=book+marketing+reviews+author&tags=story&hitsPerPage=50",
        "type": "api"
    },
    # Reddit — self-publishing community (via Pushshift, no auth needed)
    {
        "name": "Reddit r/selfpublish",
        "url": "https://api.pullpush.io/reddit/search/submission/?subreddit=selfpublish&size=25&sort=score",
        "type": "api"
    }
]


def fetch_json(url: str) -> dict:
    """Fetch JSON from a URL."""
    req = Request(url, headers=HEADERS)
    try:
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (HTTPError, Exception) as e:
        print(f"  ⚠️  Error fetching {url}: {e}")
        return {}


def process_hn_data(data: dict) -> list:
    """Extract leads from HN Algolia results."""
    leads = []
    hits = data.get("hits", [])
    for hit in hits[:20]:
        title = hit.get("title", "")
        url = hit.get("url") or hit.get("story_url", "")
        points = hit.get("points", 0)
        if points < 5:
            continue
        leads.append({
            "source": "Hacker News",
            "title": title,
            "url": url,
            "relevance_score": points,
            "discovered_at": datetime.now().isoformat()
        })
    return leads


def process_reddit_data(data: dict) -> list:
    """Extract leads from Pushshift/Reddit search results."""
    leads = []
    submissions = data.get("data", [])
    for post in submissions[:20]:
        title = post.get("title", "")
        # Skip if no real title
        if not title or len(title) < 10:
            continue
        url = post.get("url", "")
        # Use reddit permalink if no external url
        permalink = post.get("permalink", "")
        full_url = url or f"https://reddit.com{permalink}"
        score = post.get("score", 0)
        num_comments = post.get("num_comments", 0)
        relevance = score + (num_comments * 2)  # Weight comments as engagement
        if relevance < 3:
            continue
        leads.append({
            "source": f"Reddit r/{post.get('subreddit', 'selfpublish')}",
            "title": title,
            "url": full_url,
            "relevance_score": relevance,
            "discovered_at": datetime.now().isoformat()
        })
    return leads


def save_leads(leads: list, filename: str = "leads.csv"):
    """Save leads to CSV."""
    if not leads:
        print("  ℹ️  No leads found this run.")
        return

    fieldnames = ["source", "title", "url", "relevance_score", "discovered_at"]
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(leads)

    print(f"  ✅ Saved {len(leads)} leads to {filename}")


def main():
    print("🔍 LaunchShelf Lead Scraper")
    print(f"   Started at {datetime.now().isoformat()}")
    print()

    all_leads = []

    for source in SOURCES:
        print(f"📡 Scanning: {source['name']}")
        data = fetch_json(source["url"])
        if "reddit" in source["name"].lower():
            leads = process_reddit_data(data)
        else:
            leads = process_hn_data(data)
        all_leads.extend(leads)
        print(f"   Found {len(leads)} leads")
        time.sleep(1)  # Rate limiting

    save_leads(all_leads)
    print(f"\n✅ Done. Total leads: {len(all_leads)}")


if __name__ == "__main__":
    main()
