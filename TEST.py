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
        else:  # Если нашёлся элемент в середине
            print("Number on the left: ", list1[i - 1], 'Number on the right : ', list1[i + 1])
            break
else:
    print('Number is not in the list')

