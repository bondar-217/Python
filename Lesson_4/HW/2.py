n = int(input("Введите количество кустов черники: "))
bushes = list(map(int, input("Введите количество ягод на каждом кусте черники, разделенных пробелами: ").split()))

max_harvest = 0

for i in range(n):
    current_harvest = bushes[i] + bushes[(i+1) % n] + bushes[(i-1) % n]
    max_harvest = max(max_harvest, current_harvest)

print("Максимальное количество ягод, которое может быть собрано за один заход:", max_harvest)
