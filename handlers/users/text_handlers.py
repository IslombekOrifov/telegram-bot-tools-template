from aiogram import types

from aiogram.dispatcher.filters import Text

from loader import dp


@dp.message_handler(Text(contains='Assalomu alaykum', ignore_case=True)) # xabar ichida Assalomu alaykumga bo'lsa
@dp.message_handler(Text(equals='Assalomu alaykum', ignore_case=True)) # xabar Assalomu alaykumga teng bo'lsa 
async def text_equals_example(msg: types.Message):
    """ bu funksiya tepadegi ikkita filter uchun ham ishlaydi."""
    await msg.reply("Vaalaykum Assalom")
