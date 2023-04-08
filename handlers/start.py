from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards import Keyboard
from loader import dp, bot

@dp.message_handler(CommandStart())
async def start(message: types.Message, kb = Keyboard):
    await bot.send_message(
        message.from_user.id,
        "Привет! Тыкай кнопку.",
        reply_markup=kb.start_kb()
        )