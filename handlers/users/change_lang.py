from aiogram import types

from aiogram.dispatcher.filters.builtin import Command
from loader import dp



@dp.message_handler(Command('til'))                     # Command bilan custom handler
async def change_language(message: types.Message):
    await message.answer("Kerakli tilni tanlang .!.")


@dp.message_handler(Command(['til', 'vaqt']))           # Command bilan custom handler ko'p  komandalar uchun bitta funksiya ishlaganda
async def change_language(message: types.Message):
    await message.answer("Kerakli tilni tanlang .!.")


@dp.message_handler(commands='til')
async def change_language(message: types.Message):
    await message.answer("Kerakli tilni tanlang .!.")


@dp.message_handler(commands=['til', 'vaqt'])
async def change_language(message: types.Message):
    await message.answer("Kerakli tilni tanlang .!.")