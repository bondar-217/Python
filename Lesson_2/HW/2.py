import math

def find_numbers(S, P):
    discriminant = S*S - 4*P  # вычисляем дискриминант

    if discriminant < 0:  # если дискриминант отрицательный, невозможно найти целочисленные значения x и y
        return None

    sqrt_discriminant = int(math.sqrt(discriminant))  # извлекаем корень из дискриминанта

    if sqrt_discriminant * sqrt_discriminant != discriminant:  # если дискриминант не является полным квадратом, невозможно найти целочисленные значения x и y
        return None

    x = (S + sqrt_discriminant) // 2  # находим значение x с помощью формулы Виета
    y = (S - sqrt_discriminant) // 2  # находим значение y с помощью формулы Виета

    return x, y

# Пример использования:
S = 4
P = 4
numbers = find_numbers(S, P)

if numbers:
    print("Задуманные числа Петей:", numbers[0], numbers[1])
else:
    print("Невозможно найти задуманные числа по заданным условиям.")
