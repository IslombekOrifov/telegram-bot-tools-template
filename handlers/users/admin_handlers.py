from aiogram import types

from aiogram.dispatcher.filters import AdminFilter, Command

from loader import dp


# @dp.message_handler(Command('change_photo'), AdminFilter)
@dp.message_handler(commands='ban_user', is_chat_admin=True)                            # Chatlarda adminlar uchun ishlaydi
async def set_state(msg: types.Message):
    """Admindan kelgan komandalarni qabul qilish uchun ishlatiladi"""
    await msg.answer('Qonday admin')