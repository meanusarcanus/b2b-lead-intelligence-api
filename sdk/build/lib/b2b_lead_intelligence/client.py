import requests
from typing import Dict, Any, Optional

def enrich_company(domain: str, base_url: str = "https://b2b-lead-intelligence-api.vercel.app") -> Dict[str, Any]:
    """Enrich company domain with firmographics and tech stack."""
    endpoint = f"{base_url.rstrip('/')}/api/v1/enrich-company"
    try:
        res = requests.post(endpoint, json={"domain": domain}, timeout=20)
        return res.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}

def find_executives(domain: str, department: str = "All", limit: int = 5, base_url: str = "https://b2b-lead-intelligence-api.vercel.app") -> Dict[str, Any]:
    """Find decision makers and verified corporate emails."""
    endpoint = f"{base_url.rstrip('/')}/api/v1/find-executives"
    try:
        res = requests.post(endpoint, json={"domain": domain, "department": department, "limit": limit}, timeout=20)
        return res.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_hiring_signals(domain: str, base_url: str = "https://b2b-lead-intelligence-api.vercel.app") -> Dict[str, Any]:
    """Get active job openings and hiring growth signals."""
    endpoint = f"{base_url.rstrip('/')}/api/v1/hiring-signals"
    try:
        res = requests.post(endpoint, json={"domain": domain}, timeout=20)
        return res.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}

class B2BLeadIntelligence:
    def __init__(self, api_key: Optional[str] = None, base_url: str = "https://b2b-lead-intelligence-api.vercel.app"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def enrich(self, domain: str) -> Dict[str, Any]:
        return enrich_company(domain, base_url=self.base_url)

    def get_leads(self, domain: str, department: str = "All", limit: int = 5) -> Dict[str, Any]:
        return find_executives(domain, department=department, limit=limit, base_url=self.base_url)

    def get_growth(self, domain: str) -> Dict[str, Any]:
        return get_hiring_signals(domain, base_url=self.base_url)
