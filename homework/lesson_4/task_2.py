value = int(input("Input value: "))

count = 0
iteration = value

while iteration > 0:
    count += 1
    iteration //= 10
for i in range(1, value + 1):
    for k in range(1, count + 1):
        if i == i * i % 10 ** k:
            print(i, '*', i, '=', i * i)
            break
