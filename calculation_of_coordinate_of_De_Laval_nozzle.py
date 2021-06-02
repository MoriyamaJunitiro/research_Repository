import numpy as np
import scipy.optimize as so
import matplotlib.pyplot as plt
import csv


def prandtl(M):    
    ans = 6**0.5*np.arctan(((M**2-1)/6)**0.5)-np.arctan((M**2-1)**0.5)
    return ans
#任意のマッハ数に対するプラントル数の計算

def A_nozzle(M): 
    ans = ((0.4*M**2+2)/2.4)**3 /M 
    return ans
#スロート断面積、出口断面積の比

def r(M):
    ans = r_throat * A_nozzle(M)
    return ans
#任意のマッハ数に対する半径の計算

def l(M):
    ans = M * r(M) * (prandtl(M)-v_inflection)
    return ans

def alpha(M):
    ans = np.arcsin(1/M)
    return ans

def X(M):
    ans = -r_inflection* np.cos(inflection_angle) + r(M)* np.cos(v_test - prandtl(M)) + l(M)* np.cos(v_test - prandtl(M)+ alpha(M))  + x_inflection
    return ans
#終わり部x座標計算

def Y(M):
    ans = r(M)* np.sin(v_test - prandtl(M))+ l(M)*np.sin(v_test - prandtl(M)+ alpha(M))
    return ans
#終わり部y座標計算

def contraction(y1 , y2 , L1 , L2):
    ans = (y1 - y2)/ L1  ** 2 * L2 **2 + y2
    return ans
#縮流部関数

M_test =2.0   #測定部マッハ数
inflection_angle = 0.20   #変曲点角度[rad]
height_test = 14   #ノズル出口高さ[mm]
contraction_len = 30 #縮流部長さ[mm]


v_test = prandtl(M_test)
#出口プラントル数
#print("v_test:%f"%v_test)

v_inflection = v_test - inflection_angle 
#変曲点でのプラントル数
#print("v_inflection:%f"%v_inflection)

y = lambda M: prandtl(M)- v_inflection
M_inflection = so.brentq(y, 1 ,M_test)
#変曲点でのマッハ数
#print("M_inflection:%f"%M_inflection)

height_throat = height_test/A_nozzle(M_test)
#スロート高さ[mm]
#print("height_throat:%f[mm]"%height_throat)

r_throat = height_throat / inflection_angle 
#スロート半径[mm]
#print("r_throat:%f[mm]"%r_throat)

height_inflection = height_throat*A_nozzle(M_inflection)
#変曲点高さ[mm]
#print("height_inflection:%f[mm]"%height_inflection)

r_inflection = r_throat * (height_inflection / height_throat)
#初期広がり部での半径
#print("r_inflection:%f[mm]"%r_inflection)

x_inflection = 3*(height_inflection - height_throat) / (2 * np.tan(inflection_angle))
print("x_coordinate length to inflection point : %f" %x_inflection)
#変曲点までの距離

x_initial = np.linspace(0, x_inflection, 10)
y_initial = height_throat + np.tan(inflection_angle)/x_inflection*x_initial**2*(1-x_initial/3/x_inflection)
#ノズル始まり部[mm]


M_terminal = np.linspace(M_inflection + 0.05, M_test, 10)
x_terminal = X(M_terminal)
y_terminal= Y(M_terminal)
#ノズル終わり部[mm]


x_contraction= np.linspace(-contraction_len , -1 , 10)
y_contraction= contraction(height_test , height_throat , contraction_len , x_contraction)
#縮流部[mm]


x = np.concatenate([x_initial , x_terminal ])
x = np.concatenate([x_contraction , x ])

y = np.concatenate([y_initial , y_terminal])
y = np.concatenate([y_contraction, y])

O1 = np.zeros(len(x))

plt.plot(x , y)
plt.xlabel('X[cm]')
plt.ylabel('y[cm]')
plt.title('nozzle_inflection0.20')
plt.grid(True)
plt.axes().set_aspect('equal', 'datalim')
plt.show()

with open('nozzle.csv','w')as file:
   writer = csv.writer(file, lineterminator='\n')
   writer.writerow(x)
   writer.writerow(y)
   writer.writerow(O1)

file_name = 'nozzle_contraction_len30' + 'inflection_angle0.20'+ '.csv'

fin =  open('nozzle.csv', 'r')
fout = open(file_name, 'w') 
 
for line in np.array([s.strip('\n').split(',') for s in fin]).T:
    fout.write(",".join(line) + "\n")


fin.close()
fout.close()