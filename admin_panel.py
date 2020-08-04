from aiogram import types
from config import admin_id
from load_all import dp


@dp.message_handler(user_id=admin_id, commands=["count"])
async def count_user(message: types.Message):
    await message.answer('')
