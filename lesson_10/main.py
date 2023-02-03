from candy_bot.bot_handlers import dp
from aiogram import executor

async def startup(_):
    print('Грачи прилетели')

executor.start_polling(dp, skip_updates=True, on_startup=startup)