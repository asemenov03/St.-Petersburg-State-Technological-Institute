import math

def two_numbers():
    a = input('Введите первый элемент:')
    while is_int(a) == False:
        a = input('Введенный элемент не является числом, введите первый элемент:')
    b = input('Введите второй элемент:')
    while is_int(b) == False:
        b = input('Введенный элемент не является числом, введите второй элемент:')
    return float(a),float(b)

def is_int(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

a = input('Введите необходимую функцию (1.cложение, 2.вычитание, 3.умножение, 4.деление,\n5.возведение в степень, 6.логарифм, 7.округление в большую сторону до N знака после запятой,\n8.округление в меньшую сторону до N знака после запятой): ')
if a == '1':
    print(f'Результат: {sum(two_numbers())}')
if a == '2':
    n1,n2 = two_numbers()
    print(f'Результат: {n1-n2}')
if a == '3':
    n1, n2 = two_numbers()
    print(f'Результат: {n1 * n2}')
if a == '4':
    n1, n2 = two_numbers()
    print(f'Результат: {n1 / n2}')
if a == '5':
    n1, n2 = two_numbers()
    print(f'Результат: {n1 ** n2}')
if a == '6':
    print('Первое введенное число - числовое выражение, второе число - основание логарифма')
    n1, n2 = two_numbers()
    print(f'Результат: {math.log(n1,n2)}')
if a == '7':
    print('Первое введенное значение - само число, второе значение - кол-во знаков после запятой')
    n1, n2 = two_numbers()
    print(f'Результат: {round(n1,int(n2))}')
if a == '8':
    print('Первое введенное значение - само число, второе значение - кол-во знаков после запятой')
    n1, n2 = two_numbers()
    n1 = str(n1).split('.')
    n3 = n1[1]
    print(f"Результат: {str(n1[0])+'.'+n3[:int(n2)]}")


