import fanc
import time

i = int(input('Выберете сортировку: 1 - быстрая сортировка, 2 - сортировка расческой - '))
if i == 1:
    my_list = list(map(int,input("Ввод списка: ").split()))
    start = time.time() * 1000
    print(fanc.f(my_list))
    print(f'Время в миллисекундах: {time.time() * 1000 - start}')
elif i == 2:
    my_list = list(map(int,input("Ввод списка: ").split()))
    start = time.time() * 1000
    print(fanc.greben(my_list))
    print(f'Время в миллисекундах: {time.time() * 1000 - start}')
