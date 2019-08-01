import numpy as np
import matplotlib.pyplot as plt

def end():
    print()

# 3.1.6 그래프를 장식하기
def f2(x, w):
    return (x-w) * x * (x+2)

x= np.linspace(-3, 3, 100)
plt.plot(x, f2(x, 2), color='black', label='$w=2$')
plt.plot(x, f2(x, 1), color='cornflowerblue', label='$w=1$')
plt.legend(loc="upper left")
plt.ylim(-15, 15)
plt.title('$f_2(x)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True)
plt.show()

import matplotlib
print(matplotlib.colors.cnames)
# color=(a, b, c)의 형태로도 나타낼 수 있다.
end()

# 3.1.7 그래프를 여러 개 보여주기
plt.figure(figsize=(10, 3))
plt.subplots_adjust(wspace=0.5, hspace=0.5)
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.title(i + 1)
    plt.plot(x, f2(x, i), 'k')
    plt.ylim(-20, 20)
    plt.grid(True)
plt.show()
end()