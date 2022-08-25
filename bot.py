import telebot
import os
import json

with open('data/keys.json', 'r', encoding='UTF-8') as f:
    bot = telebot.TeleBot(json.load(f)["token"])


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Приветики-пистолетики. Я рифмоплёт, пиши сюда слово, а я подберу рифму))')


mas = []
if os.path.exists('data/dict.txt'):
    with open('data/dict.txt', 'r', encoding='UTF-8') as f:
        for x in f:
            if(len(x.strip()) > 1):
                mas.append(x.strip())

import random
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
    # Отправка ответа
    bot.send_message(message.chat.id, s)


bot.polling(none_stop=True, interval=0)
