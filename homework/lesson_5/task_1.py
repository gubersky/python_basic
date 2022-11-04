value = input("Input text: ").strip()

text = value.replace(" ", "")

if text.isalpha():
    text = value[::-1].title().split()
    text[0], text[-1] = text[-1], text[0]
    print(" ".join(text))
else:
    print("Wrong data! Please input the text")
