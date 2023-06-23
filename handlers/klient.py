from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from config import bot, dp
from button.button import start_markup 

async def start_handler(message: types.Message):
    # photo = open("media/Group 10(2).png", "rb")
    # await bot.send_photo(message.from_user.id, photo=photo)
    await bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}  это IT-школа DEVIATES", reply_markup=start_markup )  

async def quiz_1 (message:types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("СЛЕДУЮЩИЙ", callback_data="button_call_1")
    markup.add(button_call_1)

    questions = """ Имеется кортеж вида T = (4, 2, 3).
    Какая из операций приведёт к тому,
    что имя T будет ссылаться на кортеж (1, 2, 3)?"""

    ansvers = [
        "T[0] = 1",
        "T = (1) + T[1:]",
        "T = (1,) + T[1:]",
        "T.startswith(1)"
    ] 
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=questions,
        options=ansvers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Вот тупой',
        open_period=10,
        reply_markup=markup
    )




def register_handlers_klient(dp:Dispatcher):
    dp.register_message_handler(start_handler,commands=["start"])
    dp.register_message_handler(quiz_1, text="🎬 Пройти викторину")
