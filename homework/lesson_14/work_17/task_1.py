def sum_num(a, b):
    try:
        print(a + b)
    except TypeError:
        print(str(a) + str(b))


if __name__ == '__main__':
    first_num = 5
    second_num = "7"
    sum_num(first_num, second_num)
