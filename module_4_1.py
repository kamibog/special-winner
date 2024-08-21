from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(55, 99)
result2 = fake_divide(333, 0)
result3 = true_divide(44, 88)
result4 = true_divide(111, 0)

print(result1)
print(result2)
print(result3)
print(result4)