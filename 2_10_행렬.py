import numpy as np


def end():
    print()

# 2.10.1. 행렬의 정의
"""
ndarray의 2차원 배열로 다음과 같이 행렬을 정의할 수 있습니다.
"""
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)
end()

# 2.10.2 행렬의 크기
"""
행렬(배열)의 크기는 ndarray변수명.shape 명령으로 알 수 있습니다.
"""
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x.shape)

w, h = x.shape
print(w)
print(h)
end()

# 2.10.3 요소의 참조
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x[1, 2])
end()

# 2.10.4 요소의 수정
x = np.array([[1, 2, 3], [4, 5, 6]])
x[1, 2]=100
print(x)
end()

# 2.10.5 요소가 0과 1인 ndarray 만들기
""""
모든 요소가 0인 ndarray는 np.zeros(size)로 만들 수 있습니다.
"""
print(np.zeros(10))
"""
또한, size=(a, b)을 사용하면 모든 요소가 0인 a x b 크기의 행렬이 생성됩니다.
"""
print(np.zeros((2, 10)))
# 몇 차원이든 튜플 형태의 size를 넣어 고차원의 행렬을 생성할 수 있다.
# 모든 요소를 0이 아닌, 1로 하려면 np.ones(size) 사용
print(np.ones((2, 10)))
end()

# 2.10.6 요소가 랜덤인 행렬 생성
"""
요소가 랜덤인 행렬을 생성하는 경우 --> np.random.rand(size)
0과 1 사이의 균일한 분포 형태
"""
print(np.random.rand(2, 3))
end()
"""
np.random.randn(size) --> 평균 0, 분산 1의 가우스 분포의 난수 생성
"""

# 2.10.7 행렬의 크기 변경
"""
행렬의 크기를 변경하고 싶을 때는, 변수명.reshape(n, m) 사용
"""
a = np.arange(10)
print(a)
a = a.reshape(2, 5)
print(a)