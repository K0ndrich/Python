# Создание Классов И Обьектов(Екзепляров)


# -----   САМИ КЛАССЫ   ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# создание класса
class MyClass:

    # созданеи атрибута класса, их значение будут общие(одинаковые) для всех екзепляров обьекта
    # можно создавать переменные с одинаковыми названиями для класса и екзеплара класса потому, что оно храняться в разних областях памяти
    my_name: str = "Kondrich"
    my_age: int = 20

    # dunder метод __init__ (магические методы)
    # метод инициализации класса, вызываеться при создании екзеплара текущего класса
    # self содержит ссылку на текущий создаваемый екзепляр текущего класса, можно обращаться по нему к полям и методам текущего екзепляра
    # также self может содержать ссылку на обьект созданный классом-наследником
    def __init__(self, a, b: int):

        # присваиваем значение полям(атрибутам) текущего екзепляра класса
        self.a = a
        self.b = b

    def my_method(self):
        return "- call my_method -"

    # dunder(магический) метод
    def __str__(self):
        return f"my_object (a:{self.a}) (b:{self.b})"


# -----   ЕКЗЕПЛЯРЫ (ОБЬЕКТЫ) КЛАССА  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


type(MyClass)  # -> <class 'type'>

# создание обьекта(екзепляра) моего класа
my_object = MyClass(3, 5)

my_object  # -> <__main__.MyClass object at 0x000001BE72286360>

type(my_object)  # -> <class '__main__.MyClass'>


# возвращает значение поля указаного екзепляра
my_object.a  # -> 3

# измение значения указаного поля екзепляра класа
my_object.a = 777  # -> 777
my_object.a  # -> 777

# обьект класса вызывает свой метод
my_object.my_method()  # -> - call my_method -

# вызов переопределеного нашего dunder(магическго) метода __str__
my_object  # -> my_object (a:777) (b:5)
