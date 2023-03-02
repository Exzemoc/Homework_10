print('''Выберите операцию:
        1 - Сумма
        2 - Разность
        3 - Умножение
        4 - Деление
        5 - Возведение а в степень b
        6 - Деление по модулю
        7 - Целочисленное деление''')
x = int(input())
if 1<=x<=7:
    try:
        if x == 1:
            print('Сумма:')
            a = int(input('a = '))
            b = int(input('b = '))
            c = a + b
            print(c)
        elif x == 2:
            print('Разность:')
            a = int(input('a = '))
            b = int(input('b = '))
            c = a - b
            print(c)
        elif x == 3:
            print('Умножение:')
            a = int(input('a = '))
            b = int(input('b = '))
            c = a * b
            print(c)
        elif x == 4:
            print('Деление:')
            a = int(input('a = '))
            b = int(input('b = '))
            c = a / b
            print(c)
        elif x == 5:
            print('Возведение а в степень b:')
            a = int(input('a = '))
            b = int(input('b = '))
            c = a**b
            print(c)
        elif x == 6:
            print('Деление по модулю:')
            a = int(input('a = '))
            b = int(input('b = '))
            c = a % b
            print(c)
        elif x == 7:
            print('Целочисленное деление:')
            a = int(input('a = '))
            b = int(input('b = '))
            c = a//b
            print(c)
    except ValueError:
        print('Invalid value')
    except ZeroDivisionError:
        print('Divided by zero')
else:
    print('Incorrect value')
