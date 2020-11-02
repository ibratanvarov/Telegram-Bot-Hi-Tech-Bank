import telebot
import config
import object
import requests
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
my_id = '29555488'
my_id1 = '509393103'

@bot.message_handler(commands=['start'])
def zero(message):
    key = telebot.types.ReplyKeyboardMarkup(True, True)
    key.row("🇺🇿", "🇷🇺",)
    send = bot.send_message(message.from_user.id, "Выберите язык ", reply_markup=key)
    bot.register_next_step_handler(send, lang)



def lang(message):
    if message.text == "🇺🇿":
        firstuz(message)

    elif message.text == "🇷🇺":
        first(message)

def first(message):
    key = telebot.types.ReplyKeyboardMarkup(True, True)
    key.row("Частным Клиентам", "Бизнесу", "Контакты",)
    key.row("Kurs valut")
    key.row("Служба поддержки")
    send = bot.send_message(message.from_user.id, "Добро пожаловать на оффициальный телеграм бот HI-TECH bank",
                            reply_markup=key)
    bot.register_next_step_handler(send, second)
    bot.register_next_step_handler(send, five)


def second(message):
    if message.text == "Kurs valut":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        data1 = object.ien
        data2 = object.frank
        data3 = object.sterling
        data4 = object.dollar
        data5 = object.evro
        data6 = object.rubl
        send = bot.send_message(message.from_user.id,   "Курс валют\n\n "
                                                      "Иена: {}\n"
                                                      "Швейцарский франк: {}\n"
                                                      "Фунт стерлингов: {}\nДоллар США: {}\n"
                                                      "Евро: {}\nРоссийский рубль: {}".
                                                       format( "{:,}".format(float(data1)),
                                                               "{:,}".format(float(data2)),
                                                               "{:,}".format(float(data3)),
                                                               "{:,}".format(float(data4)),
                                                               "{:,}".format(float(data5)),
                                                               "{:,}".format(float(data6)),
                                                         ),
                                                        reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    if message.text == "Частным Клиентам":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Кредиты", "Карты")
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id, "Раздел для частным клиентам", reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == "Бизнесу":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Кредиты для бизнеса")
        keyboard.row("Специальные Тарифы")
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id, "Добро пожаловать, какую информацию вы хотите узнать?",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    elif message.text == "Контакты":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id,
                                "Контакты:Адрес: ул. Т. Шевченко 36а/36б Тел.:+998(71) 150 3366, +998 (71) 150 1133 Telegram: @infohtbuz Страница на Facebook: Hi-tech bank Наш профиль в Instagram: htb.uzПочта: info@htb.uz",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, third)


def third(message):
    if message.text == "Кредиты":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Микрозайм", "Ипотечный Кредит")
        keyboard.row("Потребительские кредиты")
        keyboard.row("Частным Клиентам")
        send = bot.send_message(message.from_user.id, "Раздел кредиты", reply_markup=keyboard)
        bot.register_next_step_handler(send, fourth)
        bot.register_next_step_handler(send, second)
    elif message.text == "Карты":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Карты UZCARD")
        keyboard.row("Карты CASHBACK")
        keyboard.row("Карты VISA")
        keyboard.row("Карты HUMO")
        keyboard.row("Частным Клиентам")

        send = bot.send_message(message.from_user.id, "Раздел карт", reply_markup=keyboard)
        bot.register_next_step_handler(send, fourth)
        bot.register_next_step_handler(send, second)
    elif message.text == "Кредиты для бизнеса":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Долгосрочный Кредит", "Краткосрочный Кредит")
        keyboard.row("Лизинг", "Кредитование малого бизнеса")
        keyboard.row("Агрокредиты", "Микрокредит")
        keyboard.row("Бизнесу")
        send = bot.send_message(message.from_user.id, "Раздел кредиты для бизнеса", reply_markup=keyboard)
        bot.register_next_step_handler(send, fourth)
        bot.register_next_step_handler(send, second)
    elif message.text == "Специальные Тарифы":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Бизнесу")
        send = bot.send_message(message.from_user.id,
                                "Специальные тарифные пакеты на банковские услуги по некоторым операциям в национальной и иностранной валюте  в HI-TECH BANK ** (* Данный тарифный пакет действует с 8 апреля 2019 г.)",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fourth)
        bot.register_next_step_handler(send, second)
    elif message.text == "Назад":
        first(message)


def fourth(message):
    if message.text == "Ипотечный Кредит":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Ipotechnyj-kredit-10-19",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == "Потребительские кредиты":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Potrebitelskie-kredity-10-19",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == "Микрозайм":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Mikrozajm-10-19", reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == "Карты CASHBACK":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Karty-Cashback-10-19", reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == "Карты HUMO":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Karty-HUMO-10-19", reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == "Карты UZCARD":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Karty-UzCard-10-19", reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == "Карты VISA":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Karty-Visa-10-19", reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == "Долгосрочный Кредит":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Dolgosrochnyj-Kredit-10-19",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == "Краткосрочный Кредит":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Kratkosrochnyj-kredit-10-19",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == "Лизинг":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Lizing-mikrolizing-10-19",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == "Кредитование малого бизнеса":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Kredity-dlya-malogo-biznesa-10-19",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == "Агрокредиты":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Agro-Kredit-10-19", reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == "Микрокредит":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Mikrokreditovanie-10-19",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, third)


def five(message):
    if message.text == "Служба поддержки":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        send = bot.send_message(message.from_user.id, "Пожалуйста опишите свою проблему", reply_markup=keyboard)
        bot.register_next_step_handler(send, six)


def six(message):
    bot.forward_message(my_id, message.chat.id, message.message_id)
    bot.forward_message(my_id1, message.chat.id, message.message_id)
    seven(message)


def seven(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="📞 Отправить номер телефона", request_contact=True)
    keyboard.add(button_phone)
    send = bot.send_message(message.chat.id, "Отправьте нам свой номер телефона чтобы мы могли с вами связаться",
                            reply_markup=keyboard)
    # keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    # send = bot.send_message(message.from_user.id, "Пожалуйста оставьте свои контакты", reply_markup=keyboard)
    bot.register_next_step_handler(send, eight)


def eight(message):
    bot.forward_message(my_id, message.chat.id, message.message_id)
    bot.forward_message(my_id1, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Отправлено")
    first(message)

########################################################### UZB ###############################################################3

def firstuz(message):
    key = telebot.types.ReplyKeyboardMarkup(True, True)
    key.row("Xususiy mijozlar uchun", "Biznes uchun", "Kontaktlar")
    key.row("Valyutalar kursi")
    key.row("Qo'llab-quvvatlash xizmati")
    send = bot.send_message(message.from_user.id, "HI-TECH bankning rasmiy telegram botiga xush kelibsiz",
                            reply_markup=key)
    bot.register_next_step_handler(send, seconduz)
    bot.register_next_step_handler(send, fiveuz)


def seconduz(message):
    if message.text == "Valyutalar kursi":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Назад")
        data1 = object.ien
        data2 = object.frank
        data3 = object.sterling
        data4 = object.dollar
        data5 = object.evro
        data6 = object.rubl
        send = bot.send_message(message.from_user.id, f"Valyutalar kursi\n\nYen: {data1}\n"
                                                      f"Shveytsariya franki: {data2}\n"
                                                      f"Funt sterling: {data3}\nUSD: {data4}\n"
                                                      f"Evro: {data5}\nRossiya rubli: {data6}", reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    if message.text == "Xususiy mijozlar uchun":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Kreditlar", "Kartalar")
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id, "Xususiy mijozlar uchun bo'lim", reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)
    elif message.text == "Biznes uchun":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Biznes uchun kreditlar")
        keyboard.row("Maxsus narxlar")
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id, "Xush kelibsiz, qanday ma'lumotlarni bilmoqchisiz?",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)
    elif message.text == "Kontaktlar":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id,"Aloqa: Manzil: st. T. Shevchenko 36a / 36b Tel .: + 998 (71) 150 3366, +998 (71) 150 1133 Telegram: @infohtbuz Facebook-dagi sahifa: Hi-tech bank Bizning Instagram-dagi profilimiz: htb.uz Pochta: info@htb.uz",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)


def thirduz(message):
    if message.text == "Kreditlar":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Mikrozaym", "Ipoteka Kredit")
        keyboard.row("Iste'mol kreditlari")
        keyboard.row("Xususiy mijozlar uchun")
        send = bot.send_message(message.from_user.id, "Kreditlar bo'limi", reply_markup=keyboard)
        bot.register_next_step_handler(send, fourthuz)
        bot.register_next_step_handler(send, seconduz)
    elif message.text == "Kartalar":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("UZCARD kartalari")
        keyboard.row("CASHBACK kartalari")
        keyboard.row("VISA kartalari")
        keyboard.row("HUMO kartalari")
        keyboard.row("Xususiy mijozlar uchun")

        send = bot.send_message(message.from_user.id, "Xaritalar bo'limi", reply_markup=keyboard)
        bot.register_next_step_handler(send, fourthuz)
        bot.register_next_step_handler(send, seconduz)
    elif message.text == "Biznes uchun kreditlar":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Uzoq muddatli kredit "," Qisqa muddatli kredit")
        keyboard.row("Lizing "," Kichik biznesni kreditlash")
        keyboard.row("Agrokreditlar "," Mikrokreditlar")
        keyboard.row("Biznesga")
        send = bot.send_message(message.from_user.id, "Biznes kreditlari bo'limi", reply_markup=keyboard)
        bot.register_next_step_handler(send, fourthuz)
        bot.register_next_step_handler(send, seconduz)
    elif message.text == "Maxsus narxlar":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Biznesga")
        send = bot.send_message(message.from_user.id,
                                "HI-TECH BANK-da milliy va xorijiy valyutadagi ayrim operatsiyalar bo'yicha bank xizmatlari uchun maxsus tarif paketlari ** (* Ushbu tarif to'plami 2019 yil 8 apreldan amal qiladi)",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, fourthuz)
        bot.register_next_step_handler(send, seconduz)
    elif message.text == "Ortga":
        firstuz(message)


def fourthuz(message):
    if message.text == "Ipoteka Kreditlari":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Ipotechnyj-kredit-10-19",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)
    elif message.text == "Iste'mol kreditlari":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Potrebitelskie-kredity-10-19",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)
    elif message.text == "Mikrokredit":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Mikrozajm-10-19", reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)
    elif message.text == "CASHBACK kartalari":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Karty-Cashback-10-19", reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)
    elif message.text == "HUMO kartalari":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Karty-HUMO-10-19", reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)
    elif message.text == "UZCARD kartalari":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Karty-UzCard-10-19", reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)
    elif message.text == "VISA kartalari":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Karty-Visa-10-19", reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)
    elif message.text == "Uzoq muddatli kredit":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Dolgosrochnyj-Kredit-10-19",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)
    elif message.text == "Qisqa muddatli kredit":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Kratkosrochnyj-kredit-10-19",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)
    elif message.text == "Lizing":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Lizing-mikrolizing-10-19",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)
    elif message.text == "Kichik biznesni kreditlash":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Kredity-dlya-malogo-biznesa-10-19",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)
    elif message.text == "Agro kreditlar":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Agro-Kredit-10-19", reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)
    elif message.text == "Mikro kreditlar":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Ortga")
        send = bot.send_message(message.from_user.id, "https://telegra.ph/Mikrokreditovanie-10-19",
                                reply_markup=keyboard)
        bot.register_next_step_handler(send, thirduz)


def fiveuz(message):
    if message.text == "Qo'llab-quvvatlash xizmati":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        send = bot.send_message(message.from_user.id, "Iltimos, muammoingizni tasvirlab bering", reply_markup=keyboard)
        bot.register_next_step_handler(send, sixuz)


def sixuz(message):
    bot.forward_message(my_id, message.chat.id, message.message_id)
    bot.forward_message(my_id1, message.chat.id, message.message_id)
    sevenuz(message)


def sevenuz(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="📞 Telefon raqamini yuboring", request_contact=True)
    keyboard.add(button_phone)
    send = bot.send_message(message.chat.id, "Biz bilan bog'lanishimiz uchun bizga telefon raqamingizni yuboring",
                            reply_markup=keyboard)
    # keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    # send = bot.send_message(message.from_user.id, "Пожалуйста оставьте свои контакты", reply_markup=keyboard)
    bot.register_next_step_handler(send, eightuz)


def eightuz(message):
    bot.forward_message(my_id, message.chat.id, message.message_id)
    bot.forward_message(my_id1, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Yuborildi")
    firstuz(message)



bot.polling(none_stop=True)