
"""
Называют один город, потом надо назвать город,
начинающийся с последней буквы названия предыдущего и так далее, пока города не кончатся.
Надо написать программу,
которая из набора названий городов (все названия разные) строит цепочку максимальной длины.
Запрещено повторять название городов.
Города пользователь вводит одним действием в виде строки, где города разделены пробелами.
"""

import random

cities = ['Киев  ', 'Львов  ', 'Одесса ', 'Днепропетровск',
          'Харьков ', 'Донецк ', 'Запорожье', 'Кривой Рог',
          'Полтава ', 'Чернигов ', 'Херсон ', 'Хмельницк'
          'Тернополь', 'Ужгород', 'Херсон ', 'Николаев ',
          'Хмельницкий', 'Александровка', 'Чернигов', 'Черновцы',
          'Антоновка', 'Белгород', 'Бровары', 'Волгодонск',
          'Гатчина', 'Дубно', 'Евпатория', 'Житомир','Ровно',
          'Винница','Кропивницк', 'Луцк', 'Львов', 'Миргород',
          ]

avialable_cities = list(cities)
random.shuffle(avialable_cities)  # перемешиваем города
first_city = avialable_cities.pop()
print(first_city)

while True:
    user = input('Введите название города: ')

    if user.lower()[0] != first_city.lower()[-1]:
       print('не верно, начинатся должен с буквы', first_city.lower()[-1])
    elif user not in cities:
        print('нет такого города')
    elif user not in avialable_cities:
        print('Город уже выбран')
    else:
        city_found = False
        avialable_cities.remove(user)  # удаляем город из доступных
        for city in avialable_cities:
            if city.lower()[0] == user.lower()[-1]:
                user = city
                avialable_cities.remove(city)
                print(city)
                city_found = True
                break
        else:
            print('Нет городов начинающихся с последней буквы', user[-1])
            city_found = True
            break

print('Ваша цепочка:', first_city, user)




