# is_login = True
# def check_login(func):
#     def inner(name):
#         if is_login == True:
#             res = func(name.capitalize())
#             return res
#         else:
#             return "Please login!"
#     return inner

# @check_login
# def hello(name) -> str:
#     return f"Hello {name}"
# print(hello("akbar"))



# add = lambda a,b: [i for i in range(a,b+1) if i%2==0]
# print(add(1,11))
    
# def welcome(func):
#     def wrap(*args, **kwargs):
#         print("Welcome!")
#         return func(*args, **kwargs)
#     return wrap
# @welcome
# def hello(a):
#     return a
# print(hello(input()))
    
#2
# def goodbye(func):
#     def wrap(*args, **kwargs):
#         print("Goodbye!")
#         return func(*args, **kwargs)
#     return wrap
# @goodbye
# def sed(a):
#     return a
# print(sed(input()))

#3
# def repeat_three_times(repeat):
#     def inner(func):
#         def wrap():
#             for i in range(repeat):
#                 func()
#         return wrap
#     return inner
# @repeat_three_times(3)
# def hello():
#     print("Hello")
# hello()

# #4
# def show_function_name(func):
#     def wrap(*args, **kwargs):
#         print(f"Function: {func.__name__}")
#         return func(*args, **kwargs)
#     return wrap
# @show_function_name
# def add(a,b):
#     return a+b
# print(add(2,3))
#5
# def uppercase_result(func):
#     def inner(name):
#             res = func(name.upper())
#             return res
     
#     return inner

# @uppercase_result 
# def hello(name) -> str:
#     return f"{name}"
# print(hello(input()))
#6
# def positive_number(func):
#     def inner(num):
#         if num < 0:
#             print("The number must be positive")
#         else:
#             num=num ** 2
#             print(num)
#         return func(num)
#     return inner
# @positive_number
# def al(num):
#     return num
# al(-5)
#7
# add = lambda a,b:a+b
# print(add(7,5))
#8
# add = lambda a:a*a
# print(add(6))
#9
# add = lambda a,b: [i for i in range(a,b+1) if i%2==0]
# print(add(1,6))
    
#10
# data = [('Ali', 22), ('Sara', 19), ('Bob', 25)]
# n = sorted(data, key=lambda x: x[1])
# print(n)