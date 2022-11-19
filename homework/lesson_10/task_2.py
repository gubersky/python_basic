import random

first_list = [random.randint(1, 10 + 1) for i in range(10)]
second_list = [random.randint(1, 10 + 1) for k in range(10)]

first_result = map(lambda x, y=2: x ** y, first_list)
second_result = map(lambda x, y=2: x ** y, first_list, second_list)

for i in first_result:
    print(i, end=" ")

print()

for i in second_result:
    print(i, end=" ")
