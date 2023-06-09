def power_recursive(A, B):
    if B == 0:
        return 1
    return A * power_recursive(A, B - 1)

# Ввод чисел A и B
A = int(input("Введите число A: "))
B = int(input("Введите степень B: "))

# Вызов функции power_recursive и вывод результата
result = power_recursive(A, B)
print("Результат возведения числа", A, "в степень", B, ":", result)
