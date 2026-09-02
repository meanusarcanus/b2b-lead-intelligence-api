# 💼 B2B Company & Decision-Maker Lead Intelligence SDK

Official Python SDK for **B2B Lead Intelligence** (Open-Source Apollo & Proxycurl Alternative).

---

## ⚡ Quickstart

```bash
pip install b2b-lead-intelligence
```

```python
from b2b_lead_intelligence import enrich_company, find_executives, get_hiring_signals

# 1. Company Firmographics & Tech Stack
company = enrich_company("stripe.com")
print(f"Company: {company['company_name']} | Headcount: {company['firmographics']['headcount_tier']}")
print(f"Tech Stack: {company['tech_stack']['technologies']}")

# 2. Executive Decision-Maker Leads
leads = find_executives("stripe.com", department="Engineering", limit=3)
for exec in leads["decision_makers"]:
    print(f"{exec['name']} ({exec['title']}) -> {exec['email']} [Confidence: {exec['email_confidence']}%]")

# 3. Growth & Hiring Signals
growth = get_hiring_signals("stripe.com")
print(f"Growth Stage: {growth['growth_stage']} (Score: {growth['hiring_intent_score']}/100)")
```
