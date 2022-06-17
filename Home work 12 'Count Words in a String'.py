def word_count(string=input("Enter a string: ")):
    import re

    string = re.sub(r'[^\w\s]', '', string)
    string = string.lower()
    string = string.split()
    counts = dict()
    for word in string:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print("First five values: ", sorted(word_count().items(), key=lambda x: x[1], reverse=True)[:5])




