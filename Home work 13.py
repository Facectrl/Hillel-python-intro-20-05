translations = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}

inv_dict = {}

for key, value in translations.items():
    for i in value:
        if i in inv_dict:  # если значение в словаре есть
            inv_dict[i].append(key)
        else:
            inv_dict[i] = [key]
print(inv_dict)

# словарь translations имеет неуникальные значения 'malum' один из ключей затрётся в новом словаре.
# По этому использую метод append() для добавления значения в список.
