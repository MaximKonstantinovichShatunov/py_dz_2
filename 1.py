# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное
# число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.

from random import randint
k = 0
n = int(input())
a = [randint(0, 1) for i in range(n)]
print(a)
for i in range(n):
    if a[i] == 0:
        k += 1
if k <= n/2:
    print(k)
else:
    print(n-k)
