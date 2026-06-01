# x = ("apple", "banana", "cherry")
# y = enumerate(x)

# print(y)

from typing import List

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

print(x)


def greet(names: List[str]) -> str:
    return f"Hello {', '.join(names)}"


result = greet(["Emil", "Linus"])
print(result)
