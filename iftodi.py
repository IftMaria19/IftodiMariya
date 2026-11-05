print('1-активная нагрузка')
print('2-индуктивная нагрузка')
print('3-смешанная нагрузка')
choice=int(input('номер варианта:'))
name=''
cosf=''
match choice:
    case 1:
        name='активная'
        cosf=1.0
    case 2:
        name='индуктивная'
        cosf=0.85
    case 3:
        name='смешанная'
        cosf=0.75
    case _:
        name='неизвестный тип'
        
f1=True
while f1:
    try:
        U=float(input('Введите напряжение(12..1000):'))
        f1= False
    except ValueError:
        print('error U')

f2=True
while f2:
    try:
        I=float(input('Введите ток(0.1..500):'))
        f2= False
    except ValueError:
        print('error I')
        
if not(12<=U<=1000):
    print('Знач. напряжения выходит за ограничение!')
elif not(0.1<=I<=500):
    print('Знач. тока выходит за ограничение!')
else:
    P=U*I*cosf/1000
    if U<220:
        klass='Низкое напряжение'
    elif U<=400:
        klass='Нормальное напряжение'
    else:
        klass='Высокое напряжение'
    print(f'Тип нагрузки: {name} {cosf}', f'Мощность:{P} кВт', f'Класс напряжения: {klass}')