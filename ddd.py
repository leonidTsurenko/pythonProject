import requests
import colorama
def foo():
    pass


class Human:
    def __init__(self, age, height, name="Serg"):
        self.age = age
        self.height = height
        self.name =name

rg = requests
f = foo
h = Human

'''print(requests.__name__)
print(rg.__name__)
print(foo.__name__)
print(f.__name__)
print(Human.__name__)
print(h.__name__)
print(__name__)

print(tupe(Human))
print(type(h))
prrint(type(foo))
print(type(f))'''


col = colorama.Back

'''list = []'''
for method in dir(colorama):
    print(method)

''name = "Serg"
print(hasattr(name, "reverse"))
print(hasattr(name, "index"))
print(getatte(name, "index"))
print(getattr(name, "startswith"), None)

print(callable((name)))
print(callable((foo)))

class First:
    pass


class Second(First):
    pass

print(issubclass(First, Second))
print(issubclass(Second, First))


s = Second()
'''print(isinstance(s, Second))
print(isinstance(s, First))'''

import inspect

'''print(inspect,ismodule(s))
print(inspect.isclass(s))
print(inspect.isfunction(s))'''

'''signature = inspect.signature(Human)
print(signature)
for param in signature.parameters.values():
    print(param.name, param.default)'''
