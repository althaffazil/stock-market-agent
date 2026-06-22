from app.services.gemini_service import get_llm
from app.prompts.news_prompt import NEWS_PROMPT
from app.tools.news_search import (
    search_company_news
)
from app.utils.llm_response import (
    extract_text
)

from app.services.progress_store import (
    update_progress
)
from app.tools.news_search import (
    search_company_news,
    get_news_items
)

llm = get_llm()


def news_agent_node(state):
    company = state["company"]

    print(
        f"[News Agent] Researching {company}"
    )

    news_data = search_company_news(
        company
    )
    news_items = get_news_items(company)
    response = llm.invoke(
        f"""
        {NEWS_PROMPT}

        Recent News:

        {news_data}
        """
    )

    print("[News Agent] Completed")

    update_progress(
    state["job_id"],
    "News Research Complete"
    )
    
    return {
        "news_analysis":
            extract_text(
                response.content
            ),

        "recent_news":
            news_items
    }