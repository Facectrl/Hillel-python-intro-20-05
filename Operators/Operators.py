group1 = int(input())  # детей в 1 группе
group2 = int(input())  # детей в 2 группе
sum_group = group1 + group2  # общее колличество,детей
remain = sum_group % 2  # Остаток от деления
bed = sum_group // 2 + remain  # В 1 кровати до 2-х детей + остаток
print(bed)
