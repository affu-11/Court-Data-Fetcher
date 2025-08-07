from flask import Flask, render_template, request
from scraper import fetch_case_data
import sqlite3
from datetime import datetime

app = Flask(__name__)

# DB setup
def init_db():
    conn = sqlite3.connect('cases.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            timestamp DATETIME,
            raw_response TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        case_type = request.form.get('case_type')
        case_number = request.form.get('case_number')
        filing_year = request.form.get('filing_year')

        try:
            result, raw_response = fetch_case_data(case_type, case_number, filing_year)

            # Log to SQLite
            conn = sqlite3.connect('cases.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO queries (case_type, case_number, filing_year, timestamp, raw_response)
                VALUES (?, ?, ?, ?, ?)
            ''', (case_type, case_number, filing_year, datetime.now(), raw_response))
            conn.commit()
            conn.close()

            return render_template('index.html', result=result)

        except Exception as e:
            return render_template('index.html', error=str(e))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
