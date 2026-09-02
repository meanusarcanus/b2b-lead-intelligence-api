import requests
from typing import Dict, Any, Optional

def enrich_company(domain: str, rapidapi_key: Optional[str] = None, base_url: Optional[str] = None) -> Dict[str, Any]:
    url = f"{base_url or 'https://b2b-lead-intelligence.p.rapidapi.com'}/api/v1/enrich-company"
    headers = {"Content-Type": "application/json"}
    if rapidapi_key:
        headers["x-rapidapi-key"] = rapidapi_key
        headers["x-rapidapi-host"] = "b2b-lead-intelligence.p.rapidapi.com"
    try:
        res = requests.post(url, json={"domain": domain}, headers=headers, timeout=20)
        return res.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}

def find_executives(domain: str, department: str = "All", limit: int = 5, rapidapi_key: Optional[str] = None, base_url: Optional[str] = None) -> Dict[str, Any]:
    url = f"{base_url or 'https://b2b-lead-intelligence.p.rapidapi.com'}/api/v1/find-executives"
    headers = {"Content-Type": "application/json"}
    if rapidapi_key:
        headers["x-rapidapi-key"] = rapidapi_key
        headers["x-rapidapi-host"] = "b2b-lead-intelligence.p.rapidapi.com"
    try:
        res = requests.post(url, json={"domain": domain, "department": department, "limit": limit}, headers=headers, timeout=20)
        return res.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_hiring_signals(domain: str, rapidapi_key: Optional[str] = None, base_url: Optional[str] = None) -> Dict[str, Any]:
    url = f"{base_url or 'https://b2b-lead-intelligence.p.rapidapi.com'}/api/v1/hiring-signals"
    headers = {"Content-Type": "application/json"}
    if rapidapi_key:
        headers["x-rapidapi-key"] = rapidapi_key
        headers["x-rapidapi-host"] = "b2b-lead-intelligence.p.rapidapi.com"
    try:
        res = requests.post(url, json={"domain": domain}, headers=headers, timeout=20)
        return res.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}

class B2BLeadIntelligence:
    def __init__(self, rapidapi_key: Optional[str] = None, base_url: Optional[str] = None):
        self.rapidapi_key = rapidapi_key
        self.base_url = base_url or "https://b2b-lead-intelligence.p.rapidapi.com"

    def enrich(self, domain: str) -> Dict[str, Any]:
        return enrich_company(domain, rapidapi_key=self.rapidapi_key, base_url=self.base_url)

    def get_leads(self, domain: str, department: str = "All", limit: int = 5) -> Dict[str, Any]:
        return find_executives(domain, department=department, limit=limit, rapidapi_key=self.rapidapi_key, base_url=self.base_url)

    def get_growth(self, domain: str) -> Dict[str, Any]:
        return get_hiring_signals(domain, rapidapi_key=self.rapidapi_key, base_url=self.base_url)
