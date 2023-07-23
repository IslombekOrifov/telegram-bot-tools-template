from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import shaurma_callback


# 1-usul
category_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Shaurma', callback_data="shaurma"),
            InlineKeyboardButton(text='Lavash', callback_data="lavash"),
        ],
        [
            InlineKeyboardButton(text="Ijtimoiy sahifalarimiz", url="https://mohirdev.uz"),
        ],
        [
            InlineKeyboardButton(text="Qidirish", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="Ulashish", switch_inline_query="Zo'r bot ekan."),
        ],
    ],
)



# Shaurma uchun keyboard

shaurma_menu = InlineKeyboardMarkup(row_width=2)
big_shaurma = InlineKeyboardButton(text='Big shaurma', callback_data=shaurma_callback.new(item_name='big_shaurma'))
shaurma_menu.insert(big_shaurma)