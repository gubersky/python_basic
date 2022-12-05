from sorted import *
from random import randint

if __name__ == '__main__':
    arr = [randint(1, 50) for i in range(10)]
    print(bubble_sort(arr))
    print(insertion_sort(arr))
