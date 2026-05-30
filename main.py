# def my_function():
#     print("Hello from a function")


# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5 / 9


# print(fahrenheit_to_celsius(77))
# print(fahrenheit_to_celsius(95))
# print(fahrenheit_to_celsius(50))


# def get_greeting():
#     return "Hello from a function"


# message = get_greeting()
# print(message)


# def my_function():
#     pass


# def my_function(fname):
#     print(fname + " Refsnes")


# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# def my_function(name):  # name is a parameter
#     print("Hello", name)


# my_function("Emil")  # "Emil" is an argument


# def my_function(name="friend"):
#     print("Hello", name)


# my_function("Emil")
# my_function("Tobias")
# my_function()
# my_function("Linus")


# def my_function(country="Norway"):
#     print("I am from", country)


# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


# def my_function(fruits):
#     for fruit in fruits:
#         print(fruit)


# my_fruits = ["apple", "banana", "cherry"]
# my_function(my_fruits)


# def add(x, y):
#     return x + y


# print(add(3, 5))


# def my_function(*, name):
#     print("Hello", name)


# my_function(name="Emil")


# def my_function(name, /):
#     print("Hello", name)


# my_function("Emil")


# def my_function(*kids):
#     print("The youngest child is " + kids[2])


# my_function("Emil", "Tobias", "Linus")


# def my_function(*args):
#     print("Type:", type(args))
#     print("First argument:", args[0])
#     print("Second argument:", args[1])
#     print("All arguments:", args)


# my_function("Emil", "Tobias", "Linus")


# def my_function(greeting, *names):
#     for name in names:
#         print(greeting, name)


# my_function("Hello", "Emil", "Tobias", "Linus")


# def my_function(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total


# print(my_function(1, 2, 3))
# print(my_function(10, 20, 30, 40))
# print(my_function(5))


# def my_function(**kid):
#     print("His last name is " + kid["lname"])


# my_function(fname="Tobias", lname="Refsnes")


# def myfunc1():
#     x = "Jane"

#     def myfunc2():
#         nonlocal x
#         x = "hello"

#     myfunc2()
#     return x


# print(myfunc1())


# x = "global"


# def outer():
#     x = "enclosing"

#     def inner():
#         x = "local"
#         print("Inner:", x)

#     inner()
#     print("Outer:", x)


# outer()
# print("Global:", x)


# def changecase(func):
#     def myinner():
#         return func().upper()

#     return myinner


# @changecase
# def myfunction():
#     return "Hello Sally"


# @changecase
# def otherfunction():
#     return "I am speed!"


# print(myfunction())
# print(otherfunction())


# def changecase(n):
#     def changecase(func):
#         def myinner():
#             if n == 1:
#                 a = func().lower()
#             else:
#                 a = func().upper()
#             return a

#         return myinner

#     return changecase


# @changecase(1)
# def myfunction():
#     return "Hello Linus"


# print(myfunction())


# def myfunction():
#     return "Have a great day!"


# print(myfunction.__name__)


# def myfunc(n):
#     return lambda a: a * n


# mydoubler = myfunc(6)

# print(mydoubler(11))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_numbers = list(filter(lambda number: number % 2 != 0, numbers))
# print(odd_numbers)


# def countdown(n):
#     if n <= 0:
#         print("Done!")
#     else:
#         print(n)
#         countdown(n - 1)


# countdown(5)


# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(7))


# def my_generator():
#     yield 1
#     yield 2
#     yield 3


# for value in my_generator():
#     print(value)


# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1


# for num in count_up_to(5):
#     print(num)


def simple_gen():
    yield "Emil"
    yield "Tobias"
    yield "Linus"


gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
