import numpy as np

def NAND(x1, x2):
    x = np.array([x1, x2])      # 데이터
    w = np.array([-0.5, -0.5])  # 가중치
    b = 0.7                     # 편향 : 신호가 얼마나 쉽게 활성화 되는지

    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print(NAND(1, 1))
