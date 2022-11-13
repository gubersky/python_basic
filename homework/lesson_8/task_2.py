import random

n = int(input("Enter the number: "))

arr = [[random.randint(1, 100) for i in range(n)] for k in range(n)]

first_sum = 0
second_sum = 0

for i in range(n):
    for k in range(n):
        print("{:>5}".format(arr[i][k]), end='')
        if i == k:
            first_sum += arr[i][k]
        if k == n - 1:
            second_sum += arr[i][k]
    print()

print("Sum of the numbers on the diagonal:", first_sum)
print("Sum of the numbers in the last column:", second_sum)
