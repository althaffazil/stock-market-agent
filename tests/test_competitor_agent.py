from app.agents.competitor_agent import (
    competitor_agent_node
)

state = {
    "company": "NVIDIA"
}

result = competitor_agent_node(state)

print(
    "\n=== COMPETITOR ANALYSIS ===\n"
)

print(
    result["competitor_analysis"]
)