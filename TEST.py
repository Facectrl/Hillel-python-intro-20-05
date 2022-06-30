import random

cities = ['Киев', 'Львов', 'Одесса', 'Днепропетровск',
          'Харьков', 'Донецк', 'Запорожье', 'Кривой Рог',
          'Полтава', 'Чернигов', 'Херсон', 'Хмельницк',
          'Тернополь', 'Ужгород', 'Херсон ', 'Николаев',
          'Хмельницкий', 'Александровка', 'Чернигов', 'Черновцы',
          'Антоновка', 'Белгород', 'Бровары', 'Волгодонск',
          'Гатчина', 'Дубно', 'Евпатория', 'Житомир','Ровно',
          'Винница', 'Кропивницк', 'Луцк', 'Львов', 'Миргород',
          ]

avialable_cities = list(cities)
random.shuffle(avialable_cities)  # перемешиваем города
answer_city = avialable_cities.pop()   # город для ответа пользователю
print(answer_city)


while True:
    user = input('Введите название города: ')

    if user.lower()[0] != answer_city.lower()[-1]:
        print('не верно,город начинаться должен с буквы -->', avialable_cities.pop()[-1])
        continue
        break
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
        

print('Ваша цепочка:', answer_city, user)
