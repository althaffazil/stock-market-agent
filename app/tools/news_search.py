from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_company_news(company: str):
    response = client.search(
        query=f"{company} latest business news",
        max_results=5
    )

    results = []

    for item in response["results"]:
        title = item.get("title", "")
        content = item.get("content", "")

        results.append(
            f"Title: {title}\n"
            f"Content: {content}"
        )

    return "\n\n".join(results)

def get_news_items(company):
    response = client.search(
        query=f"{company} latest business news",
        max_results=5
    )

    items = []

    for result in response["results"]:
        items.append(
            {
                "title":
                result.get(
                    "title",
                    ""
                ),

                "url":
                result.get(
                    "url",
                    ""
                )
            }
        )

    return items