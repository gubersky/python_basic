"""

This is a module for sorting lists.

"""

__all__ = ["bubble_sort", "insertion_sort"]


def bubble_sort(array: list) -> list:
    """
    The algorithm compares the elements of the list in pairs, swapping them if
    necessary. It is not as efficient if we need to make only one exchange in
    the list, since this algorithm will repeat the process again when the end
    of the list is reached.

    Args:
    :param array: list
    :return: sorted list
    """
    for i in range(len(array) - 1):
        for k in range(len(array) - 1, i, -1):
            if array[i] > array[k]:
                array[i], array[k] = array[k], array[i]
    return array


def insertion_sort(array: list) -> list:
    """
    The algorithm divides the list into two parts, according to which the second
     part of the list falls in their place, removing them from the first.

    Args:
    :param array: list
    :return: sorted list
    """
    for i in range(1, len(array)):
        item = array[i]
        i2 = i - 1
        while i2 >= 0 and array[i2] > item:
            array[i2 + 1] = array[i2]
            i2 -= 1
        array[i2 + 1] = item
    return array


def selection_sort(array: list) -> list:
    """
    Like insertion sort, this algorithm in Python divides the list into
    two parts: the main part and the sorted part. The smallest element
    is removed from the main part and goes into the sorted part.

    Args:
    :param array: list
    :return: sorted list
    """
    for i in range(len(array)):
        index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[index]:
                index = j
        array[i], array[index] = array[index], array[i]
    return array
