import csv
import math

# Файл - .csv (таблица), что значит, что колонки (данные) разделены запятой (в большинстве случаев, как и тут).
# Есть встроенный модуль csv, что позволяет удобно работать с такими файлами,
# но можете просто читать файл и разбивать колонки по запятой.
# Надо вывести немного статистики по этому файлу, а именно:
# Как часто люди берут кофе и чай в: А - выходные, Б - будние
# Топ-15 популярных товаров
# Распределение продаж по месяцам (сколько % на какой месяц пришлось)
# Распределение продаж по часам работы пекарни


def add_to_dict(dict_name: dict, key: str, value: int):  # добавляем в словарь ключ и значение

    if key in dict_name:  # добавляем к значению ключа,value
        dict_name[key] += value
    else:
        dict_name[key] = value # иначе добавляем ключ и значение
        return dict_name


top_15_product = dict()  #
sales_month = dict()  # для подсчета процентов продаж, сколько % пришлось на какой месяц
sales_hour_bakery = dict()  # для подсчета продаж по часам работы пекарни
tea_sale = dict()  # для подсчета продаж чая
coffee_sale = dict()  # Переменная для подсчета продаж кофе
profit = 0   # Переменная для подсчета общего прибыли. 0 для проверки на пустоту переменной

with open("Bakery.csv", 'r', newline='') as csvfile:
    bakery_reader = csv.reader(csvfile, delimiter=',')  # delimiter - разделитель колонок в файле
    for row in bakery_reader:
        if not row or row[0] == '':    # Если пустая строка или первая строка, то пропускаем ее
            continue

while True:
    row = csvfile.readline() # прочитали одну строку из файла и удалили пробелы и  строк
    if not row:
        continue

for row in bakery_reader:
    if row[1] not in top_15_product:
       top_15_product[row[1]] = 1
    else:
        top_15_product[row[1]] += 1
    top_15_product = sorted (top_15_product.items (), key=lambda x: x[1], reverse=True)
    print('Топ-15 популярных товаров :', top_15_product[:15])
    print('\n')



with open(r"C:\[Users\True\Documents\GitHub\Hillel-python-intro-20-05\Bakery.csv", newline='') as csvfile:
# Распределение продаж по часам работы пекарни
    reader = csv.reader(csvfile, delimiter=',')  # Создал объект для чтения файла с разделителем между колонами
    header = next(reader)
    for row in reader:
        if row[1] == 'Чай':
            if row[2] not in tea_sale:
                tea_sale[row[2]] = 1
            else:
                tea_sale[row[2]] += 1
        elif row[1] == 'Кофе':
            if row[2] not in coffee_sale:
                coffee_sale[row[2]] = 1
            else:
                coffee_sale[row[2]] += 1









