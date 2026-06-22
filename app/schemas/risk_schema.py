from pydantic import BaseModel


class RiskAssessment(BaseModel):
    risk_rating: str