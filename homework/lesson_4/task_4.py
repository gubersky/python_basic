value = int(input("Input value: "))

for i in range(value):
    i *= i
    if i > value:
        break
    if i != 0:
        print(i)
    if value == 1:
        print(value)
