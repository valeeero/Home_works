# 1

from collections import OrderedDict

user_info = OrderedDict({'Имя': 'Валерий', 'Фамилия': 'Лысенко', 'Рост': 184, 'Вес': 81, 'Пол': 'Мужской'})

print(user_info, id(user_info))

first_user_info = list(user_info.items())[0]
last_user_info = list(user_info.items())[-1]
user_info.move_to_end(key=first_user_info[0])
user_info.move_to_end(key=last_user_info[0], last=False)

second_user_info = list(user_info.items())[1]
del user_info[second_user_info[0]]

user_info['new_key'] = 'new_value'

print(user_info, id(user_info))

# 2

student = {"name": "Emma", "class": 9, "marks": 75}

info_marks = student.get("marks")
print("key_marks: ", info_marks)

# 3

p = {"name": "Mike", "salary": 8000}
print(p.get("age"))

# 4

sample = {"1": ["a", "b"], "2": ["c", "d"]}
print(sample.get("2")[1])

# 5
list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
list_2 = ["Киев", "Токио", "Минск"]
countryes = []
cityes = []

for item_country in list_1:
    country = item_country
    for item_city in list_2:
        city = item_city
        if country.find(city) != -1:
            countryes.append(country.split("-")[0])
            cityes.append(city)
        else:
            continue
dict_ = dict(zip(countryes, cityes))
print(dict_)

# 6

if __name__ == '__main__':

    value = []
    de_value = []
    txt = input("Введите текст для шифровки: ")
    keys = {'а': 574, 'б': 242, 'в': 334, 'г': 394, 'д': 324,
    'е': 584, 'ж': 264, 'з': 344, 'и': 284, 'й': 404,
    'к': 414, 'л': 484, 'м': 374, 'н': 564, 'о': 594,
    'п': 504, 'р': 364, 'с': 384, 'т': 494, 'у': 444,
    'ф': 572, 'х': 242, 'ц': 332, 'ч': 392, 'ш': 322, 'щ': 582,
    'ь': 262, 'ы': 342, 'э': 282, 'ю': 402, 'я': 412,
    'А': 482, 'Б': 372, 'В': 562, 'Г': 592, 'Д': 502,
    'Е': 362, 'Ж': 382, 'З': 492, 'И': 442, 'Й': 578, 'К': 248, 'Л': 338, 'М': 398,
    'Н': 328, 'О': 588, 'П': 268, 'Р': 348, 'С': 288,
    'Т': 408, 'У': 418, 'Ф': 488, 'Х': 378, 'Ц': 568, 'Ч': 598, 'Ш': 508, 'Щ': 368,
    'Ь': 388, 'Ы': 498, 'Э': 448, 'Ю': 575, 'Я': 245,
    'a': 335, 'b': 395, 'c': 325, 'd': 585, 'e': 265,
    'f': 345, 'g': 285, 'h': 405, 'i': 415, 'j': 485, 'k': 375, 'l': 565, 'm': 595,
    'n': 505, 'o': 365, 'p': 385, 'q': 495, 'r': 445,
    's': 577, 't': 247, 'u': 337, 'v': 397, 'w': 327, 'x': 587, 'y': 267, 'z': 347,
    'A': 287, 'B': 407, 'C': 417, 'D': 487, 'E': 377,
    'F': 567, 'G': 597, 'H': 507, 'I': 367, 'J': 387, 'K': 497, 'L': 447, 'M': 573,
    'N': 243, 'O': 333, 'P': 393, 'Q': 323, 'R': 583,
    'S': 263, 'T': 343, 'U': 283, 'V': 403, 'W': 413, 'X': 483, 'Y': 373, 'Z': 563,
    ' ': 593, '.': 503, ',': 363, '!': 383, '?': 493,
    '0': 571, '1': 241, '2': 331, '3': 391, '4': 321,
    '5': 581, '6': 261, '7': 341, '8': 281, '9': 401, '+': 411, '-': 481,
    '<': 371, '>': 561, '@': 591, '#': 501, '$': 361,
    '%': 381, '^': 491, '&': 441, '*': 579, '(': 249, ')': 339, '_': 399, '=': 329,
    '~': 589, '`': 269, '"': 349, ':': 289, ';': 409,
    '[': 419, ']': 489, '{': 379, '}': 569}
    txt = list(txt)

    for item in txt:
        for key in keys:
            if key == item:
                value.append(keys[key])
                de_value.append(key)
    decrypted_value = "".join(de_value)
    print(value)
    print(decrypted_value)

# 7

dict_vlaue = {i : i ** 3 for i in range(1, 11)}
print(dict_vlaue)

# 8

text = str(input("Введите текст: "))
my_dict = {i: text.count(i) for i in text}
print(my_dict)