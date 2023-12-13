import math


def circle(radius):
    return math.pi * radius ** 2


def cylinder():
    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))

    base_area = circle(radius)

    full_area = input("Вам нужна вся площадь цилиндра? (да/нет): ").lower() == 'да'

    if full_area:

        lateral_area = 2 * math.pi * radius * height
        total_area = 2 * base_area + lateral_area
        print(f"Полная площадь цилиндра равна: {total_area}")
    else:
        # Print the area of the base only
        print(f"Площадь основания цилиндра равна: {base_area}")


cylinder()
