from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    ans = """
        Привет!\nЭтот бот создан для получения актуальной информации по ценам на базовые продукты потребления! Вы можете посмотреть динамику изменения цен корзины или по позициям.
    """
    await message.reply(ans)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    ans = """Команды для получения информации:\n/help - список команд\n/month - динамика корзины за месяц\n/year - динамика корзины за год
    """
    await message.reply(ans)

@dp.message_handler(commands=['month'])
async def process_month_command(message: types.Message):
    ans = "Пока не реализована"
    await message.reply(ans)

@dp.message_handler(commands=['year'])
async def process_year_command(message: types.Message):
    ans = "Пока не реализована"
    await message.reply(ans)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)