from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ingliz_tili_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Gramatika'),
            KeyboardButton(text='lugat')
        ],
        [
            KeyboardButton(text='Inglizcha adabiyotlar'),
            KeyboardButton(text='Inglizcha ilmiy kitoblar')
        ],
        [
            KeyboardButton(text='Asosiy menyuga qaytish')
        ]
    ], resize_keyboard=True
)
