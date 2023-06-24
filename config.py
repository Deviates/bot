from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = "6066902061:AAGKuHKrXK6u1MhcvE1hIt3x-Dh-melQs-M"

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
URL = "http://deviates.site/"
