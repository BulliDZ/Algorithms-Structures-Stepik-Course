# python 3

"""
Даны целые числа 1≤n≤1018 и 2≤m≤105, необходимо найти остаток от деления n-го числа Фибоначчи на m.

https://stepik.org/lesson/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0-%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8-13228/step/8?course=%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B-%D1%82%D0%B5%D0%BE%D1%80%D0%B8%D1%8F-%D0%B8-%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0-%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D1%8B&unit=3414

TODO:

    При решении на С++ с помощью периода Пизано необходимо учитывать, что:
    1. Период можно найти эмпирически через условие: F(i) == 1 && F(i-1) == 0, где i - номер числа Фибоначчи. Тогда период равен (i-1).
    2. Следить за переполнением при расчете i-го числа Фибоначчи, то есть выполнять строчку F(i) = (F(i-1) + F(i-2))%m, так как необходим только остаток, а он заведомо не более 100 000.
    Минус подобного решения "в лоб" - это создание динамического массива, например типа вектор, и добавление нового рассчитанного остатка от деления в конец структуры, так как необходимо отследить момент появления "периода" . Если кто-то знает как сделать лаконичнее через предварительный расчет периода Пизано и без создания массива (расчет только текущего i-го числа ФИионачии), то отпишитесь. И возможно ли это в принципе без тяжелых затрат-расчетов?

"""

from math import sqrt, floor


def fib_mod(n, m):
    sqrt5 = sqrt(5)
    if n > 100:
        golden_ratio = (1 + sqrt5) / 2
        fib = ((golden_ratio**n)%m)//(sqrt5%m)
    else:
        fib = 1 / sqrt5 * (((1 + sqrt5) / 2)**n - ((1 - sqrt5)/2)**n)
    return floor(fib % m)


if __name__ == "__main__":
    print(fib_mod(100, 1234))
    print(fib_mod(10**4, 1234))
    print(fib_mod(10**18, 2))
    print(fib_mod(1, 10**5))
    #print(fib_mod(10**18, 10**5))
    n, m = map(int, input().split())
    print(fib_mod(n, m))
