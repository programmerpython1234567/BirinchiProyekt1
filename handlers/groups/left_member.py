from aiogram import types
from aiogram.types import ContentType

from loader import dp
from filters import Gurux


# Echo bot
@dp.message_handler(Gurux(),content_types=ContentType.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
    ism=message.left_chat_member.first_name
    await message.answer(text=f'Guruxni tark etdi {ism}')
