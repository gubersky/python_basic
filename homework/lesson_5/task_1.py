value = input("Input to words using one a space: ")

if value.count(" ") == 1:
    text = value.replace(" ", "")
    if text.isalpha():
        text = value[::-1].title().split()
        text[0], text[-1] = text[-1], text[0]
        print(" ".join(text))
    else:
        print("Wrong data! Please input the text")
else:
    print("Wrong data! Please Input two words using one a space")
