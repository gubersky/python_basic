value = int(input("Input value: "))
for i in range(value):
    print(f'{i:>2} {"1" + "0" * i: >{value}}')
