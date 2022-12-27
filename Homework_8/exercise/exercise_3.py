# Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца
#  - и возвращает название сезона, к которому относится этот месяц. 
# Например, передаем 2, на выходе получаем 'Зима'.

number = int(input("Enter the month number:"))
list_winter = [1, 2, 3]
list_spring = [4, 5, 6]
list_summer = [7, 8, 9]
list_autume = [10, 11, 12]

def month_to_season(number:int):
   if number in list_winter:
      return str ('winter')
   if number in  list_spring:
      return str ('spring')
   if number in list_summer:
      return str ('summer')
   if number in list_autume:
      return str ('autumn')

print ('Season:', month_to_season(number))