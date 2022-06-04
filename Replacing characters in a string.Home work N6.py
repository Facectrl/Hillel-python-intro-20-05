text: str = input("")
text[:text.find(" ")]
text[text.rfind(" "):]
text[text.find(" "):text.rfind(" ")]
print(text[:text.find(" ")], text[text.find(" "):text.rfind(" ")].replace('n', 'N'), text[text.rfind(" "):], sep='')
#
#читаемый > эффективный?
text: str = input("")
a = text[:text.find(" ")]
b = text[text.rfind(" "):].replace('n', 'N')
c = text[text.find(" "):text.rfind(" ")]
print(a, b, c, sep='')
