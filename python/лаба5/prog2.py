import matplotlib.pyplot

y = sorted([int(i) for i in input().split()])
x = [i for i in range(len(y))]
sr = sum(y) / len(y)
print('Мат. ожидание - ', round(sr, 3))
s = 0
for i in y:
    s += (i - sr) ** 2
otkl = (s / len(y)) ** 0.5
print('Среднеквадратическое отклонение - ', round(otkl, 3))
mx = sum(x) / len(x)
my = sum(y) / len(y)
a2 = 0
a11 = 0
for i in x:
    a2 += i ** 2
for i in range(len(x)):
    a11 += x[i] * y[i]
k = (a11 - mx * my) / (a2 - mx ** 2)
b = my - k * mx
k = round(k, 3)
b = round(b, 3)
print('Константы k, b - ', k, b)
yy = []
for i in range(len(x)):
    yy.append(k * x[i] + b)
fig, ax = matplotlib.pyplot.subplots()
ax.plot(x, yy)
ax.plot(x, y)
matplotlib.pyplot.show()
