import yfinance as yf


from app.services.gemini_service import get_llm
from app.prompts.financial_prompt import FINANCIAL_PROMPT
from app.utils.llm_response import (
    extract_text
)

from app.services.progress_store import (
    update_progress
)
from app.utils.formatters import (
    format_large_number
)


llm = get_llm()


def financial_agent_node(state):
    company = state["company"]

    ticker = state["ticker"]

    if not ticker:
        return {
            "financial_analysis": f"No ticker found for {company}"
        }

    print(f"[Financial Agent] Fetching data for {ticker}")

    stock = yf.Ticker(ticker)

    info = stock.info

    market_cap = info.get("marketCap")
    pe_ratio = info.get("trailingPE")
    revenue = info.get("totalRevenue")
    profit_margin = info.get("profitMargins")




    financial_data = f"""
    Company: {company}

    Market Cap: {market_cap}

    P/E Ratio: {pe_ratio}

    Revenue: {revenue}

    Profit Margin: {profit_margin}
    """

            # Add it here
    # print("\n=== RAW FINANCIAL DATA ===")
    # print(financial_data)
    # print("==========================\n")

    response = llm.invoke(
        f"""
        {FINANCIAL_PROMPT}

        Financial Data:

        {financial_data}
        """
    )

    print("[Financial Agent] Completed")

    update_progress(
    state["job_id"],
    "Financial Analysis Complete"
    )

    return {
        "financial_analysis": extract_text(
            response.content
        ),
        "market_cap":
        format_large_number(
            market_cap
        ),

        "pe_ratio": str(
            pe_ratio
        ),

        "revenue":
        format_large_number(
            revenue
        ),
    }