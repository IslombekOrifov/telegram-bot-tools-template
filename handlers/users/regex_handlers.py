from aiogram import types

from aiogram.dispatcher.filters import Regexp

from loader import dp


PHONE_EXP = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
EMAIL_EXP = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
COMMAND_EMAIL = r'/email:' + EMAIL_EXP

@dp.message_handler(Regexp(PHONE_EXP))
async def phone_get(msg: types.Message):
    await msg.answer(f"Telefon raqamingiz: {msg.text} -> qabul qilindi!")


@dp.message_handler(Regexp(EMAIL_EXP))
async def phone_get(msg: types.Message):
    await msg.answer(f"Email: {msg.text} -> qabul qilindi!")


@dp.message_handler(regexp_commands=[COMMAND_EMAIL])
async def phone_get(msg: types.Message):
    await msg.answer(f"Email: {msg.text} -> qabul qilindi!")