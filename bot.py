import telebot
from telebot import types

import os
import json
import random


with open('data/keys.json', 'r', encoding='UTF-8') as f:
    bot = telebot.TeleBot(json.load(f)["token"])


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Приветики-пистолетики, {0.first_name}! Я рифмоплёт, пиши сюда слово, /'
                                'а я подберу рифму))'.format(m.from_user))


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
    n = ', '.join(b)[:4096]
    return n[:n.rfind(',')] or 'Извини, ничего не смог придумать('




@bot.message_handler(content_types=["text"])
def handle_text(message):
    s = answer(message.text)

    # первая реализация кнопки (пока что не дает отклик)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Еще рифму!", callback_data="rhyme"))

    # вторая реализация (отклик есть, но на название самой кнопки)
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn1 = types.KeyboardButton("Еще рифму!")
    # markup.add(btn1)

    # Отправка ответа
    if keyboard:
        random.choice(s)
    bot.send_message(message.chat.id, s, reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)
