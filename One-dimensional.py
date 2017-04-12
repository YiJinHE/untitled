#coding=utf-8
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(1000)
y=np.random.standard_normal(20) # 產生20個標準分布隨機數
x=range(len(y))

plt.plot(y.cumsum())
plt.grid(True) #  加格線
plt.axis('tight') #  縮小限值
#設置每個座標最小值及最大值
plt.xlim(-1,20) #X軸範圍
plt.ylim(np.min(y.cumsum())-1,np.max(y.cumsum())+1)
plt.show()