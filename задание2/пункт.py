1
f1 = True
while f1:
    s = str(input('Введите строку:'))
    if s.isalpha():
        f1 = False
    else:
        print('введите только буквы!')

print(s.lower())