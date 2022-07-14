# Сгенерировать список случайных целых чисел от 0 до N (N вводит пользователь).
# После этого он еще может ввести число,
# которое программа должна постараться найти в списке и вывести на экран его соседей (числа слева и справа).
# Если оно стоит в начале или конце, то очевидно сосед будет только
# 1. Если введённого числа не было в списке то так об этом и написать на экране.
# Для решения может понадобиться написать цикл с поиском элемента и использовать индексы.
# Индексы в цикле можно получить функцией enumerate.


import random

N = int(input('Enter number: '))
list1 = [random.randint(0, N) for i in range(0, N)]  # Сгенерировать список случайных целых чисел от 0 до N
print('Random number list is: ', list1)
X = int(input('Enter number to find: '))
for i, l1 in enumerate(list1):  # Индексы в списке
    if l1 == X:  # Проверка есть ли число в списке
        if i == 0:  # if begin
            print('Number begin in list:', list1[i + 1])
        elif i == len(list1) - 1:  # end
            print('Number end in list:', list1[i - 1])
        else:  #
            print("Number on the left: ", list1[i - 1], 'Number on the right : ', list1[i + 1])
            break
else:
    print('Number is not in the list')
