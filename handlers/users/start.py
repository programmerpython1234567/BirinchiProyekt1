from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import asosiy_menu
from loader import dp, data_base
from filters import Shaxsiy


@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    surname = message.from_user.full_name
    user_name = message.from_user.username
    idd = message.from_user.id
    try:
        data_base.foydalanuvchi_qoshish(ism=ism, fam=surname, tg_id=idd, username=user_name)
    except Exception as x:
        print(x)
    await message.answer(f"Salom, {message.from_user.full_name}! Botga hush kelibsiz", reply_markup=asosiy_menu)
