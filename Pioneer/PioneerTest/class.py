import sqlite3

class ExpenseTracker:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        sql = CREATE expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            amount REAL,
            category TEXT,
            description TEXT
        )
        
        self.conn.execute(sql)
        self.conn.commit()

    def add_expense(self, date, amount, category, description):
        sql = "INSERT INTO expenses (date, amount, category, description) VALUES (?, ?, ?, ?)"
        self.conn.execute(sql, (date, amount, category, description))
        self.conn.commit()




