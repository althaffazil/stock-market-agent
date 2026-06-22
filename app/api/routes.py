from fastapi import APIRouter
from threading import Thread
from uuid import uuid4

from app.graphs.research_graph import build_graph

from app.schemas.request_schema import (
    AnalysisRequest
)

from app.services.progress_store import (
    get_progress
)

from app.services.company_search import (
    search_companies
)

from app.services.company_validator import (
    validate_company_and_ticker
)

router = APIRouter()

graph = build_graph()

results_store = {}


def run_analysis(
    job_id: str,
    company: str,
    ticker: str
):
    result = graph.invoke(
        {
            "job_id": job_id,

            "query": company,

            "company": company,
            "ticker": ticker,

            "market_cap": "",
            "pe_ratio": "",
            "revenue": "",
            "risk_rating": "",

            "news_analysis": "",
            "financial_analysis": "",
            "competitor_analysis": "",

            "risk_analysis": "",
            "final_report": "",

            "recent_news": []
        }
    )

    results_store[job_id] = result


@router.post("/analyze")
def analyze_company(
    request: AnalysisRequest
):

    job_id = str(uuid4())

    if not validate_company_and_ticker(
        request.company,
        request.ticker
    ):
        return {
            "status": "error",
            "message":
            "Please select a valid publicly traded company."
        }
        
    thread = Thread(
        target=run_analysis,
        args=(
            job_id,
            request.company,
            request.ticker
        )
    )

    thread.start()

    return {
        "status": "accepted",
        "job_id": job_id
    }

@router.get("/progress/{job_id}")
def progress(job_id: str):
    return {
        "steps": get_progress(job_id)
    }

@router.get("/search-companies")
def company_search(q: str):

    if len(q.strip()) < 2:
        return []

    return search_companies(q)

@router.get("/result/{job_id}")
def result(job_id: str):

    if job_id not in results_store:
        return {
            "status": "processing"
        }

    result = results_store[job_id]

    return {
        "status": "completed",

        "company":
        result["company"],

        "ticker":
        result["ticker"],

        "market_cap":
        result["market_cap"],

        "pe_ratio":
        result["pe_ratio"],

        "revenue":
        result["revenue"],

        "risk_rating":
        result["risk_rating"],

        "recent_news":
        result["recent_news"],

        "report":
        result["final_report"]
    }

