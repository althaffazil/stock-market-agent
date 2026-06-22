from app.services.gemini_service import get_llm
from app.prompts.risk_prompt import RISK_PROMPT

from app.utils.llm_response import (
    extract_text
)

from app.services.progress_store import (
    update_progress
)

from app.schemas.risk_schema import (
    RiskAssessment
)

llm = get_llm()


def risk_agent_node(state):

    company = state["company"]

    news_analysis = state.get(
        "news_analysis",
        ""
    )

    financial_analysis = state.get(
        "financial_analysis",
        ""
    )

    competitor_analysis = state.get(
        "competitor_analysis",
        ""
    )

    print(
        f"[Risk Agent] Analyzing risks for {company}"
    )

    response = llm.invoke(
        f"""
        {RISK_PROMPT}

        Company:
        {company}

        News Analysis:
        {news_analysis}

        Financial Analysis:
        {financial_analysis}

        Competitor Analysis:
        {competitor_analysis}
        """
    )

    risk_analysis = extract_text(
        response.content
    )

    structured_llm = (
        llm.with_structured_output(
            RiskAssessment
        )
    )

    risk_result = structured_llm.invoke(
        f"""
        Based on the following risk analysis,
        classify the overall company risk as exactly one of:

        Low
        Moderate
        High

        Risk Analysis:

        {risk_analysis}

        Return only the rating.
        """
    )

    rating = (
        risk_result.risk_rating
        .strip()
        .title()
    )

    print(
        f"[Risk Agent] Risk Rating: {rating}"
    )

    update_progress(
        state["job_id"],
        "Risk Assessment Complete"
    )

    print("[Risk Agent] Completed")

    return {
        "risk_analysis": risk_analysis,
        "risk_rating": rating
    }