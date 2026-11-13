x=[]
for i in range(10):
    f1 = True
    while f1:
        try:
            n=int(input(f'Введите {i+1} элемент:'))
            x.append(n)
            f1 = False
        except ValueError:
            print('Введите целое число!')
print('Маcсив х:', x)
un_x=[]
for c in x:
    if c not in un_x:
        un_x.append(c)
print('Новый массив:', un_x)
