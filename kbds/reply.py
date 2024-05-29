from aiogram.types import KeyboardButtonPollType, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Документ"),
            KeyboardButton(text="О проекте"),
            KeyboardButton(text='Образец наряд-допуск')
        ],
        {
            KeyboardButton(text="Список работников"),
            KeyboardButton(text="Прочее"),
        }
    ],
    resize_keyboard=True,
    input_field_placeholder='Что Вас интересует?'
)

del_kbd = ReplyKeyboardRemove()


start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text="Документы"),
    KeyboardButton(text="О проекте"),
    KeyboardButton(text="Список работников"),
    KeyboardButton(text="Прочее"),
    KeyboardButton(text='Образец наряд-допуск')
)
start_kb2.adjust(2, 3)


start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)






