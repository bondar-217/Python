n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set1 = set()
set2 = set()

print("Введите элементы первого множества:")
for _ in range(n):
    element = int(input())  # Вводим элемент первого множества на новой строке
    set1.add(element)  # Добавляем элемент в первое множество

print("Введите элементы второго множества:")
for _ in range(m):
    element = int(input())  # Вводим элемент второго множества на новой строке
    set2.add(element)  # Добавляем элемент во второе множество

common_elements = sorted(set1.intersection(set2))

print("Общие элементы в порядке возрастания, без повторений:")
for element in common_elements:
    print(element)
