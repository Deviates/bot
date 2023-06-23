from aiogram.utils import executor
from aiogram import types, Dispatcher

from config import bot, dp
from handlers import klient, viktorin, lesson, question, anketa
import logging
from database.bot_db import sql_create

klient.register_handlers_klient(dp)
viktorin.register_handlers_viktorin(dp)
lesson.register_handlers_lesson(dp)
question.register_handlers_question(dp)
anketa.register_handlers_ankete(dp)



async def on_startup(_):
    sql_create()

   


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)