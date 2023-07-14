from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp



@dp.message_handler(CommandStart(deep_link='orifov_academy'))   # t.me/taom_delivery_bot?start=orifov_academy
async def bot_start(message: types.Message):
    """ Bu handler deep link orqali kirgan userlarga xabar yuboradi"""

    text = 'sizni orifov academy taklif qildi'
    await message.answer(f"Salom, {message.from_user.full_name}! {text}")


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
