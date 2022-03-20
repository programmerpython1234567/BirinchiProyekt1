from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from filters.userlar_bilan_ishlash import Shaxsiy
from loader import dp


@dp.message_handler(Shaxsiy(),CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))
