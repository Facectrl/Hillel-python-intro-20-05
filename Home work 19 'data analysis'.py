import csv


def key_value_func(dict_name: dict, key: str, value: int) -> dict:
    # функция для передачи key и value в словарь

    if key in dict_name:
        dict_name[key] += value
    else:
        dict_name[key] = value
    return dict_name


def percent_func(dict_name: dict, key: str, value: int):
    # функция для подсчета процентов продаж, сколько % пришлось на какой месяц

    if key in dict_name:
        dict_name[key] = round(dict_name[key] / value * 100, 2)  # 2 знака  после запятой
    else:
        dict_name[key] = 0
    return dict_name

    

with open(r"C:\Users\True\Documents\GitHub\Hillel-python-intro-20-05\Bakery.csv", newline='')as csvfile:
    bakery_reader = csv.reader(csvfile, delimiter=',')
    header = next(bakery_reader)  # первая строка игнорируется
    top_15_product = {}
    for row in bakery_reader:
        if row[1] not in top_15_product:
            top_15_product[row[1]] = 1
        else:
            top_15_product[row[1]] += 1
    top_15_product = sorted(top_15_product.items(), key=lambda x: x[1], reverse=True)  #
    print('Топ 15 популярных товаров: ', top_15_product[:15])
    print('\n')

with open(r"C:\Users\True\Documents\GitHub\Hillel-python-intro-20-05\Bakery.csv", newline='') as csvfile:
    bakery_reader = csv.reader(csvfile, delimiter=',')
    header = next(bakery_reader)  # первая строка игнорируется
    time_dict = {}
    for row in bakery_reader:
        if row[2][11:13] not in time_dict:
            time_dict[row[2][11:13]] = 1
        else:
            time_dict[row[2][11:13]] += 1
    time_dict = sorted(time_dict.items(), key=lambda x: x[0], reverse=True)  # отсортировали по ключу
    print('Распределение продаж по часам работы пекарни: ', time_dict)
    print('\n')

with open(r"C:\Users\True\Documents\GitHub\Hillel-python-intro-20-05\Bakery.csv", newline='') as csvfile:
    bakery_reader = csv.reader(csvfile, delimiter=',')
    header = next(bakery_reader)  # первая строка игнорируется
    item = header[1]  # первая колонка из файла - название товара
    day_Type = row[-1]  # день недели
    tea = {}
    coffee = {}
    for row in bakery_reader:
        if row[1] == 'Coffee' and day_Type == 'Weekend':
            key_value_func(coffee, day_Type, 1)
        elif row[1] == 'Coffee' and day_Type == 'Weekday':
            key_value_func(coffee, day_Type, 1)
        elif row[1] == 'Tea' and day_Type == 'Weekend':
            key_value_func(tea, day_Type, 1)
        elif row[1] == 'Tea' and day_Type == 'Weekday':
            key_value_func(tea, day_Type, 1)

    print('Количество продаж : ', tea)
    print('Количество продаж : ', coffee)
    print('\n')


