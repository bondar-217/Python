import random

number = int(input("введите макс. чисел: "))
num = []
for i in range (number):
    num.append(random.randint(-3, 3))
print (num)
print(len(set(num)))