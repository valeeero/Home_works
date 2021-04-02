# 1

school = {'2а': 12, '3а': 15, '4а': 20, '5а': 11, '2б': 33, '3б': 14, '4б': 25, '5б': 9, '2в': 16, '5в': 13}

print('Классы и количество учеников до изменений', school)

school['3б'] += 2
school['4в'] = 11
del school['5а']

print('Классы и количество учеников после изменений', school)
print('Количество всех учеников = ', sum(school.values()))

# 2

dict_ = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
print(dict_)

keys = dict_.keys()
value = dict_.values()

dict_ = dict(zip(value, keys))
print(dict_)