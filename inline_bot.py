# t.me/karazin261022_bot

from telebot import types
import telebot
from tokens import INLINE_API_TOKEN


bot = telebot.TeleBot(INLINE_API_TOKEN)

morze = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
         'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
         'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
         'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
         'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
         'z': '--..', '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....', '7': '--...',
         '8': '---..', '9': '----.', '0': '-----'}


@bot.inline_handler(func=lambda query: len(query.query) == 0)
def empty_query(query):
    hint = "Input letters or numbers!"
    msg = "Should be letters or numbers"
    try:
        r = types.InlineQueryResultArticle(id='1', title="Morze-bot", description=hint,
                                           input_message_content=types.InputTextMessageContent(message_text=msg))
        bot.answer_inline_query(query.id, [r])
    except Exception as e:
        print(e)


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    line = ''
    for x in query.query:
        try:
            line += morze[x]
            line += ' '
        except KeyError as ex:
            return
    res = types.InlineQueryResultArticle(id='1', title="Morze code", description = "Result: {!s}".format(line),
    input_message_content = types.InputTextMessageContent(message_text="{!s}".format(line)))
    bot.answer_inline_query(query.id, [res])


bot.polling()