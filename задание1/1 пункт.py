# validation
f1 = True
while f1:
    try:
        a=int(input('Введите начальное целое число:'))
        b=int(input('Введите конечное целое число:'))
        f1 = False
    except ValueError:
        print('ошибка ввода!')
s=0
for i in range(a,b+1):
    s+=i
print(s)