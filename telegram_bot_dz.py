import telebot
from random import randint
from telebot import types

user_sweets = 0
sweets = 221
max_count_sweets = 28
current_player = 1
bot = telebot.TeleBot("6030598086:AAEHabgyoYxaGH4WbnbC_N9Qw1H-ac3sy2A")


@bot.message_handler(commands=['start']) # вызов функции по команде в списке
def controller(message):
    global sweets
    global max_count_sweets
    if current_player == 1 and sweets>0:
        bot.send_message(message.chat.id,
            f"Введите количество не больше {max_count_sweets}") # отправка сообщения (кому отправляем, что отправляем(str))
        bot.register_next_step_handler(message, user_input)
    elif current_player == 2 and sweets>0:
        user_input(message)
    if sweets<=0:
        if current_player == 1:
            bot.send_message(message.chat.id, f"Победил БОТ!")
            bot.send_message(message.chat.id, f"Обновить игру! /restart")
        elif current_player == 2:
            bot.send_message(message.chat.id, f"Победил Игрок!")
            bot.send_message(message.chat.id, f"Обновить игру! /restart")


def get_count(message):
    global sweets
    global user_sweets
    sweets = sweets - user_sweets
    bot.send_message(message.chat.id, f"осталось {sweets}")
    controller(message)

def user_input(message):
    global user_sweets
    global current_player
    global max_count_sweets
    if current_player==1:
        user_sweets = int(message.text)
        if user_sweets>max_count_sweets:
            controller(message)
        else:
            current_player=2
            get_count(message)
    elif current_player==2:
        user_sweets = int(randint(1,max_count_sweets))
        bot.send_message(message.chat.id, f"Бот взял -> {user_sweets} конфет")
        current_player=1
        get_count(message)


@bot.message_handler(commands=['restart']) # вызов функции по команде в списке
def restart_game(message):
    global user_sweets
    global sweets
    global max_count_sweets
    global current_player
    user_sweets = 0
    sweets = 221
    max_count_sweets = 28
    current_player = 1
    bot.send_message(message.chat.id, f"Игра обновлена! /start")

bot.infinity_polling()