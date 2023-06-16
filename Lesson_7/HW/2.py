def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):  # Цикл для перебора номеров строк от 1 до num_rows
        row = []  # Создаем пустой список для хранения элементов строки
        for j in range(1, num_columns + 1):  # Цикл для перебора номеров столбцов от 1 до num_columns
            element = operation(i, j)  # Вычисляем элемент таблицы с помощью переданной функции operation
            row.append(str(element))  # Добавляем вычисленный элемент в список row, преобразовывая его в строку
        print(" ".join(row))  # Выводим элементы строки, объединяя их через пробел

print_operation_table(lambda x, y: x * y)
