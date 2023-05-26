def min_coin_flips(coins):
    heads_down = coins.count(0)  # количество монеток, лежащих решкой вниз
    tails_down = coins.count(1)  # количество монеток, лежащих гербом вниз

    return min(heads_down, tails_down)  # возвращаем минимальное количество монеток, которые нужно перевернуть

# Пример использования:
coins = [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0]
min_flips = min_coin_flips(coins)
print("Минимальное количество монеток, которые нужно перевернуть:", min_flips)
