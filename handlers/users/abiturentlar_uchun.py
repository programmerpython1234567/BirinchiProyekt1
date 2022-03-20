from aiogram import types
from filters.userlar_bilan_ishlash import Shaxsiy
from loader import dp
from keyboards.default.Abiturentlar import Abiturentlar_button
from keyboards.inline.menu_darsliklar import inline_button


@dp.message_handler(Shaxsiy(),text='Abiturentlar uchun')
async def bot_echo(message: types.Message):
    await message.answer(text="yo'nalishingizni tanlang", reply_markup=Abiturentlar_button)
@dp.message_handler(Shaxsiy(),text='fizika')
async def bot_echo(message: types.Message):
    await message.answer(text="yo'nalishni tanlang", reply_markup=inline_button)