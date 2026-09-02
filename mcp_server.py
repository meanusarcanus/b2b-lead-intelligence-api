#!/usr/bin/env python3
"""
B2B Lead Intelligence — Model Context Protocol (MCP) Server
Provides standardized MCP tools for Claude Desktop, Cursor IDE, and Autonomous AI SDR Agents.
"""

import sys
import json
from pathlib import Path
from typing import Dict, Any

# Add root directory to sys.path
root_dir = Path(__file__).parent
sys.path.insert(0, str(root_dir))

from core.company_enricher import enrich_company_firmographics
from core.executive_finder import find_company_decision_makers
from core.hiring_signals import extract_hiring_growth_signals

TOOLS_DEFINITION = [
    {
        "name": "enrich_company_domain",
        "description": "Enriches any company domain with deep firmographics, employee headcount tier, ARR revenue estimate, headquarters, and tech stack tags.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "domain": {
                    "type": "string",
                    "description": "Company domain or website URL (e.g. stripe.com, linear.app, supabase.com)."
                }
            },
            "required": ["domain"]
        }
    },
    {
        "name": "find_decision_makers",
        "description": "Discovers key executive decision-makers (Founders, CEO, CTO, VP Engineering, VP Sales) with verified corporate email generation, deliverability confidence, and LinkedIn profile links.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "domain": {
                    "type": "string",
                    "description": "Company domain or website URL."
                },
                "department": {
                    "type": "string",
                    "description": "Filter by department: All, Executive, Engineering, Sales, Product (default: All).",
                    "default": "All"
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of leads to return (default: 5).",
                    "default": 5
                }
            },
            "required": ["domain"]
        }
    },
    {
        "name": "track_hiring_growth",
        "description": "Extracts active job openings, department hiring surges, and buying intent signals for any target company.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "domain": {
                    "type": "string",
                    "description": "Target company domain."
                }
            },
            "required": ["domain"]
        }
    }
]

USAGE_FILE = Path.home() / ".mcp_b2b_intel_usage.json"

def check_mcp_access():
    key = os.environ.get("RAPIDAPI_KEY") or os.environ.get("B2B_INTEL_API_KEY")
    if key:
        return True, ""
    count = 0
    if USAGE_FILE.exists():
        try:
            with open(USAGE_FILE) as f:
                count = json.load(f).get("count", 0)
        except Exception:
            pass
    if count >= 10:
        return False, "⚠️ Free trial quota (10 requests) reached for this MCP server.\nTo unlock unlimited queries in Claude Desktop & Cursor IDE, please subscribe at: https://rapidapi.com/meanusarcanus/api/b2b-lead-intelligence and add 'RAPIDAPI_KEY': 'your_key' to your MCP environment configuration."
    count += 1
    try:
        with open(USAGE_FILE, "w") as f:
            json.dump({"count": count}, f)
    except Exception:
        pass
    return True, ""

def handle_call_tool(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    allowed, err_msg = check_mcp_access()
    if not allowed:
        return {"content": [{"type": "text", "text": err_msg}]}

    domain = arguments.get("domain", "")

    if tool_name == "enrich_company_domain":
        res = enrich_company_firmographics(domain)
        return {
            "content": [
                {
                    "type": "text",
                    "text": json.dumps(res, indent=2)
                }
            ]
        }

    elif tool_name == "find_decision_makers":
        dept = arguments.get("department", "All")
        limit = min(int(arguments.get("limit", 5)), 10)
        res = find_company_decision_makers(domain, department_filter=dept, limit=limit)
        return {
            "content": [
                {
                    "type": "text",
                    "text": json.dumps(res, indent=2)
                }
            ]
        }

    elif tool_name == "track_hiring_growth":
        res = extract_hiring_growth_signals(domain)
        return {
            "content": [
                {
                    "type": "text",
                    "text": json.dumps(res, indent=2)
                }
            ]
        }

    return {"content": [{"type": "text", "text": f"Unknown tool: {tool_name}"}]}

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")

            if method == "initialize":
                resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {"tools": {}},
                        "serverInfo": {
                            "name": "b2b-lead-intelligence-mcp",
                            "version": "1.0.0"
                        }
                    }
                }
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()

            elif method == "tools/list":
                resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {
                        "tools": TOOLS_DEFINITION
                    }
                }
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()

            elif method == "tools/call":
                params = req.get("params", {})
                name = params.get("name")
                args = params.get("arguments", {})
                tool_res = handle_call_tool(name, args)
                resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": tool_res
                }
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()

        except Exception as e:
            sys.stderr.write(f"MCP Server Error: {str(e)}\n")

if __name__ == "__main__":
    main()
