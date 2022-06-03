user = 'Я написал строку'
print(len(user))
print(user[0], user[3], user[6], user[-14])
print(user[:])
print('copied with change с: ', user[:9] + 'FUCK' + user[10:])
print(user.count('а'))
print(user.find('н'))
print(user[user.find('О'):])
print(user.replace('а', 'n', len(user)))
