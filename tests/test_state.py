from app.schemas.research_state import ResearchState


def test_state():
    state: ResearchState = {
        "query": "Analyze NVIDIA",
        "company": "NVIDIA",
        "news_analysis": "",
        "financial_analysis": "",
        "competitor_analysis": "",
        "risk_analysis": "",
        "final_report": "",
    }

    print(state)


if __name__ == "__main__":
    test_state()