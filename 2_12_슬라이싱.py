import numpy as np


def end():
    print()

# 2.12.1 슬라이싱의 이용
"""
슬라이스는 ':'을 사용하여 나타냅니다.
변수명[:n] --> 0부터 n-1까지의 요소
"""
x = np.arange(10)
print(x)
print(x[:5])
print(x[5:])
print(x[3:8])
print(x[3:8:2])
print(x[::-1])  # 배열 순서가 반대로 됩니다.

y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(y)
print(y[:2, 1:2])
