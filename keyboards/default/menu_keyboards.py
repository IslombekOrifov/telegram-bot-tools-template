from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Menyu',),
        ]
        [
            KeyboardButton(text='Mening Buyurtmalarim'),

            KeyboardButton(text='Fikr bildirish'),
            KeyboardButton(text='Sozlamalar'),
            
        ]
        [
            KeyboardButton(text='Ijtimoiy tarmoqlarimiz'),
        ]
    ],
    resize_keyboard=True,
)

secondary_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Menyu',),
        ]
        [
            KeyboardButton(text='Mening Buyurtmalarim'),

            KeyboardButton(text='Fikr bildirish'),
            KeyboardButton(text='Sozlamalar'),
            
        ]
        [
            KeyboardButton(text='Ijtimoiy tarmoqlarimiz'),
        ]
    ],
    resize_keyboard=True,
)