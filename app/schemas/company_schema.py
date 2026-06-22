from pydantic import BaseModel


class CompanyExtraction(BaseModel):
    company: str