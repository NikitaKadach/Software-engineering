def make_abbreviation(text):
    abbreviation = ""
    words = text.split()

    for word in words:
        if len(word) >= 3:
            abbreviation = abbreviation + word[0].upper()

    return abbreviation
text1 = "New York City"
print("Вход:", text1)
print("Выход:", make_abbreviation(text1))
print()

text2 = "Yanka Kupala State University of Grodno"
print("Вход:", text2)
print("Выход:", make_abbreviation(text2))