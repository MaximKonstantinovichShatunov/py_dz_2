# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Входной файл INPUT.TXT содержит целое число N (1 < N ≤ 106).

print('введите целое число, отличное от 1')
n=int(input())

for i in range(2,n+1):
    if n%i==0:
        print(i)
        break
