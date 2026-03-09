import sqlite3

DB_PATH = "database/leads.db"

def save_leads(leads):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        website TEXT UNIQUE,
        status TEXT
    )
    """)

    for lead in leads:
        try:
            cursor.execute(
                "INSERT INTO leads (website, status) VALUES (?, ?)",
                (lead, "new")
            )
        except:
            pass

    conn.commit()
    conn.close()

    print("Leads saved to database")
