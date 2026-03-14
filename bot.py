from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
import asyncio

TOKEN = "8452220227:AAF_kV0w9nKd0nNh82xs7RgrRwzW6OtPz1E"
WEBAPP_URL = "https://sushi-63f5.onrender.com"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="🍣 Меню", web_app=WebAppInfo(url=WEBAPP_URL))]]
    )
    await message.answer("Добро пожаловать в Sushi Katana 🍣", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
