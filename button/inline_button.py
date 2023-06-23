from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove


kurs_frontend = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
    text='📢 Подробнее',
    url='https://google.com'
        )
    ],
    [
        InlineKeyboardButton(
    text='🙋🏻‍♂️ Связатся c админом',
    url='https://t.me/Abdykadyrov_S'
        )
    ],
    [
        InlineKeyboardButton(
            text="↪️ Назад",
            callback_data="↪️ Назад"
        )
    ]
])

# -------------------------------------------------------------------------------------------------

kurs_backend = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
    text='📢 Подробнее',
    url='https://google.com'
        )
    ],
    [
        InlineKeyboardButton(
    text='🙋🏻‍♂️ Связатся c админом',
    url='https://t.me/Abdykadyrov_S'
        )
    ],
    [
         InlineKeyboardButton(
            text="↪️ Назад",
            callback_data="↪️ Назад"
        )
    ]
])

# ------------------------------------------------------------------------------------------------------

kurs_dizain = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
    text='📢 Подробнее',
    url='http://yurconsule.kg/'
        )
    ],
    [
        InlineKeyboardButton(
    text='🙋🏻‍♂️ Связатся c админом',
    url='https://t.me/Abdykadyrov_S'
        )
    ],
    [
         InlineKeyboardButton(
            text="↪️ Назад",
            callback_data="↪️ Назад"
        )
    ]
])
# -------------------------------------------------------------------------------------------------------
kurs_android = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
    text='📢 Подробнее',
    url='https://google.com'
        )
    ],
    [
        InlineKeyboardButton(
    text='🙋🏻‍♂️ Связатся c админом',
    url='https://t.me/Abdykadyrov_S'
        )
    ],
    [
         InlineKeyboardButton(
            text="↪️ Назад",
            callback_data="↪️ Назад"
        )
    ]
])

# ---------------------------------------------------------------------------------------------------------

markup10 = InlineKeyboardMarkup(row_width=1)
button1 = InlineKeyboardButton(text="Как выбрать язык?", callback_data="butt_1")
button2 = InlineKeyboardButton(text="Какой ноутбук нужен?", callback_data="butt_2")
button3 = InlineKeyboardButton(text="Можно ли поступать без опыта в IT?", callback_data="butt_3")
button4 = InlineKeyboardButton(text="Я получу сертификат?", callback_data="butt_4")
button5 = InlineKeyboardButton(text="Помогаете трудостройством?", callback_data="butt_5")
button6 = InlineKeyboardButton(text="Естли огриничения по возрасту?", callback_data="butt_6")
button7 = InlineKeyboardButton(text="Получиться шомешать со школой?", callback_data="butt_7")
button8 = InlineKeyboardButton(text="Назад", callback_data="butt_8")
markup10.add(button1,button2,button3, button4, button5, button6, button7, button8)