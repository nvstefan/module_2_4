# Домашняя работа по уроку "Цикл for.
# Элементы списка. Полезные функции в цикле"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(2, len(numbers) + 1):
    for j in range(2, int(i / 2) + 1):
        if (i % j) == 0:
            not_primes.append(i)
            break
    else:
        primes.append(i)
print(primes)
print(not_primes)
