from app.services.gemini_service import get_llm
from app.prompts.coordinator_prompt import COORDINATOR_PROMPT
from app.schemas.company_schema import CompanyExtraction

from app.services.progress_store import (
    update_progress
)
llm = get_llm()


def coordinator_node(state):
    query = state["query"]

    structured_llm = llm.with_structured_output(
        CompanyExtraction
    )

    response = structured_llm.invoke(
        f"""
        {COORDINATOR_PROMPT}

        Query:
        {query}
        """
    )

    company = response.company
    
    ticker = state["ticker"]
    company = state["company"]
    print(
        f"[Coordinator] {company} -> {ticker}"
    )

    job_id = state["job_id"]

    update_progress(
        job_id,
        "Company Identified"
    )
    return {
        "company": company,
        "ticker": ticker
    }