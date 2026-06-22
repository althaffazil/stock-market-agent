from app.agents.coordinator import coordinator_node


state = {
    "query": "Analyze Tesla"
}

result = coordinator_node(state)

print(result)