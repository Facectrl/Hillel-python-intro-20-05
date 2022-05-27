num = int(input())
c = num % 10
b = (num % 100)//10
a = num // 100
print(c*100+b*10+a)
