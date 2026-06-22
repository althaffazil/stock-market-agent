from pydantic import BaseModel


class TickerExtraction(BaseModel):
    ticker: str