import numpy as np

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2

    tmp = np.sum(w*x) + b   # 이게 0을 넘느냐 안 넘느냐가 중요
    if tmp <= 0:
        return 0
    else:
        return 1

print(OR(0, 0))