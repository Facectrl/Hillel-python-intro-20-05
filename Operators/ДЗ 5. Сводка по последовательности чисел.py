sum_digit = 0
count = 0
min_digit = 0
max_digit = 0
arithmetic_mean = 0
while True:
    x = input('enter: ')
    if not x:
        print(('sum_digit:'), sum_digit, 'count:', count, 'max_digit:', max_digit, 'min_digit:', min_digit, 'arithmetic_mean:', arithmetic_mean, end=',')
        break
    count += 1
    num = int(x)
    sum_digit += num
    arithmetic_mean = sum_digit // count
    if num > max_digit or max_digit is None:
        max_digit = num
    if num < min_digit or min_digit is None:
        min_digit = num
#
#Почитать про None!