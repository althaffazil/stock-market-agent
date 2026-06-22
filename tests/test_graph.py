from app.graphs.research_graph import (
    build_graph
)

graph = build_graph()

result = graph.invoke(
    {
        "query": "Analyze Netflix stock"
    }
)

print(
    "\n=== FINAL REPORT ===\n"
)

print(
    result["final_report"]
)