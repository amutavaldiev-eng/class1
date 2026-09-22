# class Person:
#     def __init__(self,name,age,city):
#         self.name =name
#         self.age= age
#         self.city = city
#     def info(self):
#         return f"Меня зовут {self.name}, мне {self.age} лет, я живу в {self.city}."
# a = Person("Akbar", 15, "Dushanbe")
# print(a.info())
#2
# class Dog:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age

#     def bark(self):
#         return f"{self.name} гавкает: Гав-гав!"


# dog1 = Dog("Шарик", "Овчарка", 3)
# dog2 = Dog("Бобик", "Лабрдор", 5)
# dog3 = Dog("Рекс", "Такса", 2)

# print(dog1.bark())
# print(dog2.bark())
# print(dog3.bark())
#3
# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def show_price(self):
#         return f"Price {self.price}"
# d = Product("Laptop", 2000)
# print(d.show_price())
#4
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return f"Area: {3.14*self.radius**2}"
#     def circumference(self):
#         return f"Circumference: {2*3.14*self.radius}"
# d = Circle(5)
# print(d.area())
# print(d.circumference())
#5
# class Wallet:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance += amount
#     def withdraw(self,amount):
#         self.balance -= amount
# d = Wallet("Akbar",200)
# d.deposit(int(input()))
# d.withdraw(int(input()))
# print(d.balance)
#6
# class Student:
#     def __init__(self,name,grades):
#         self.name=name
#         self.grades=grades
    
#     def add_grade(self, grade):
#         self.grades.append(grade)
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)


# a = Student("Me", [89])
# a.add_grade(90)
# a.add_grade(80)
# print(a.grades)
# print(a.average_grade())
#7
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_borrowed = False
#     def borrow(self):
#         if self.is_borrowed == False:
#             self.is_borrowed = True
#             print("Вы взяли книгу")
#         else:
#             print("Книга уже занята")
#     def return_book(self):
#         self.is_borrowed = False
#         print("Книга возвращена")

# book = Book("Python", "Иван")
# book.borrow()
# book.borrow()
# book.return_book()
#8

# class Thermometer:
#     def __init__(self, city, temperature):
#         self.city=city
#         self.temperature=temperature

#     def is_hot(self):
#         return self.temperature>30

#     def describe(self):
#         if self.is_hot():
#             print(f"В городе {self.city} сейчас {self.temperature}°C — жарко.")
#         else:
#             print(f"В городе {self.city} сейчас {self.temperature}°C — холодно.")


# t = Thermometer("Душанбе", 35)
# s = Thermometer("Москва", 20)

# t.describe()
# s.describe()
#9



#10
# class BankCard:
#     def __init__(self, card_number, pin, balance):
#         self.card_number= card_number
#         self.pin=pin
#         self.balance=balance

#     def check_pin(self, entered_pin):
#         return entered_pin == self.pin

#     def withdraw(self, amount, entered_pin):
#         if not self.check_pin(entered_pin):
#             print("Неверный пин-код")

#         elif amount > self.balance:
#             print("Недостаточно средств")

#         else:
#             self.balance -= amount
#             print(f"Снято {amount} сомони. Остаток: {self.balance} сомони")


# card = BankCard("123456789", 1234, 100)

# card.withdraw(20, 5555)   
# card.withdraw(200, 1234)  
# card.withdraw(30, 1234)   
