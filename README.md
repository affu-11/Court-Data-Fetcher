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
1. Input form to search for court cases
2. Displays key case details
3. Download link to latest order/judgment PDF
4. Raw HTML stored in SQLite for debugging or audit
5. Simple UI using Bootstrap

# Tech Stack
# Layer	                   Tool
1. Backend:               	Python, Flask
2. Web:                     Scraping	Playwright (or Requests + BeautifulSoup)
3. Frontend:	         HTML, Bootstrap
4. Database:	         SQLite

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
<img width="1451" height="465" alt="Screenshot 2025-08-10 121136" src="https://github.com/user-attachments/assets/dbc6c795-ef96-460d-a459-ad16bbdbf970" />


5. Run the app
python app.py
Visit http://127.0.0.1:5000 in your browser.
<img width="1462" height="747" alt="Screenshot 2025-08-10 120953" src="https://github.com/user-attachments/assets/3d84fe3f-dc0f-48d2-9f0f-55b33202b5ab" />



<img width="1920" height="1080" alt="Screenshot 2025-08-10 120714" src="https://github.com/user-attachments/assets/5ac6ec82-d961-47a4-8d23-6e97c5c33eeb" />


# Project Structure
court-data-fetcher/
   1.  app.py                  # Main Flask backend
   2.  scraper.py              # Web scraping logic
   3.  templates --->
         index.html          # Frontend form and result display
   4. cases.db                # SQLite database (auto-created)
   5. requirements.txt        # Python dependencies
   6. README.md               # Project documentation

# Demo Video
https://www.loom.com/share/b68eb30585234e55be4bbb081a431818?sid=e6bab454-6dc7-4b4c-98b9-7df50fd27e4b

# Future Improvements
1. Add captcha handling (if scraping more courts)
2. Support for multiple court websites (e.g., Faridabad, Mumbai)
3. Admin dashboard to view query logs
4. Export logs to CSV
 
# Disclaimer
This tool is built for educational/demo purposes. Court data may be subject to change, and scraping should comply with the target website's terms of use.

