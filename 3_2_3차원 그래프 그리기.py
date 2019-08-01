import numpy as np
import matplotlib.pyplot as plt

def end():
    print()

# 3.2.1 이변수 함수
import numpy as np
import matplotlib.pyplot as plt

def f3(x0, x1):
    r = 2 * x0 ** 2 + x1 ** 2
    ans = r * np.exp(-r)
    return ans

xn = 9
x0 = np.linspace(-2, 2, xn)
x1 = np.linspace(-2, 2, xn)
y = np.zeros((len(x0), len(x1)))
for i0 in range(xn):
    for i1 in range(xn):
        y[i1, i0] = f3(x0[i0], x1[i1])
print(x0)
print(np.round(y, 1))
end()

# 3.2.2 수치를 색으로 표현하기: pcolor
plt.figure(figsize=(3.5, 3))
plt.gray()
plt.pcolor(y)
plt.colorbar()
plt.show()
end()

# 3.2.3 함수의 표면을 표시: surface
from mpl_toolkits.mplot3d import Axes3D

xx0, xx1 = np.meshgrid(x0, x1)

plt.figure(figsize=(5, 3.5))
ax = plt.subplot(1, 1, 1, projection='3d')
ax.plot_surface(xx0, xx1, y, rstride = 1, cstride = 1, alpha = 0.3,
                color = 'blue', edgecolor = 'black')
ax.set_zticks((0, 0.2))
ax.view_init(75, -95)
plt.show()

print(x0)
print(x1)

print(xx0)
print()
print(xx1)
end()

# 3.2.4 등고선으로 표시: contour
xn = 50
x0 = np.linspace(-2, 2, xn)
x1 = np.linspace(-2, 2, xn)

y = np.zeros((len(x0), len(x1)))
for i0 in range(xn):
    for i1 in range(xn):
        y[i1, i0] = f3(x0[i0], x1[i1])

xx0, xx1 = np.meshgrid(x0, x1)
plt.figure(1, figsize=(4, 4))
cont = plt.contour(xx0, xx1, y, 5, colors = 'black')
cont.clabel(fmt = '%3.2f', fontsize=8)
plt.xlabel('$x_0$', fontsize=14)
plt.ylabel('$x_1$', fontsize=14)
plt.show()