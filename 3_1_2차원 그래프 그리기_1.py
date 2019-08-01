import numpy as np
import matplotlib.pyplot as plt

def end():
    print()

# 3.1.1 2차원 그래프 그리기
np.random.seed(1)  # 난수를 고정
x = np.arange(10)
y = np.random.rand(10)

plt.plot(x, y)
plt.show()

# 3.1.2 프로그램 리스트 규칙
"""
지금까지의 이력을 메모리에서 삭제하려면 다음과 같은 명령을 입력합니다.
%reset
"""

# 3.1.3 3차 함수 그리기
def f(x):
    return (x-2) * x * (x+2)
print(f(1))
print(f(np.array([1, 2, 3])))
end()

# 3.1.4 그리는 범위를 결정하기
x = np.arange(-3, 3.5, 0.5)
print(x)

"""
np.linspace(n1, n2, n)
--> 범위 n1에서 n2 사이를 일정 간격 n개의 구간으로 나눈 값을 돌려준다.
"""
x = np.linspace(-3, 3, 10)
print(np.round(x, 2))

# 3.1.5 그래프 그리기
plt.plot(x, f(x))
plt.show()
end()