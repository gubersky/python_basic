import random

list_numbers = [random.randint(1, 10 + 1) for i in range(10)]


def check_number(some_list, number):
    check = False
    for i in range(len(some_list)):
        for k in range(i + 1, len(some_list)):
            if some_list[i] + some_list[k] == number:
                check = True
    return check


print(check_number(list_numbers, 6))
print(check_number(list_numbers, 7))
