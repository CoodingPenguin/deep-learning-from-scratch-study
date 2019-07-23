import numpy as np

A = np.array([[1, 2] ,[3, 4]])
print(A)    # 행렬 A 출력
print(A.shape)  # 행렬의 m*n 출력
print(A.dtype)  # 행렬의 원소의 자료형 출력

B = np.array([[3, 0], [0, 6]])
print(A + B)    # 행렬의 덧셈
print(A * B)    # 행렬의 곱셈

print(A * 10)   # 행렬의 스칼라 곱