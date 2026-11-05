x=[]
for i in range(10):
    print('Введите', i+1, 'элемент:')
    x.append(int(input()))
print('Маcсив х:', x)
un_x=[]
for c in x:
    if c not in un_x:
        un_x.append(c)
print('Новый массив:', un_x)
