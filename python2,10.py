import aiogram
import random
from aiogram import Bot, Dispatcher, types
from  aiogram.utils import executor

API_TOKEN = '8022034258:AAEv5Tw7P4NRyWSP93rAZ8hczAush1rub1M'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
        await message.reply("Сыграем в кости числа ои 1 до 10")

@dp.message_handler(commands="roll")
async def random_num(message:types.Message):
    ran_user=random.randint(1,10)
    ran_bot=random.randint(1,10)
    message.reply(f"У пользователя {ran_user} у бота {ran_bot}")

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)





