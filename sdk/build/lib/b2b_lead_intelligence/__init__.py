"""
B2B Company & Decision-Maker Lead Intelligence SDK
Official Python client for real-time firmographics, executive contact discovery, and hiring intent.
"""

from .client import B2BLeadIntelligence, enrich_company, find_executives, get_hiring_signals

__version__ = "1.0.0"
__all__ = ["B2BLeadIntelligence", "enrich_company", "find_executives", "get_hiring_signals"]
