from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Darsliklar', callback_data='menu1'),
            InlineKeyboardButton(text='Testlar', callback_data='menu2'),
            InlineKeyboardButton(text='Uashish', switch_inline_query='')
        ]
    ]
)
