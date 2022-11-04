text = input("Input string: ")
symbol = input("Input char: ")

iteration = int(len(text))

for i in range(iteration):
    for k in text:
        value = text.find(symbol, i, i + 1)
        if text[value] == symbol and value != - 1:
            print(value)
            break

