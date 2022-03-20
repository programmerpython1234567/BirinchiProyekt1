from aiogram import types
from filters.userlar_bilan_ishlash import Shaxsiy
from loader import dp
from keyboards.default.menu import asosiy_menu


@dp.message_handler(Shaxsiy(),text='menu')
async def bot_echo(message: types.Message):
    await message.answer(text="yo'nalishingizni tanlang", reply_markup=asosiy_menu_button)
