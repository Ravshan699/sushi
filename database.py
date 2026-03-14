import sqlite3

conn = sqlite3.connect("menu.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
price INTEGER,
image TEXT
)
""")

conn.commit()
conn.close()