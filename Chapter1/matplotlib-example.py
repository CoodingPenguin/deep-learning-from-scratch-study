import numpy as np
import matplotlib.pyplot as plt     # 그래프를 그릴 수 있는 모듈

# 데이터 준비
x = np.arange(0, 6, 0.1)    # 0에서 6까지 0.1 간격으로 생성
y1 = np.sin(x)
y2 = np.cos(x)

'''
# 그래프 그리기
plt.plot(x, y1)
plt.show()  # 이걸 해줘야 그래프를 그릴 수 있다. 앞에 거는 설정하는 것
'''

# 그래프에 제목과 레이블 표시
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")    # cos함수는 점선으로
plt.xlabel("x")     # x축 이름
plt.ylabel("y")     # y축 이름
plt.title("sin & cos")   # 그래프 이름
plt.legend()
plt.show()