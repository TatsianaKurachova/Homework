# Напишите функцию, которая принимает аргумент в виде списка и возвращает словарь, 
# в котором каждый элемент списка является и ключом и значением. Предполагается, 
# что элементы списка будут соответствовать правилам задания ключей в словарях.

def to_dict(lst):
  return {element: element for element in lst}
print(to_dict([1, 2, 3, 4]))
print(to_dict(['grey', (2, 17), 3.11, -4]))





def to_dict(list):
    dictus = {list[0]: list[0],
              list[1]: list[1],
              list[2]: list[2],
              list[3]: list[3],
              list[4]: list[4]}
    return dictus
 
print(to_dict(list))