from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_1 = KeyboardButton('Чек листы/гайды')
button_2 = KeyboardButton('Комплексы тренировок')
button_3 = KeyboardButton('Марафон')
button_4 = KeyboardButton('Соц.сети')
button_5 = KeyboardButton('Обо мне')


courses_kb1 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_1).add(button_2).add(button_3).add(button_4).add(button_5)

keyboard_buy_1 = InlineKeyboardMarkup()
keyboard_buy_1.add(InlineKeyboardButton("Pay", pay=True))



button_14 = KeyboardButton('6 кубиков')
button_24 = KeyboardButton('Для начинающих дома / restart')
button_34 = KeyboardButton('Быстрая сушка')
button_44 = KeyboardButton('Меню')

courses4_kb4 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_14).add(button_24).add(button_34).add(button_44)


# Чек листы/гайды
button_11 = KeyboardButton('Спортивыне добавки')
button_21 = KeyboardButton('Как тренироваться для набора мышц')
button_31 = KeyboardButton('Как тренироваться на рельеф')
button_41 = KeyboardButton('Меню')

course1_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_11).add(button_21).add(button_31).add(button_41)

# гайд спортивыне добавки
button_18 = KeyboardButton('Получить гайд спортивыне добавки')
button_28 = KeyboardButton('Меню')
course8_kb_guid = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_18).add(button_28)

# гайд как тренироваться для набора мышц
button_19 = KeyboardButton('Купить гайд как тренироваться для набора мышц')
button_29 = KeyboardButton('Меню')
course9_kb_guid = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_19).add(button_29)

# гайд как тренироваться на рельеф
button_110 = KeyboardButton('Купить гайд как тренироваться на рельеф')
button_210 = KeyboardButton('Меню')
course10_kb_guid = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_110).add(button_210)


# 6 кубиков
button_13 = KeyboardButton('Купить 6 кубиков')
button_23 = KeyboardButton('О курсе 6 кубиков')
button_33 = KeyboardButton('Меню')

course3_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_13).add(button_23).add(button_33)

# дома для начинающих / RESTART
button_15 = KeyboardButton('Для кого?')
button_25 = KeyboardButton('Купить RESTART')
button_35 = KeyboardButton('Меню')

course5_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_15).add(button_25).add(button_35)

# быстрая сушка
button_16 = KeyboardButton('Быстрая сушка - для кого?')
button_26 = KeyboardButton('Купить быструю сушку')
button_36 = KeyboardButton('Меню')

course6_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_16).add(button_26).add(button_36)

# Марафон 21 день
button_17 = KeyboardButton('О марафоне')
button_27 = KeyboardButton('Хочу участвовать!')
button_37 = KeyboardButton('Меню')

course7_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(button_17).add(button_27).add(button_37)


