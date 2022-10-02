choise = input('1)Транспонирование матрицы\n2)Умножение матриц\n3)Определение ранга\n')
if choise == '1':
    size = input('Размер матрицы:1*2, 2*1, 1*3, 3*1, 2*2, 3*3\n')
    m = [[0] * int(size[-1]) for i in range(int(size[0]))]
    trans_m = [[0] * int(size[0]) for i in range(int(size[-1]))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = int(input('Введите элемент матрицы: '))
            trans_m[j][i] = m[i][j]
    print(m)
    print(trans_m)
elif choise == '2':
    size1 = input('Размер первой матрицы:1*2, 2*1, 1*3, 3*1, 2*2, 3*3\n')
    size2 = input('Размер второй матрицы:1*2, 2*1, 1*3, 3*1, 2*2, 3*3\n')
    if size1[-1] == size2[0]:
        m1 = [[0] * int(size1[-1]) for i in range(int(size1[0]))]
        m2 = [[0] * int(size2[-1]) for i in range(int(size2[0]))]
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                m1[i][j] = int(input('Введите элемент первой матрицы: '))
        for i in range(len(m2)):
            for j in range(len(m2[0])):
                m2[i][j] = int(input('Введите элемент второй матрицы: '))
        answer = [[0] * int(size2[-1]) for i in range(int(size1[0]))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                answer[i][j] = sum(m1[i][w] * m2[w][j] for w in range(len(m2)))
        print(m1, '*', m2, '=', answer)
    else:
        print("Столбцы первой матрицы должны быть равны строкам второй матрицы")
elif choise == '3':
    size = input('Размер матрицы:2*2, 3*3\n')
    rang = int(size[-1])
    m = [[0] * int(size[-1]) for i in range(int(size[0]))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = int(input('Введите элемент матрицы: '))
    for i in range(len(m)):
        count = 0
        for j in range(len(m[0])):
            if m[i][j] == 0:
                count += 1
            if count == int(size[-1]):
                rang -= 1
    print(f'Ранг матрицы равен {rang}')
