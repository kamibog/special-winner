def generate_keys(n):
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    result = ''
    pairs = []

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                pairs.append(f"{i}{j}")

    result = ''.join(pairs)
    return result


for n in range(3, 21):
    keys = generate_keys(n)
    print(f"{n} - {keys}")
