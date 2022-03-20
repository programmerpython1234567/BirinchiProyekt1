from aiogram import types
from aiogram.types import ContentType, InputFile
from loader import dp, bot
from filters.userlar_bilan_ishlash import Shaxsiy
from pip._internal import commands


@dp.message_handler(Shaxsiy(),content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
        await message.document.download()
        doc_id = message.document.file_id
        await message.answer(Shaxsiy(),text=f'Dokument yuborildi doc id da {doc_id}')

@dp.message_handler(Shaxsiy(),content_types=ContentType.STICKER)
async def bot_echo(message: types.Message):
        await message.sticker.download()
        sticer_id = message.sticker.file_id
        await message.answer(text=f'stiker yuborildi ')

@dp.message_handler(Shaxsiy(),content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message):
        await message.video.download()
        video_id = message.video.file_id
        await message.answer(text=f'video yuborildi {video_id}')

@dp.message_handler(Shaxsiy(),content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message):
        await message.photo[0].download()
        rasm_id = message.photo[0].file_id
        await message.answer(text=f'rasm yuborildi {rasm_id}')

@dp.message_handler(Shaxsiy(),commands = 'rasm')
async def bot_echo(message: types.Message):
        user_id = message.from_user.id
        rasm_id = 'AgACAgIAAxkBAAIDRGIknuZhBFOVtjGl_SKbIhv_a6ALAALduDEbAAG3IEm-s6fUhJspBgEAAwIAA3MAAyME'
        await bot.send_photo(chat_id = user_id, photo = rasm_id)


@dp.message_handler(Shaxsiy(),commands = 'Python_dasturlash_tili')
async def bot_echo(message: types.Message):
        user_id = message.from_user.id
        video_manzil = InputFile(path_or_bytesio='videos/file_9.MP4')
        await bot.send_video(chat_id=user_id,video=video_manzil)