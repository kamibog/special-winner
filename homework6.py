my_dict={'Poly': 2008, 'Nataly': 1978, 'Boris': 1982, 'Viky': 2000}
print(my_dict)
print(my_dict['Boris'])
my_dict['Slava']=1965
print(my_dict['Slava'])
my_dict.update({'Vera':2014,'Valera':1999})
print(my_dict)
a=my_dict.pop('Nataly')
print(my_dict)
print(a)
print(my_dict)

my_set_={1,1,1,5,5,5,'soup','soup','soup'}
print(my_set_)
my_set_.update({'cat', 'dog', 'cat', 'dog'})
print(my_set_)
print(my_set_.discard('soup'))
print(my_set_)

