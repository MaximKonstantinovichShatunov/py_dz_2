# Петя впервые пришел на урок физкультуры в новой школе. Перед началом урока ученики выстраиваются по росту, в порядке
#  невозрастания. Напишите программу, которая определит на какое место в шеренге Пете нужно встать, чтобы не нарушить 
# традицию, если заранее известен рост каждого ученика и эти данные уже расположены по невозрастанию (то есть каждое следующее
#  число не больше предыдущего). Если в классе есть несколько учеников с таким же 
# ростом, как у Пети, то программа должна расположить его после них.

# Первая строка входного файла INPUT.TXT содержит натуральное число N (N ≤ 100) – количество учеников (не считая Петю). Во второй 
# строке записаны N натуральных чисел Ai (Ai ≤ 200) – рост учеников в сантиметрах в порядке невозрастания. Третья строка содержит 
# единственное натуральное число X (X ≤ 200) – рост Пети.
n= int(input())
Rost = list()
for i in range(n):
    Rost.append(int(input()))
Rost.sort()
Rost.reverse()
print(Rost)
print('введите рост новенького')
nomer=1
new_rost = int(input())
for i in Rost:
    if new_rost<=i:
        nomer+=1
print(nomer)
