lst = input("Введите элементы списка через пробел: ").split()
lst = [int(x) for x in lst]

minimum = int(input("Введите минимум: "))
maximum = int(input("Введите максимум: "))

indexes = [i for i in range(len(lst)) if lst[i] >= minimum and lst[i] <= maximum]

if len(indexes) > 0:
    print("Индексы элементов, значения которых находятся в диапазоне [{}; {}]:".format(minimum, maximum))
    print("\n".join(map(str, indexes)))
else:
    print("В списке нет элементов, удовлетворяющих заданному диапазону.")
