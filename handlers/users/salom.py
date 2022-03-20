from aiogram import types
from filters.userlar_bilan_ishlash import Shaxsiy
from loader import dp



@dp.message_handler(Shaxsiy(),text='salom')
async def bot_echo(message: types.Message):
    await message.answer(text='Assalomalekum botga hush kelibsiz')
