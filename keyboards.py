from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/close')
b4 = KeyboardButton('/quiz')
kb.add(b1).insert(b2).add(b3).insert(b4)

kb_quiz = InlineKeyboardMarkup(row_width=4)
ib1 =InlineKeyboardButton(text='1',
                          url='https://docs.aiogram.dev/en/latest/telegram/types/inline_keyboard.html?highlight=inline%20keyboard')
ib2 =InlineKeyboardButton(text='2',
                          url='https://docs.aiogram.dev/en/latest/telegram/types/inline_keyboard.html?highlight=inline%20keyboard')
ib3 =InlineKeyboardButton(text='3',
                          url='https://docs.aiogram.dev/en/latest/telegram/types/inline_keyboard.html?highlight=inline%20keyboard')
ib4 =InlineKeyboardButton(text='4',
                          url='https://docs.aiogram.dev/en/latest/telegram/types/inline_keyboard.html?highlight=inline%20keyboard')
kb_quiz.add(ib1, ib2, ib3, ib4)
