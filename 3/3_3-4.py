# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(a, b, c):
    return a + b + c - min(a, b, c)


a = 1
b = 7
c = 10
print(my_func(a, b, c))

# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func1(x, y):
    if complex(x).imag == 0 and x > 0:
        if y == int(y) and y < 0:
            return x ** y
        else:
            print('Некорректный ввод')

def my_func2(x, y):
    if complex(x).imag == 0 and x > 0:
        if y == int(y) and y < 0:
            result = 1
            for i in range(0, abs(y)):
                result = result / x
            return result
        else:
            print('Некорректный ввод')



print(my_func1(3, -4))
print(my_func2(3, -4))
