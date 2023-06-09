# Создаем словарь с буквами и их очками для английского алфавита
eng_scores = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
              'D': 2, 'G': 2,
              'B': 3, 'C': 3, 'M': 3, 'P': 3,
              'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
              'K': 5,
              'J': 8, 'X': 8,
              'Q': 10, 'Z': 10}

# Создаем словарь с буквами и их очками для русского алфавита
rus_scores = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
              'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
              'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
              'Й': 4, 'Ы': 4,
              'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
              'Ш': 8, 'Э': 8, 'Ю': 8,
              'Ф': 10, 'Щ': 10, 'Ъ': 10}

# Просим пользователя ввести слово
word = input("Введите слово: ")

# Инициализируем переменную для хранения суммы очков
score = 0

# Проверяем, что введенное слово состоит только из букв
if word.isalpha():
    # Проверяем, принадлежит ли первая буква введенного слова английскому алфавиту
    if word[0] in eng_scores:
        # Проходимся по каждой букве в верхнем регистре в слове
        for letter in word.upper():
            # Получаем значение очков для каждой буквы из словаря eng_scores и добавляем его к общей сумме score
            score += eng_scores.get(letter, 0)
    # Проверяем, принадлежит ли первая буква введенного слова русскому алфавиту
    elif word[0] in rus_scores:
        # Проходимся по каждой букве в верхнем регистре в слове
        for letter in word.upper():
            # Получаем значение очков для каждой буквы из словаря rus_scores и добавляем его к общей сумме score
            score += rus_scores.get(letter, 0)
    else:
        # Если первая буква не принадлежит ни английскому, ни русскому алфавиту, выводим сообщение об ошибке
        print("Ошибка! Слово не соответствует выбранному алфавиту.")
        exit(1)  # Завершаем программу с кодом ошибки 1
else:
    # Если введено некорректное слово (содержит символы помимо букв), выводим сообщение об ошибке
    print("Ошибка! Введено некорректное слово.")

# Выводим общую сумму очков
print(score)
