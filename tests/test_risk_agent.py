from app.agents.risk_agent import (
    risk_agent_node
)

state = {
    "company": "NVIDIA",

    "news_analysis":
        "NVIDIA continues expanding AI partnerships.",

    "financial_analysis":
        "Revenue growth remains strong with high margins.",

    "competitor_analysis":
        "AMD and Intel remain primary competitors."
}

result = risk_agent_node(state)

print("\n=== RISK ANALYSIS ===\n")

print(result["risk_analysis"])