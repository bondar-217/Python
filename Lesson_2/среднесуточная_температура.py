n= int(input('Введите количество дней: '))
count = 0
max_count = 0

for n in range (n):
    temp = int(input('Введите температуру: '))
    if temp>0:
        count+=1
    elif temp<=0:
        count = 0
    if count>max_count:
        max_count=count
print(max_count)