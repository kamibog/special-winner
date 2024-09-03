import io
from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}
    for index, strings in enumerate(strings, start=1):
        byte = file.tell()
        file.write(strings + '\n')
        strings_positions[(index, byte)] = strings

    return strings_positions


file_name = 'test.txt'
file = open(file_name, 'w', encoding='utf-8')

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

file.close()
