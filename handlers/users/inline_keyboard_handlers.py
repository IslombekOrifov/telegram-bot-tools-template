from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text

from loader import dp
from keyboards.inline.product_keyboards import category_menu, shaurma_menu


@dp.message_handler(Text(equals="Maxsulotlar", ignore_case=True))
async def select_menu(msg: Message):
    await  msg.answer(f"Maxsulotni tanlang", reply_markup=category_menu)



@dp.callback_query_handler(text='shaurma')
async def next_menu(call: CallbackQuery):
    await  call.message.answer(f"Maxsulotni tanlang", reply_markup=shaurma_menu)
    await call.answer(cache_time=60)