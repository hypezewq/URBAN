def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        return "Простое" if sum([result % i == 0 for i in range(1, result)]) < 2 else "Составное"

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(6, 0, 0)
print(result)
