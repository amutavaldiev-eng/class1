# def show_arguments(func):
#     def multiply(a,b):
#         print("Arguments",a,b)
#         print(a*b)
#         return func(a,b)
#     return multiply
# @show_arguments
# def n(a,b):
#     pass 
# n(4,5)
#2
# def frame(func):
#     def inner(a):
#         print("==========")
#         print(a)
#         print("==========")
#         return func(a)
#     return inner
# @frame
# def show(a):
#     pass
# show("Python")
#3
# def double_result(func):
#     def inner(a):
#         return func(a)*2
#     return inner
# @double_result
# def get_number(a):
#     return a
# print(get_number(10))
#4
# add = lambda a,b:a*b
# print(add(6,7))
#5
# def Call(func):
#     cnt = 0 
#     def wrap():
#         nonlocal cnt
#         cnt+=1
#         print(f"Call: {cnt}")
#         func()
#     return wrap
# @Call
# def fer():
#     print("Hello")
# fer()
# fer()
# fer()
#6
# def string_only(func):
#     def inner(value):
#         if type(value) == str:
#             func(value)
#         else:
#             print("A string is required")
#     return inner
# @string_only
# def show(value):
#     print(value)

# show(100)
#7
# def adult_only(func):
#     def enter_club(age):
#         if age <= 18:
#             func(age)
#             print("Access denied")
#         else:
#             print("Welcome")
#     return enter_club
# @adult_only
# def ag(age):
#     return age
# ag(16)
# ag(20)
# #8
# data = [('Ali', 75), ('Sara', 92), ('Bob', 84)]
# n = sorted(data, key=lambda x: -x[1])
# print(n)
#9
# def add_prefix(func):
#     def inner(name):
#         return "Result: "+func(name)
#     return inner
# @add_prefix
# def get_name(name):
#     return name
# print(get_name("Ali"))
#10
# def check_division(func):
#     def inner(a,b):
#         if b == 0:
#             print("Cannot divide by zero")
#         else:
#             print(a/b)
#     return inner
# @check_division
# def divide(a, b):
#     return a,b
# divide(4,2)
    
#11
# lict = [-4, 7, 0, -2, 9, 3]
# add = list(filter(lambda a: a > 0, lict))
# print(add)
#12