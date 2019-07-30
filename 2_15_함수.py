import numpy as np


def end():
    print()

# 2.15.1 함수의 사용
def my_func1():
    print("Hi!")
my_func1()

def my_func2(a, b):
    c=a+b
    return c
print(my_func2(1, 5))
end()

# 2.15.2 인수와 반환값
def my_func3(D):
    m = np.mean(D)
    s = np.std(D)
    return m, s

data=np.random.randn(100)
data_mean, data_std=my_func3(data)
print("mean:{0:3.2f}, std:{1:3.2f}".format(data_mean, data_std))