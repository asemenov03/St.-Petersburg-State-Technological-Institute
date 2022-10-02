import time

import numpy as np


def minor(array):
    return array[0][0] * array[1][1] - array[1][0] * array[0][1]


def division(array):
    if len(array[0]) > 2:
        result = 0
        for i in range(len(array[0])):
            new_arr = []
            for j in range(len(array[0])):
                if j != i:
                    new_arr.append([array[j][k] for k in range(1, len(array[0]))])
            result += division(new_arr) * array[i][0] * (-1 + 2 * ((i + 1) % 2))
        return result
    else:
        return minor(array)


def trans_m(m_m):
    m = m_m
    trans_m = [[0] * int(3) for i in range(3)]
    for i in range(len(m)):
        for j in range(len(m[0])):
            trans_m[j][i] = m_m[i][j]
    return trans_m


def inputt():
    m = [[0] * 3 for i in range(3)]
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = int(input('Введите элемент матрицы: '))
    return m


def bez_numpy(m):
    start = time.perf_counter()
    m1_new = [[0] * 3 for k in range(3)]
    for k1 in range(len(m)):
        for k2 in range(len(m)):
            m_new = []
            for i in range(len(m)):
                for j in range(len(m)):
                    if k1 != i and k2 != j:
                        m_new.append(m[i][j])
            m_new = [[m_new[0], m_new[1]], [m_new[2], m_new[3]]]
            m1_new[k1][k2] = (-1) ** (k1 + k2 + 2) * minor(m_new)

    det = division(m)
    m1_new = trans_m(m1_new)
    for i in range(len(m1_new)):
        for j in range(len(m1_new)):
            m1_new[i][j] = round(1 / det * m1_new[i][j],2)
    print('Результат:')
    for i in range(len(m1_new)):
        print(*m1_new[i])
    print(f'{time.perf_counter() - start} секунд')


def s_numpy(m):
    start = time.perf_counter()
    m = np.array(m)
    m = np.linalg.inv(m)
    for i in range(len(m)):
        for j in range(len(m)):
            m[i][j] = round(m[i][j],2)
    print('Результат:')
    for i in range(len(m)):
        print(*m[i])
    print(f'{time.perf_counter() - start} секунд')


f = inputt()
print('Решение без numpy')
bez_numpy(f)
print('Решение с numpy')
s_numpy(f)
