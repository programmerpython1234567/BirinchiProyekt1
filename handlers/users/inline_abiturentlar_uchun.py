from aiogram import types
from aiogram.types import CallbackQuery
from filters.userlar_bilan_ishlash import Shaxsiy
from keyboards.default.Abiturentlar import Abiturentlar_button
from loader import dp




@dp.callback_query_handler(Shaxsiy(),text='menu1')
async def bot_echo(xabar: CallbackQuery):
    await xabar.message.answer(text='kitoblardan tanlang', reply_markup=Abiturentlar_button)
