import matplotlib.pyplot as plt

dots = int(input('Введите кол-во точек: '))
a, b, c = int(input('Введите аргумент a: ')), int(input('Введите аргумент b: ')), int(input('Введите аргумент c: '))
equation = str(a) + 'x^2' + ' + ' + str(b) + 'x ' + str(c)
x = []
y = []
for i in range(-dots, dots + 1):
    x.append(i)
    y.append(a * i ** 2 + b * i + c)

plt.title('Линейная зависимость y = ax^2 + bx + c')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x, y)
plt.show()
