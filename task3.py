print('Варіант №24, Лaбораторна робота №1, Завдання #3:знайти значення функції')
print('Федорченко Ростислав КМ-91')
print('Введіть змінну')
while True:
    try:
        a = int(input())
        break
    except :
        print("Введіть число")
if a <= 13:
    b = -1 / (a**2 + 9)
    print(str(b))
else :
    b = -(a**2 + 9)
    print(str(b))