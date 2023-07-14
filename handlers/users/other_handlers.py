from aiogram import types

from aiogram.dispatcher import filters

from loader import dp


# is reply filter
@dp.message_handler(is_reply=True, commands='user_id')                       # botga reply qilib /user_id komandasi yuborilsa bot user id sini yuboradis
async def reply_filter_example(msg: types.Message):
    """Admindan kelgan komandalarni qabul qilish uchun ishlatiladi"""
    await msg.answer(msg.reply_to_message.from_user.id)


# is contact filter
@dp.message_handler(content_types='contact', is_sender_contact=True)        # botga yuborilgan kontakt yuboruvchiga tegishlimi yo'qmi tekshiradi
# @dp.message_handler(filters.IsSenderContact(True), content_types='contact')        # botga yuborilgan kontakt yuboruvchiga tegishlimi yo'qmi tekshiradi
async def contact_filter_example(msg: types.Message):
    """Kontaktni tekshirish"""
    await msg.answer("telefon raqam sizniki")


# forwarded message filter
@dp.message_handler(is_forwarded=True)        # botga yuborilgan forward xabarni ushlaydi
async def forward_filter_example(msg: types.Message):
    """Forward xabar filtri"""
    await msg.answer("Nimaa mena forward xabar yuborasiz")


# chat type filter
# @dp.message_handler(chat_type='group', commands='is_pm')        # guruhda
# @dp.message_handler(chat_type='super_group', commands='is_pm')      # super guruhda
# @dp.message_handler(chat_type='private', commands='is_pm')          # botni chatida
# @dp.message_handler(chat_type='channel', commands='is_pm')        # kanalda
@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands='shaxsiy')
async def chat_type_filter_example(msg: types.Message):
    """Bot chatida shaxsiy komandasi kelganda ishlidigan funksiya"""
    await msg.answer(f"siz shaxsiy chatda /shaxsiy komandasini yubordingiz sizning id ingiz {msg.from_user.id}")