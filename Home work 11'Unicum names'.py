names = [input("Enter a list of names: ").split()]
seen = set()  # Словарь для подсчета количества повторений
duplicate = set()
for name in names[0]: # Подсчет количества повторений

    if name in seen:  # Если имя повторяется в списке  добавляем в список дубликатов
        duplicate.add(name)
    seen.add(name)
    print("Duplicate names: ", duplicate)
print("Unique names: ", seen - duplicate)





# Пользователь вводит список имен (например, детей в классе).
# Просто имена, вроде "Вася, Маша, /,...".
# Вам нужно вывести на экран те имена, которые встретились только ЕДИНОЖДЫ.
# То есть имена детей без тезки.
# Решается с помощью цикла и множества (set).