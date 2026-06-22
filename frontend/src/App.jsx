import { useState } from "react";
import ReactMarkdown from "react-markdown";
import "github-markdown-css/github-markdown.css";
import API from "./api";

function App() {
  const [query, setQuery] = useState("");

  const [loading, setLoading] = useState(false);

  const [progress, setProgress] = useState([]);

  const [error, setError] = useState("");

  const [report, setReport] = useState("");

  const [company, setCompany] = useState("");

  const [ticker, setTicker] = useState("");

  const [marketCap, setMarketCap] = useState("");

  const [peRatio, setPeRatio] = useState("");

  const [revenue, setRevenue] = useState("");

  const [riskRating, setRiskRating] = useState("");

  const [recentNews, setRecentNews] = useState([]);
  const [suggestions, setSuggestions] = useState([]);
  const [selectedTicker, setSelectedTicker] = useState("");

  const analyze = async () => {
    if (!selectedTicker) return;

    try {
      setLoading(true);

      setError("");

      setProgress([]);

      setReport("");
      setCompany("");
      setTicker("");

      setMarketCap("");
      setPeRatio("");
      setRevenue("");
      setRiskRating("");

      setRecentNews([]);

      const startResponse = await API.post("/analyze", {
        company: query,
        ticker: selectedTicker,
      });



      const jobId = startResponse.data.job_id;

      const interval = setInterval(async () => {
        try {
          const progressResponse = await API.get(`/progress/${jobId}`);

          setProgress(progressResponse.data.steps || []);

          const resultResponse = await API.get(`/result/${jobId}`);

          if (resultResponse.data.status === "completed") {
            clearInterval(interval);

            setCompany(resultResponse.data.company);

            setTicker(resultResponse.data.ticker);

            setMarketCap(resultResponse.data.market_cap);

            setPeRatio(resultResponse.data.pe_ratio);

            setRevenue(resultResponse.data.revenue);

            setRiskRating(resultResponse.data.risk_rating);

            setRecentNews(resultResponse.data.recent_news || []);

            setReport(resultResponse.data.report);
            setSuggestions([]);
            setLoading(false);
          }
        } catch (err) {
          console.error(err);
        }
      }, 2000);
    } catch (error) {
      console.error(error);

      setError("Something went wrong.");

      setLoading(false);
    }
  };

  const searchCompanies = async (value) => {
    setQuery(value);

    setSelectedTicker("");

    if (value.length < 2) {
      setSuggestions([]);
      return;
    }

    try {
      const response = await API.get(`/search-companies?q=${value}`);

      setSuggestions(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const riskBadgeClass = () => {
    switch (riskRating) {
      case "Low":
        return "bg-green-100 text-green-700";

      case "Moderate":
        return "bg-yellow-100 text-yellow-700";

      case "High":
        return "bg-red-100 text-red-700";

      default:
        return "bg-gray-100 text-gray-700";
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="max-w-6xl mx-auto p-8">
        {/* Header */}

        <h1 className="text-4xl font-bold mb-2">Stock Market Research Agent</h1>

        <p className="text-gray-600 mb-8">
          AI-Powered Equity Research & Investment Analysis
        </p>

        {/* Search */}
        {/* Search */}

        <div className="bg-white p-6 rounded-xl shadow">
          <div className="flex gap-4 items-start">
            
            <div className="flex-1 relative">

              <input
                value={query}
                onChange={(e) =>
                  searchCompanies(e.target.value)
                }
                placeholder="Search for companies..."
                className="w-full border rounded-lg p-3"
              />

              {suggestions.length > 0 && (
                <div
                  className="
                    absolute
                    top-full
                    left-0
                    right-0
                    mt-1
                    bg-white
                    border
                    rounded-lg
                    shadow-lg
                    z-50
                    max-h-72
                    overflow-y-auto
                  "
                >
                  {suggestions.map(
                    (companyItem, index) => (
                      <button
                        key={index}
                        type="button"
                        className="
                          block
                          w-full
                          text-left
                          px-4
                          py-3
                          hover:bg-gray-100
                          border-b
                          last:border-b-0
                        "
                        onClick={() => {
                          setQuery(
                            `${companyItem.name}`
                          );

                          setSelectedTicker(
                            companyItem.symbol
                          );

                          setSuggestions([]);
                        }}
                      >
                        <div className="font-medium">
                          {companyItem.name}
                        </div>

                        <div className="text-sm text-gray-500">
                          {companyItem.symbol}
                        </div>
                      </button>
                    )
                  )}
                </div>
              )}

            </div>

            <button
              onClick={analyze}
              disabled={
                loading ||
                !selectedTicker
              }
              className="
                px-6
                py-3
                bg-black
                text-white
                rounded-lg
                disabled:opacity-50
              "
            >
              {loading
                ? "Researching..."
                : "Analyze"}
            </button>

          </div>

          {selectedTicker && (
            <div className="mt-3">
              <span className="inline-flex items-center px-3 py-1 rounded-full bg-green-100 text-green-700 text-sm font-medium">
                ✓ {query} ({selectedTicker})
              </span>
            </div>
          )}

          {error && (
            <div className="mt-3 text-red-600">
              {error}
            </div>
          )}
        </div>


    
        {/* Progress */}

        {loading && (
          <div className="mt-6 bg-white rounded-xl shadow p-6">
            <h3 className="font-semibold mb-4">Analysis Progress</h3>

            <div className="space-y-3">
              {progress.map((step, index) => {
                const isLast = index === progress.length - 1;

                return (
                  <div
                    key={index}
                    className="
                        flex
                        items-center
                        gap-3
                      "
                  >
                    <div>{loading && isLast ? "⏳" : "✅"}</div>

                    <div>{step}</div>
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* Dashboard Cards */}

        {company && (
          <div
            className="
              grid
              grid-cols-2
              md:grid-cols-5
              gap-4
              mt-6
            "
          >
            <div className="bg-white p-4 rounded-xl shadow">
              <div className="text-sm text-gray-500">Company</div>

              <div className="font-bold mt-1">{company}</div>
            </div>

            <div className="bg-white p-4 rounded-xl shadow">
              <div className="text-sm text-gray-500">Ticker</div>

              <div className="font-bold mt-1">{ticker}</div>
            </div>

            <div className="bg-white p-4 rounded-xl shadow">
              <div className="text-sm text-gray-500">Market Cap</div>

              <div className="font-bold mt-1">{marketCap}</div>
            </div>

            <div className="bg-white p-4 rounded-xl shadow">
              <div className="text-sm text-gray-500">P/E Ratio</div>

              <div className="font-bold mt-1">{peRatio}</div>
            </div>

            <div className="bg-white p-4 rounded-xl shadow">
              <div className="text-sm text-gray-500">Risk Rating</div>

              <span
                className={`
                  inline-block
                  mt-2
                  px-3
                  py-1
                  rounded-full
                  text-sm
                  font-medium
                  ${riskBadgeClass()}
                `}
              >
                {riskRating}
              </span>
            </div>
          </div>
        )}

        {/* Recent News */}

        {recentNews.length > 0 && (
          <div className="mt-6 bg-white rounded-xl shadow p-6">
            <h3 className="font-semibold text-lg mb-4">Recent News</h3>

            <ul className="space-y-2">
              {recentNews.map((article, index) => (
                <li key={index}>
                  <a
                    href={article.url}
                    target="_blank"
                    rel="noreferrer"
                    className="
                        text-blue-600
                        hover:text-blue-800
                        hover:underline
                      "
                  >
                    {article.title}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Report */}

        {report && (
          <div className="mt-6 bg-white rounded-xl shadow overflow-hidden">
            <div className="markdown-body p-8">
              <ReactMarkdown>{report}</ReactMarkdown>
            </div>
          </div>
        )}

        {/* Footer */}

        <div className="mt-8 text-center text-sm text-gray-500">
          Powered by LangGraph • Gemini • Tavily • Yahoo Finance
        </div>
      </div>
    </div>
  );
}

export default App;
