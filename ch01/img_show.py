# coding: utf-8
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np
import numpy as np  #载入numpy
import matplotlib.pyplot as plt  #载入matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D  #载入Axes3D用以实现3D作图



fig=plt.figure(figsize=(6,6)) #创建一个对象（正方形窗体）#注意由于3D作图是设置'equal'没什么效果，且3D作图的缩放是等比例缩放所以只需要设定窗体为正方形并且不去变动窗体形状就可以保证x、y、z刻度长度一致
ax=Axes3D(fig) #设置这个对象为3D作图的



t=np.linspace(-1,1,100)#设置一个参数t

#设计一个单变量的参数方程
x=t
y=t**3
z=t




ax.plot(x,y,z,label='First Curve') #用ax进行3D作画


# m=max(max(x),max(y),max(z))#求出x,y,z三个集合中的最大元素
#
#
# #用xyz中的最大元素建立直角坐标系，由于此时xyz三个方向上的最大最小值大小都相同，→此时xyz三轴的刻度长度是相等的（一举两得）
# ax.plot([-m,m],[0,0],[0,0],label='x-axis')
# ax.plot([0,0],[-m,m],[0,0],label='y-axis')
# ax.plot([0,0],[0,0],[-m,m],label='z-axis')
#
# ax.legend()
# ax.set_xlabel('x axis')#标注x、y、z轴帮助观察
# ax.set_ylabel('y axis')
# ax.set_zlabel('z axis')
plt.show()