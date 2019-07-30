import numpy as np


def end():
    print()

# 2.11.1 행렬의 사칙 연산
x = np.array([[4, 4, 4], [8, 8, 8]])
y = np.array([[1, 1, 1], [2, 2, 2]])
print(x + y)
end()

# 2.11.2 스칼라 X 행렬
"""
스칼라를 행렬에 곱하면 다음과 같이 모든 요소에 적용됩니다.
"""
x = np.array([[4, 4, 4], [8, 8, 8]])
print(10 * x)
end()

# 2.11.3 산술 함수
x = np.array([[4, 4, 4], [8, 8, 8]])
print(np.exp(x))
print(np.mean(x))  # 평균값
print(np.std(x))  # 표준편차
print(np.sqrt(x))
print(np.log(x))
end()

# 2.11.4 행렬 곱의 계산
v = np.array([[1, 2, 3], [4, 5, 6]])
w = np.array([[1, 1], [2, 2], [3, 3]])
print(v.dot(w))
end()