# Инкапсуляция

# Ето ограничение доступа к атрибутам и методам текущего класса, классов наследников или екзепляров етого класса

# Суть Инкапсуляции ето взаемодействие с private атрибутами и методам класса только через public атрибуты и методы класса,
# чтоб не нарушить работу и целосность класса или екземпляра класса

# public      attribute    - может работать текущий класс, классы наследники и екзепляры классов
# protected   _attribute   - может работать текущий класс и классы наследники
# private     __attribute  - может работать только сам текущий класс в котором обьявлены ети атрибуты


# _attribute    одно подчеркивание только носит информационых характер для програмиста, ничего не запрещает
# ___attribute  два подчеркивание уже запрещают взаемодествовать програмисту с етими атрибутами или


class Point:

    def __init__(self, x=0, y=0):

        # указываем начальные значения атрибутов __x и __y
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    # private метод, етот метод можна вызывать только внутри текущего класса, во всех остальных случаях не можна
    def __check_value(cls, x):
        return type(x) in (int, float)

    # сеттер
    # метод служит для изменение значений private атрибутов нашего екзепляра класса
    def set_coord(self, x, y):

        # проверка типа полученых значений при изменениее значений атрибутов
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Coords must be numbers")

    # геттер
    # метод возвращает значение private атрибутов нашего екзепляра класса
    def get_coord(self):

        # значения возвращаем в виде кортежа tuple
        return (self.__x, self.__y)


my_object = Point(9, 10)

my_object.set_coord(7, 8)

# my_object.__y  # -> Error
# my_object.__x  # -> Error

my_object.get_coord()  # -> (7, 8)

dir(
    my_object
)  # -> ['_Point__check_value', '_Point__x', '_Point__y', 'get_coord', 'set_coord']

# так делать НЕЛЬЗЯ
my_object._Point__x  # -> 7
