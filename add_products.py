import sqlite3

conn = sqlite3.connect("menu.db")
cursor = conn.cursor()

products = [
    ("Филадельфия", 45000, "https://i.imgur.com/0umadnY.jpg"),
    ("Калифорния", 40000, "https://i.imgur.com/W5D9b0T.jpg"),
    ("Дракон", 50000, "https://i.imgur.com/IJ6yE5B.jpg")
]

cursor.executemany(
    "INSERT INTO products(name,price,image) VALUES(?,?,?)",
    products
)

conn.commit()
conn.close()
print("Роллы добавлены")