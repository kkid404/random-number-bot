from aiogram import types

from loader import dp, bot
from keyboards import Keyboard
from utils import generate_number

@dp.message_handler(text="Сгенерировать число")
async def get_number(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        generate_number(),
        reply_markup=Keyboard.start_kb()
    )