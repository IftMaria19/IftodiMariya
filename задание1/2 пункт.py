# validation
f1 = True
while f1:
    try:
        N=int(input('Введите целое число(степень двойки):'))
        f1 = False
    except ValueError:
        print('ошибка ввода!')
K=0
while N>1:
    N=N//2
    K+=1
print(f'Показатель степени K = {K}')