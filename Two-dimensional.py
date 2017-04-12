#coding=utf-8
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(2000)
y = np.random.standard_normal((20, 2)).cumsum(axis=0)#產生20*2個變數，計算樣本數在0的位置總和

fig,ax1=plt.subplots()
plt.plot(y[:,0],'b',lw=1.5,label='1st')#lw線寬
plt.plot(y[:,0],'ro')#r指紅色 ，o指圓標記
plt.grid(True)#  加格線
plt.legend(loc=0)#plt. legend位置選項
plt.axis('tight') #  縮小限值
plt.xlabel('index')#x軸名稱
plt.ylabel('value 1st')#y軸名稱
plt.title('A Simple Plot')#圖表標題
ax2=ax1.twinx()
plt.plot(y[:,1],'g',lw=1.5,label='2nd')
plt.plot(y[:,1],'ro')#r指紅色 ，o指圓標記
plt.legend(loc=0)#plt. legend位置選項
plt.ylabel('value 2nd')#y軸名稱
plt.show()


#兩張圖表
#上圖
plt.figure(figsize=(7, 5))
plt.subplot(211)#subplots繪圖列
plt.plot(y[:,0],'b',lw=1.5,label='1st')#lw線寬
plt.plot(y[:,0],'ro')#r指紅色 ，o指圓標記
plt.grid(True)#  加格線
plt.legend(loc=0)#plt. legend位置選項
plt.axis('tight')#  縮小限值
plt.ylabel('value 1st')#y軸名稱
plt.title('A Simple Plot')#圖表標題
#下圖
plt.subplot(212)#subplots繪圖列
plt.plot(y[:,1],'g',lw=1.5,label='2nd')#lw線寬
plt.plot(y[:,1],'ro')#r指紅色 ，o指圓標記
plt.legend(loc=0)#plt. legend位置選項
plt.grid(True)#  加格線
plt.xlabel('index')#x軸名稱
plt.ylabel('value 2nd')#y軸名稱
plt.show()

