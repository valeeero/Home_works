from time import time


def main():
    list_of_dict_(int(input("Введите значение: ")))


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        finish_time = time()
        print(f"Функция завершена за {finish_time - start_time} секунд")

    return wrapper


@time_decorator
def list_of_dict_(n):
    list_ = []
    for v in range(n):
        dict_ = {v: v ** 2 for v in range(v + 1)}
        list_.append(dict_)
    print(list_)


if __name__ == "__main__":
    main()

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

even1 = list(filter(lambda x: x % 2 == 0, list_1))
print('1:', even1)
even2 = list(filter(lambda x: x % 2 == 0, list_3))
print('1:', even2)
odd = list(filter(lambda x: not x % 2 == 0, list_2))
print('2:', odd)
result = tuple(zip(list_1, list_2, list_3))
print('3:', result)
sum_ = tuple(map(sum, result))
print('4:', sum_)
a = tuple(filter(lambda x: not x % 2 == 0, sum_))
print('5:', a)