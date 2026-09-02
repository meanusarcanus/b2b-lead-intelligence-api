"""
Apify Actor Entrypoint: B2B Company & Decision-Maker Lead Intelligence Pro
Enriches target company domains and pushes structured firmographics & executive contacts to Apify dataset.
"""

import asyncio
from core.company_enricher import enrich_company_firmographics
from core.executive_finder import find_company_decision_makers
from core.hiring_signals import extract_hiring_growth_signals

try:
    from apify import Actor
except ImportError:
    class Actor:
        @staticmethod
        async def init(): pass
        @staticmethod
        async def exit(): pass
        @staticmethod
        async def get_input():
            return {
                "company_domains": ["stripe.com", "linear.app", "supabase.com"],
                "extract_decision_makers": True,
                "max_leads_per_company": 5
            }
        @staticmethod
        async def push_data(data):
            print(f"[Apify Dataset Push] Pushed item.")

async def main():
    async with Actor:
        actor_input = await Actor.get_input() or {}
        domains = actor_input.get("company_domains", [])
        extract_leads = actor_input.get("extract_decision_makers", True)
        limit = min(int(actor_input.get("max_leads_per_company", 5)), 10)

        if isinstance(domains, str):
            domains = [d.strip() for d in domains.splitlines() if d.strip()]

        print(f"🚀 Enriching {len(domains)} company domains with executive intelligence...")

        total_enriched = 0
        for domain in domains:
            if not domain:
                continue
            firmographics = enrich_company_firmographics(domain)
            leads_data = find_company_decision_makers(domain, limit=limit) if extract_leads else {"decision_makers": []}
            hiring_data = extract_hiring_growth_signals(domain)

            merged_record = {
                "domain": firmographics["domain"],
                "company_name": firmographics["company_name"],
                "description": firmographics["description"],
                "firmographics": firmographics["firmographics"],
                "tech_stack": firmographics["tech_stack"],
                "social_profiles": firmographics["social_profiles"],
                "decision_makers": leads_data.get("decision_makers", []),
                "growth_signals": hiring_data.get("growth_signals", []),
                "active_job_listings": hiring_data.get("active_job_listings", [])
            }

            await Actor.push_data(merged_record)
            total_enriched += 1

        print(f"✅ Enriched {total_enriched} companies successfully.")

if __name__ == "__main__":
    asyncio.run(main())
