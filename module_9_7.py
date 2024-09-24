def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 2:
            print(f'Составное')
            return result
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                print(f'Составное')
                return result
        print(f'Простое')
        return result

    return wrapper


@is_prime
def summ_three(a, b, c):
    return a + b + c


result = summ_three(2, 3, 6)
print(result)
