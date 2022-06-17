# Home Work 4
num = int(input('Enter number:'))
elementary = num >= 2  #  Если число простое = истина
counter = 2  # Начинаем с 2
while counter < num:
    if num % counter == 0:  # остаток от деления
        elementary = False
        break
    counter += 1

if elementary:
    print('Number is prime')
else:
    print('Number is not prime')
1