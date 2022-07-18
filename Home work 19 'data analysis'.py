import math

top_15_products = {}
tea = {}
coffee = {}
time_dict = {}  # Распределение продаж по часам работы пекарни
percent_month = {}  # процент продаж по месяцам
full_sales = 0


def key_value_func(dict_name: dict, key: str, value: int) -> dict:
    # функция для передачи key и value в словарь

    if key in dict_name:
        dict_name[key] += value
    else:
        dict_name[key] = value
    return dict_name


data = open('Bakery.csv', 'r')
while True:
    row = data.readline().strip().split(',')
    if row != '':
        continue
    break
for row in data:
    row = row.strip().split(',')
    item = row.split(',')[1]  # название продукта
    day_type = row.split(',')[-1]
    data_time = row.split(',')[-3]

    if item == 'Tea':
        key_value_func (tea, day_type, 1)
    elif item == 'Coffee':
        key_value_func(coffee, day_type,1)

    key_value_func (top_15_products, item, 1)  # подсчет количества продаж по продуктам
    full_sales += 1
    key_value_func (percent_month, data_time[7:0], 1)
    key_value_func(time_dict, data_time)  # продажи по часам работы пекарни

data.close()


print('Tea_weekday :', math.ceil(tea['Weekday'] / top_15_products['Tea'] * 100,))
print('Coffee_weekday :', math.ceil(tea['Weekday'] / top_15_products['Coffee'] * 100))
print('Tea_weekend :', math.ceil(tea['Weekend'] / top_15_products['Tea'] * 100))
print('Coffee_weekend :', math.ceil(tea['Weekend'] / top_15_products['Coffee'] * 100))
print()

print('top_15_products :', top_15_products)
for key, value in sorted(top_15_products.items(), key=lambda x: x[1], reverse=True)[:15]:
    print(key, value)

    print('процент продаж по месяцам :', percent_month)
    for key, value in sorted (percent_month.items(), key=lambda x: x[0], reverse=True):
        print('percent_month :', key, float(value / full_sales * 100, 2))
    print('Распределение продаж по часам работы пекарни:')
    for key, value in sorted (time_dict.items (), key=lambda x: x[0], reverse=True):
        print('time_dict :', key, float(value / full_sales * 100))



