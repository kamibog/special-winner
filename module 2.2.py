first=int(input('Введите первое число: '))
second=int(input('Введите второе число: '))
third=int(input('Введите третье число число: '))
if first == second and first == third and second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')
#Если ввести все три числа одинаковые, например 10, то в консоль выведется 3.
#Если ввести например первое число 5, второе число 2, третье число 5, то в консоль выведется 2, так как два чила одинаковых.
#Если ввести все 3 числа разные, например первое число 6, второе число 8, третье число 9, то в консоль выведится 0, так как все числа разные.
