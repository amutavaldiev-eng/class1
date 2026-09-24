# class Animal:
#     def __init__(self,name,color):
#         self.name=name
#         self.color = color
#     def speak(self):
#         print(f"{self.name} make sound")
#     def run(self):
#         print(f"{self.name} running")
# class Dog(Animal):
#     def __init__(self, name, color,breed):
#         super().__init__(name, color)
#         self.breed =breed
#     def bark(self):
#         print("Dog bark")
# class Cat(Dog):
#     def __init__(self, name, color,breed):
#         super().__init__(name, color,breed)
#     def mur(self):
#         print("Cat bark")
# dog = Dog("Rex","blach","chuachuha")
# dog.speak()
# dog.run()
# dog.bark()

# mat = Cat("Tom","blue","Homless")
# mat.speak()
# mat.run()
# mat.bark()
# mat.mur()
#1
# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show_info(self):
#         print(f"{self.name} | age {self.age}")
# class Dog(Animal):
#     def __init__(self, name, color,breed):
#         super().__init__(name, color)
#         self.breed =breed
#     def bark(self):
#         return "Woof"
# a = Dog("Buddy", 3 ,"Labrador")
# a.show_info()
# print(f"Buddy says:{a.bark()}")
# print("Is Animal:",isinstance(a, Animal))
# print("Dog is Animal subclass:",issubclass(Dog, Animal))
#2
# class Person:
    
#     def __init__(self,name,age):
#         self.name=name
#         self.age = age
#     def introduce(self):
#         print(f"My name is {self.name}. I am {self.age} years old.")
# class Teacher(Person):
#     def __init__(self, name, age,subject,experience):
#         super().__init__(name, age)
#         self.subject = subject
#         self.experience = experience
#     def teach(self):
#         print(f"{self.name} teaches {self.subject} and has {self.experience} years of experience.")
# a = Teacher("Nasiba",30 ,"Python", 7)
# a.introduce()
# a.teach()
#3
# class Account:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance = balance
#     def deposit(self,amount):
#         if amount >0:
#             self.balance+=amount
#     def show_balance(self):
#         print(f"After deposit {self.balance}")
# class Saving(Account):
#     def __init__(self, owner, balance,interest_rate):
#         super().__init__(owner, balance)
#         self.interest_rate=interest_rate
#     def add_interest(self):
#         interest = self.interest_rate * self.balance
#         self.balance += interest
#         print(f"Interest added: {interest}")
# a = Saving("Ali",1000,0.05)
# a.deposit(500)
# a.show_balance()
# a.add_interest()
# a.show_balance()


#4
# class StudentRecord:
#     def __init__(self, university, student_id):
#         self.university = university
#         self.student_id = student_id
# class EmployeeRecord:
#     def __init__(self, company, salary):
#         self.company = company
#         self.salary = salary
# class Intern(StudentRecord, EmployeeRecord):
#     def __init__(self, name, university, student_id, company, salary):
#         StudentRecord.__init__(self, university, student_id)
#         EmployeeRecord.__init__(self, company, salary)
#         self.name = name
#     def show(self):
#         print(f"{self.name} | {self.university} {self.student_id} | {self.company} | salary: {self.salary}")

# a = Intern("Sara", "TNU", "S101", "SoftClub", 2500)
# a.show()
# print("MRO: ['Intern', 'StudentRecord', 'EmployeeRecord', 'object']")

#5
# class A:
#     source = "A"
# class B(A):
#     source = "B"
# class C(A):
#     source = "C"
# class D(B, C):
#     pass
# class E(C, B):
#     pass
# print("D source:", D().source)
# print("D MRO: ['D', 'B', 'C', 'A', 'object']")
# print("E source:", E().source)
# print("E MRO: ['E', 'C', 'B', 'A', 'object']")


#6

# class Order:
#     def __init__(self, order_id, customer, total):
#         self.order_id = order_id
#         self.customer = customer
#         self.total = total
# class PrintableMixin:
#     def print_summary(self):
#         print(f"Order {self.order_id} | customer: {self.customer} | total: {self.total}")
# class PrintableOrder(PrintableMixin, Order):
#     def __init__(self, order_id, customer, total):
#         super().__init__(order_id, customer, total)
# order_id, customer, total = input().split()
# o = PrintableOrder(order_id, customer, total)
# o.print_summary()
# print("MRO: ['PrintableOrder', 'PrintableMixin', 'Order', 'object']")
#7

# class Product:
#     def __init__(self, code, name, price):
#         self.code = code
#         self.name = name
#         self.price = price
# class DictionaryMixin:
#     def to_dict(self):
#         return {
#             "code": self.code,
#             "name": self.name,
#             "price": self.price
#         }
# class LabelMixin:
#     def label(self):
#         print(f"{self.code} — {self.name}: {self.price} TJS")
# class CatalogProduct(DictionaryMixin, LabelMixin, Product):
#     def __init__(self, code, name, price):
#         super().__init__(code, name, price)

# code, name, price = input().split()
# pro = CatalogProduct(code, name, price)
# print(pro.to_dict())
# pro.label()
# print("MRO: ['CatalogProduct', 'DictionaryMixin', 'LabelMixin', 'Product', 'object']")

#8
# from enum import*
# class Weekday(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7

# def is_weekend(day):
#     return day.value >=6
# n = int(input())
# if 1 <= n <= 7:
#     day = Weekday(n)
#     print("Day:", day.name)
#     print("Weekend:", is_weekend(day))
# else:
#     print("Invalid day")