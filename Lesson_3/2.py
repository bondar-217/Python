def shift_sequence(sequence, k):
    k %= len(sequence)  # Вычисляем остаток от деления K на длину последовательности
    shifted_sequence = sequence[-k:] + sequence[:-k]  # Выполняем сдвиг последовательности

    return shifted_sequence  # Возвращаем сдвинутую последовательность


size = int(input("Введите размер списка: "))  # Вводим желаемый размер списка
list_nums = []
for i in range(size):  # Итерируем от 0 до размера списка
    num = int(input(f"Введите число {i + 1}: "))  # Вводим число для заполнения списка
    list_nums.append(num)  # Добавляем число в список

k = int(input("Введите количество позиций для сдвига: "))  # Вводим количество позиций для сдвига
shifted_list = shift_sequence(list_nums, k)  # Вызываем функцию для выполнения сдвига
print(shifted_list)  # Выводим результирующую последовательность
