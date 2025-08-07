import sqlite3

def log_query(case_type, case_number, case_year, raw_response):
    conn = sqlite3.connect('queries.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_type TEXT,
        case_number TEXT,
        case_year TEXT,
        raw_response TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')

    cur.execute('''INSERT INTO logs (case_type, case_number, case_year, raw_response)
                   VALUES (?, ?, ?, ?)''',
                (case_type, case_number, case_year, raw_response))
    conn.commit()
    conn.close()
