from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.message):
    text = "Agarda sizda bot bilan bog'liq muammolar bo'lsa \
        yoki buyurtmangiz yetib bormagan bo'lsa @orifov_islombek bilan bog'laning!"
    await message.answer(text)
