my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
zero = 0
while zero < len(my_list):
    num = my_list[zero]
    zero += 1
    if num == 0:
        continue
    elif num < 0:
        print('Отрицательное число')
        break
    elif zero == len(my_list):
        print(num)
        print('End')
    else:
        print(num)
