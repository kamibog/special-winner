def print_params(a=1, b='stroka', c=True):
    if c is True:
        c = [1, 2, 3]
        b = int
        b = 25

    print(a, b, c)


print_params(3)
print_params(5, b=3, c=[3, 8, 9])


def print_params(a=1, b='строка', c=True):
    print(f"a: {a}, b: {b}, c: {c}")


values_list = [42, 'слово', False]
values_dict = {'a': 99, 'b': 'слово', 'c': [4, 5, 6]}

print_params(*values_list)
print_params(**values_dict)


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list_2 = [54.32, 'Cтрока']
print_params(*values_list_2, 42)
