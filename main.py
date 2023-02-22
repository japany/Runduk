from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API
from const import HELP_COMMAND, DESCRIPTION, POHUI_LIST
from aiogram.types import ReplyKeyboardRemove
from keyboards import kb


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот успешено запущен!')


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
    executor.start_polling(dp, on_startup=on_startup,
                           skip_updates=True)