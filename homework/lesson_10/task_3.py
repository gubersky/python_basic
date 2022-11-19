def prime_gen(n, z):
    for i in range(n, z):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime and i >= 2:
            yield i


for k in prime_gen(2, 33):
    print(k, end=" ")
