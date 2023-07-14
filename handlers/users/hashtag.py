from aiogram import types

from loader import dp


@dp.message_handler(hashtags='money')
@dp.message_handler(cashtags=['usd', 'eur'])
async def hasntag_exaple(msg: types.Message):
    text = f"siz {msg.text } hastegini yoki keshtegini iishlattingiz!"
    await msg.answer(f'akang kuchayyyydi. {text}')