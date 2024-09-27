# Методы Класов и Обьетков
# __my_method__ ето dunder(магические методы)


# -----   Сам Класс и его Атрибуты и Методы   ---------------------------------------------------------------------------------------------------------------------------------------------------------


class MyClass:

    # метод new вызваеться  перед создание екзепляра обьекта класса
    # cls ссылаеться на текущий екзепляр класса, а именно на наш текущий класс MyClass
    def __new__(cls, *args, **kwargs):
        return str(cls)

    # метод __init__ вызываеться в момент создания екзепляра обьекта класса
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # метод __str__ управляет что будет выводить print()
    def __str__(self):
        return f"my_object -> a:{self.a} , b:{self.b}"

    # создание моего методы
    def my_method(self):
        pass


# -----   Атрибуты Обьектов   ---------------------------------------------------------------------------------------------------------------------------------------------------------

my_object = (
    MyClass()
)  # -> -> <class '__main__.MyClass'> , -> <class '__main__.MyClass'>


# возвращает словарь с полями(атрибутами) и названиями методов текущего класса
MyClass.__dict__  # -> {'__module__': '__main__', '__init__': <function MyClass.__init__ at 0x0000015FFF5AD3A0>, '__str__': <function MyClass.__str__ at 0x0000015FFF5AD1C0>, 'my_method': <function MyClass.my_method at 0x0000015FFF5AD440>, '__dict__': <attribute '__dict__' of 'MyClass' objects> }


# возвращает MRO последовательность наследования текущего дочернего класса от родительских классов
MyClass.__mro__  # -> (<class '__main__.MyClass'>, <class 'object'>)


# возвращает словарь с локальными полями(атрибутами) и локальными значениями текущего одного обьекта класса
my_object = MyClass(3, 5)
# my_object.__dict__  # -> {'a': 3, 'b': 5}


# возвращает название класса по которому создался текущий обьект
my_object.__class__  # -> <class '__main__.MyClass'>
