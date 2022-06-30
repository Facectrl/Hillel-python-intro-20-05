
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
          'Полтава ', 'Севастополь', 'Симферополь', 'Сумы ',
          'Тернополь', 'Ужгород', 'Херсон ', 'Николаев ',
          'Хмельницкий', 'Черкассы', 'Чернигов', 'Черновцы'
          'Антоновка', 'Белгород', 'Бровары', 'Волгодонск',
          ]

avialable_cities = list(cities)
random.shuffle(avialable_cities)  # перемешиваем города
first_city = avialable_cities.pop()
print(first_city)

while True:
    user = input()

    if user.lower()[0] != first_city.lower()[-1]:
       print('не верно, начинатся должен с буквы', first_city[-1])
    elif user not in cities:
        print('нет такого города')
    elif user not in avialable_cities:
        print('Город уже выбран')
    else:
        avialable_cities.remove(user)  # удаляем город из доступных
        for city in avialable_cities:
            if city.lower()[0] == user.lower()[-1]:
                user = city
                avialable_cities.remove(city)
                print(city)
                break



print('Ваша цепочка:', first_city, user)




