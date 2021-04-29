# Задача 2

set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}

print(set1.intersection(set2, set3))

# Задача 3

print("="*70)

set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}

print(set1.difference(set2, set3))

# Задача 4

print("="*70)

set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}

print(set1.union(set2,set3))

# Задача 5

print("="*70)

sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]

print(sampleSet.union(sampleList))

# Задача 6

print("="*70)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.intersection(set2)

print(set3)

# Задача 7

print("="*70)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.union(set2)

print(set3)

# Задача 8

print("="*70)

set1 = {10, 20, 30}
set2 = {20, 40, 50}

elements = set1.intersection(set2)

for i in elements:
    set1.discard(i)

print(set1)

# Задача 9

print("="*70)

set1 = {10, 20, 30, 40, 50}
delete_set = {10, 20, 30}
set1 -= delete_set
print(set1)

# Задача 11

print("="*70)

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
print(set1 & set2)

# Задача 12

print("="*70)

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

print(set1.union(set2))

# Задача 13

print("="*70)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1 = set1.intersection(set2)

print(set1)

# Задача 14

list_ = [[1, None, 2, 3, 4 + 5j, 6], [1.0, 2.5, None, 3, 9, 4.0 + 5.2j, 6.1], ['1', '2', '3.6', None, '4+5.7j', '6']]
print("Исходный список\n", list_)

list_int = []
list_float = []
list_str = []

for item in list_:
    types = [type(item_in).__name__ for item_in in item]
    type_names = []
    type_names = [elem_type for elem_type in types if elem_type not in type_names]
    types_count = [types.count(element_type) for element_type in type_names]
    max_types_count = max(types_count)
    index_max = types_count.index(max(types_count))
    max_type = type_names[index_max]
    filter_list = [element for element in item if type(element).__name__ == max_type]
    list_int.extend(filter_list)
    list_float.extend(filter_list)
    list_str.extend(filter_list)

print('Отфильтрованый список (копия)', list_int, 'id -', id(list_int))
print('Отфильтрованый список (копия)', list_float, 'id -', id(list_float))
print('Отфильтрованый список (копия)', list_str, 'id -', id(list_str))

final_list_int = [i for i in list_int if type(i).__name__ == 'int']
final_list_float = [i for i in list_float if type(i).__name__ == 'float']
final_list_str = [i for i in list_float if type(i).__name__ == 'str']

print('Результат int: ', final_list_int)
print('Результат float: ', final_list_float)
print('Результат str: ', final_list_str)