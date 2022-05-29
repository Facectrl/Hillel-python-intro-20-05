group1 = int(input('Детей в группе:'))
group2 = int(input('Детей в группе:'))
bed_group1 = (group1 // 2) + group1 % 2
bed_group2 = (group2 // 2) + group2 % 2
print(bed_group2 + bed_group1)

