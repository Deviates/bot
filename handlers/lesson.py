from aiogram import types, Dispatcher
from config import bot, dp
from button.button import kursy_button, start_markup
from button.inline_button import kurs_backend, kurs_android, kurs_dizain, kurs_frontend



async def kurs(message: types.Message):
    await bot.send_message(message.from_user.id, f"🥳 Выбери язык программирования! 🥳", reply_markup=kursy_button )

async def backend(message:types.Message):
     photo = open("media/61377ba5ace322607b7222b87d27a833.jpg", "rb")     
     await message.answer_photo(photo=photo)
     await message.answer(f"""✅ Введение в IT и Python
✅ Изучение вёрстки на HTML, CSS, JS
✅ Backend-разработка на Python и Django
✅ PostgreSQL и работа с базами данных """, reply_markup=kurs_backend)    

async def frontend(message: types.Message):
     photo = open("media/java-script1.jpg", "rb")
     await message.answer_photo(photo=photo)
     await message.answer( f""" ✅ Устройство веба и основы HTML
✅ CSS и верстка на Flexbox
✅ Работа с Git
✅ Синтаксис языка Javascript
✅ Объекты, EventLoop
✅ Модель DOM и сборщики (Webpack)
✅ Разработка на React.js """, reply_markup=kurs_frontend) 
     
async def android(message: types.Message):
     photo = open("media/java.png", "rb")
     await message.answer_photo(photo=photo)
     await message.answer(f""" ✅ Профессия
✅ Проекты для портфолио 
✅ Офлайн и онлайн уроки
✅ Запись уроков
✅ Практические занятия """, reply_markup=kurs_android) 

async def dizain(message: types.Message):
     photo = open("media/5a84e819b8b275a95759276dbad635f2.png", "rb")
     await message.answer_photo(photo=photo)
     await message.answer(f""" ✅ Официальный сертификат
✅ Проекты для портфолио 
✅ Офлайн и онлайн уроки
✅ Запись уроков
✅ Практические занятия  """, reply_markup=kurs_dizain)           

async def nazad1(message: types.Message):
     match message.text:
          case "↪️ Назад":
            await message.answer(f"Главная меню",reply_markup=start_markup) 

async def nazad(call: types.CallbackQuery):
     if call.data == "↪️ Назад":
          await call.message.answer(f"Наши курсы",reply_markup=kursy_button)  

def register_handlers_lesson(dp:Dispatcher):
    dp.register_message_handler(kurs, text="👨‍🎓 Наши курсы")   
    dp.register_message_handler(backend, text="🛠 Backend-разработчик")  
    dp.register_message_handler(frontend, text="🎨 Frontend-разработчик")
    dp.register_message_handler(android, text="🔧 Android-разработчик")
    dp.register_message_handler(dizain, text="💃 UX/UI-дизайнер")
    dp.register_message_handler(nazad1, text="↪️ Назад")
    dp.register_callback_query_handler(nazad, lambda call: call.data == "↪️ Назад")