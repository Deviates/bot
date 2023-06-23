from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from config import bot, dp
from button.button import start_markup



async def quiz_2 (call:types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("СЛЕДУЮЩИЙ", callback_data="button_call_2")
    
    markup.add(button_call_1)

 

    questions = """ Необходимо собрать и вывести все уникальные слова из строки рекламного текста.
    Какой из перечисленных типов данных Python подходит лучше всего?"""
    
    ansvers = [
        "кортеж (tuple)",
        "список (list)",
        "множество (set)",
        "словарь (dict)"
    ] 
    
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=questions,
        options=ansvers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Вот тупой',
        open_period=10,
        reply_markup=markup
    )
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_coll_1 = InlineKeyboardButton("СЛЕДУЮЩИЙ ВОПРОС", callback_data="button_call_3")
    markup.add(button_coll_1)



    questions = "Как можно более кратко представить следующую запись?"
    ansvers = [
        "A = Y if Z else Y",
        "A = Y if X else Z",
        "A = X if Z else Y",
        "A = X if Y else Z",
    ]   

    photo = open("media/Screenshot from 2023-05-02 16-42-48.png", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=questions,
        options=ansvers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Вот тупой',
        open_period=10,
        reply_markup=markup,
    )
async def quiz_4( message: types.Message):
    questions = " Что выведет следующий код?"
    ansvers = [
        "IndexError",
        "Получено исключение.",
        "None",
        "TypeError",
        "Получено исключение. Но в этом нет ничего страшного.",
    ]   

    
    photo = open("media/Screenshot from 2023-05-02 17-01-14.png", "rb")
    await bot.send_photo(message.from_user.id, photo=photo)
    
    

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=questions,
        options=ansvers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Вот тупой',
        open_period=10,
        reply_markup=start_markup
        
    )

async def back(message:types.Message):
    markup = ReplyKeyboardMarkup()
    button = KeyboardButton("Назад")
    markup.add(button)
    await message.answer(f"fdjngh", reply_markup=start_markup)     

def register_handlers_viktorin(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2,lambda call: call.data == "button_call_1" )   
    dp.register_callback_query_handler(quiz_3,lambda call: call.data == "button_call_2" )    
    dp.register_callback_query_handler(quiz_4,lambda call: call.data == "button_call_3" ) 
    dp.register_message_handler(back, text="Назад")  



