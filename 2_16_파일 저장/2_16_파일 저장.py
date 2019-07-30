import numpy as np


def end():
    print()

# 2.16.1 하나의 ndarray 형을 저장
"""
1) ndarray 형을 파일에 저장
    np.save('파일명.npy', 변수명)
2) 데이터 로드
    np.load('파일명.npy')
"""

data=np.random.randn(5)
print(data)
np.save('datafile.npy', data)
data=[]
print(data)
data=np.load('datafile.npy')
print(data)
end()

# 2.16.2 여러 ndarray 형을 저장
"""
여러 개를 저장할 때는 np.savez('파일명.npz', 변수명1 = 변수명1, 변수명2 = 변수명2, ...)
"""
data1=np.array([1, 2, 3])
data2=np.array([10, 20, 30])
np.savez('datafile2.npz', data1=data1, data2=data2)
data1=[]
data2=[]
outfile=np.load('datafile2.npz')
print(outfile.files)
data1=outfile['data1']
data2=outfile['data2']
print(data1)
print(data2)
end()