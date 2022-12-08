import random


def sorted_arr(array):
    temp_arr = []
    count = 0
    for i in range(len(array)):
        for k in range(len(array)):
            count += array[k][i]
        temp_arr.append(count)
        count = 0
    for n in range(len(temp_arr) - 1):
        for j in range(len(temp_arr) - 1, n, -1):
            if temp_arr[n] > temp_arr[j]:
                temp_arr[n], temp_arr[j] = temp_arr[j], temp_arr[n]
                for k in range(len(temp_arr) - 1, -1, -1):
                    array[k][n], array[k][j] = array[k][j], array[k][n]
    count = 0
    while True:
        temp_arr = []
        for i in range(count, len(array)):
            for k in range(len(array)):
                temp_arr.append(array[k][i])
            break
        if count % 2 == 0:
            for n in range(len(temp_arr) - 1):
                for j in range(len(temp_arr) - 1, n, -1):
                    if temp_arr[n] < temp_arr[j]:
                        temp_arr[n], temp_arr[j] = temp_arr[j], temp_arr[n]
        else:
            for n in range(len(temp_arr) - 1):
                for j in range(len(temp_arr) - 1, n, -1):
                    if temp_arr[n] > temp_arr[j]:
                        temp_arr[n], temp_arr[j] = temp_arr[j], temp_arr[n]
        for i in range(count, len(temp_arr)):
            for k in range(len(temp_arr)):
                array[k][i] = temp_arr[k]
            break
        count += 1
        if count == len(array):
            break
    temp_arr = []
    count = 0
    for i in range(len(array)):
        for k in range(len(array)):
            count += array[k][i]
        temp_arr.append(count)
        count = 0
    for n in range(len(temp_arr) - 1):
        for j in range(len(temp_arr) - 1, n, -1):
            if temp_arr[n] > temp_arr[j]:
                temp_arr[n], temp_arr[j] = temp_arr[j], temp_arr[n]
    array.append(temp_arr)
    return array


def print_arr(array):
    for i in range(len(array)):
        for k in range(len(array) - 1):
            print("{:>5}".format(array[i][k]), end='')
        print()


if __name__ == '__main__':
    num = int(input("Enter an array length greater than 5: "))
    new_list = [[random.randint(1, 50) for i in range(num)] for k in range(num)]

    print_arr(sorted_arr(new_list))
