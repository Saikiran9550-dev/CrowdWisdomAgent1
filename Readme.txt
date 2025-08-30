==============================
CrowdWisdomAgent
==============================

Project Overview:
-----------------
CrowdWisdomAgent is a Python-based multi-agent system built with CrewAI. 
It fetches SEC Form 4 filings (insider trading activity), compares recent activity 
over the last 24 hours with the prior week, and generates a report with charts.

The system is designed for internship assessment purposes and demonstrates 
skills in API integration, data processing, visualization, and agent-based workflows.

Features:
---------
1. Fetches real SEC Form 4 insider trading data (last 24 hours) using API (placeholder key: <YOUR_API_KEY_HERE>).
2. Fetches prior week's insider trading data.
3. Compares recent activity with prior week and summarizes insights.
4. Generates a bar chart: `insider_activity.png` for visual trends.
5. Creates a Markdown report: `insider_report.md` with analysis tables.
6. Implements CrewAI Agents and Flow for modular task assignment.
7. Uses placeholders for API keys for secure submission.

Setup Instructions:
------------------
1. Clone or download the repository into a folder:
   CrowdWisdomAgent/

2. Ensure Python 3.9+ is installed.

3. Create and activate a virtual environment (optional but recommended):
   Windows:
       python -m venv .venv
       .venv\Scripts\activate
   Linux/Mac:
       python3 -m venv .venv
       source .venv/bin/activate

4. Install required packages:
       pip install -r requirements.txt

5. Run the main script:
       python main.py

6. Output:
   - `insider_report.md` : Full report with insights and data tables
   - `insider_activity.png` : Bar chart of insider trades in last 24 hours

Requirements:
-------------
crewai>=0.28.0
litellm>=1.0.0
requests>=2.31.0
pandas>=2.0.0
matplotlib>=3.7.0
python-dotenv>=1.0.0

Notes:
------
- API keys are placeholders (`<YOUR_API_KEY_HERE>`). Real keys can be added to access live SEC data.
- The system is modular; additional agents can be added for more features.
- Designed to demonstrate practical skills for CrowdWisdomTrading internship assessment.

Submission:
-----------
- GitHub/GitLab repository link: [https://github.com/Saikiran9550-dev/CrowdWisdomAgent1.git]
- Sample outputs included:
  - `insider_report.md`
  - `insider_activity.png`

Author:
-------
Sai Kiran
BCA Intern Applicant

