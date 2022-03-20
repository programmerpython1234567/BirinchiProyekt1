from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

asosiy_menu = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='Abiturentlar uchun'),
            KeyboardButton(text='Badiy adabiyotlar')
        ],
        [
            KeyboardButton(text='Informatsion texnologiya'),
            KeyboardButton(text='Inglis tili')
        ]
    ],
    resize_keyboard=True
)
