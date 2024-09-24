def all_variants(text):
    x = len(text)
    for start in range(x):
        for end in range(start + 1, x + 1):
            yield text[start:end]


a = all_variants("abc")
for i in a:
    print(i)
