def end():
    print()

# 2.9.1 넘파이의 이용
import numpy as np
end()

# 2.9.2 벡터의 정의
x = np.array([1, 2, 3])
print(x)

y=np.array([4, 5, 6])
print(x+y)
print(type(x))
end()

# 2.9.3 요소의 참조
print(x[0])

# 2.9.4 요소의 수정
x[0] = 100
print(x)
end()

# 2.9.5 연속된 정수 벡터의 생성
print(np.arange(10))
"""np.arange(n): 요소의 값이 1씩 증가하는 벡터 배열을 만들 수 있다."""
print(np.arange(5, 10))
end()

# 2.9.6 ndarray 형의 주의점
"""
b=a 와 같이 ndarray 형을 복사하면 a의 내용이 저장된 곳의 참조 주소가 전달된다.
따라서, b=a.copy() 로 복사를 하게 된다.
"""
a = np.array([1, 1])
b = a
print('a = ' + str(a))
print('b = ' + str(b))
b[0]=100
print('b = ' + str(b))
print('a = ' + str(a))

a = np.array([1,1])
b = a.copy()
print('a = ' + str(a))
print('b = ' + str(b))
b[0] = 100
print('b = ' + str(b))
print('a = ' + str(a))
end()