# class Teacher:
#     def __init__(self,full,subject,experiens=0):
#         self.full =full
#         self.subject = subject
#         self.experiens = experiens
#     def teach(self):
#         return f"{self.full} is teching {self.subject}"
#     def set_experience(self,year):
#         if year >0:
#             self.experiens=year
#         else:
#             print("Erorr 404")
#     def get_experience(self):
#         return f"Experiens {self.experiens}"
# t=Teacher("Nasiba Karimova","Python")
# t.set_experience(6)
# print(t.teach())
# print(t.get_experience())
#2
# class Student:
#     school_name="School 21"
#     def __init__(self,name,grade):
#         self.name =name
#         self.grade = grade
    
#     def show(self):
#         return f"{self.name} | {self.grade} | {Student.school_name}"
# a = Student("ALi",10,)
# b = Student("Sara",11,)
# print(a.show())
# print(b.show())
# Student.school_name= "Python Academy"
# print(a.show())
# Student.school_name= "Python Academy"
#print(b.show())
#3
# class Employee:
#     employees_count = 0
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#         Employee.employees_count += 1
#     @classmethod
#     def get_count(cls):
#         return cls.employees_count

#     def show_info(self):
#         print(f"{self.name} | {self.position}")

# while True:
#     line = input()
#     if line == "stop":
#         break

#     name, position = line.split()
#     e= Employee(name, position)
#     e.show_info()

# print(f"Total employees: {Employee.get_count()}")
#4
# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     @staticmethod
#     def add(a,b):
#         return "Add:", a+b
#     def sub(a,b):
#         return "Subtract:", a-b
#     def mul(a,b):
#         return "Multiply:", a*b
#     def div(a,b):
#         if b == 0:
#             return "Cannot divide by zero"
#         else:
#             return "Divide:",a/b
# c =Calculator
# print(*c.add(12,3))
# print(*c.sub(12,3))
# print(*c.mul(12,3))
# print(*c.div(12,3))

#5
# class Currency:
#     usd_rate=10.90
#     def __init__(self,usd):
#         self.usd =usd 
#     def to_somoni(self):
#         return self.usd_rate*self.usd
#     @staticmethod
#     def valid(value):
#         return value > 0
#     @classmethod
#     def chang(cls,new):
#         if cls.valid(new):
#             cls.usd_rate = new
#             return True
#         return False
# a = Currency(100)
# print(f"Before: {a.to_somoni()} TJS")
# print(f"Rate changed: {Currency.chang(11.20)}")
# print(f"After: {a.to_somoni()} TJS")



#7
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def __str__(self):
#         return f"{self.name} — {self.price} TJS, stock: {self.quantity}"
#     def __repr__(self):
#         return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"

# name, price, quantity = input().split()
# price = int(price)
# quantity = int(quantity)

# t = Product(name, price, quantity)

# print(str(t))
# print(repr(t))
#8
# class Book:
#     def __init__(self, title, author, isbn):
#         self.title = title
#         self.author = author
#         self.isbn = isbn

#     def __eq__(self, other):
#         if type(other) != Book:
#             return False
#         return self.isbn == other.isbn

#     def __repr__(self):
#         return f"Book('{self.title}', '{self.author}', '{self.isbn}')"


# book1 = Book("Python101", "Ali", "978-1")
# book2 = Book("PythonBasics", "Sara", "978-1")
# book3 = Book("Django101", "Rustam", "978-2")

# print("Book 1 == Book 2:", book1 == book2)
# print("Book 1 == Book 3:", book1 == book3)
# print("Book 1 == '978-1':", book1 == "978-1")
#9
# class Playlist:
#     def __init__(self, name):
#         self.name = name
#         self.songs = []

#     def add_song(self, song):
#         self.songs.append(song)

#     def __len__(self):
#         return len(self.songs)

#     def __contains__(self, song):
#         for i in self.songs:
#             if i.lower() == song.lower():
#                 return True
#         return False


# playlist = Playlist("Study")

# playlist.add_song("Believer")
# playlist.add_song("Numb")
# playlist.add_song("Imagine")

# print("Size:", len(playlist))
# print("numb" in playlist)
# print("Ha" in playlist)
# #10
