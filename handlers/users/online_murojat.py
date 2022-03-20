from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state
from aiogram.types import ContentType
from pip._internal import commands
from keyboards.default.tel import tel_button
from states.holatlar import Forma
from keyboards.default.tasdiqlash import tasdiq_button
from keyboards.default.menu import asosiy_menu
from loader import dp, bot
from filters.userlar_bilan_ishlash import Shaxsiy


@dp.message_handler(Shaxsiy(),text='Adminga murojat qilish')
async def bot_echo(message: types.Message):
    await message.answer(text='Adnminga murojat qilish uchun anketa toldiring')
    await message.answer(text='Ismni kiriting')
    await Forma.ism_qabul_qilish.set()

@dp.message_handler(Shaxsiy(),state=Forma.ism_qabul_qilish)
async def bot_echo(message: types.Message, state: FSMContext):
    ism = message.text
    await state.update_data({'ism': ism})
    await message.answer(text='Faimilyani kiriting')
    await Forma.fam_qabul_qilish.set()

@dp.message_handler(Shaxsiy(),state=Forma.fam_qabul_qilish)
async def bot_echo(message: types.Message, state: FSMContext):
    familya = message.text
    await state.update_data({'fam': familya})
    await message.answer(text='yoshni kiriting')
    await Forma.yosh_qabul_qilish.set()

@dp.message_handler(Shaxsiy(),state=Forma.yosh_qabul_qilish)
async def bot_echo(message: types.Message, state: FSMContext):
    yosh = message.text
    await state.update_data({'yosh': yosh})
    await message.answer(text='telni kiriting', reply_markup=tel_button)
    await message.answer(text='Tel nomerni jonatish uchun Contakt tugmasini bosing yoki lokatsiyani jonatish uchun Lokatsiya tugmasini bosing')

    await Forma.tel_qabul_qilish.set()

@dp.message_handler(Shaxsiy(),state=Forma.tel_qabul_qilish,content_types=ContentType.CONTACT)
async def bot_echo(message: types.Message, state: FSMContext):
    tel = message.contact.phone_number
    await state.update_data({'tel': tel})
    await message.answer(text='Murojatni kiriting')
    await Forma.murojat_qabul_qilish.set()

@dp.message_handler(Shaxsiy(),state=Forma.murojat_qabul_qilish)
async def bot_echo(message: types.Message, state: FSMContext):
    matn = message.text
    await state.update_data({'matn': matn})


    malumotlar = await state.get_data()

    user_ismim = malumotlar.get('ism')
    user_fam = malumotlar.get('fam')
    user_yosh = malumotlar.get('yosh')
    user_tel = malumotlar.get('tel')

    await message.answer(text=f'Quyidagi malumotlarni adminga yuborish uchun tasdiqlash tugmasini bosing\n'
                              f'Ism: {user_ismim}\n'
                              f'Fam: {user_fam}\n'
                              f'Yosh: {user_yosh}\n'
                              f'Tel: {user_tel}\n\n'                              
                              f'Murojat: {matn}\n',reply_markup=tasdiq_button  )

    await Forma.tasdiqlash.set()

@dp.message_handler(Shaxsiy(),text ='Tasdiqlash', state=Forma.tasdiqlash )
async def bot_echo(message: types.Message, state: FSMContext):
    malumotlar = await state.get_data()
    matn = malumotlar.get('matn')
    user_ismim = malumotlar.get('ism')
    user_fam = malumotlar.get('fam')
    user_yosh = malumotlar.get('yosh')
    user_tel = malumotlar.get('tel')
    user_name = message.from_user.first_name
    await bot.send_message(chat_id=587497692, text=f'Ushbu foydalanuvchi {user_name} quyidagi xabarni yubordi\n'
                                                   f'{matn}\n'
                                                   f'{user_ismim}\n'
                                                   f'{user_tel}\n'
                                                   f'{user_yosh}\n'
                                                   f'{user_fam}')

    await state.finish()

