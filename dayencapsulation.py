# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def make_sound(self):
#         print(f"{self.name}: sound")
# class Dog(Animal):
#     def make_sound(self):
#         print(f"{self.name}: Woof!")
# class Cat(Animal):
#     def make_sound(self):
#         print(f"{self.name}: Meow!")
# class Bird(Animal):
#     def make_sound(self):
#         print(f"{self.name}: Tweet ")
# a = Dog("Rex")
# b = Cat("Momo")
# c = Bird("kesha")
# lict =[a,b,c,]
# for i in lict:
#     i.make_sound()
#2
# class Shapes:
#     def __init__(self,a):
#         self.a = a
# class Circle(Shapes):
#     def area(self):
#         return 3.14*self.a**2
# class Rectangle(Shapes):
#     def __init__(self, a,b):
#         super().__init__(a)
#         self.b=b
#     def area(self):
#         return self.a*self.b
# class Square(Shapes):
#     def area(self):
#         return self.a*self.a
# a = Circle(5)
# b = Rectangle(4,5)
# c = Square(3)
# print(f"Circle: {a.area()}")
# print(f"Rectangle: {b.area()}")
# print(f"Square: {c.area()}")
# #3
# class EmailSender:
#     def send(self, message):
#         return f"Email: {message}"
# class SMSSender:
#     def send(self, message):
#         return f"SMS: {message}"
# class TelegramSender:
#     def send(self, message):
#         return f"Telegram: {message}"
# def notify(sender, message):
#     print(sender.send(message))

# message = input()

# email = EmailSender()
# sms = SMSSender()
# telegram = TelegramSender()

# notify(email, message)
# notify(sms, message)
# notify(telegram, message)
#4
# class Calculator:
#     def add(self, *numbers):
#         if 2 <=len(numbers)<= 4:
#             return sum(numbers)
#         else:
#             return "Invalid number of arguments"


# cal = Calculator()

# print(cal.add(5))
# print(cal.add(5, 10))
# print(cal.add(1, 2, 3))
# print(cal.add(1, 2, 3, 4))
# print(cal.add(1, 2, 3, 4, 5))
#5
# from abc import ABC, abstractmethod


# class Notification(ABC):
#     @abstractmethod
#     def send(self, message):
#         pass

# class EmailNotification(Notification):
#     def send(self, message, recipient):
#         print(f"Sent email to {recipient}: {message}")


# class SMSNotification(Notification):
#     def send(self, message, recipient):
#         print(f"Sent SMS to {recipient}: {message}")
# b = EmailNotification()
# c =SMSNotification()
# b.send("hello","user@mail.com")
# c.send("hello","+992900001122")

# print("Notification is abstract")

#6
# from abc import ABC, abstractmethod

# class PaymentMethod(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
#     @abstractmethod
#     def refund(self, amount):
#         pass
# class CardPayment(PaymentMethod):
#     def pay(self, amount):
#         if amount > 0:
#             print(f"Card payment: {amount}")
#     def refund(self, amount):
#         if amount > 0:
#             print(f"Card refund: {amount}")
# class CashPayment(PaymentMethod):
#     def pay(self, amount):
#         if amount > 0:
#             print(f"Cash payment: {amount}")
#     def refund(self, amount):
#         if amount > 0:
#             print(f"Cash refund: {amount}")
# class CryptoPayment(PaymentMethod):
#     def pay(self, amount):
#         if amount > 0:
#             print(f"Crypto payment: {amount}")
#     def refund(self, amount):
#         if amount > 0:
#             print(f"Crypto refund: {amount}")

# def process_payment(total, amount):
#     return total.pay(amount)
# process_payment(CardPayment(), 250)
# process_payment(CashPayment(), 100)
# process_payment(CryptoPayment(), 75)

#7
# from abc import ABC, abstractmethod
# class Exporter(ABC):
#     @abstractmethod
#     def export(self, data):
#         pass
# class CSVExporter(Exporter):
#     def export(self, data):
#         return f"CSV: name,age | {data['name']},{data['age']}"
# class JSONExporter(Exporter):
#     def export(self, data):
#         return f'JSON: {{"name": "{data["name"]}", "age": {data["age"]}}}'
# class XMLExporter(Exporter):
#     def export(self, data):
#         return f"XML: <person><name>{data['name']}</name><age>{data['age']}</age></person>"

# data = {
#     "name": "Ali",
#     "age": 22
# }
# print(CSVExporter().export(data))
# print(JSONExporter().export(data))
# print(XMLExporter().export(data))