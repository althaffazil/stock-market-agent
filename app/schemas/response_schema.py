from pydantic import BaseModel


class AnalysisResponse(BaseModel):
    company: str
    ticker: str
    report: str