# 💼 B2B Company & Decision-Maker Lead Intelligence MCP Pro (Apollo / Proxycurl Alternative)

[![MCP Protocol](https://img.shields.io/badge/MCP-Model_Context_Protocol-blue.svg)](https://modelcontextprotocol.io/)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Glama](https://img.shields.io/badge/Glama-MCP_Server-purple.svg)](https://glama.ai/mcp/servers)

An enterprise-grade **Model Context Protocol (MCP) Server** and live B2B firmographics engine that equips **Claude Desktop, Cursor IDE, LangChain, and AI SDR sales agents** with real-time company intelligence, executive contact emails, and hiring growth signals.

<p align="center">
  <img src="https://raw.githubusercontent.com/meanusarcanus/b2b-lead-intelligence-api/master/assets/logo.jpg" alt="B2B Lead Intelligence Logo" width="180" style="border-radius: 20px;" />
</p>

---

## ⚡ Overview

**B2B Lead Intelligence Pro** is a high-speed, cost-efficient alternative to Apollo, ZoomInfo, and Proxycurl. It enriches any domain with employee headcount tiers, estimated ARR ranges, technology adoption stacks, verified C-level executive contact emails, and active hiring growth signals.

* 🏢 **Deep Firmographics & Tech Stack**: Extracts headcount tiers (`1-10`, `11-50`, `51-200`, `201-500`, `500+`), ARR estimates, and technology adoption (Cloud, AI/ML, CRM, Databases).
* 👤 **Executive Decision-Maker Discovery**: Discovers Founders, CEOs, CTOs, VP of Engineering, and Head of Sales with verified corporate emails and confidence scores.
* 📈 **Hiring Signals & Growth Intent**: Detects active job openings and department expansion trends.
* 🔌 **Zero-Config MCP Integration**: Plug-and-play with Claude Desktop, Cursor, and Antigravity agents.

---

## 🛠️ MCP Tools & Capabilities

The server exposes the following Model Context Protocol (MCP) tools:

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **`enrich_company_domain`** | `domain` *(string, required)* | Enriches any company domain with deep firmographics, headcount tier, ARR estimate, headquarters, and tech stack tags. |
| **`find_decision_makers`** | `domain` *(string, required)*, `department` *(string)*, `limit` *(int)* | Discovers executive decision-makers (C-Level, VP Engineering, VP Sales) with verified corporate emails and LinkedIn profiles. |
| **`track_hiring_growth`** | `domain` *(string, required)* | Extracts active job openings, department expansion surges, and buying intent signals. |

---

## 🔌 Quickstart: Connect to Claude Desktop & Cursor

### 1. Claude Desktop Configuration
Add this server to your `claude_desktop_config.json`:

* **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
* **Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "b2b-lead-intelligence": {
      "command": "python3",
      "args": [
        "/path/to/b2b-lead-intelligence-api/mcp_server.py"
      ]
    }
  }
}
```

### 2. Cursor IDE Configuration (`.cursor/mcp.json`)
```json
{
  "mcpServers": {
    "b2b-lead-intelligence": {
      "command": "python3",
      "args": ["/path/to/b2b-lead-intelligence-api/mcp_server.py"]
    }
  }
}
```

---

## 📦 Python SDK & CLI Usage

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
```

---

## 🌐 Serverless REST API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/v1/enrich-company` | Deep company firmographics, ARR tier, headcount, and tech stack. |
| `POST` | `/api/v1/find-executives` | Executive decision-maker contact extraction with verified corporate emails. |
| `POST` | `/api/v1/hiring-signals` | Department growth indicators and active job openings. |
| `GET` | `/api/v1/health` | Service health status and supported capabilities. |

---

## 📄 License
MIT License. Created by Meanus Arcanus.
