from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/close')
kb.add(b1).insert(b2).add(b3)