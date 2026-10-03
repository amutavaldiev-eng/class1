# # class Tamagotchi:
# #     def __init__(self, name):
# #         self.name = name
# #         self.hunger = 50
# #         self.happiness = 50
# #         self.is_alive = True

# #     def _check_alive(self):
# #         if self.hunger >= 100 or self.happiness <= 0:
# #             self.is_alive = False
# #         if not self.is_alive:
# #             print(f"{self.name} больше не с нами... 😢")
# #         return self.is_alive

# #     def feed(self):
# #         if not self._check_alive():
# #             return
# #         self.hunger = max(0, self.hunger - 20)
# #         self.happiness = max(0, self.happiness - 5)
# #         print(f"{self.name} поел 🍖")

# #     def play(self):
# #         if not self._check_alive():
# #             return
# #         self.happiness = min(100, self.happiness + 20)
# #         self.hunger = min(100, self.hunger + 15)
# #         print(f"{self.name} поиграл 🎾")
# #         self._check_alive()

# #     def tick(self):
# #         if not self._check_alive():
# #             return
# #         self.hunger = min(100, self.hunger + 10)
# #         self.happiness = max(0, self.happiness - 10)
# #         self._check_alive()

# #     def status(self):
# #         if not self._check_alive():
# #             return
# #         print(f"{self.name}: голод {self.hunger}, счастье {self.happiness}")


# # pet = Tamagotchi(input("Name of your pet: "))

# # while True:
# #     n = int(input("1)Status\n2)Play\n3)Feed\n4)Tick\n0)Kill pet\nChouse one"))
# #     match n:
# #         case 1:
# #             pet.status()
# #         case 2:
# #             pet.play()
# #         case 3:
# #             pet. feed()
# #         case 4:
# #             pet.tick()
# #         case 0:
# #             print("You kill own pet!")
# #             break
# #         case _:
# #             print("Invalid input")












#________________________________________________________________________________________________________________________
# class Hero:
#     def __init__(self, name):
#         self.name = name
#         self.health = 100
#         self.power = 10

#     def attack(self, other):
#         other.health -= self.power
#         print(f"{self.name} Атакует {other.name}")

#     def is_alive(self):
#         return self.health > 0

# class Warrior(Hero):
#     def __init__(self, name):
#         super().__init__(name)
#         self.power = 15

        
# import random


# class Mage(Hero):
#     def __init__(self, name):
#         super().__init__(name)
#         self.power = 20

#     def attack(self, other):
#         if random.random() < 0.5:
#             print(f"{self.name} Атакует {other.name}")        
#             print(f"{self.name} промахнулся! ✨")
#         else:
#             super().attack(other)        

# class Healer(Hero):
#     def __init__(self, name):
#         super().__init__(name)
#         self.power = 5

#     def attack(self,other):
#         if random.random() <0.5:
#             self.heal()
#         else:
#             super().attack(other)

#     def heal(self):
#         self.health = min(100, self.health + 15)
#         print(f"{self.name} лечится 💚 (+15 HP)")


# def battle(hero1, hero2):
#     round_num = 1
#     while hero1.is_alive() and hero2.is_alive():
#         print(f"--- Раунд {round_num} ---")
#         hero1.attack(hero2)
#         if hero2.is_alive():            
#             hero2.attack(hero1)
#         round_num += 1
        

#     if hero1.is_alive():
#         print(f"🏆 Победил {hero1.name}!")
#     else:
#         print(f"🏆 Победил {hero2.name}!")


# def create_hero(hero_num):
#     h1 = input(f"Выбирите тип воина для Hero{hero_num}\nТипы воинов Герой, Воин, Маг, Целитель: ") 
#     match h1.lower():
#         case "герой":
#             hero1 = Hero(input("Вводите Имя вашего Героя: "))
#         case "маг":
#             hero1 = Mage(input("Вводите Имя вашего Мага: "))
#         case "воин":
#             hero1 = Warrior(input("Вводите Имя вашего воин: "))
#         case "целитель":
#             hero1 = Healer(input("Вводите Имя вашего Целитель: "))
#         case _:
#             print("Вы ввели не правильно!")
        
#     return hero1

# while True:
#     n = int(input("1)Start\n2)Exit\nChouse: "))
#     match n:
#         case 1:
#             battle(create_hero(1), create_hero(2))
#         case 2:
#             print("End the game!")
#             break







# 
# 
# 
# 
# 
# 
# 
# _________________________________________________________________
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"{self.name} — {self.price} руб."


# class Cart:
#     def __init__(self):
#         self.items = []

#     def add(self, product, quantity=1):
#         for _ in range(quantity):
#             self.items.append(product)

#     def total(self):
#         return sum(item.price for item in self.items)

#     def remove(self, name):
#         for item in self.items:
#             if item.name == name:
#                 self.items.remove(item)
#                 return                # нашли и удалили — сразу выходим!
#         print(f"Товара «{name}» нет в корзине")

#     def checkout(self):
#         print("===== ЧЕК =====")
#         for item in self.items:
#             print(item)               # сработает наш __str__!
#         print("---------------")
#         print(f"ИТОГО: {self.total()} руб.")

    
# cart = Cart()
# print("====MENU====")
# while True:
#     n = int(input("1)Add product\n2)Remove\n3)Show cart\n4)Checkout\n5)Exit\n Chouse one: "))
#     match n:
#         case 1 :
#             name = input("Product name: ")
#             price = int(input("Price: "))
#             qty = int(input("Quantity: "))
#             cart.add(Product(name, price), qty)
#             print(f"{name} Added to cart")
#         case 2:
#             name = input("Enter name to remove: ")
#             cart.remove(name)
#         case 3:
#             for item in cart.items:
#                 print(item)
#         case 4:
#             cart.checkout()
#         case 5:
#             print("Good bye!")
#             break
#         case _:
#             print("You dont have this choose")
#________________________________________________________________________
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.history = []   # список строк-записей об операциях
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"+{amount} руб.")
    def withdraw(self, amount):
        if amount > self.balance:
            self.history.append(f"ОТКАЗ: попытка снять {amount} руб.")
            print("Недостаточно средств!")
        else:
            self.balance -= amount
            self.history.append(f"-{amount} руб.")
    def show_history(self):
        print(f"История счёта {self.owner}:")
        for i, op in enumerate(self.history, 1):
            print(f"{i}. {op}")
class SavingsAccount(BankAccount):
    def __init__(self, owner, rate=0.05):
        super().__init__(owner)     # owner, balance, history — сделает родитель
        self.rate = rate            # а ставку добавляем сами

    def add_interest(self):
        interest = self.balance * self.rate
        self.balance += interest
        self.history.append(f"Проценты: +{interest:.0f} руб.")

    def withdraw(self, amount):
        if amount > self.balance / 2:
            self.history.append(f"ОТКАЗ: лимит снятия (запрошено {amount})")
            print("Нельзя снять больше половины баланса!")
        else:
            super().withdraw(amount)   # прошёл наш фильтр → дальше решает родитель




# #________________________________________________________________________
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_available = True   # новая книга свободна


# class Reader:
#     def __init__(self, name):
#         self.name = name
#         self.books = []            # на руках пока ничего

# class Library:
#     def __init__(self):
#         self.catalog = []
#     def add_book(self, book):
#         self.catalog.append(book)

#     def _find(self, title):
#         for book in self.catalog:
#             if book.title == title:
#                 return book
#         return None

#     def lend(self, book_title, reader):
#         book = self._find(book_title)

#         if book is None:
#             print("Такой книги нет")
#         elif not book.is_available:
#             print("Книга занята")
#         elif len(reader.books) >= 3:
#             print("Верните сначала что-нибудь")
#         else:
#             book.is_available = False
#             reader.books.append(book)
#             print(f"{reader.name} взял «{book.title}»")

#     def take_back(self, book_title, reader):
#         for book in reader.books:
#             if book.title == book_title:
#                 book.is_available = True
#                 reader.books.remove(book)
#                 print(f"{reader.name} вернул «{book.title}»")
#                 return
#         print(f"У {reader.name} нет этой книги")

#     def show_available(self):
#         print("Свободные книги:")
#         for book in self.catalog:
#             if book.is_available:
#                 print(f"  {book.title} — {book.author}")


# print("===== МЕНЮ =====")
# lib = Library()
# reader = Reader(input("Enter your name: "))
# while True:
#     n = int(input("1)Add book\n2)Lend book\n3)Take book\n4)Show available book\n5)Exit\n Chouse one: "))
#     match n:
#         case 1:
#             title = input("Book title: ")
#             author = input("Author: ")
#             lib.add_book(Book(title, author))
#             print(f"{title} added to library")
#         case 2:
#             title = input("Book title to take: ")
#             lib.lend(title, reader)
#         case 3:
#             title = input("Book title to return: ")
#             lib.take_back(title, reader)
#         case 4:
#             lib.show_available()
#         case 5:
#             print("Good bye!")
#             break
#         case _:
#             print("you dont have book")