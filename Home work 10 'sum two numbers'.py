# Создается список случайных целых чисел от 0 до N (N вводит пользователь).
# После - пользователь вводит X, а вам нужно найти и вывести индексы ДВУХ чисел из списка, которые в сумме дают введенный X.
# Детальнее условия задачки с примером есть тут: https://leetcode.com/problems/two-sum/
# Так как список случайный будет, то таких пар чисел может быть несколько - просто найдите первую встречную.
# Там же можно найти решения, если хотите, но не надо брать сложные решения со структурами, которые мы еще не рассматривали.
# Достаточно циклов.
import random

N = int(input('Enter number: '))
list1 = [random.randint(0, N) for i in range(0, N)]
print('Random number in list: ', list1)
X = int(input('Enter X: '))
for i, l1 in enumerate(list1):
    for j, l2 in enumerate(list1):
        if l1 + l2 == X:
            print(i, j)
            continue
        else:
            break






