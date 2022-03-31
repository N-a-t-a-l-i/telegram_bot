#!/usr/bin/python
# -*- coding: utf8 -*-

import telebot
from telebot import types
from constants import *
import random
from functions import kb_parts_of_speech, dictionary, button_symbols, buttons_text


bot = telebot.TeleBot('5190118002:AAGM1A41EYRaD9zZlv8-pKDD-Ph3hg1smzo')


@bot.message_handler(commands=["start"])
def send_hello(message):
    kb = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    bt1 = types.KeyboardButton(text='Открыть словарь')
    bt2 = types.KeyboardButton(text='Результаты тренировок')
    bt3 = types.KeyboardButton(text='Начать тренировку')
    kb.add(bt1, bt2, bt3)
    bot.send_message(message.from_user.id,
                     'Привет! Если хочешь сначала узнать, какие слова могут встретиться на экзамене, открой словарь. '
                     'Чтобы перейти к упражнениям, выбери "начать тренировку". В разделе "результаты тренировок" '
                     'ты можешь увидеть свою статистику и оценить, какие слова не нуждаются в повторении, а какие'
                     ' стоит повторить.',
                     reply_markup=kb)


@bot.message_handler(content_types='text')
def send_message(message):
    if message.text == 'Открыть словарь':
        kb = dictionary()
        bot.send_message(message.from_user.id, 'Выбери нужный раздел.', reply_markup=kb)
    elif message.text == 'Результаты тренировок':
        with open('results.txt', 'w') as file:
            file.write('Слово'.ljust(20)+'Правильные ответы'.ljust(20)+'Неправильные ответы'.ljust(20)+'\n'*5)
            for key in all_vars.keys():
                file.write(all_vars[key][2] + '\n\n')
                for word, value in all_vars[key][1].items():
                    file.write(word.ljust(20) + " " + str(value[0]).ljust(20) + " " + str(value[1]).ljust(20) + "\n")
                file.write('\n\n')
        with open('results.txt', 'rb') as results:
            bot.send_document(message.from_user.id, results)
    elif message.text == 'Начать тренировку':
        kb = kb_parts_of_speech()
        bot.send_message(message.from_user.id, 'Выбери режим тренировки', reply_markup=kb)


cnt = 0
number = 0
word1 = ''
word2 = ''
data1 = ''
data2 = ''
current_list = []
mistakes = []


@bot.callback_query_handler(func=lambda callback: callback.data)
def answer_callback(callback):

    global cnt
    global word1
    global word2
    global data1
    global data2
    global current_list
    global number

    if callback.data in list(all_vars.keys()) or callback.data == 'mistakes':
        if callback.data == 'mistakes':
            current_list = tuple(mistakes)
            if len(current_list) == 0:
                kb = kb_parts_of_speech()
                bot.send_message(callback.from_user.id, 'У тебя пока нет ошибок, выбери другой раздел', reply_markup=kb)
                return
        else:
            current_list = all_vars[callback.data][0]
        cnt = 0
        number = len(current_list)

        current_pair = current_list[cnt]
        word1 = random.choice(list(current_pair.keys()))
        data1 = current_pair[word1]
        if list(current_pair.keys())[0] == word1:
            word2 = list(current_pair.keys())[1]
        else:
            word2 = list(current_pair.keys())[0]
        data2 = current_pair[word2]

        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text=word1, callback_data=data1)
        btn2 = types.InlineKeyboardButton(text=word2, callback_data=data2)
        kb.add(btn1, btn2)
        bot.send_message(callback.from_user.id, f'Слово №{cnt + 1} из {number}.', reply_markup=kb)
        cnt += 1

    elif callback.data in ['correct', 'incorrect']:
        new_dic = {
            word1: data1,
            word2: data2,
        }
        if data1 == 'correct':
            correct_word = word1
        else:
            correct_word = word2

        if callback.data == 'incorrect':
            if new_dic not in mistakes:
                mistakes.append(new_dic)

            for value in all_vars.values():
                results = value[1]
                if correct_word in results.keys():
                    results[correct_word][1] += 1
        else:
            if new_dic in mistakes:
                mistakes.remove(new_dic)
            for value in all_vars.values():
                results = value[1]
                if correct_word in results.keys():
                    results[correct_word][0] += 1

        text = buttons_text(callback.data)
        symbol1, symbol2 = button_symbols(data1)
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text=f'{word1} {symbol1}', callback_data='data1')
        btn2 = types.InlineKeyboardButton(text=f'{word2} {symbol2}', callback_data='data2')
        kb.add(btn1, btn2)
        bot.edit_message_text(chat_id=callback.message.chat.id,
                              message_id=callback.message.id,
                              text=text,
                              reply_markup=kb)

        if cnt == number:
            kb2 = kb_parts_of_speech()
            bot.send_message(callback.from_user.id,
                             f'Отлично, это все слова в этом разделе! Я запомнил твои ошибки, '
                             f'чтобы повторить их, выбери раздел "Мои ошибки".',
                             reply_markup=kb2)
            cnt = 0
            return

        current_pair = current_list[cnt]
        word1 = random.choice(list(current_pair.keys()))
        data1 = current_pair[word1]
        if list(current_pair.keys())[0] == word1:
            word2 = list(current_pair.keys())[1]
        else:
            word2 = list(current_pair.keys())[0]
        data2 = current_pair[word2]

        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text=word1, callback_data=data1)
        btn2 = types.InlineKeyboardButton(text=word2, callback_data=data2)
        kb.add(btn1, btn2)
        bot.send_message(callback.from_user.id, f'Слово №{cnt + 1} из {number}.', reply_markup=kb)
        cnt += 1

    elif callback.data in ['nouns_dic', 'adjectives_dic', 'verbs_dic', 'participles_dic', 'gerunds_dic', 'adverbs_dic']:
        path = 'images/' + callback.data + '.png'
        photo = open(path, 'rb')
        bot.send_photo(callback.from_user.id, photo)
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Тренировка', callback_data=callback.data[:-4])
        kb.add(btn1)
        bot.send_message(callback.from_user.id, text='Хочешь лучше запомнить эти слова?', reply_markup=kb)


bot.polling()
