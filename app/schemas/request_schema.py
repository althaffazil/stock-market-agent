from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    company: str
    ticker: str