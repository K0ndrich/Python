# Методы Класов и Обьетков
# __my_method__ ето dunder(магические методы)


class MyClass:

    # метод __init__ создает обьект(екзепляр) текущего класса
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # метод __str__ управляет что будет выводить print()
    def __str__(self):
        return f"my_object -> a:{self.a} , b:{self.b}"

    def my_method(self):
        pass


# возвращает словарь с полями(атрибутами) и значениями текущего всего класса
MyClass.__dict__  # -> {'__module__': '__main__', '__init__': <function MyClass.__init__ at 0x0000015FFF5AD3A0>, '__str__': <function MyClass.__str__ at 0x0000015FFF5AD1C0>, 'my_method': <function MyClass.my_method at 0x0000015FFF5AD440>, '__dict__': <attribute '__dict__' of 'MyClass' objects> }


my_object = MyClass(3, 5)
# возвращает словарь с полями(атрибутами) и значениями текущего одного обьекта класса
my_object.__dict__  # -> {'a': 3, 'b': 5}
