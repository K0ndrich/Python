# Виды Копирования Списков


# 1) -----   Простое Копирование   -------------------------------------------------------------------------------------------------------------------------------

# Копируеться только ссылка на обьект
# Теперь один обьект имеет два названия

my_list1 = [1, 2, 3, 4, 5]
my_list2 = my_list1

my_list1  # -> [1, 2, 3, 4, 5]
my_list2  # -> [1, 2, 3, 4, 5]


my_list1.pop()

my_list1  # -> [1, 2, 3, 4]
my_list2  # -> [1, 2, 3, 4]


my_list2.append(10)

my_list1  # -> [1, 2, 3, 4, 10]
my_list2  # -> [1, 2, 3, 4, 10]

# 2) -----   Копирование Первого Уровня   -------------------------------------------------------------------------------------------------------------------------------

import copy 

# Копируються значения только первого уровня вложения
# ["a", "b", "c"] Не копируеться, на них продолжают ссылаться

my_list1 = [1, 2, ["a", "b", "c"], 4, 5]
my_list2 = my_list1.copy()
# или 
# my_list2 = copy.copy(my_list1)

my_list2.pop()
my_list1  # -> [1, 2, ['a', 'b', 'c'], 4, 5]
my_list2  # -> [1, 2, ['a', 'b', 'c'], 4]


my_list1 = [1, 2, ["a", "b", "c"], 4, 5]
my_list2 = my_list1.copy()


my_list2[2].append("d")
my_list1  # -> [1, 2, ['a', 'b', 'c', 'd'], 4, 5]
my_list2  # -> [1, 2, ['a', 'b', 'c', 'd'], 4, 5]


# 3) -----   Копирование Второего Уровня (Углубленное)   -------------------------------------------------------------------------------------------------------------------------------

# Копируться значения первого и второго уровня вложения

import copy
from copy import deepcopy

my_list1 = [1, 2, ["a", "b", "c"], 4, 5]

my_list2 = copy.deepcopy(my_list1)
# или 
# my_list2 = deepcopy(my_list1)

my_list2[2].append("d")

my_list1  # -> [1, 2, ['a', 'b', 'c'], 4, 5]
my_list2  # -> [1, 2, ['a', 'b', 'c', 'd'], 4, 5]


