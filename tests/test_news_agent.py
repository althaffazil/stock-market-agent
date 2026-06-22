from app.agents.news_agent import news_agent_node

state = {
    "company": "NVIDIA"
}

result = news_agent_node(state)

print("\n=== NEWS ANALYSIS ===\n")
print(result["news_analysis"])