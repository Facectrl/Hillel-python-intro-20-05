text: str = input("Enter your text:")
text[:text.find(" ")]
text[text.rfind(" "):]
text[text.find(" "):text.rfind(" ")]
print(text[:text.find(" ")], text[text.find(" "):text.rfind(" ")].replace('n', 'N'), text[text.rfind(" "):], sep='')
#
#читаемый > эффективный?
text: str = input("Enter your text:")
a = text[:text.find(" ")]
b = text[text.find(" "):text.rfind(" ")].replace('n', 'N')
c = text[text.rfind(" "):]
print(a, b, c, sep='')
