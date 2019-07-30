import numpy as np


def end():
    print()

# 2.13.1 bool 배열 사용
"""
넘파이를 통해 행렬 데이터에서 특정 조건을 만족하는 것을 추출하여 쉽게 수정할 수 있다.
"""

x = np.array([1, 1, 2, 3, 5, 8, 13])
print(x > 3)
print(x[x > 3])
x[x > 3] = 0  # 조건을 만족하는 경우 0으로 값을 바꾼다.
print(x)