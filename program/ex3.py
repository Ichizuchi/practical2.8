#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def multiply_numbers():

    # Функция считывает числа с клавиатуры и перемножает их.
    # Функция запрашивает числа до тех пор, пока не будет введен 0.
    # Возвращает полученное произведение.

    result1 = 1
    while True:
        number = int(input("Введите число:"))
        if number == 0:
            break
        result1 *= number
    return result1


if __name__ == "__main__":
    result = multiply_numbers()
    print("Результат:", result)
