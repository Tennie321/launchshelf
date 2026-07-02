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
    # HN Who's Hiring threads are good for freelance writers
    {
        "name": "HN Writing Threads",
        "url": "https://hn.algolia.com/api/v1/search?query=writing&tags=story&hitsPerPage=50",
        "type": "api"
    },
    # ProductHunt for writing tools
    {
        "name": "ProductHunt Writing",
        "url": "https://api.producthunt.com/v1/posts?category=writing-tools",
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
        leads = process_hn_data(data)
        all_leads.extend(leads)
        print(f"   Found {len(leads)} leads")
        time.sleep(1)  # Rate limiting

    save_leads(all_leads)
    print(f"\n✅ Done. Total leads: {len(all_leads)}")


if __name__ == "__main__":
    main()
