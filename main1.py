# main.py
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from crewai import Agent, Flow, tools

# -------------------------------
# Data fetching functions
# -------------------------------
@tools.tool
def fetch_sec_data(api_key="<YOUR_API_KEY_HERE>"):
    """Fetch SEC Form 4 filings in last 24 hours."""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=1)
    
    url = "https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json"  # Example placeholder
    headers = {
        "User-Agent": "CrowdWisdomInternAgent/1.0",
        "Authorization": f"Bearer {api_key}"
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    filings = []
    for item in data.get("filings", {}).get("recent", []):
        filing_date = item.get("filingDate")
        if filing_date:
            filing_date_obj = datetime.strptime(filing_date, "%Y-%m-%d")
            if start_date <= filing_date_obj <= end_date:
                filings.append({
                    "company": item.get("companyName", "Unknown"),
                    "insider": item.get("insiderName", "Unknown"),
                    "transaction": item.get("transactionCode", ""),
                    "date": filing_date_obj,
                    "shares": item.get("transactionShares", 0),
                    "price": item.get("transactionPricePerShare", 0)
                })
    return pd.DataFrame(filings)

@tools.tool
def fetch_prior_week_data(api_key="<YOUR_API_KEY_HERE>"):
    """Fetch prior 7 days of insider trading data."""
    end_date = datetime.now() - timedelta(days=1)
    start_date = end_date - timedelta(days=7)
    
    url = "https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json"
    headers = {
        "User-Agent": "CrowdWisdomInternAgent/1.0",
        "Authorization": f"Bearer {api_key}"
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    filings = []
    for item in data.get("filings", {}).get("recent", []):
        filing_date = item.get("filingDate")
        if filing_date:
            filing_date_obj = datetime.strptime(filing_date, "%Y-%m-%d")
            if start_date <= filing_date_obj <= end_date:
                filings.append({
                    "company": item.get("companyName", "Unknown"),
                    "insider": item.get("insiderName", "Unknown"),
                    "transaction": item.get("transactionCode", ""),
                    "date": filing_date_obj,
                    "shares": item.get("transactionShares", 0),
                    "price": item.get("transactionPricePerShare", 0)
                })
    return pd.DataFrame(filings)

# -------------------------------
# Agents
# -------------------------------
sec_agent = Agent(
    name="SEC Agent",
    tools=[fetch_sec_data, fetch_prior_week_data],
    role="Analyst",
    goal="Fetch and compare insider trading activity.",
    backstory="Handles all SEC Form 4 filings and analysis."
)

# -------------------------------
# Report & Chart
# -------------------------------
def generate_report(today_df, prior_df):
    if today_df.empty:
        print("No filings in last 24 hours.")
        return

    # Chart
    plt.figure(figsize=(10,6))
    plt.bar(today_df['insider'], today_df['shares'])
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Shares")
    plt.title("Insider Trades Last 24 Hours")
    plt.tight_layout()
    plt.savefig("insider_activity.png")
    plt.close()
    
    # Markdown report
    report_lines = [
        "# Insider Trading Report",
        f"Generated on: {datetime.now()}",
        "\n## Last 24 Hours Activity\n",
        today_df.to_markdown(index=False),
        "\n## Comparison with Prior Week\n"
    ]
    combined = pd.concat([prior_df, today_df])
    summary = combined.groupby("insider")[["shares"]].sum().reset_index()
    report_lines.append(summary.to_markdown(index=False))
    
    with open("insider_report.md", "w") as f:
        f.write("\n".join(report_lines))
    print("Report and chart generated: insider_report.md & insider_activity.png")

# -------------------------------
# CrewAI Flow
# -------------------------------
flow = Flow(
    name="Insider Trading Flow",
    agents=[sec_agent],
    goal="Fetch SEC data, compare with prior week, generate report with chart."
)

def main():
    today_df = fetch_sec_data()
    prior_df = fetch_prior_week_data()
    generate_report(today_df, prior_df)
    print("CrowdWisdomAgent completed!")

if __name__ == "__main__":
    main()
