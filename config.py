from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = "5938110366:AAElefNYLRV3LXHaLvLtxmeD0rdY7ciXTzA"

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
URL = "https://google.com"
