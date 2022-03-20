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
        ],
        [
            KeyboardButton(text='Adminga murojat qilish')
        ]
    ],
    resize_keyboard=True
)
