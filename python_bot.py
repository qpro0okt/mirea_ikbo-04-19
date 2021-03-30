from vk_api import vk_api,VkUpload
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import requests
from vk_api.longpoll import  VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import json
import bitcoin_value as bitcoin
import COVID19Py
vk_session = vk_api.VkApi(token = 'eae5639d93f80a7e930a970547188dba4cdaabcf9a13b11b1f492e9d0a09af53436ffcc149314e00a8d98')


Users = {}
covid19 = COVID19Py.COVID19()

def sendmsg(message, user_id):
    vk.messages.send(user_id = event.user_id, random_id = get_random_id(), message = message)

"""Погода"""


response1 = requests.get("http://api.openweathermap.org/data/2.5/weather?q=moscow&appid=3ca717606dc59ad438b5d8ff39475f5a&units=metric&lang=ru")
info = response1.json()

response1 = requests.get("https://blockchain.info/ticker")
info3 = response1.json()

response2 = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=Moscow,ru&mode=json&appid=3ca717606dc59ad438b5d8ff39475f5a&units=metric&lang=ru")
info2 = response2.json()

"""Обработка страницы"""


def StartKey(): #функция, осуществляющая начало диалога
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Начать', color=VkKeyboardColor.POSITIVE)
    return keyboard

def MainKey(): #функция, выводящая меню
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Погода', color = VkKeyboardColor.POSITIVE)
    keyboard.add_button('Курс биткоина', color = VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Коронавирус', color = VkKeyboardColor.NEGATIVE)
    vk.messages.send(user_id=event.user_id, random_id=get_random_id(), keyboard=keyboard.get_keyboard(), message = 'Выберите функцию')


def PogoKey(): #эта функция выдаёт информацию о погоде
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Сейчас', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('На сегодня', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('На завтра', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('На 5 дней', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Меню', color=VkKeyboardColor.POSITIVE)
    vk.messages.send(user_id=event.user_id, random_id=get_random_id(), keyboard=keyboard.get_keyboard(),
                     message='Показать погоду...')

def CoronaKey(): #эта функция выдаёт статистику по covid-19
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Россия', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Украина', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('США', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Во всем мире', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Меню', color=VkKeyboardColor.POSITIVE)
    vk.messages.send(user_id=event.user_id, random_id=get_random_id(), keyboard=keyboard.get_keyboard(),
                     message='Показать статистику...')

def BitcoinKey(): #эта функция выдаёт текущий курс биткоина
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Рублю', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Доллару', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Евро', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Фунту', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Меню', color=VkKeyboardColor.POSITIVE)
    vk.messages.send(user_id=event.user_id, random_id=get_random_id(), keyboard=keyboard.get_keyboard(),
                     message='Показать курс биткоина к...')




def ShowWeatherDay(start,end): #вспомогательная функция вывода погоды
    ans = []
    ans = 'УТРО\n'
    ans += 'Описание: ' + info2['list'][start+2]['weather'][0]['description']
    ans += '\n' + "Температура утром: " + str(round(info2['list'][start+2]['main']['temp'])) + ' °C'
    ans += '\n' + 'Давление: ' + str(info2['list'][start+2]["main"]["pressure"]*0.75) + " мм рт. столба"
    ans += '\n' + "Влажность: " + str(info2['list'][start+2]["main"]["humidity"]) + "%"
    ans += '\n' + "Скорость ветра: " + str(info2['list'][start+2]["wind"]["speed"]) + " м\с" + '\n'
    ans += '\n'
    ans += 'ДЕНЬ\n'
    ans += 'Описание: ' + info2['list'][start+4]['weather'][0]['description']
    ans += '\n' + "Температура утром: " + str(round(info2['list'][start+4]['main']['temp'])) + ' °C'
    ans += '\n' + 'Давление: ' + str(info2['list'][start+4]["main"]["pressure"]*0.75) + " мм рт. столба"
    ans += '\n' + "Влажность: " + str(info2['list'][start+4]["main"]["humidity"]) + "%"
    ans += '\n' + "Скорость ветра: " + str(info2['list'][start+4]["wind"]["speed"]) + " м\с" + '\n'
    ans += '\n'
    ans += 'ВЕЧЕР\n'
    ans += 'Описание: ' + info2['list'][start+6]['weather'][0]['description']
    ans += '\n' + "Температура утром: " + str(round(info2['list'][start+6]['main']['temp'])) + ' °C'
    ans += '\n' + 'Давление: ' + str(info2['list'][start+6]["main"]["pressure"]*0.75) + " мм рт. столба"
    ans += '\n' + "Влажность: " + str(info2['list'][start+6]["main"]["humidity"]) + "%"
    ans += '\n' + "Скорость ветра: " + str(info2['list'][start+6]["wind"]["speed"]) + " м\с" + '\n'
    ans += '\n'
    ans += 'НОЧЬ\n'
    ans += 'Описание: ' + info2['list'][start+8]['weather'][0]['description']
    ans += '\n' + "Температура утром: " + str(round(info2['list'][start+8]['main']['temp'])) + ' °C'
    ans += '\n' + 'Давление: ' + str(info2['list'][start+8]["main"]["pressure"]*0.75) + " мм рт. столба"
    ans += '\n' + "Влажность: " + str(info2['list'][start+8]["main"]["humidity"]) + "%"
    ans += '\n' + "Скорость ветра: " + str(info2['list'][start+2]["wind"]["speed"]) + " м\с" + '\n'
    sendmsg(ans,event1.user_id)

def Weather5Day():#вспомогательная функция вывода погоды
    sendmsg("Погода в Москве с " + info2["list"][0]["dt_txt"][5:10:1] + " по " + info2["list"][39]["dt_txt"][5:10:1],event1.user_id)
    pic = []
    day = []
    night = []
    i = 3
    while i < 40:
        night.append(info2["list"][i+4]["main"]["temp"])
        day.append(info2["list"][i]["main"]["temp"])
        i += 8
    pic = 'Температура днем\n'
    for j in day:
        pic += str(round(j)) + ' °C ' + ' // '
    pic += '\nТемпература ночью\n'
    for j in night:
        pic += str(round(j)) + ' °C ' + ' // '
    sendmsg(pic,event1.user_id)

def Covid_by_country(location):#вспомогательная функция вывода статистики по covid-19
    date = location[0]['last_updated'].split("T")
    time = date[1].split(".")
    return f"Данные по стране:\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n" \
				f"Заболевших: {location[0]['latest']['confirmed']:,}\nСмертей: " \
				f"{location[0]['latest']['deaths']:,}"






#реализация взаимодействия с API VK
longpool = VkLongPoll(vk_session)
vk = vk_session.get_api()
swap = False
for event1 in longpool.listen():    
    Users[event1.user_id] = {}
    Users[event1.user_id]["ID"] = event1.user_id

    vk.messages.send(user_id=event1.user_id, random_id=get_random_id(), keyboard=StartKey().get_keyboard(),
                     message="Для начала работы нажмите кнопку начать")
    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.text.lower() == 'начать' or event.text.lower() == 'меню':
                sendmsg('Введите погода, чтобы узнать погоду\nВведите коронавирус, чтобы получить статистику',event.user_id)
                MainKey()


            elif event.text.lower() == 'serlialization':
                json.dump(Users, open("Users.json","w"))

            elif event.text.lower() == "погода":
                PogoKey()

            elif event.text.lower() == "сейчас":
                Ans = 'Описание: ' + info['weather'][0]['description']
                Ans += '\n' + " В Москве температура " + str(round(info['main']['temp'])) + ' °C'
                Ans += '\n' + 'Давление: ' + str(info["main"]["pressure"]*0.75) + " мм рт. столба"
                Ans += '\n' + "Влажность: " + str(info["main"]["humidity"]) + "%"
                Ans += '\n' + "Скорость ветра: " + str(info["wind"]["speed"]) + " м\с"
                sendmsg(Ans,event.user_id)
                PogoKey()

            elif event.text.lower() == "на завтра":
                ShowWeatherDay(8,16)
                PogoKey()

            elif event.text.lower() == "на сегодня":
                ShowWeatherDay(0,8)
                PogoKey()

            elif event.text.lower() == "на 5 дней":
                Weather5Day()
                PogoKey()
            elif event.text.lower() == "коронавирус":
                CoronaKey()
            elif event.text.lower() == "сша":          
                sendmsg(Covid_by_country(covid19.getLocationByCountryCode('US')), event.user_id)
                CoronaKey()
            elif event.text.lower() == "украина":          
                sendmsg(Covid_by_country(covid19.getLocationByCountryCode('UA')), event.user_id)
                CoronaKey()
            elif event.text.lower() == "россия":          
                sendmsg(Covid_by_country(covid19.getLocationByCountryCode('RU')), event.user_id)
                CoronaKey()
            elif event.text.lower() == "во всем мире":
                location = covid19.getLatest()
                final_message = f"Данные по всему миру:\nЗаболевших: {location['confirmed']:,}\nСмертей: {location['deaths']:,}"
                sendmsg(final_message, event.user_id)
                CoronaKey()
            elif event.text.lower() == "курс биткоина":
                BitcoinKey()
            elif event.text.lower() == "доллару":
                final_message = '1 BTC = ' + str(info3['USD']['last']) + ' ' + str(info3['USD']['symbol'])
                sendmsg(final_message, event.user_id)
                BitcoinKey()
            elif event.text.lower() == "рублю":
                final_message = '1 BTC = ' + str(info3['RUB']['last']) + ' ' + str(info3['RUB']['symbol'])
                sendmsg(final_message, event.user_id)
                BitcoinKey()
            elif event.text.lower() == "евро":
                final_message = '1 BTC = ' + str(info3['EUR']['last']) + ' ' + str(info3['EUR']['symbol'])
                sendmsg(final_message, event.user_id)
                BitcoinKey()
            elif event.text.lower() == "фунту":
                final_message = '1 BTC = ' + str(info3['GBP']['last']) + ' ' + str(info3['GBP']['symbol'])
                sendmsg(final_message, event.user_id)
                BitcoinKey()
            else:
                sendmsg('Не понял команду, попробуйте заново', Users[event.user_id]["ID"])
                MainKey()

