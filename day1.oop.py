# #1
# class Student:
#     def __init__(self):
#         pass
# Ali = Student()
# valijon = Student()
# Said = Student()
#2
# class Cat:
#     def __init__(self,name,age,color):
#         self.name=name
#         self.age = age
#         self.color = color
# bio=Cat("Tom", 1 ,"black")
# print(bio.name)
# print(bio.age)
# print(bio.color)
#3
# class Car:
#     def __init__(self,brand,model,year,color):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color
# d = Car("Mers","G-class",2026,"white")
# print(d.brand)
# print(d.model)
# print(d.year)
# print(d.color)
#4
# class Bank:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance=balance
#     def bal(self):
#         print(self.balance) 
# d = Bank("ME", 222)
# print(d.owner)
# print(d.bal())
#5
# class Phone:
#     def __init__(self,brand,model,battery):
#         self.brand = brand
#         self.model=model
#         self.battery= battery
#     def turnon(self):
#         return "ON"
#     def turnoff(self):
#         return "OFF"
#     def show(self):
#         return self.brand,self.model,self.battery
# a = Phone("Samsung","A56","50%")
# print(a.turnon())
# print(a.turnoff())
# print(a.show())
#6
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimetr(self):
#         return 2 * (self.width + self.height)
# s = Rectangle(2, 4)

# print(s.area())
# print(s.perimetr())
#7
# class Employee:
#     def __init__(self,name,pasition,salary):
#         self.name=name
#         self.pasition = pasition
#         self.salary = salary
#     def show(self):
#         return f"Name is {self.name} position is {self.pasition} solary {self.salary}"
#     def pro(self):
#         return self.salary+self.salary*10/100
# a = Employee("Me","lawyer",2000)
# print(a.show())
# print(a.pro())
#8
# class Produck:
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
#     def total(self):
#         return f"price is {self.price}"
#     def update(self):
#         self.quantity = int(input("New quantity: "))
#         return self.quantity
# a = Produck("laptop", 2000, 4)

# print(a.total())
# print(a.update())
#9
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def read(self):
#         print(f'Вы читаете книгу "{self.title}"')
#     def book_info(self):
#         return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
# b = Book("Python для начинающих", "Van Gusto", 300)

# b.read()
# print(b.book_info())