from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config import URL

#  старт
start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2,
).add(
    KeyboardButton("👨‍🎓 Наши курсы"),
    KeyboardButton("✍️ Записаться на урок"),
    KeyboardButton("🎬 Пройти викторину"),
    KeyboardButton("❓ Часто задаваемые вопросы"),
)

# ------------------------------------------------------------------------------------------------------------------------------------------

kursy_button = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
).add(
    KeyboardButton("🎨 Frontend-разработчик"),
    KeyboardButton("🛠 Backend-разработчик"),
    KeyboardButton("🔧 Android-разработчик"),
    KeyboardButton("💃 UX/UI-дизайнер"),
    KeyboardButton("↪️ Назад")
)
# ----------------------------------------------------------------------------------------------------------------------------------------

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("Да"),
    KeyboardButton("Нет")
)
# -------------------------------------------------------------------------------------------------------------------------------------

nazad5 = ReplyKeyboardMarkup(
    one_time_keyboard=True
).add(
    KeyboardButton("↪️ Назад")
)
# -----------------------------------------------------------------------------------------------------------------------
otmena_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False
).add(
    KeyboardButton("Отмена"),
)
# ------------------------------------------------------------
gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
).add(
    KeyboardButton("Мужина"),
    KeyboardButton("Женшина"),
    KeyboardButton("Не знаю"),
    KeyboardButton(" Отмена")
)
# -------------------------------------------------------------------
region_button = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("Бишкек"),
    KeyboardButton("Ош"),
    KeyboardButton("Жалал-Абад"),
    KeyboardButton("Ысыккол"),
    KeyboardButton("Талас"),
    KeyboardButton("Баткен"),
    KeyboardButton("Нарын"),
    KeyboardButton(" Отмена")

)