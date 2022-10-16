import os
os.system('cls' if os.name == 'nt' else 'clear')
import mrtxee

'''
# Walrus operator - Моржовый оператор
#num = int(input())
#print(num)
#тоже самое что ти
#print(num:=int(input())) 

# синтаксический сахар for ... else
contacts = [
    ('James', 42),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18),
    ('Amy', 24)
]
n='Amy'
for trumple in contacts:
    if n in trumple:
        print(f'{n} is {trumple[1]}')
        break
else:
    print('not found')

# прикольный способ подставлять данные в строку
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

list = [1, 1, 2, 3, 5, 8, 13]
list = list[::-1] # список задом на перед
input = input('Как тебя зовут? ')
print (f'Привет, {input}')

print("""this
is a 
\' \t\t multiline
text""")

import requests
import json
def explore_obj(o):
    data = {
        "type"      : str(type(o))
        ,"id"       : str(id(o))
        ,"struct"   : json.loads( str(dir(o)).replace('\'','"') )
        }
    print(json.dumps(data, indent=4))

url = 'https://wttr.in/spb'
weather_parameters = {
    '0': '',
    'T': ''
}
request_headers = {
    'Accept-Language': 'ru'
}
response = requests.get(url, params=weather_parameters, headers=request_headers)
explore_obj(response)
#доступен клик правой кнопки мыши для того, чтобы провалиться в дефиницию классов
print ( response.url )
#print ( response.text )

import datetime as dt
# подключите библиотеку datetime под именем dt

start_moment = dt.datetime(2022, 10, 10, 11, 5)
current_moment = dt.datetime(2022, 10, 11, 12, 7)

for i in range(0,100):
    print (i)

total_time = current_moment-start_moment

print(total_time)


DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

# Новая функция, она возвращает правильное словосочетание, склоняя слово "друзья" 
# в зависимости от того, какое число передано в аргументе friends_count
def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        # Вызовите функцию format_friends_count() и передайте в неё count.
        # Отредактируйте строку ниже: в ней должно использоваться выражение, 
        # которое вернёт функция format_friends_count()
        return f'У тебя {format_friends_count(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'

def process_query(query):
    query_list = query.split(', ')
    if 'Анфиса' == query_list[0]:
        return process_anfisa(query_list[1])
    else:
        return process_friend(query_list[0], query_list[1])

def process_friend(name, query):
    if name in DATABASE.keys():
        if 'ты где?' == query:
            return f'{name} в городе {DATABASE[name]}'
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'

print('Привет, я Анфиса!')
print(process_query('Анфиса, сколько у меня друзей?'))
print(process_query('Анфиса, кто все мои друзья?'))
print(process_query('Анфиса, где все мои друзья?'))
print(process_query('Анфиса, кто виноват?'))
print(process_query('Соня, ты где?'))
print(process_query('Коля, что делать?'))
print(process_query('Антон, ты где?')) 

def show_meteo(temperature, weather):
    print(f'Сейчас {weather}, на градуснике {str(temperature)}.')

show_meteo(24, 'облачно')


DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}
print (DATABASE.keys())
str=' ||| kfkfkf ||| '
print( str.join(DATABASE.keys() ) )


friends = {
    'Серёга': 'Омск', 
    'Соня': 'Москва', 
    'Дима': 'Челябинск', 
    'Алина': 'Хабаровск', 
    'Егор': 'Пермь'
}

for friend in friends:
    print(friend)
    print(friends[friend])

friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']
# Объявлен пустой словарь, его нужно будет наполнить элементами, 
# каждый из которых составлен по схеме "имя: город"
friends =  {}
# Допишите ваш код сюда
print(friends_names[0])
print(len(friends_names))
for i in range(0,len(friends_names)):
    friends[friends_names[i]]=friends_cities[i]
print(friends)

print('hello world!')

def me():
    print('hello world! from me')

favorite_songs = {
    'Тополиный пух': 'Иванушки international',
    'Город золотой': 'Аквариум',
    'Звезда по имени Солнце': 'Кино',
    'Группа крови': 'Кино'
}
for track in favorite_songs:
    print(track + ' :: ' + favorite_songs[track])

friends =  {
    'Серёга': 'Оренбург',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}
cities = set(friends.values())
print(cities)

import this #философия питона, пасхалка
'''