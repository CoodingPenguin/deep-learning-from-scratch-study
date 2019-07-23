import numpy as np

# broadcast : 곱할 때 알아서 배열을 확장해 곱해주는 것
# 내가 아는 행렬 곱이랑 다른 것 같다. 그냥 각 원소를 곱해주기 쉽게 하기 위한 것
A = np.array([[1, 2], [3, 4]])    # 2차원 배열 (2 * 2)
B = np.array([10, 20])            # 1차원 배열 (1 * 2)

print(A * B)