from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

informatika_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ofis dasturlari bilan ishlash'),
            KeyboardButton(text='C++ dasturlash tili')
        ],
        [
            KeyboardButton(text='/Python_dasturlash_tili')
        ],
        [
            KeyboardButton(text='Asosiy menyuga qaytish')
        ]
    ], resize_keyboard=True

)
