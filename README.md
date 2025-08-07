# Court-Data-Fetcher
Flask app that fetches Delhi High Court case info using Playwright, stores it in SQLite, and displays parsed results via a simple dashboard.
# Court-Data Fetcher & Mini-Dashboard

# Objective
A lightweight web application that lets users search Indian court case details (like parties involved, filing date, next hearing date, and download the latest order/judgment) by entering:
         Case Type
         Case Number
         Filing Year
The app uses a backend scraper (e.g., Playwright or Requests+BeautifulSoup) to fetch data from the Delhi High Court portal or an eCourts website and stores logs in a SQLite database.

# Features
Input form to search for court cases
Displays key case details
Download link to latest order/judgment PDF
Raw HTML stored in SQLite for debugging or audit
Simple UI using Bootstrap
Tech Stack

# Layer	                   # Tool
Backend                	Python, Flask
Web                     Scraping	Playwright (or Requests + BeautifulSoup)
Frontend	              HTML, Bootstrap
Database	              SQLite


# How to Run
1. Clone the repository
git clone https://github.com/your-username/court-data-fetcher.git
cd court-data-fetcher

2. Set up virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run the app
python app.py
Visit http://127.0.0.1:5000 in your browser.

# Project Structure
court-data-fetcher/
│
├── app.py                  # Main Flask backend
├── scraper.py              # Web scraping logic
├── templates/
│   └── index.html          # Frontend form and result display
├── cases.db                # SQLite database (auto-created)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

# Demo Video
https://www.loom.com/share/b68eb30585234e55be4bbb081a431818?sid=e6bab454-6dc7-4b4c-98b9-7df50fd27e4b

# Future Improvements
Add captcha handling (if scraping more courts)
Support for multiple court websites (e.g., Faridabad, Mumbai)
Admin dashboard to view query logs
Export logs to CSV
 
# Disclaimer
This tool is built for educational/demo purposes. Court data may be subject to change, and scraping should comply with the target website's terms of use.

