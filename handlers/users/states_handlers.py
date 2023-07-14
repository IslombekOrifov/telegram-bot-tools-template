from aiogram import types

from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(commands='xarid')
async def set_state(msg: types.Message, state: FSMContext):
    """Foydalanuvchini birorta state ichiga kiritamiz"""
    await state.set_state('xarid_state')
    await msg.answer('Maxsulot tanlang')


@dp.message_handler(state='xarid_state')
async def state_example(msg: types.Message, state: FSMContext):
    """Foydalanuvchini birorta state ichiga kiritamiz"""
    await msg.answer("Maxsulot savatchaga qo'shildi")
    await state.finish()
    