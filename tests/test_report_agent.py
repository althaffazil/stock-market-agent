from app.agents.report_agent import (
    report_agent_node
)

state = {
    "company": "NVIDIA",

    "news_analysis":
        "NVIDIA continues expanding AI partnerships.",

    "financial_analysis":
        "Revenue growth remains strong with high margins.",

    "competitor_analysis":
        "NVIDIA leads AMD and Intel in AI accelerators.",

    "risk_analysis":
        "Valuation remains the primary risk."
}

result = report_agent_node(state)

print("\n=== FINAL REPORT ===\n")

print(result["final_report"])