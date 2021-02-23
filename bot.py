token = '******'

import vk_api
import random
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
import requests


url = 'http://wttr.in/?0t'
response = requests.get(url)

ids = []

def what_weather():
    url = f'http://wttr.in/Moscow\n'
    weather_parameters = {
        'format': 2,
        'M': '',
        'm': '',
	'2': '',
    }
    try:
       response = requests.get(url, params = weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<ошибка на сервере погоды>'
print(what_weather())
def Moon():
	u = 'http://wttr.in/Moscow?format="%m"\n'
	moon = requests.get(u)
	return moon.text[1]


def preasure():
    u = 'http://wttr.in/Moscow?format="%P"\n'
    Preasure = requests.get(u)
    return str(Preasure.text).replace('"', '')

def get_random_id():
    """ Get random int32 number (signed) """
    return random.getrandbits(31) * random.choice([-1, 1])




# API-ключ созданный ранее
token = token

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)


def write_msg(user_id, message, random_id):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        print(event.text)
        chek = event.user_id in ids
        if (str(event.text).lower() == "луна"):
            write_msg(event.user_id,f'{Moon()}',get_random_id())
        if (event.text == "давление"):
            write_msg(event.user_id,f'{preasure()}',get_random_id())
        if ((str(event.text).lower() != "давление") and (str(event.text).lower() != 'луна') and (str(event.text).lower() != 'погода')):
            write_msg(event.user_id,f'Напиши мне: погода, я расскажу, как сейчас в Москве',get_random_id())
        if (str(event.text).lower() == "погода"):
            write_msg(event.user_id,f'Привет, погода в Москве: {what_weather()}',get_random_id())
            ids.append(event.user_id)
        
	
	        
        
