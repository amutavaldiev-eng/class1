# a = int(input())
# b = int(input())
# try:
#     print("Result",a/b)
# except ValueError:
#     print("Enter number")
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# finally:
#     print("Calculation finished")
#2
# Cities=['Dushanbe', 'Khujand', 'Bokhtar']
# try:
#     a=int(input())
#     print(f"City {Cities[a]}")
# except ValueError:
#     print("Enter Number")
# except IndexError:
#     print("Position does not exist")
#3
# Prices= {'mouse': 100, 'keyboard': 250, 'monitor': 1200}
# try:
#     key=input()
#     quantity=int(input())
#     print(f"Total:{Prices[key]*quantity}")
# except KeyError:
#     print("Produkt not found")
# except ValueError:
#     print("Erorr")
#4
# a = input().split()
# def calculate_average(values):
#     try:
#         for i in range(len(values)):
#             values[i]=int(values[i])
#         print(f"Averege {sum(values)/len(values)}")
#     except ValueError:
#         print("Enter Number")
#     except ZeroDivisionError:
#         print("ZeroDivisionError")
#     except Exception as error:
#         print(error)
# calculate_average(a)          
#5
# def register_participant(name, age):


#6
# class InsufficientFundsError(Exception):
#     pass
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#     def deposit(self, amount):
#         if amount <= 0:
#             return "ValueError: amount must be positive"
#         self.__balance += amount
#     def withdraw(self, amount):
#         if amount <= 0:
#             return "ValueError: amount must be positive"
#         if amount > self.__balance:
#             return f"InsufficientFundsError: requested {amount}, available {self.__balance}"
#         self.__balance -= amount
#         return "Withdrawal completed"
#     def get_balance(self):
#         return self.__balance

# a = BankAccount("Ali", 500)
# print(a.withdraw(700))
# print(a.deposit(-10))
# print(a.withdraw(200))
# print("Balance:", a.get_balance())
#7

# def process_payment(balance, amount):
#     if amount <= 0:
#         return "amount must be positive"
#     if amount > balance:
#        return "insufficient funds"
#     return balance - amount
# balance = 1000
# amount = 250
# try:
#     new = process_payment(balance, amount)
# except ValueError as error:
#     print("ValueError:", error)
# except InsufficientFundsError as error:
#     print("InsufficientFundsError:", error)
# else:
#     print("New balance:", new) 
# finally:
#     print("Payment attempt finished")


    
        
# #8
# def price_per_item(total, quantity):
#     return total / quantity
# def build_report(order):
#     return price_per_item(order["total"], order["quantity"])
# def main():
#     order = {"total": 600, "quantity": 3}
#     print(build_report(order))
# main()

#9
# def line_total(price, quantity):
#     return price * quantity


# def cart_total(items):
#     total = 0
#     for index, item in enumerate(items):
#         price = item["price"]
#         quantity = item["quantity"]
#         total += line_total(price, quantity)
#     return total


# cart = [
#     {"name": "Mouse", "price": 100, "quantity": 2},
#     {"name": "Keyboard", "price": 250, "quantity": 1},
#     {"name": "Cable", "price": 30, "quantity": 3},
# ]
# print(cart_total(cart))
#10
