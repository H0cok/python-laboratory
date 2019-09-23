print('Варіант №24, Лaбораторна робота №1, Завдання #1:Три опору R1, R2, R3 з*єднані паралельно. Знайти опір з*єднання. Величина опорів вводиться користувачем.')
print('Федорченко Ростислав КМ-91')
print('Введіть опір 1')
while True:
    try:
        a = int(input())
        break
    except :
        print("Введіть число")
print('Введіть опір 2')
while True:
    try:
        b = int(input())
        break
    except :
        print("Введіть число")
print('ведіть опір 3')
while True:
    try:
        c = int(input())
        break
    except :
        print("Введіть число")

d = (a*b*c)/(a*b+b*c+c*a)
print('результуючий опір = '+str(d))
