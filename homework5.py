immutable_var=[1, 2], "a", "b"
print (immutable_var)
print(type(immutable_var))
# Если мы попытаемся поменять один из элементов, например:
# immutable_var=[1, 2], "a", "b"
# immutable_var[0]=5, то у нас будет ошибка, так как кортеж не изменяется
mutable_list=["black", "white", "red", "5"]
print(mutable_list)
print(mutable_list[1])
mutable_list[1]="green"
print(mutable_list)
mutable_list.append(10)
print(mutable_list)