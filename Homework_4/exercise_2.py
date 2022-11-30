# Создайте словарь с количеством элементов не менее 5-ти.
# Поменяйте местами первый и последний элемент объекта. 
# Удалите второй элемент. 
# Добавьте в конец ключ «new_key» со значением «new_value».
# Выведите на печать итоговый словарь. 
from collections import OrderedDict

book_numbers = [
    ['Tatsiana', '+375 25 222 22 22'], 
    ['Artem', '+375 29 888 88 88'], 
    ['Alex', '+375 44 555 55 55'], 
    ['Galina', '+375 29 999 99 99'], 
    ['Kirill', '+375 29 777 77 77'],
]

ordered_dict = OrderedDict(book_numbers)
print (ordered_dict)

# Меняем местами первый и последний элементы
ordered_dict.move_to_end('Tatsiana')
ordered_dict.move_to_end('Kirill', False)
print(ordered_dict)

# Удаляем второй элемент и вставляем новый
ordered_dict.pop('Alex')
ordered_dict['Anton'] = '+375 44 222 22 22'
print(ordered_dict)