# import telebot
# from telebot import types
#
# user_sweets = 0
#
# bot = telebot.TeleBot("6030598086:AAEHabgyoYxaGH4WbnbC_N9Qw1H-ac3sy2A")
#
#
#
# @bot.message_handler(commands = ['start'])
#
# def start(message):
#     bot.send_message(message.chat.id,f"/button")
#     #bot.register_next_step_handler(message, input_sweets)
# def summa(message):
#     summ = sum(list(map(int,message.text.split())))
#     bot.send_message(message.chat.id, str(summ))
#     button(message)
#
# def diff(message):
#     differ = list(map(int,message.text.split()))[0]-list(map(int,message.text.split()))[1]
#     bot.send_message(message.chat.id, str(differ))
#     button(message)
# # def input_sweets(message):
# #     global user_sweets
# #     user_sweets = int(message.text)
#
# @bot.message_handler(commands = ['button'])
# def button(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     but1 = types.KeyboardButton("сумма")
#     but2 = types.KeyboardButton("разность")
#     markup.add(but1)
#     markup.add(but2)
#     bot.send_message(message.chat.id, f"Выбери ниже", reply_markup=markup)
#
# @bot.message_handler(content_types = ['text'])
# def controller(message):
#     if message.text == "сумма":
#         bot.send_message(message.chat.id, f"введи два числа для суммы через пробел")
#         bot.register_next_step_handler(message, summa)
#     elif message.text == "разность":
#         bot.send_message(message.chat.id, f"введи два числа для разности через пробел")
#         bot.register_next_step_handler(message, diff)
#
# bot.infinity_polling()