import yfinance as yf


def search_companies(query: str):

    try:
        results = yf.Search(query).quotes

        companies = []

        for item in results[:8]:

            symbol = item.get("symbol")
            name = item.get("shortname")

            if symbol and name:

                companies.append(
                    {
                        "symbol": symbol,
                        "name": name,
                    }
                )

        return companies

    except Exception:
        return []