from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_1 = KeyboardButton('Чек лист и гайды')
button_2 = KeyboardButton('Комплексы тренировок')
button_3 = KeyboardButton('Марафон')
button_4 = KeyboardButton('Соц.сети')
button_5 = KeyboardButton('Обо мне')


courses_kb1 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_1).add(button_2).add(button_3).add(button_4).add(button_5)

button_14 = KeyboardButton('6 кубиков')
button_24 = KeyboardButton('Для начинающих дома / restart')
button_34 = KeyboardButton('Быстрая сушка')
button_44 = KeyboardButton('menu')

courses4_kb4 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_14).add(button_24).add(button_34).add(button_44)


# чек-лист
button_11 = KeyboardButton('Получить бесплатный чек-лист')
button_21 = KeyboardButton('menu')

course1_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_11).add(button_21)

# гайд
button_12 = KeyboardButton('💫Оплатить💫')
button_22 = KeyboardButton('menu')

course2_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_12).add(button_22)

# 6 кубиков
button_13 = KeyboardButton('купить 6 кубиков')
button_23 = KeyboardButton('о курсе 6 кубиков')
button_33 = KeyboardButton('menu')

course3_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_13).add(button_23).add(button_33)

# дома для начинающих / RESTART
button_15 = KeyboardButton('Для кого?')
button_25 = KeyboardButton('Купить RESTART')
button_35 = KeyboardButton('menu')

course5_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_15).add(button_25).add(button_35)

# быстрая сушка
button_16 = KeyboardButton('о курсе "быстрая сушка"')
button_26 = KeyboardButton('купить быструю сушку')
button_36 = KeyboardButton('menu')

course6_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_16).add(button_26).add(button_36)

# Марафон 21 день
button_17 = KeyboardButton('О марафоне')
button_27 = KeyboardButton('Хочу участвовать!')
button_37 = KeyboardButton('menu')

course7_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_17).add(button_27).add(button_37)




# for search
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k