from app.services.gemini_service import get_llm
from app.prompts.report_prompt import REPORT_PROMPT

from app.utils.llm_response import (
    extract_text
)

from app.services.progress_store import (
    update_progress
)

llm = get_llm()


def report_agent_node(state):

    update_progress(
        state["job_id"],
        "Building Final Report"
    )

    company = state["company"]

    print(
        f"[Report Agent] Building report for {company}"
    )

    response = llm.invoke(
        f"""
        {REPORT_PROMPT}

        Company:
        {company}

        News Analysis:
        {state.get("news_analysis", "")}

        Financial Analysis:
        {state.get("financial_analysis", "")}

        Competitor Analysis:
        {state.get("competitor_analysis", "")}

        Risk Analysis:
        {state.get("risk_analysis", "")}
        """
    )

    print("[Report Agent] Completed")

    update_progress(
        state["job_id"],
        "Completed"
    )

    return {
        "final_report": extract_text(
            response.content
        )
    }