import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

# Add root directory to sys.path
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from core.company_enricher import enrich_company_firmographics
from core.executive_finder import find_company_decision_makers
from core.hiring_signals import extract_hiring_growth_signals

app = FastAPI(
    title="B2B Company & Decision-Maker Lead Intelligence Pro API",
    description="Real-time B2B firmographics, executive contact finder, verified business email extractor, and hiring signal intelligence for AI SDRs and sales automation.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

handler = app
application = app

# ==============================================================================
# Pydantic Schemas
# ==============================================================================
class CompanyEnrichRequest(BaseModel):
    domain: str = Field(..., example="stripe.com", description="Company domain name or website URL.")

class DecisionMakerRequest(BaseModel):
    domain: str = Field(..., example="stripe.com", description="Target company domain.")
    department: Optional[str] = Field(default="All", example="Engineering", description="Filter by department: All, Executive, Engineering, Sales, Product.")
    limit: Optional[int] = Field(default=5, example=5, description="Maximum number of leads to return.")

class HiringSignalRequest(BaseModel):
    domain: str = Field(..., example="stripe.com", description="Target company domain.")

# ==============================================================================
# API Endpoints
# ==============================================================================
@app.get("/api/v1/health")
def health_check():
    return {
        "status": "healthy",
        "service": "B2B Company & Decision-Maker Lead Intelligence Pro API",
        "version": "1.0.0",
        "supported_features": [
            "Company Firmographics & ARR Tier",
            "Tech Stack Adoption Scanner",
            "Decision Maker & Executive Contact Finder",
            "Verified Corporate Email Permutator",
            "Hiring Signals & Growth Monitor",
            "Model Context Protocol (MCP) Server"
        ]
    }

@app.post("/api/v1/enrich-company")
def enrich_company_endpoint(payload: CompanyEnrichRequest):
    """
    Enrich any company domain with firmographics, ARR estimate, headcount, and tech stack tags.
    """
    if not payload.domain.strip():
        raise HTTPException(status_code=400, detail="domain cannot be empty.")
    return enrich_company_firmographics(payload.domain.strip())

@app.get("/api/v1/enrich-company")
def enrich_company_get(
    domain: str = Query(..., examples=["stripe.com"], description="Company domain")
):
    """
    Quick GET endpoint for company firmographic enrichment.
    """
    if not domain.strip():
        raise HTTPException(status_code=400, detail="domain cannot be empty.")
    return enrich_company_firmographics(domain.strip())

@app.post("/api/v1/find-executives")
def find_executives_endpoint(payload: DecisionMakerRequest):
    """
    Discover key decision makers (Founders, C-Suite, VP Engineering, VP Sales) with verified emails.
    """
    if not payload.domain.strip():
        raise HTTPException(status_code=400, detail="domain cannot be empty.")
    limit = min(max(1, payload.limit or 5), 10)
    dept = payload.department or "All"
    return find_company_decision_makers(payload.domain.strip(), department_filter=dept, limit=limit)

@app.post("/api/v1/hiring-signals")
def hiring_signals_endpoint(payload: HiringSignalRequest):
    """
    Extract live hiring growth indicators and active job openings.
    """
    if not payload.domain.strip():
        raise HTTPException(status_code=400, detail="domain cannot be empty.")
    return extract_hiring_growth_signals(payload.domain.strip())
