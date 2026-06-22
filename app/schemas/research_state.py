from typing import TypedDict


class ResearchState(TypedDict):
    job_id: str

    query: str

    company: str
    ticker: str

    market_cap: str
    pe_ratio: str
    revenue: str
    risk_rating: str

    news_analysis: str
    financial_analysis: str
    competitor_analysis: str

    risk_analysis: str
    final_report: str

    recent_news: list