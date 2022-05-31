sum_digit = 0
count = 0
min_digit = 20303020302302032030230203203023023023
max_digit = 0
arithmetic_mean = 0
while True:
    x = input('enter: ')
    if not x:
        print(sum_digit, count, max_digit, min_digit, arithmetic_mean)
        break
    count += 1
    num = int(x)
    sum_digit += num
    arithmetic_mean = sum_digit // count
    if num > max_digit:
        max_digit = num
    if num < min_digit:
        min_digit = num

