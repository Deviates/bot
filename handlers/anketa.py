from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from button.button import submit_markup, start_markup, otmena_markup, gender_markup, region_button
from database.bot_db import sql_command_insert



class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    gender = State()
    region = State()
    photo = State()
    submit = State()

async def anketa_start(message: types.Message):
    await FSMAdmin.name.set()
    await message.answer("Как вас завут?", reply_markup=otmena_markup)

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # print(data)
        data['id'] = message.from_user.id
        data['username'] = f"@{message.from_user.username}"
        data["name"] = message.text
        # print(data)
    await FSMAdmin.next()
    await message.answer("Сколько вам лет?",reply_markup=otmena_markup)        

async def load_age(message: types.Message, state: FSMContext):
    try:
        if 10 < int(message.text) <80:
            async with state.proxy() as data:
                data["age"] = int(message.text)
            await FSMAdmin.next()
            await message.answer("Какой пол?", reply_markup=gender_markup)    
        else:
            await message.answer("Ведите цифру от 10 до 80")     
    except:
        await message.answer("Пишите цифрами!")    

async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
    await FSMAdmin.next()
    await message.answer('Ваш регион?', reply_markup=region_button)      

async def load_region(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text
    await FSMAdmin.next()
    await message.answer('Отправте ваш фото ?')

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        await bot.send_photo(message.from_user.id, data['photo'], f"{data['name']}, {data['age']}, {data['gender']}, {data['region']}, \n {data['username']}")
    await FSMAdmin.next()
    await message.answer('Вы все провильно заполняли анкету?', reply_markup=submit_markup)      

async def submit(message: types.Message, state: FSMContext):
    if message.text == "Да":   
        await sql_command_insert(state) 
        await state.finish()
        await message.answer("Спасибо за регистрацию! Скоро с вами свясатся администрация", reply_markup=start_markup)
    elif message.text == "Нет":
        await state.finish()
        await message.answer("Заполните заново пожалуйста!", reply_markup=start_markup)
    else:
        await message.answer("Ответье да или нет")    

async def otmena_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if otmena_reg  is not None:
        await state.finish()
        await message.answer("Вы отменили регистрацию", reply_markup=start_markup)               

def register_handlers_ankete(dp: Dispatcher):
    dp.register_message_handler(otmena_reg, state="*", text='отмена')
    dp.register_message_handler(otmena_reg, Text(equals='отмена', ignore_case=True), state="*")

    dp.register_message_handler(anketa_start, text="✍️ Записаться на урок")
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(load_region, state=FSMAdmin.region)
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=FSMAdmin.submit)




