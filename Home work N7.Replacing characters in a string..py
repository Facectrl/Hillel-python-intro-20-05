text = input('Enter text: ')
count = text.count('.')
if text and text[-1] == ("."):
   print("Количество предложений: ", count)
else:
   print("Количество предложений: ", [count + 1])

#Очень много времени трачу на простые задачи..:(
