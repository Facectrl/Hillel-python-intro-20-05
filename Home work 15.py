# Алгоритм сортировки последовательности фибоначи циклом while

def fibonacci(n):
    series = []
    if n == 1:
        series = [0]
    else:
        series = [0, 1]
        count = 1
        while count < n:
            series.append(series[count-1] + series[count])
            count = count + 1
    return series


print(fibonacci(8))
"""
Рекурсия — это когда функция обращается к самой себе, чтобы разбить проблему,
которую она пытается решить.
При каждом вызове функции проблема становится меньше, пока не достигнет базового случая
"""
def fibonacci_recursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)  # вызов функции к самой себе.

for n in range(1, 9):
    print(n, ':', fibonacci_recursive(n))   # Супер медленный способ вычисления фибоначи.






