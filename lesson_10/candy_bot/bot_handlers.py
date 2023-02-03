from .bot_init import dp
from aiogram import types
from .candys import interface as game


@dp.message_handler(commands=['start_game'])
async def start_game(message: types.Message):
    msg = game.start_game(message.from_id)
    await message.answer(msg)


@dp.message_handler(commands=['stop_game'])
async def stop_game(message: types.Message):
    msg = game.stop_game(message.from_id)
    await message.answer(msg)


@dp.message_handler(commands=['start', 'help'])
async def help_msg(message: types.Message):
    msg = game.help_message()
    await message.answer(msg)


@dp.message_handler(commands=['set'])
async def set_candys_max(message: types.Message):
    msg = game.set_max(message.from_id)
    await message.answer(msg)


@dp.message_handler(regexp='\d{1,2}')
async def user_step(message):
    step = int(message.text)
    answer = game.step_result(message.from_id, step)
    await message.answer(answer)
