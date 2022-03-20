from aiogram import types
from filters.userlar_bilan_ishlash import Shaxsiy
from loader import dp
from keyboards.default.ingliz_tili import ingliz_tili_button


@dp.message_handler(Shaxsiy(),text='Inglis tili')
async def bot_echo(message: types.Message):
    await message.answer(
        text='Ingliz tili olamiga hush kelibsiz, siz bu yerda koplab inglizcha malumotlar olishingiz mumkin',
        reply_markup=ingliz_tili_button)
