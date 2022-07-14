import random
"""
randrange  
randint #
random #
uniform #
"""

for _ in range(15):
    print(random.randrange(0, 100, 1), end=", ")
print()

for _ in range(15):
    print(random.randint(0, 2), end=", ")
print()

for _ in range(15):
    print(round(random.random(), 2), end=", ")
print()

for _ in range(15):
    print(round(random.uniform(0, 3), 1), end=", ")
print()

"""
Collections:
str ""
list []
tuple (,)
set {,}
dict {1:2}
"""



l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
l4 = l3 * 2
print(id(l2))
print(id(l1))
print(id(l3))
print(l4)
print(max(l1), min(l2))
print(sum(l1))
some_list = [5, 1, 2, 3, 4, 5]
sorted_list = sorted(some_list)
print(sorted(some_list))

reversed_list = reversed(some_list)
print(reversed_list, some_list, some_list[::-1])


#
some_list = [5, 4, 3, 2, 1]
print(id(some_list))
some_list[0] = 50
print(id(some_list), some_list)

del some_list[0]
print(some_list)

some_list.append(100)
print(some_list)
some_list.insert(0, "inserted")
print(some_list)
l1.extend(l2)
print(id(l1),l1)

value = l2.pop(0)
print(value, l2)
l2_copy = l2.copy()
print(id(l2), id(l2_copy), l2, l2_copy)

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(id(l1), l1)
l1.sort(0, len(l1))
print(id(l1), l1)