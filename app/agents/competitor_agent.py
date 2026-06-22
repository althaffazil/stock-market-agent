from app.services.gemini_service import get_llm
from app.prompts.competitor_prompt import (
    COMPETITOR_PROMPT
)

from app.tools.competitor_mapper import (
    get_competitors
)

from app.utils.llm_response import (
    extract_text
)

from app.services.progress_store import (
    update_progress
)

llm = get_llm()


def competitor_agent_node(state):

    company = state["company"]

    competitors = get_competitors(
        company
    )

    competitor_text = (
        ", ".join(competitors)
        if competitors
        else "Determine the most relevant industry competitors"
    )

    print(
        f"[Competitor Agent] Comparing {company}"
    )

    response = llm.invoke(
        f"""
        {COMPETITOR_PROMPT}

        Target Company:
        {company}

        Primary Competitors:
        {competitor_text}

        Compare:

        - Market share
        - Technology leadership
        - Revenue scale
        - Growth opportunities
        - Competitive advantages
        - Strategic positioning
        """
    )

    print(
        "[Competitor Agent] Completed"
    )

    update_progress(
        state["job_id"],
        "Competitor Analysis Complete"
    )

    return {
        "competitor_analysis":
        extract_text(
            response.content
        )
    }