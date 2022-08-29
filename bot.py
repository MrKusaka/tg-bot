import telebot
from telebot import types

import os
import json
import random


with open('data/keys.json', 'r', encoding='UTF-8') as f:
    bot = telebot.TeleBot(json.load(f)["token"])


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Приветики-пистолетики, {0.first_name}! Я рифмоплёт, пиши сюда слово,'
                                      ' а я подберу рифму))'.format(message.from_user))


mas = []
if os.path.exists('data/dict.txt'):
    with open('data/dict.txt', 'r', encoding='UTF-8') as f:
        for x in f:
            if(len(x.strip()) > 1):
                mas.append(x.strip())


def answer(text):
    text = text.strip()
    b = []
    for q in mas:
        if text[-2:] == q[-2:]:
            b.append(q)
    random.shuffle(b)
    n = ', '.join(b)[:512]
    return n[:n.rfind(',')] or 'Извини, ничего не смог придумать('


@bot.message_handler(content_types=["text"])
def handle_text(message):
    s = answer(message.text)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Еще рифму!", callback_data=message.text))
    bot.send_message(message.chat.id, s, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.answer_callback_query(call.id)
    if call.message:
        keyboard1 = types.InlineKeyboardMarkup()
        keyboard1.add(types.InlineKeyboardButton(text="Больше!", callback_data=call.data))
        bot.send_message(call.message.chat.id, answer(call.data), reply_markup=keyboard1)


bot.polling(none_stop=True, interval=0)
