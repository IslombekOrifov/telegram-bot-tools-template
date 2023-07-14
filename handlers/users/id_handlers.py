from aiogram import types

from aiogram.dispatcher import filters

from loader import dp


SUPERUSERS = [1558753, 45689523]

BLACKLIST = [1558753, 45689523]


@dp.message_handler(chat_id=SUPERUSERS, text='secret')
async def id_filter_secret(msg: types.Message):
    await msg.answer("Maxfiy chatga marxamat")