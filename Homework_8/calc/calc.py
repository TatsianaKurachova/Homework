#Создать функцию calc(a, b, operation).
#  Описание входных параметров: 
# 1. Первое число 
# 2. Второе число 
# 3. Действие над ними: 
# 1) + Сложить 
# 2) - Вычесть 
# 3) * Умножить 
# 4) / Разделить 
# 5) В остальных случаях функция должна возвращать "Операция не поддерживается". 
# Типизировать ее. 
# При запуске mypy не должно быть никаких ошибок типов

import typing

a=int(input("Введите число а ="))
operation = str(input("Операция:"))
b=int(input("Введите число b ="))

def calc (a:int, b:int, operation:str):
   if "+" in operation:
      return str (a+b)
   if "-"in operation:
      return str (a-b)
   if "*" in operation:
      return str (a*b)
   if "/" in operation:
      return str (a/b)
   else:
      return str("Операция не поддерживается")   

print ('Ответ:', calc(a, b, operation))