# Напишите функцию, которая будет принимать список нечетных чисел, 
# выводит их и остановится, если встретит число 200. 
# Типизировать ее. 
# При запуске mypy не должно быть никаких ошибок типов

list = [1, 21, 19, 589, 111, 651, 8, 359, 6, 28, 1255, 349, 555, 10039, 9, 139, 56, 200, 67, 69, 90, 65, 510]

def odd_number(num:int):
    return num % 2 == 0

for i in list:
    if i == 200:
        break
    if not odd_number(i):
        print(i)
 
