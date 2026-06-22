import yfinance as yf


def validate_company_and_ticker(
    company: str,
    ticker: str
) -> bool:

    try:

        results = yf.Search(company).quotes

        for item in results:

            symbol = item.get("symbol", "")

            if symbol.upper() == ticker.upper():
                return True

        return False

    except Exception:
        return False