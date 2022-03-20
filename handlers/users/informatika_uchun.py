from aiogram import types
from filters.userlar_bilan_ishlash import Shaxsiy
from loader import dp
from keyboards.default.informatika import informatika_button



@dp.message_handler(Shaxsiy(),text='Informatsion texnologiya')
async def bot_echo(message: types.Message):
    await message.answer(text='Yonalishni tanlang', reply_markup=informatika_button)
