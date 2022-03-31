#!/usr/bin/python
# -*- coding: utf8 -*-

import telebot
from telebot import types
import random


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
