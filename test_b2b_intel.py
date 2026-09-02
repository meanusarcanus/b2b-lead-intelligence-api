"""
Automated Verification Suite for B2B Company & Decision-Maker Lead Intelligence Pro
Tests company firmographics, executive lead extraction, email deliverability scores, and FastAPI server.
"""

import sys
from pathlib import Path

# Add root directory to sys.path
root_dir = Path(__file__).parent
sys.path.insert(0, str(root_dir))

from core.company_enricher import clean_domain, enrich_company_firmographics
from core.executive_finder import generate_verified_emails, find_company_decision_makers
from core.hiring_signals import extract_hiring_growth_signals
from api.index import (
    app,
    CompanyEnrichRequest,
    enrich_company_endpoint,
    DecisionMakerRequest,
    find_executives_endpoint,
    HiringSignalRequest,
    hiring_signals_endpoint
)

def run_tests():
    print("=" * 65)
    print(" 💼 TESTING B2B COMPANY & EXECUTIVE LEAD INTELLIGENCE")
    print("=" * 65)

    # Test 1: Domain Cleaner
    print("\n[Test 1] Domain Cleaner & Normalizer...")
    assert clean_domain("https://www.stripe.com/pricing") == "stripe.com"
    assert clean_domain("linear.app") == "linear.app"
    print("✓ Domain cleaner passed!")

    # Test 2: Firmographic & Tech Stack Enrichment
    print("\n[Test 2] Company Firmographics & Tech Stack Enrichment...")
    res = enrich_company_firmographics("stripe.com")
    print(f"✓ Company: {res['company_name']}")
    print(f"✓ Headcount Tier: {res['firmographics']['headcount_tier']}")
    print(f"✓ Estimated ARR: {res['firmographics']['estimated_arr_tier']}")
    print(f"✓ Tech Stack ({res['tech_stack']['total_detected']} tools): {res['tech_stack']['technologies']}")
    assert res["status"] == "success"
    assert res["domain"] == "stripe.com"
    assert len(res["tech_stack"]["technologies"]) > 0

    # Test 3: Executive Lead Finder & Verified Email Generator
    print("\n[Test 3] Executive Lead Finder & Email Permutator...")
    email_data = generate_verified_emails("alex", "mercer", "stripe.com")
    print(f"✓ Primary Email: {email_data['primary_email']} (Confidence: {email_data['confidence_score']}%)")
    print(f"✓ Deliverability: {email_data['deliverability_status']}")
    assert email_data["primary_email"] == "alex@stripe.com"
    assert email_data["confidence_score"] >= 90

    leads = find_company_decision_makers("stripe.com", department_filter="Engineering", limit=2)
    print(f"✓ Total Leads Found: {leads['total_decision_makers_found']}")
    for l in leads["decision_makers"]:
        print(f"  - {l['name']} | {l['title']} | Email: {l['email']}")
    assert leads["status"] == "success"
    assert len(leads["decision_makers"]) == 2

    # Test 4: Hiring Signals & Growth Intent
    print("\n[Test 4] Hiring Signals & Department Growth...")
    growth = extract_hiring_growth_signals("stripe.com")
    print(f"✓ Hiring Intent Score: {growth['hiring_intent_score']}/100 ({growth['growth_stage']})")
    print(f"✓ Open Roles: {growth['total_active_openings']}")
    assert growth["status"] == "success"
    assert growth["hiring_intent_score"] > 80

    # Test 5: FastAPI Serverless Endpoints
    print("\n[Test 5] FastAPI Endpoints (/api/v1/enrich-company, /api/v1/find-executives)...")
    enrich_req = CompanyEnrichRequest(domain="stripe.com")
    api_enrich = enrich_company_endpoint(enrich_req)
    assert api_enrich["status"] == "success"
    print("✓ POST /api/v1/enrich-company: 200 OK")

    exec_req = DecisionMakerRequest(domain="stripe.com", department="All", limit=3)
    api_exec = find_executives_endpoint(exec_req)
    assert api_exec["status"] == "success"
    assert len(api_exec["decision_makers"]) == 3
    print("✓ POST /api/v1/find-executives: 200 OK")

    print("\n" + "=" * 65)
    print(" 🎉 ALL B2B LEAD INTELLIGENCE TESTS PASSED 100%!")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    run_tests()
