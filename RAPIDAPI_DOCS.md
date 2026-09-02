# 💼 B2B Company & Decision-Maker Lead Intelligence API — Documentation

Welcome to the **B2B Lead Intelligence Pro API** (Open-Source Apollo & Proxycurl Alternative). Engineered for AI SDRs, autonomous sales outreach bots, and recruiters to enrich company domains with firmographics, verified C-suite contact emails, and live hiring growth signals.

---

## ⚡ 1. Authentication & Headers

All requests to the RapidAPI endpoint require the standard RapidAPI authentication headers:

```http
x-rapidapi-key: YOUR_RAPIDAPI_KEY
x-rapidapi-host: b2b-lead-intelligence.p.rapidapi.com
Content-Type: application/json
```

---

## 🏢 2. Endpoint 1: Company Firmographics & Tech Stack (`POST /api/v1/enrich-company`)

Enriches any company domain with employee headcount tier, ARR revenue estimate, headquarters, and tech stack adoption tags.

### Request Body:
```json
{
  "domain": "stripe.com"
}
```

### Response Output:
```json
{
  "status": "success",
  "domain": "stripe.com",
  "company_name": "Stripe",
  "description": "Financial infrastructure for the internet.",
  "firmographics": {
    "industry": "Enterprise SaaS & Financial Technology",
    "headcount_tier": "500+ employees",
    "estimated_arr_tier": "$500M+ ARR",
    "founding_year": 2010,
    "headquarters": "San Francisco, CA, USA",
    "business_model": "B2B SaaS / Enterprise"
  },
  "tech_stack": {
    "total_detected": 5,
    "technologies": ["React", "Next.js", "AWS / Cloudflare", "Stripe", "PostgreSQL / Supabase"]
  },
  "social_profiles": {
    "linkedin": "https://www.linkedin.com/company/stripe",
    "twitter": "https://x.com/stripe",
    "github": "https://github.com/stripe"
  }
}
```

---

## 👤 3. Endpoint 2: Executive Decision-Maker Leads (`POST /api/v1/find-executives`)

Discovers key C-Level executives (CEO, CTO, VP Engineering, VP Sales) with verified corporate emails and confidence scores.

### Request Body:
```json
{
  "domain": "stripe.com",
  "department": "Engineering",
  "limit": 3
}
```

### Response Output:
```json
{
  "status": "success",
  "domain": "stripe.com",
  "company_name": "Stripe",
  "total_decision_makers_found": 2,
  "department_filter": "Engineering",
  "decision_makers": [
    {
      "name": "David Vance",
      "title": "Chief Technology Officer at Stripe",
      "department": "Engineering",
      "seniority": "C-Level",
      "company": "Stripe",
      "domain": "stripe.com",
      "email": "david@stripe.com",
      "email_confidence": 94,
      "deliverability": "Verified Deliverable",
      "linkedin_url": "https://www.linkedin.com/in/david-vance-stripe"
    },
    {
      "name": "Sarah Chen",
      "title": "VP of Engineering & Head of AI at Stripe",
      "department": "Engineering",
      "seniority": "VP",
      "company": "Stripe",
      "domain": "stripe.com",
      "email": "sarah@stripe.com",
      "email_confidence": 94,
      "deliverability": "Verified Deliverable",
      "linkedin_url": "https://www.linkedin.com/in/sarah-chen-stripe"
    }
  ]
}
```

---

## 📈 4. Endpoint 3: Hiring Signals & Growth Intent (`POST /api/v1/hiring-signals`)

Detects active job openings, department hiring surges, and buying intent.

### Request Body:
```json
{
  "domain": "stripe.com"
}
```

---

## 💻 5. Python Integration Example

```python
import requests

url = "https://b2b-lead-intelligence.p.rapidapi.com/api/v1/find-executives"

payload = {
    "domain": "stripe.com",
    "department": "Executive",
    "limit": 3
}

headers = {
    "x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
    "x-rapidapi-host": "b2b-lead-intelligence.p.rapidapi.com",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
data = response.json()

for leader in data["decision_makers"]:
    print(f"{leader['name']} ({leader['title']}) -> {leader['email']}")
```
