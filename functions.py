#!/usr/bin/python
# -*- coding: utf8 -*-

import telebot
from telebot import types
import random
import sqlite3


def kb_parts_of_speech():
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Существительные', callback_data='nouns')
    btn2 = types.InlineKeyboardButton(text='Прилагательные', callback_data='adjectives')
    btn3 = types.InlineKeyboardButton(text='Глаголы', callback_data='verbs')
    btn4 = types.InlineKeyboardButton(text='Причастия', callback_data='participles')
    btn5 = types.InlineKeyboardButton(text='Деепричастия', callback_data='gerunds')
    btn6 = types.InlineKeyboardButton(text='Наречия', callback_data='adverbs')
    btn7 = types.InlineKeyboardButton(text='Мои ошибки', callback_data='mistakes')
    kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    return kb


def dictionary():
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Существительные', callback_data='nouns_dic')
    btn2 = types.InlineKeyboardButton(text='Прилагательные', callback_data='adjectives_dic')
    btn3 = types.InlineKeyboardButton(text='Глаголы', callback_data='verbs_dic')
    btn4 = types.InlineKeyboardButton(text='Причастия', callback_data='participles_dic')
    btn5 = types.InlineKeyboardButton(text='Деепричастия', callback_data='gerunds_dic')
    btn6 = types.InlineKeyboardButton(text='Наречия', callback_data='adverbs_dic')
    btn7 = types.InlineKeyboardButton(text='Мои ошибки', callback_data='mistakes_dic')
    kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    return kb


def button_symbols(data1):
    if data1 == 'correct':
        return '✅', '❌'
    elif data1 == 'incorrect':
        return '❌', '✅'


def buttons_text(callback):
    if callback == 'correct':
        return 'Правильно!'
    else:
        return 'Неправильно!'


def get_words(part_of_speech):
    ret = []
    con = sqlite3.connect('users_database.db')
    cur = con.cursor()
    for row in cur.execute('''SELECT correct_word, incorrect_word FROM dict
                            WHERE part_of_speech = (?)''', (part_of_speech, )):

        ret.append({row[0]: 'correct', row[1]: 'incorrect'})
    return ret


def fill_results(user_id):
    con = sqlite3.connect('users_database.db')
    cur = con.cursor()
    info = cur.execute('SELECT * FROM results WHERE user_id=?', (user_id,))
    if info.fetchone() is None:
        words = []
        for row in cur.execute('''SELECT correct_word FROM dict'''):
            for word in row:
                words.append(word)
        for word in words:
            cur.execute('''INSERT INTO results VALUES (?, ?, ?, ?)''', (user_id, word, 0, 0))
    else:
        cur.execute('''UPDATE results SET correct == 0, incorrect = 0
                        WHERE user_id = (?)''', (user_id, ))
    con.commit()


def update_results_correct(user_id, correct_word):
    con = sqlite3.connect('users_database.db')
    cur = con.cursor()
    cur.execute('''SELECT correct FROM results WHERE word = :correct_word AND user_id = :user_id''',
                {"correct_word": correct_word, "user_id": user_id})
    number = int(cur.fetchone()[0])
    number += 1
    cur.execute('''UPDATE results SET correct ==:number 
                WHERE word =:word AND user_id=:user_id''',
                {"number": number, "user_id": user_id, "word": correct_word})
    con.commit()


def update_results_incorrect(user_id, correct_word):
    con = sqlite3.connect('users_database.db')
    cur = con.cursor()
    cur.execute('''SELECT incorrect FROM results WHERE word = :correct_word AND user_id = :user_id''',
                {"correct_word": correct_word, "user_id": user_id})
    number = int(cur.fetchone()[0])
    number += 1
    cur.execute('''UPDATE results SET incorrect ==:number 
                WHERE word =:word AND user_id=:user_id''',
                {"number": number, "user_id": user_id, "word": correct_word})
    con.commit()


def add_mistake(user_id, correct_word):
    con = sqlite3.connect('users_database.db')
    cur = con.cursor()
    cur.execute('''SELECT id FROM dict WHERE correct_word =:correct_word''',
                {"correct_word": correct_word})
    word_id = int(cur.fetchone()[0])
    info = cur.execute('''SELECT * FROM mistakes 
                        WHERE word_id =:word_id AND user_id = :user_id''',
                       {"word_id": word_id, "user_id": user_id})
    if info.fetchone() is None:
        cur.execute('''INSERT INTO mistakes (user_id, word_id) VALUES (:user_id, :word_id)''',
                    {"word_id": word_id, "user_id": user_id})
        con.commit()


def remove_mistake(user_id, correct_word):
    con = sqlite3.connect('users_database.db')
    cur = con.cursor()
    cur.execute('''SELECT id FROM dict WHERE correct_word =:correct_word''',
                {"correct_word": correct_word})
    word_id = int(cur.fetchone()[0])
    cur.execute('''DELETE FROM mistakes WHERE word_id =:word_id AND user_id =:user_id''',
                {"word_id": word_id, "user_id": user_id})
    con.commit()


def get_mistakes(user_id):
    ret = []
    con = sqlite3.connect('users_database.db')
    cur = con.cursor()
    cur.execute('''SELECT word_id FROM mistakes WHERE user_id =:user_id''', {"user_id": user_id})
    words_id = cur.fetchall()
    print(words_id)
    for ids in words_id:
        word_id = int(ids[0])
        print(word_id)
        cur.execute('''SELECT correct_word, incorrect_word FROM dict
                    WHERE id =:word_id''', {"word_id": word_id})
        pair = cur.fetchone()
        ret.append({pair[0]: 'correct', pair[1]: 'incorrect'})
    return ret


#def create_file_results(user_id):
