import config
import logging
import keyboard
import messages

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType

# log
logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# prices
PRICE1 = types.LabeledPrice(label="Чек-лист", amount=500 * 100)  # в копейках (руб)
PRICE2 = types.LabeledPrice(label="Гайд", amount=600 * 100)  # в копейках (руб)
PRICE3 = types.LabeledPrice(label="Мини курс 6 кубиков", amount=2990 * 100)  # в копейках (руб)
PRICE4 = types.LabeledPrice(label="Мини курс RESTART", amount=2990 * 100)  # в копейках (руб)
PRICE5 = types.LabeledPrice(label="Мини курс быстрая сушка", amount=2990 * 100)  # в копейках (руб)
PRICE6 = types.LabeledPrice(label="Марафон 21 день", amount=1000 * 100)  # в копейках (руб)
PRICE7 = types.LabeledPrice(label="Как тренироваться для набора мышц", amount=299 * 100)  # в копейках (руб)
PRICE8 = types.LabeledPrice(label="Как тренироваться на рельеф", amount=299 * 100)  # в копейках (руб)

# проверка на подписку на канал
def check_sub_channel(chat_member):
    print(chat_member['status'])
    if chat_member['status'] != 'left':
        return True
    else:
        return False

# start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    with open('jock.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo=photo, caption=messages.start_message, parse_mode='MarkdownV2', reply_markup=keyboard.courses_kb1)


# menu
@dp.message_handler(text=['Меню'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                           text="Привет!\n" + "Выбирай, что тебе интересно 🙏🏻",
                           reply_markup=keyboard.courses_kb1)


# Чек-лист и гайды
@dp.message_handler(text=['Чек листы/гайды'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                           text=messages.info_check_list,
                           reply_markup=keyboard.course1_kb2)
    # if check_sub_channel(await bot.get_chat_member(chat_id=config.CHANNEL_ID, user_id=message.from_user.id)) == False:
    #     await bot.send_message(message.chat.id, text=messages.NOT_SUB_MESSAGE, reply_markup=keyboard.course1_kb2)



# Получить гайд спортивыне добавки
@dp.message_handler(text=['Спортивыне добавки'])
async def start(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=config.CHANNEL_ID, user_id=message.from_user.id)):
        with open('sports_supplements.pdf', 'rb') as file:
            await bot.send_document(message.chat.id, document=file, caption='Ваш гайд', reply_markup=keyboard.course1_kb2)
    else:
        await bot.send_message(message.chat.id, text=messages.NOT_SUB_MESSAGE, reply_markup=keyboard.course1_kb2)



# гайд как тренироваться для набора мышц
@dp.message_handler(text=['Как тренироваться для набора мышц'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, text=messages.info_guide_on_how_to_train_to_gain_muscle, reply_markup=keyboard.course9_kb_guid)

# Получить гайд как тренироваться для набора мышц
@dp.message_handler(text=['Купить гайд как тренироваться для набора мышц'])
async def buy(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовый платеж!!!")
    await bot.send_message(message.chat.id, reply_markup=keyboard.courses_kb1, text=messages.text_for_gaids, parse_mode='MarkdownV2')
    await bot.send_invoice(message.chat.id,
                           title="Покупка гайда для набора мышц",
                           description="Гайд отправится вам автоматически",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://github.com/dimakpa/TG_courses/blob/main/invoice_train_to_gain_muscle.PNG?raw=true",
                           photo_width=512,
                           photo_height=512,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE7],
                           start_parameter="one-month-subscription",
                           payload="invoice-payload-set-of-muscles",
                           reply_markup=keyboard.keyboard_buy_1,
                           )



# как тренироваться на рельеф
@dp.message_handler(text=['Как тренироваться на рельеф'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, text=messages.info_how_to_train_for_relief, reply_markup=keyboard.course10_kb_guid)

# Получить гайд как тренироваться на рельеф
@dp.message_handler(text=['Купить гайд как тренироваться на рельеф'])
async def buy(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовый платеж!!!")

    await bot.send_message(message.chat.id, reply_markup=keyboard.courses_kb1, text=messages.text_for_gaids, parse_mode='MarkdownV2')
    await bot.send_invoice(message.chat.id,
                           title="Покупка гайда",
                           description="Гайд отправится вам автоматически",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://github.com/dimakpa/TG_courses/blob/main/invoice_train_for_relief.PNG?raw=true",
                           photo_width=512,
                           photo_height=512,
                           photo_size=512,
                           is_flexible=False,
                           prices=[PRICE8],
                           start_parameter="one-month-subscription",
                           payload="invoice-payload-train-for-relief",
                           reply_markup=keyboard.keyboard_buy_1)



# Комплексы тренировок
@dp.message_handler(text=['Комплексы тренировок'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                           text="Можете выбрать мини курсы",
                           reply_markup=keyboard.courses4_kb4)


# 6 кубиков
@dp.message_handler(text=['6 кубиков'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                           text="Выберите, что вас интересует",
                           reply_markup=keyboard.course3_kb2)

# о курсе 6 кубиков
@dp.message_handler(text=['О курсе 6 кубиков'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                           text=messages.info_6_dice,
                           reply_markup=keyboard.course3_kb2)

# Оплатить 6 кубиков
@dp.message_handler(text=['Купить 6 кубиков'])
async def buy(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовый платеж!!!")

    await bot.send_message(message.chat.id, reply_markup=keyboard.courses_kb1, text='Чек')
    await bot.send_invoice(message.chat.id,
                           title="Покупка мини курса 6 кубиков",
                           description="Ссылка на миникурс отправится вам сразу после успешной оплаты",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://gbuenergiya.ru/wp-content/uploads/b/9/3/b93664f1a38a911f17c937d6ceee68c3.jpeg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE3],
                           start_parameter="one-month-subscription",
                           payload="invoice-payload-6-dice",
                           reply_markup=keyboard.keyboard_buy_1)


# Для начинающих дома / restart
@dp.message_handler(text=['Для начинающих дома / restart'])
async def start(message: types.Message):
    with open('video.mp4', 'rb') as video:
        await bot.send_video(message.chat.id,
                             video=video,
                             caption="Выберите, что вас интересует",
                             reply_markup=keyboard.course5_kb2,
                             width=720,
                             height=1280)
    # await bot.send_message(message.chat.id,
    #                        text="Выберите, что вас интересует",
    #                        reply_markup=keyboard.course5_kb2)

# о курсе Для начинающих дома / restart
@dp.message_handler(text=['Для кого?'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                           text=messages.info_RESTART,
                           reply_markup=keyboard.course5_kb2)


# Оплатить для начинающих дома / restart
@dp.message_handler(text=['Купить RESTART'])
async def buy(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовый платеж!!!")

    await bot.send_message(message.chat.id, reply_markup=keyboard.courses_kb1, text='Чек')
    await bot.send_invoice(message.chat.id,
                           title="Покупка мини курса дома для начинающих / RESTART",
                           description="Ссылка на миникурс отправится вам сразу после успешной оплаты",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://gbuenergiya.ru/wp-content/uploads/b/9/3/b93664f1a38a911f17c937d6ceee68c3.jpeg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE4],
                           start_parameter="one-month-subscription",
                           payload="invoice-payload-restart",
                           reply_markup=keyboard.keyboard_buy_1)


# быстрая сушка
@dp.message_handler(text=['Быстрая сушка'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                           text="Выберите, что вас интересует",
                           reply_markup=keyboard.course6_kb2)

# о курсе быстрая сушка
@dp.message_handler(text=['Быстрая сушка - для кого?'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                           text=messages.info_quick_drying,
                           reply_markup=keyboard.course6_kb2)

# Оплатить быстрая сушка
@dp.message_handler(text=['Купить быструю сушку'])
async def buy(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовый платеж!!!")

    await bot.send_message(message.chat.id, reply_markup=keyboard.courses_kb1, text='Чек')
    await bot.send_invoice(message.chat.id,
                           title="Покупка мини курса быстрая сушка",
                           description="Ссылка на миникурс отправится вам сразу после успешной оплаты",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://gbuenergiya.ru/wp-content/uploads/b/9/3/b93664f1a38a911f17c937d6ceee68c3.jpeg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE5],
                           start_parameter="one-month-subscription",
                           payload="invoice-payload-quick-drying",
                           reply_markup=keyboard.keyboard_buy_1)


# Марафон 21 день
@dp.message_handler(text=['Марафон'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                           text="Выберите, что вам интересно",
                           reply_markup=keyboard.course7_kb2)


# О марафоне
@dp.message_handler(text=['О марафоне'])
async def buy(message: types.Message):
    with open('video2.MOV', 'rb') as video2:
        await bot.send_video(message.chat.id,
                             video=video2,
                             parse_mode='MarkdownV2',
                             caption=messages.info_marathon,
                             reply_markup=keyboard.course7_kb2,
                             width=720,
                             height=1280)


# Марафон хочу участвовать
@dp.message_handler(text=['Хочу участвовать!'])
async def buy(message: types.Message):
    await bot.send_message(message.chat.id,
                           text=messages.info_want_a_marathon,
                           parse_mode='MarkdownV2',
                           reply_markup=keyboard.course7_kb2)

# Соцсети
@dp.message_handler(text=['Соц.сети'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                           text=messages.social_network,
                           reply_markup=keyboard.courses_kb1)

# Обо мне
@dp.message_handler(text=['Обо мне'])
async def start(message: types.Message):
    with open('jock1.jpg', 'rb') as photo1, open('jock2.jpg', 'rb') as photo2, open('jock3.jpg', 'rb') as photo3, open('jock4.jpg', 'rb') as photo4, open('jock5.jpg', 'rb') as photo5:
        media = types.MediaGroup()
        media.attach_photo(photo1)
        media.attach_photo(photo2)
        media.attach_photo(photo3)
        media.attach_photo(photo4)
        media.attach_photo(photo5)
        await bot.send_media_group(message.chat.id, media)
        # await bot.send_photo(message.chat.id, )#photos=[photo1, photo2, photo3, photo4, photo5])
    await bot.send_message(message.chat.id,
                           text=messages.about_me,
                           reply_markup=keyboard.courses_kb1)


# pre checkout  (must be answered in 10 seconds)
@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# successful payment
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    print(payment_info)
    print(payment_info['invoice_payload'])
    for k, v in payment_info.items():
        print(f"{k} = {v}")
    await bot.send_message(message.chat.id,
                           f"Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")
    if payment_info['invoice_payload'] == "invoice-payload-train-for-relief":
        with open('train_for_relief.pdf', 'rb') as file:
            await bot.send_document(message.chat.id, document=file, caption='Ваш гайд "Как тренироваться на рельеф?"\n ',
                                    reply_markup=keyboard.courses_kb1)
    if payment_info['invoice_payload'] == "invoice-payload-set-of-muscles":
        with open('gaid_set_of_muscles.pdf', 'rb') as file:
            await bot.send_document(message.chat.id, document=file, caption='Ваш гайд "Как тренироваться на рост мышц?"',
                                    reply_markup=keyboard.courses_kb1)
    if payment_info['invoice_payload'] == "invoice-payload-6-dice":
        await bot.send_message(message.chat.id, messages.link_6_dice)
    if payment_info['invoice_payload'] == "invoice-payload-restart":
        await bot.send_message(message.chat.id, messages.link_RESTART)
    if payment_info['invoice_payload'] == "invoice-payload-quick-drying":
        await bot.send_message(message.chat.id, messages.link_quick_drying)
    if payment_info['invoice_payload'] == "invoice-payload-marathon":
        await bot.send_message(message.chat.id, messages.link_marathon)


# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
