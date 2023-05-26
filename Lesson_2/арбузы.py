number = 0
while number <= 0:
    number = int(input("Input number: "))

max_num = 0
min_num = 999

for i in range(number):
    watermelon = int(input(f"Input {i+1} watermelon's weight: "))
    if watermelon > max_num:
        max_num = watermelon
    if watermelon < min_num:
        min_num = watermelon

print(max_num, min_num)
