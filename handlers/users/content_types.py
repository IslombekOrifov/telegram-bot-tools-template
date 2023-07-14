from aiogram import types

from aiogram.dispatcher import filters

from loader import dp


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def image_handler(message: types.Message):
    text = 'nima bu bashara?'
    message.answer(text)


@dp.message_handler(content_types='photo')
async def image_handler(message: types.Message):
    text = 'nima bu bashara?'
    message.answer(text)


@dp.message_handler(content_types='document')
async def image_handler(message: types.Message):
    text = 'nima bu bashara?'
    message.answer(text)