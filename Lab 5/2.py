def split_sentences(text):
    sentences = []
    current = ""

    for letter in text:
        current = current + letter
        if letter in ".!?":
            sentences.append(current.strip())
            current = ""

    if current:
        sentences.append(current.strip())

    return sentences
text = "He jests at scars. That never felt a wound! Hello, friend! Are you OK?"
print("Вход:", text)
print("Выход:")
sentences = split_sentences(text)
for s in sentences:
    print(s)
print("Всего предложений:", len(sentences))
print()