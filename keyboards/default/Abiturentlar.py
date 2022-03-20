from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Abiturentlar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='fizika'),
            KeyboardButton(text='matematika')
        ],
        [
            KeyboardButton(text='ingliz tili'),
            KeyboardButton(text='kimyo')
        ],
        [
            KeyboardButton(text='Asosiy menyuga qaytish')
        ]
    ], resize_keyboard=True
)
