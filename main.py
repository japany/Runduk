import logging
import os
from aiogram import Bot, types, executor
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from config import TOKEN_API
from const import HELP_COMMAND, DESCRIPTION, POHUI_LIST
from aiogram.types import ReplyKeyboardRemove
from keyboards import kb, kb_quiz


TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)

async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)
    print('Бот успешено запущен!')

async def on_shutdown(dispatcher):
    await bot.delete_webhook()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text="НУ ЧЁ, НАРОД, ПОГНАЛИ, НАХУЙ? ЕБАНЫЙ В РООООООТ",
                         reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer(text=HELP_COMMAND,
                         parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['description'])
async def cmd_desc(message: types.Message):
    await message.answer(text=DESCRIPTION)
    await message.delete()

@dp.message_handler(commands=['quiz'])
async def cmd_quiz(message: types.Message):
    await message.answer(text='QUIZ',
                        reply_markup=kb_quiz)
    await message.delete()


@dp.message_handler(commands=['close'])
async def cmd_close(message: types.Message):
    await message.answer(text='Ну ок...',
                         reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.message_handler()
async def check_ROLF(message: types.Message):
    if 'пидор' in message.text.lower():
        await message.reply(text="Нет, ты 🫵")
    elif any(n in message.text.lower() for n in POHUI_LIST):
        await bot.send_photo(chat_id=message.chat.id,
                             photo="https://sun9-23.userapi.com/impg/MUMGtkbYNMY_pGpPJEskcWrgNUsLGgnwHvzc5w/_BmbDAdFc5I.jpg?size=600x400&quality=96&sign=d4843d6bbbd3557113b524fe6b1f5929&type=album")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )