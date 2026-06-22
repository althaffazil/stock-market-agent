from langgraph.graph import StateGraph
from langgraph.graph import END

from app.schemas.research_state import (
    ResearchState
)

from app.agents.coordinator import (
    coordinator_node
)

from app.agents.news_agent import (
    news_agent_node
)

from app.agents.financial_agent import (
    financial_agent_node
)

from app.agents.competitor_agent import (
    competitor_agent_node
)

from app.agents.risk_agent import (
    risk_agent_node
)

from app.agents.report_agent import (
    report_agent_node
)


def build_graph():

    graph = StateGraph(
        ResearchState
    )

    graph.add_node(
        "coordinator",
        coordinator_node
    )

    graph.add_node(
        "news",
        news_agent_node
    )

    graph.add_node(
        "financial",
        financial_agent_node
    )

    graph.add_node(
        "competitor",
        competitor_agent_node
    )

    graph.add_node(
        "risk",
        risk_agent_node
    )

    graph.add_node(
        "report",
        report_agent_node
    )

    graph.set_entry_point(
    "coordinator"
    )

    graph.add_edge(
        "coordinator",
        "news"
    )

    graph.add_edge(
        "coordinator",
        "financial"
    )

    graph.add_edge(
        "coordinator",
        "competitor"
    )

    graph.add_edge(
        "news",
        "risk"
    )

    graph.add_edge(
        "financial",
        "risk"
    )

    graph.add_edge(
        "competitor",
        "risk"
    )

    graph.add_edge(
        "risk",
        "report"
    )

    graph.add_edge(
        "report",
        END
    )

    return graph.compile()
