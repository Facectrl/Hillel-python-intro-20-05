string = input('Enter text:')
count = string.count('.')
if string and string[-1] != ".":
    count += 1
print("Sentence: ", string.count('.'))

