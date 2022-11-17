import random

dictionary = {i: random.randint(1, 20) for i in range(1, 20 + 1)}

result = 1

for i in dictionary.values():
    result *= i

print(dictionary)
print(result)
