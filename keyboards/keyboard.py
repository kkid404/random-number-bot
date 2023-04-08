from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class Keyboard:
    
    def start_kb():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn = KeyboardButton("Сгенерировать число")
        keyboard.add(btn)
        return keyboard
