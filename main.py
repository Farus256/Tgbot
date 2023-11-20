import requests
import telebot
import openpyxl
from bs4 import BeautifulSoup as BS
import pandas as pd

r = requests.get(
    "https://cist.nure.ua/ias/app/tt/f?p=778:201:3400382984981548:::201:P201_FIRST_DATE,P201_LAST_DATE,P201_GROUP,P201_POTOK:01.09.2023,31.01.2024,10284283,0:")
html = BS(r.content, 'html.parser')
bot = telebot.TeleBot('6018279911:AAEbo3c1bERNtS9qs_Qk2bnRycRhC6x6avE')
title1 = html.select('.linktt')

#print(title1[].text)
print(pd.__version__)
wb = openpyxl.load_workbook('ODA.xlsx')
sheet = wb['ІТІНФ-22-3']
value = sheet['F13'].value


print(value)

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} </b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler()
def info(message):
    if message.text == "расписание":
        title = html.select('.linktt')

        cnbt = html.select('.left')
        date = html.select('.date')
        print(cnbt[0].text)
        bot.send_message(message.chat.id, f'{date[3].text}')
        bot.send_message(message.chat.id,
                         f'Пара номер: {cnbt[0].text} \nПредмет: {title[2].text}  \nВремя: {cnbt[1].text}')
        bot.send_message(message.chat.id,
                          f'Пара номер: {cnbt[2].text} \nПредмет: {title[2].text} \nВремя: {cnbt[3].text}')
        bot.send_message(message.chat.id,
                          f'Пара номер: {cnbt[4].text} \nПредмет: {title[5].text} \nВремя: {cnbt[5].text}')
        bot.send_message(message.chat.id,
                          f'Пара номер: {cnbt[6].text} \nПредмет: {title[6].text} \nВремя: {cnbt[7].text}')






bot.polling(none_stop=True)
