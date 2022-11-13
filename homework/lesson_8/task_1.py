n = int(input("Enter the number: "))

arr = [[k if k % 2 == 0 else i for i in range(-n, -0)] for k in range(1, n + 1)]

for i in range(len(arr)):
    for k in range(len(arr)):
        print("{:>5}".format(arr[i][k]), end='')
    print()
