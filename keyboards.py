from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

transition_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Я готова продолжить")
        ],
    ],
    resize_keyboard=True
)
