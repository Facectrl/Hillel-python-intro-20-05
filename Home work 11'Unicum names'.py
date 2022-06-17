names = input("Enter a list of names: ")
names = names.split(' ')
names = [name.strip() for name in names]  #  удалить пробелы вначале и в конце
unique_names = [] #  список уникальных имен
for name in names:
    if name in unique_names:
        unique_names.append(name)
print(unique_names)






# Пользователь вводит список имен (например, детей в классе).
# Просто имена, вроде "Вася, Маша, /,...".
# Вам нужно вывести на экран те имена, которые встретились только ЕДИНОЖДЫ.
# То есть имена детей без тезки.
# Решается с помощью цикла и множества (set).