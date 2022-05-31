# Home Work 4
num = int(input('Enter number:'))
elementary = True  #  Если число простое = истина
counter = 2  # Начинаем с 2
while counter < num:
    if num % counter == 0:  # остаток от деления
        elementary = False  # иначе сложное
    counter += 1
    break
if elementary:
    print('Number is prime')
else:
    print('Number is not prime')
