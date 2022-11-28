def decorator(func):
    def wrapper(*args, **kwargs):
        for i in sorted(func(*args, **kwargs)):
            if i % 2 == 0 and i // 3 * 3 == i:
                print(f"Number: {i:<3} |{'multiple of 3':^18}| "
                      f"{'even number':<12}|")
            if i % 2 == 0 and i // 3 * 3 != i:
                print(f"Number: {i:<3} |{'not multiple of 3':^18}| "
                      f"{'even number':<12}|")
            if i % 2 != 0 and i // 3 * 3 == i:
                print(f"Number: {i:<3} |{'multiple of 3':^18}| "
                      f"{'odd number':<12}|")
            if i % 2 != 0 and i // 3 * 3 != i:
                print(f"Number: {i:<3} |{'not multiple of 3':^18}| "
                      f"{'odd number':<12}|")

    return wrapper


@decorator
def set_number(n):
    gen_set = set([i ** 2 for i in range(1, n + 1)])
    return gen_set


if __name__ == '__main__':
    set_number(12)
