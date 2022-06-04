text: str = input("")
text[:text.find(" ")]
text[text.rfind(" "):]
text[text.find(" "):text.rfind(" ")]
print(text[:text.find(" ")], text[text.find(" "):text.rfind(" ")].replace('n', 'N'), text[text.rfind(" "):], sep='')
