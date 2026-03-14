from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import sqlite3
import requests
from fastapi.middleware.cors import CORSMiddleware

BOT_TOKEN = "ВАШ_BOT_TOKEN"
ADMIN_CHAT_ID = "ВАШ_CHAT_ID"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory="webapp", html=True), name="webapp")

@app.get("/menu")
def get_menu():
    conn = sqlite3.connect("menu.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    conn.close()
    return data

@app.post("/order")
async def create_order(request: Request):
    data = await request.json()
    cart = data["cart"]
    name = data["name"]
    phone = data["phone"]
    address = data["address"]

    msg = f"🍣 *НОВЫЙ ЗАКАЗ*\n\nИмя: {name}\nТелефон: {phone}\nАдрес: {address}\n\n"
    total = 0

    conn = sqlite3.connect("menu.db")
    cursor = conn.cursor()

    for id, count in cart.items():
        if count > 0:
            cursor.execute("SELECT name, price FROM products WHERE id=?",(id,))
            product = cursor.fetchone()
            msg += f"{product[0]} x{count} = {product[1]*count} сум\n"
            total += product[1]*count

    msg += f"\n*Итого: {total} сум*"

    # Отправка в Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id":ADMIN_CHAT_ID, "text":msg, "parse_mode":"Markdown"})

    conn.close()
    return JSONResponse({"status":"ok"})