# class MyClass:
#     x = 5


# p = MyClass()

# # del p


# p1 = MyClass()
# p2 = MyClass()
# p3 = MyClass()

# print(p1.x)
# print(p2.x)
# print(p3.x)


# class Person:
#     pass


""" "
All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
"""

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person("Emil", 36)

# print(p1.name)
# print(p1.age)


# class Person:
#     pass


# p1 = Person()
# p1.name = "Tobias"
# p1.age = 25

# print(p1.name)
# print(p1.age)


# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age


# p1 = Person("Emil")
# p2 = Person("Tobias", 25)

# print(p1.name, p1.age)
# print(p2.name, p2.age)


# class Person:
#     def __init__(self, name, age, city, country):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.country = country


# p1 = Person("Linus", 30, "Oslo", "Norway")

# print(p1.name)
# print(p1.age)
# print(p1.city)
# print(p1.country)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print("Hello, my name is " + self.name)


# p1 = Person("Emil", 25)
# p1.greet()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def printName(self):
#         print(self.name)


# p1 = Person("Tobias")
# p2 = Person("Linus")

# p1.printname()
# p2.printname()


# class Person:
#     def __init__(myobject, name, age):
#         myobject.name = name
#         myobject.age = age

#     def greet(abc):
#         print("Hello, my name is " + abc.name)


# p1 = Person("Emil", 36)
# p1.greet()


# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"{self.year} {self.brand} {self.model}")


# car1 = Car("Toyota", "Corolla", 2020)
# car1.display_info()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return "Hello, " + self.name

#     def welcome(self):
#         message = self.greet()
#         print(message + "! Welcome to our website.")


# p1 = Person("Tobias")
# p1.welcome()


# class Car:
#     def __init__(self, brand):
#         self.brand = brand

#     def show(self):
#         print(self.brand)


# c1 = Car("Ford")
# c1.show()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person("Emil", 36)

# print(p1.name)
# print(p1.age)


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model


# car1 = Car("Toyota", "Corolla")

# print(car1.brand)
# print(car1.model)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person("Tobias", 25)
# print(p1.age)

# p1.age = 26
# print(p1.age)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person("Linus", 30)

# del p1.age

# print(p1.name)  # This works
# # print(p1.age) # This would cause an error


# class Person:
#     species = "Human"  # Class property

#     def __init__(self, name):
#         self.name = name  # Instance property


# p1 = Person("Emil")
# p2 = Person("Tobias")

# print(p1.name)
# print(p2.name)
# print(p1.species)
# print(p2.species)


# class Person:
#     lastname = ""

#     def __init__(self, name):
#         self.name = name


# p1 = Person("Linus")
# p2 = Person("Emil")

# Person.lastname = "Refsnes"

# print(p1.lastname)
# print(p2.lastname)


# class Person:
#     def __init__(self, name):
#         self.name = name


# p1 = Person("Tobias")

# p1.age = 25
# p1.city = "Oslo"

# print(p1.name)
# print(p1.age)
# print(
#     p1.city
# )  # Note: Adding properties this way only adds them to that specific object, not to all objects of the class.


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


s1 = Student("Anna", "A")
print(s1.grade)
s1.grade = "B"
print(s1.grade)
