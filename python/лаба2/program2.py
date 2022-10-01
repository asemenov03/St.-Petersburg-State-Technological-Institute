import numpy as np

def inputt():
    size = input('Размер матрицы: 1*2, 2*1, 1*3, 3*1, 2*2, 3*3\n')
    m = [[0] * int(size[-1]) for i in range(int(size[0]))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = int(input('Введите элемент матрицы: '))
    return m

choise = input('1)Транспонирование матрицы\n2)Умножение матриц\n3)Определение ранга\n')
if choise == '1':
    m = np.array(inputt())
    m = m.transpose()
    for i in range(len(m)):
        print(*m[i])
if choise == '2':
    print('Заполнение первой матрицы')
    m1 = np.array(inputt())
    print('Заполнение второй матрицы')
    m2 = np.array(inputt())
    m3 = np.dot(m1,m2)
    for i in range(len(m3)):
        print(*m3[i])
if choise == '3':
    size = input('Размер матрицы: 2*2, 3*3\n')
    m = [[0] * int(size[-1]) for i in range(int(size[0]))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = int(input('Введите элемент матрицы: '))
    m = np.array(m)
    print(np.linalg.matrix_rank(m))
