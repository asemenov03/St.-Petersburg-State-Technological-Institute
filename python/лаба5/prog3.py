from math import *
import random
visa = open('visa2021.txt')
visa = visa.read().split()
mcard = open('mastercard2021.txt')
mcard = mcard.read().split()
visa_price = []
mcard_price = []
for i in range(3, len(visa)-3, 2):
    visa_price.append(float(visa[i]))
    mcard_price.append(float(mcard[i]))

def pirson(visa_price,mcard_price):
    visa_otcl = []
    mcard_otcl = []
    visa_otcl2 = []
    mcard_otcl2 = []
    pr_price = []
    sr_visa = sum(visa_price)/len(visa_price)
    sr_mcard = sum(mcard_price)/len(mcard_price)
    for i in range(len(visa_price)):
        visa_otcl.append(sr_visa - visa_price[i])
        mcard_otcl.append(sr_mcard - mcard_price[i])
    for i in range(len(visa_otcl)):
        visa_otcl2.append(visa_otcl[i]**2)
        mcard_otcl2.append(mcard_otcl[i]**2)
    visa_otcl2 = sum(visa_otcl2)
    mcard_otcl2 = sum(mcard_otcl2)
    for i in range(len(visa_otcl)):
        pr_price.append(visa_otcl[i]*mcard_otcl[i])
    print(f'Коэффициент корреляции Пирсона: {sum(pr_price)/(sqrt(visa_otcl2*mcard_otcl2))}')

def dell(visa_price, mcard_price): #удаление случайных элементов из списка
    visa_price1 = []
    mcard_price1 = []
    index = [int(random.randint(0,len(visa_price))) for i in range(40)]
    for i in range(len(visa_price)):
        if i in index:
            visa_price1.append(0)
            mcard_price1.append(0)
        else:
            visa_price1.append(visa_price[i])
            mcard_price1.append(mcard_price[i])
    return visa_price1,mcard_price1

visa_price1, mcard_price1 = dell(visa_price,mcard_price)

def vinzon(visa_price1,mcard_price1): #восстановление с помощью винзорирования
    print('Список после удаление случайных элементов')
    print(f'Visa: {visa_price1}')
    print(f'Mastercard: {mcard_price1}')
    if visa_price1[0] == 0:
        visa_price1[0] = visa_price1[1]
    if visa_price1[len(visa_price1)-1] == 0:
        visa_price1[len(visa_price1)-1] = visa_price1[len(visa_price1)-2]
    if mcard_price1[0] == 0:
        mcard_price1[0] = mcard_price1[1]
    if mcard_price1[len(mcard_price1)-1] == 0:
        mcard_price1[len(mcard_price1)-1] = mcard_price1[len(mcard_price1)-2]
    for i in range(1,len(visa_price1)-1):
        if visa_price1[i] == 0:
            visa_price1[i] = visa_price1[i-1]
        if mcard_price1[i] == 0:
            mcard_price1[i] = mcard_price1[i-1]
    print('Метод винзорирования')
    print(f'Visa: {visa_price1}')
    print(f'Mastercard: {mcard_price1}')

def lin(visa_price1, mcard_price1):
    count = 2
    if visa_price1[0] == 0:
        visa_price1[0] = visa_price1[1]
    if visa_price1[len(visa_price1)-1] == 0:
        visa_price1[len(visa_price1)-1] = visa_price1[len(visa_price1)-2]
    if mcard_price1[0] == 0:
        mcard_price1[0] = mcard_price1[1]
    if mcard_price1[len(mcard_price1)-1] == 0:
        mcard_price1[len(mcard_price1)-1] = mcard_price1[len(mcard_price1)-2]
    for i in range(1,len(visa_price1)-1):
        if visa_price1[i] == 0:
            if visa_price1[i-1] != 0 and visa_price1[i+1] != 0:
                visa_price1[i] = (visa_price1[i-1]+visa_price1[i+1])/count
                print(count)
            else:
                for j in range(i+1,len(visa_price1)):
                    if j != 0:
                        visa_price1[i] = round((visa_price1[i-1]+visa_price1[i+1])/count,2)
                        break
                    else:
                        count += 1
    print('Метод линейной аппроксимации')
    print(f'Visa: {visa_price1}')


pirson(visa_price, mcard_price)
vinzon(visa_price1, mcard_price1)
lin(visa_price1, mcard_price1)
