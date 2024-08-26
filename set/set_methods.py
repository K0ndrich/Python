# Методы Множеств

my_set = {1, 3, 4}

# добавление указаного значения в множество
my_set.add(2)  # -> {1, 2, 3, 4}

# удаление указаного значения из множества
my_set.remove(3)  # -> {1, 2, 4}

# удаление указаного значения из множества при ненахождении не выдает ошибку
my_set.discard(7)  # -> None


# issubset проверяет включено ли первое множество my_set1 внутрь второго my_set2
my_set1 = {1, 2}
my_set2 = {1, 2, 3, 4, 5, 6}
my_set1.issubset(my_set2)  # -> True


# issuperset проверяет включено ли воторое множество my_set1 внутрь первого my_set2
my_set1 = {1, 2}
my_set2 = {1, 2, 3, 4, 5, 6}
my_set2.issuperset(my_set1)  # -> True




# -----   Обьединение Множеств   -----------------------------------------------------------------------------------------------------------------------------------

my_set1 = {1, 2, 3, 4}
my_set2 = {3, 4, 5, 6}


# - (1, 2, 3, 4, 3, 4, 5, 6) -
my_set1 | my_set2  # -> {1, 2, 3, 4, 5, 6}
my_set1.union(my_set2)  # -> {1, 2, 3, 4, 5, 6}


# - 1, 2, (3, 4, 3, 4) 5, 6 -
my_set1.intersection(my_set2)  # -> {3, 4}
my_set1 & my_set2  # -> {3, 4}


# - (1, 2) 3, 4, 3, 4, 5, 6 -
my_set1.difference(my_set2)  # -> {1, 2}


# - (1, 2) 3, 4, 3, 4, (5, 6) -
my_set1.symmetric_difference(my_set2)  # -> {1, 2, 5, 6}
(my_set1 | my_set2) - (my_set1 & my_set2)  # -> {1, 2, 5, 6}
