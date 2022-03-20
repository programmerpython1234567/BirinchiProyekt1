from aiogram import types
from aiogram.types import ContentType

from loader import dp,bot
from filters import Gurux


# Echo bot
@dp.message_handler(Gurux(),content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message):
    user_id=message.from_user.id
    await message.answer(text=f'Guruxni tark etdi ')
    await bot.kick_chat_member(chat_id='@inglis_tiliBot',user_id=user_id)

@dp.message_handler(Gurux(),content_types=ContentType.STICKER)
async def bot_echo(message: types.Message):
    user_id=message.from_user.id
    await message.answer(text=f'Guruxni tark etdi ')
    await bot.kick_chat_member(chat_id='@dars1314',user_id=user_id)
