
from aiogram import Bot, Dispatcher, executor


API_TOKEN = '6723244609:AAG3YVvZyOHlknyNQmFu31paW_MUr9nkSkA'

# Создаем экземпляр бота
bot = Bot(token=API_TOKEN)

# Создаем диспетчер для обработки обновлений
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Hello! I'm your bot.")

# Запуск бота
if __name__ == '__main__':
    try:
        print('Бот запущен')
        executor.start_polling(dp, timeout=10)
    except Exception as e:
        print("An error occurred while starting the bot: %s", e)

# Ожидание пользовательского ввода перед закрытием
input("Нажмите Enter для выхода...")