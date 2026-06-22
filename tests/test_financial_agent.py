from app.agents.financial_agent import financial_agent_node

state = {
    "company": "NVIDIA"
}

result = financial_agent_node(state)

print("\n=== FINANCIAL ANALYSIS ===\n")
print(result["financial_analysis"])