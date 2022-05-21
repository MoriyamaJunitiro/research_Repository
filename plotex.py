from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
 
# ランダムな点を生成する(x, y, z座標)
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)
 
# figureを生成する
fig = plt.figure()
 
# axをfigureに設定する
ax = fig.add_subplot(projection='3d')
 
# axesに散布図を設定する
ax.scatter(x, y, c='b')
 
# 表示する
plt.show()
