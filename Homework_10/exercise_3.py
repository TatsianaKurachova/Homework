# Напишите программу с классом Car. 
# Создайте конструктор класса Car. 
# Создайте атрибуты класса Car:
# 1) цвет — color, 
# 2) тип -type, 
# 3) год -year. 
# Напишите пять методов. 
# 1) Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». 
# 2) Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». 
# 3) Третий — присвоение автомобилю года выпуска. 
# 4) Четвертый метод — присвоение автомобилю типа.
# 5) Пятый — присвоение автомобилю цвета


class Car:
   
   def __init__(self, color, type, year):
    self.color = color
    self.type = type
    self.year = year

   def start(self):
    print ("Start car")

   def mute(self):
    print ("Mute car")
       
   def year_of_release(self):
    print("Year of release:", self.year) 
             
   def set_the_type(self):
    print("Set the type:", self.type)

   def set_the_color(self):
    print("Set the color:", self.color)

car_1 = Car('red', 'Truck', 2022)
car_2 = Car('green', 'Cupe', 2000)
car_1.start()
car_1.mute()
car_1.year_of_release()
car_1.set_the_color()
car_1.set_the_type()

car_2.start()
car_2.mute()
car_2.year_of_release()
car_2.set_the_color()
car_2.set_the_type()