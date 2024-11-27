#t.me/school250422_bot
# t.me/karazin261022_bot
# /setinline Hint
from importlib import import_module


from telebot import types
import telebot
import random
from tokens import API_TOKEN


bot = telebot.TeleBot(API_TOKEN)


audios = {"AwACAgIAAxkDAAIPK2NasdDqvSrvRPEbtSP-riscOlWpAAInIAACTzfQSnBAJg29MrpNKgQ": "Game of thrones",
"AwACAgIAAxkDAAIPLWNasdR1ZzH1buFAf2FKyhOl4rRhAAIpIAACTzfQSqD0lgWO9LZVKgQ" : "Terminator",
"AwACAgIAAxkDAAIPL2NasdgTuYyx9d0xDsyRpokIhtiGAAIqIAACTzfQSlus2A-1PmhPKgQ" : "Rocky",
"AwACAgIAAxkDAAIPMWNasdvsVs9VkP8tj-iVwj6avfVTAAIrIAACTzfQSpCqQFdVvWFHKgQ" : "Indiana Jones",
"AwACAgIAAxkDAAIPM2Nasd8Re334GFD79FljivzAiBETAAIsIAACTzfQSvGNTvUIsCU9KgQ" : "Pirates of the Caribbean",
"AwACAgIAAxkDAAIPNWNaseMt5qf-Afcu8uKJqbfVk1DYAAItIAACTzfQSp1EFeeWVxtdKgQ" : "The Imperial March (Star Wars)"}

users = {}

def generate_markup(answers):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    random.shuffle(answers)
    for item in answers:
        markup.add(item)
    return markup


@bot.message_handler(commands=['game'])
def game(message):
    markup = generate_markup(list(audios.values()))
    file_id = random.choice(list(audios))
    bot.send_voice(message.chat.id, file_id, reply_markup=markup)
    users[message.chat.id] = audios[file_id]


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    if message.chat.id in users:
        keyboard_hider = types.ReplyKeyboardRemove()
        answer = users[message.chat.id]
        if message.text == answer:
            msg = 'Congratulations! Your answer is correct!'
        else:
            msg = 'Your answer is not correct. Try again!'
        bot.send_message(message.chat.id, msg, reply_markup=keyboard_hider)
        users.pop(message.chat.id)
    else:
        msg = 'To start the game use command /game'
        bot.send_message(message.chat.id, msg)


# @bot.message_handler(func=lambda message: True)
# def start(message):
#     print(message.chat.id)
#     bot.send_message(message.chat.id, message.text)

bot.polling()