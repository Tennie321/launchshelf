#!/usr/bin/env python3
"""
Analytics — Track page visits from server logs (basic).

Reads a log file, extracts unique visitors, page views, and top pages.
Outputs a summary report.

Usage:
    python3 analytics.py /path/to/access.log
"""

import re
import sys
from collections import Counter
from datetime import datetime


LOG_PATTERN = re.compile(
    r'(?P<ip>\S+)\s+\S+\s+\S+\s+\[(?P<time>[^\]]+)\]\s+'
    r'"(?P<method>\S+)\s+(?P<path>\S+)\s+\S+"\s+'
    r'(?P<status>\d+)\s+(?P<size>\d+|-)'
)


def parse_log(filepath: str) -> dict:
    """Parse a log file and return stats."""
    ips = []
    paths = []
    statuses = []
    total = 0

    with open(filepath, "r") as f:
        for line in f:
            match = LOG_PATTERN.search(line)
            if match:
                ips.append(match.group("ip"))
                paths.append(match.group("path"))
                statuses.append(int(match.group("status")))
                total += 1

    return {
        "total_requests": total,
        "unique_visitors": len(set(ips)),
        "page_views": dict(Counter(paths).most_common(10)),
        "status_codes": dict(Counter(statuses)),
        "top_ips": dict(Counter(ips).most_common(5)),
    }


def print_report(stats: dict):
    """Print a formatted report."""
    print("📊 LaunchShelf Analytics Report")
    print(f"   Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()
    print(f"   Total requests:    {stats['total_requests']}")
    print(f"   Unique visitors:   {stats['unique_visitors']}")
    print()
    print("   Top Pages:")
    for path, count in stats.get("page_views", {}).items():
        print(f"     {path:40s} {count}")
    print()
    print("   Status Codes:")
    for code, count in stats.get("status_codes", {}).items():
        print(f"     {code}: {count}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 analytics.py <logfile>")
        sys.exit(1)

    stats = parse_log(sys.argv[1])
    print_report(stats)


if __name__ == "__main__":
    main()
