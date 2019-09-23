import math
print('Варіант №24, Лaбораторна робота №1,Завдання #2:Ввести три додатних числа а, b, с. Перевірити, чи будуть вони сторонами трикутника. Якщо так, то обчислити площу цього трикутника.')
print('Федорченко Ростислав КМ-91')
print('Введіть першу сторону')
while True:
    try:
        a = int(input())
        break
    except :
        print("Введіть число")
print('Введіть другу сторону')
while True:
    try:
        b = int(input())
        break
    except :
        print("Введіть число")
print('Введіть третю сторону')
while True:
    try:
        c = int(input())
        break
    except :
        print("Введіть число")
if a < (b+c) and b < (c+a) and c < (a+b) :
   print('Такий трикутник існує')
   v = (a+b+c)/2
   f = math.sqrt((v*(v-a)*(v-b)*(v-c)))
   print('Площа трикутника = ' + str(f))
else:
    print('такого трикутника не існує')
