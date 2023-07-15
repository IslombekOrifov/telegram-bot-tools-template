from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import PersonalData


@dp.message_handler(Command('anketa'))
async def registration_func(msg: types.Message):
    await msg.answer("T'liq ismingizni kiriting!")
    await PersonalData.full_name.set()


@dp.message_handler(state=PersonalData.full_name)
async def get_fullname_func(msg: types.Message, state: FSMContext):
    full_name = msg.text

    await state.update_data(
        {'name': full_name}
    )

    await msg.answer("Email manzil kiriting")
    # await PersonalData.email.set()
    await PersonalData.next()


@dp.message_handler(state=PersonalData.email)
async def get_email_func(msg: types.Message, state: FSMContext):
    email = msg.text

    await state.update_data(
        {'email': email}
    )

    await msg.answer("Telefon raqam kiriting")
    # await PersonalData.email.set()
    await PersonalData.next()


@dp.message_handler(state=PersonalData.phone)
async def get_email_func(msg: types.Message, state: FSMContext):
    phone = msg.text

    await state.update_data(
        {'phone': phone}
    )

    # ma'lumotlarni o'qimiz
    data = await state.get_data()
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')

    text = "Quyidagi ma'umotlar qabul qilindi!\n"
    text += f"Ismingiz {name}\n"
    text += f"Telefon raqamingiz {phone}\n"
    text += f"Emailizngiz {email}\n"

    await msg.answer(text)

    await state.finish()                        #statedagi hamma ma'lumotlar ram dan o'chib ketadi
    # await state.reset_state(with_data=False)    #statedagi hamma ma'lumotlar ram da qoladi.