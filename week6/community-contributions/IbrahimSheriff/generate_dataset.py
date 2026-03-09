#!/usr/bin/env python3
"""Generate support_tickets.csv with 500 labeled support-style messages (synthetic)."""
import csv
import random

random.seed(42)

CATEGORIES = ["Billing", "Shipping", "Technical", "Refund", "Other"]

TEMPLATES = {
    "Billing": [
        "I was charged twice for my order #{}. Can you fix this?",
        "My invoice for {} is wrong. I need a correction.",
        "Why was I charged ${}? I didn't authorize this.",
        "I want to cancel my subscription. I'm still being billed.",
        "Please send me a copy of my invoice for last month.",
        "There's an unexpected charge of ${} on my account.",
        "I never received a refund for my cancelled order.",
        "My payment failed but the amount was deducted from my card.",
        "I need to update my payment method for my subscription.",
        "Can you explain the ${} fee on my last statement?",
        "I was overcharged for my order. Order ID: {}.",
        "When will my refund be processed? It's been 2 weeks.",
        "I need to dispute a charge from {}.",
        "My billing address is wrong. How do I change it?",
        "Why am I being charged a monthly fee I didn't sign up for?",
    ],
    "Shipping": [
        "My order hasn't arrived yet. It's been 2 weeks. Order #{}.",
        "Where is my package? Tracking says delivered but I didn't get it.",
        "I need to change the delivery address for my order.",
        "The package arrived damaged. What do I do?",
        "Can I get a tracking number for my shipment?",
        "My delivery was left at the wrong address.",
        "When will my order ship? I placed it {} days ago.",
        "I never received my order. Please resend.",
        "The shipping address is wrong. Order #{}. Can you update it?",
        "My package has been stuck in transit for a week.",
        "I need to cancel my order before it ships.",
        "Do you ship to international addresses?",
        "What are the shipping options for my region?",
        "The courier says they attempted delivery but I was home.",
        "My order was sent to the wrong city. Order #{}.",
    ],
    "Technical": [
        "I can't log in to my account. It says password invalid.",
        "The app keeps crashing when I open the settings.",
        "I forgot my password. How do I reset it?",
        "The website is not loading on my browser.",
        "I'm getting an error code {} when I try to checkout.",
        "My account is locked. How do I unlock it?",
        "The app won't let me upload my profile photo.",
        "I need help with two-factor authentication setup.",
        "The page keeps timing out when I submit the form.",
        "I can't receive the verification email. I checked spam.",
        "The mobile app is very slow after the last update.",
        "I get a 404 error when I click the link in your email.",
        "My session expires after 1 minute. Is that normal?",
        "The checkout button doesn't work on my phone.",
        "I want to delete my account. Where is the option?",
    ],
    "Refund": [
        "I want a refund for my order #{}.",
        "I need to return this item. How do I get my money back?",
        "I cancelled my order. When will I get the refund?",
        "Please process the refund for my returned item.",
        "I was told I'd get a refund but it hasn't appeared.",
        "Can I get a full refund? The product was defective.",
        "I need to return an item and get a refund. Order #{}.",
        "How long do refunds take to show up on my card?",
        "I want to cancel and get a refund before shipping.",
        "I returned the item 2 weeks ago. Where is my refund?",
        "The refund amount is wrong. I paid ${}.",
        "I'd like to request a refund for a duplicate charge.",
        "My refund was declined. Can you tell me why?",
        "I need a refund to my original payment method.",
        "Can I get a partial refund? The item was damaged.",
    ],
    "Other": [
        "I have a general question about your services.",
        "How do I contact the sales team?",
        "I want to know more about your return policy.",
        "Can you send me the terms and conditions?",
        "I need to update my email address on file.",
        "How do I change my account username?",
        "I'd like to speak to a manager please.",
        "Where can I find your privacy policy?",
        "I have feedback about your customer service.",
        "What are your business hours for support?",
        "I need to verify my identity. What documents do you need?",
        "Can I get a certificate of purchase for my order?",
        "I want to subscribe to your newsletter.",
        "How do I refer a friend to your service?",
        "I have a complaint I'd like to escalate.",
    ],
}

def main():
    rows = [{"message": "", "category": ""}]
    rows.clear()
    for category in CATEGORIES:
        templates = TEMPLATES[category]
        for i in range(100):
            t = templates[i % len(templates)]
            # Inject variation for placeholders
            if "${}" in t:
                msg = t.replace("${}", f"${random.randint(20, 200)}")
            elif "{}" in t:
                fill = random.randint(1000, 99999) if "#" in t or "Order" in t or "order" in t else random.randint(1, 30)
                msg = t.format(fill)
            else:
                msg = t
            rows.append({"message": msg, "category": category})
    random.shuffle(rows)
    path = "support_tickets.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["message", "category"])
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {len(rows)} rows to {path}")

if __name__ == "__main__":
    main()
