import telebot
from telebot import types
import datetime
numbers = 0

bot = telebot.TeleBot("6030598086:AAEHabgyoYxaGH4WbnbC_N9Qw1H-ac3sy2A")



@bot.message_handler(commands = ['start'])

def start(message):
    global numbers
    numbers = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("rational")
    but2 = types.KeyboardButton("complex")
    markup.add(but1,but2)
    log(message)
    bot.send_message(message.chat.id, f"Выбери ниже", reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def numb(message):
    if message.text == "rational":
        rational(message)
    elif message.text == "complex":
        complexn(message)

def rational(message):
    global numbers
    numbers=1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("сумма")
    but2 = types.KeyboardButton("разность")
    but3 = types.KeyboardButton("деление")
    but4 = types.KeyboardButton("умножение")
    but5 = types.KeyboardButton("деление с остатком")
    but6 = types.KeyboardButton("целочисленное деление")
    markup.add(but1,but2,but3,but4,but5,but6)
    bot.send_message(message.chat.id, f"Выбери операцию", reply_markup=markup)
    bot.register_next_step_handler(message, op_rational)
@bot.message_handler(content_types = ['text'])
def op_rational(message):
    if message.text == "сумма":
        bot.send_message(message.chat.id, f"введи два числа для суммы через пробел")
        bot.register_next_step_handler(message, operation_1)
    elif message.text == "разность":
        bot.send_message(message.chat.id, f"введи два числа для разности через пробел")
        bot.register_next_step_handler(message, operation_2)
    elif message.text == "деление":
        bot.send_message(message.chat.id, f"введи два числа для деления через пробел")
        bot.register_next_step_handler(message, operation_3)
    elif message.text == "умножение":
        bot.send_message(message.chat.id, f"введи два числа для умножения через пробел")
        bot.register_next_step_handler(message, operation_4)
    elif message.text == "деление с остатком":
        bot.send_message(message.chat.id, f"введи два числа для деления с остатком через пробел")
        bot.register_next_step_handler(message, operation_5)
    elif message.text == "целочисленное деление":
        bot.send_message(message.chat.id, f"введи два числа для целочисленного деления через пробел")
        bot.register_next_step_handler(message, operation_6)
    log(message)
def complexn(message):
    global numbers
    numbers=2
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("сумма")
    but2 = types.KeyboardButton("разность")
    but3 = types.KeyboardButton("деление")
    but4 = types.KeyboardButton("умножение")
    markup.add(but1,but2,but3,but4)
    bot.send_message(message.chat.id, f"Выбери операцию", reply_markup=markup)
    bot.register_next_step_handler(message, op_complex)
@bot.message_handler(content_types = ['text'])
def op_complex(message):
    if message.text == "сумма":
        bot.send_message(message.chat.id, f"введи два комплексных числа для суммы через пробел")
        bot.register_next_step_handler(message, operation_1)
    elif message.text == "разность":
        bot.send_message(message.chat.id, f"введи два комплексных числа для разности через пробел")
        bot.register_next_step_handler(message, operation_2)
    elif message.text == "деление":
        bot.send_message(message.chat.id, f"введи два комплексных числа для деления через пробел")
        bot.register_next_step_handler(message, operation_3)
    elif message.text == "умножение":
        bot.send_message(message.chat.id, f"введи два комплексных числа для умножения через пробел")
        bot.register_next_step_handler(message, operation_4)
    log(message)
def operation_1(message):
    global numbers
    result=''
    if numbers==1:
        list_numbers = list(map(int, message.text.split()))
        result=str(sum(list_numbers))
    elif numbers==2:
        list_numbers = list(map(str,message.text.split()))
        complex1=complex(list_numbers[0])
        complex2 = complex(list_numbers[1])
        result = complex1+complex2
    bot.send_message(message.chat.id, {str(result)})
    start(message)

def operation_2(message):
    global numbers
    result = ''
    if numbers==1:
        list_numbers = list(map(int, message.text.split()))
        result=str(list_numbers[0]-list_numbers[1])
    elif numbers==2:
        list_numbers = list(map(str,message.text.split()))
        complex1=complex(list_numbers[0])
        complex2 = complex(list_numbers[1])
        result = complex1-complex2
    bot.send_message(message.chat.id, {str(result)})
    start(message)

def operation_3(message):
    global numbers
    result = ''
    if numbers==1:
        list_numbers = list(map(int, message.text.split()))
        if list_numbers[1]!=0:
            result=str(round(list_numbers[0]/list_numbers[1],2))
        elif list_numbers[1]==0:
            result="Нельзя делить на ноль!"
    elif numbers==2:
        list_numbers = list(map(str,message.text.split()))
        complex1=complex(list_numbers[0])
        complex2 = complex(list_numbers[1])
        result = complex1/complex2
    bot.send_message(message.chat.id, {str(result)})
    start(message)
def operation_4(message):
    global numbers
    result = ''
    if numbers==1:
        list_numbers = list(map(int, message.text.split()))
        result=str(list_numbers[0]*list_numbers[1])
    elif numbers==2:
        list_numbers = list(map(str,message.text.split()))
        complex1=complex(list_numbers[0])
        complex2 = complex(list_numbers[1])
        result = complex1*complex2
    bot.send_message(message.chat.id, {str(result)})
    start(message)
def operation_5(message):
    global numbers
    result = ''
    list_numbers = list(map(int, message.text.split()))
    if numbers==1:
        list_numbers = list(map(int, message.text.split()))
        if list_numbers[1]!=0:
            result=str(list_numbers[0]%list_numbers[1])
        elif list_numbers[1]==0:
            result="Нельзя делить на ноль!"
    bot.send_message(message.chat.id, {str(result)})
    start(message)
def operation_6(message):
    global numbers
    result = ''
    list_numbers = list(map(int, message.text.split()))
    if numbers==1:
        list_numbers = list(map(int, message.text.split()))
        if list_numbers[1]!=0:
            result=str(list_numbers[0]//list_numbers[1])
        elif list_numbers[1]==0:
            result="Нельзя делить на ноль!"
    bot.send_message(message.chat.id, {str(result)})
    start(message)


def log(message):
    text=message.text
    with open('log.txt', 'a+', encoding='UTF8') as file:
         file.write('{}|{}|{}\n'.format(message.from_user.first_name,text,datetime.datetime.now()))

bot.infinity_polling()