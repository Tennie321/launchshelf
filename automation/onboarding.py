#!/usr/bin/env python3
"""
Onboarding — Auto-sends welcome email + product access.

Requires SMTP credentials configured via environment variables:
    SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS

Usage:
    export SMTP_HOST=smtp.gmail.com
    export SMTP_PORT=587
    export SMTP_USER=your@email.com
    export SMTP_PASS=your-app-password

    python3 onboarding.py newcustomer@example.com "Jane Doe"
"""

import os
import smtplib
import sys
from email.message import EmailMessage
from datetime import datetime


def send_welcome(customer_email: str, customer_name: str) -> bool:
    """Send a welcome email with product access instructions."""

    subject = "Welcome to LaunchShelf! 🚀"

    body = f"""Hi {customer_name},

Welcome to LaunchShelf! Here's everything you need to get started:

📥 YOUR DOWNLOAD LINK
https://launchshelf.co/download?email={customer_email}

📋 QUICK START
1. Open README.md for the full setup guide
2. Start with the book outline generator (product/01-book-outline.md)
3. Follow the 30-day planner to schedule your writing

💬 QUESTIONS?
Reply to this email or use the LaunchShelf support form.

Happy writing!
The LaunchShelf Team
"""

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = os.environ.get("SMTP_USER", "hello@launchshelf.co")
    msg["To"] = customer_email

    try:
        host = os.environ["SMTP_HOST"]
        port = int(os.environ.get("SMTP_PORT", 587))
        user = os.environ["SMTP_USER"]
        pwd = os.environ["SMTP_PASS"]

        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(user, pwd)
            server.send_message(msg)

        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 onboarding.py <email> <name>")
        print("Example: python3 onboarding.py jane@example.com 'Jane Doe'")
        sys.exit(1)

    email = sys.argv[1]
    name = sys.argv[2]

    print(f"📧 Sending welcome to {name} <{email}>...")
    success = send_welcome(email, name)

    if success:
        log_entry(email, name)
        print(f"✅ Welcome email sent to {email}")
    else:
        print(f"❌ Failed to send welcome email")
        sys.exit(1)


def log_entry(email: str, name: str):
    """Log the onboarding to a CSV file."""
    timestamp = datetime.now().isoformat()
    with open("onboarding_log.csv", "a") as f:
        f.write(f"{timestamp},{email},{name}\n")
    print(f"   Logged to onboarding_log.csv")


if __name__ == "__main__":
    main()
