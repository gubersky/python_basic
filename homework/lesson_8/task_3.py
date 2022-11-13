import random

arr = [random.randint(1, 100) for i in range(15)]

count_even = 0
count_odd = 0

for i in arr:
    if i % 2 == 0:
        count_even += i
    else:
        count_odd += i

print("Yes" if count_even < count_odd else "No")
