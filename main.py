import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram import executor


API_TOKEN = '6723244609:AAG3YVvZyOHlknyNQmFu31paW_MUr9nkSkA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!")
    print("хуй")

@dp.message_handler(commands=['info'])
async def send_info(message: types.Message):
    await message.reply("Это простой телеграм-бот, созданный с использованием aiogram.")


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)