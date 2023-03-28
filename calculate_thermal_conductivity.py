import os 
import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('tkagg')
#------------------------开始时间
time_start = time.time()
#------------------------开始时间
#-------------------------------模拟初始设定
lattice_constant = float(4.04)
full_length = float(100*lattice_constant)#材料全长
y_length = float(10*lattice_constant)#宽
z_length = float(10*lattice_constant)#高
Area = y_length*z_length#--------------------换热面积A^2


material_length = (0.2-0.05)*full_length#参与热流长度


##  equation ##
def Ther_cond_equation(deltaQ,deltaZ,deltaT) :
    K=(deltaQ*deltaZ)/deltaT
    return K

#-------------------------------输入文件路径
filepath = r'E:\2022-2023-30nm实验数据汇总\2023.3.27.REDAOLVLV\1100'
filepath = filepath +'/'
filename = 'caiyang_temp.txt'
file = filepath + filename
## 能量通量 ##
##              (+dQ)in----------------------------out(-dQ) ##
inQ = 10 #(eV/ps)
inQ_in_J = inQ*1.60217*(10**(-7))  #(W)
Huanre_mianji = Area*(10**(-20))    #(m^2)
deltaQ = inQ_in_J/Huanre_mianji/2    #传热方向是双线的所以除以2
material_length_in_m = material_length*(10**(-10))
temp_data = pd.read_table(file,sep=',',skiprows=1,header=None)
Trans_temp_data = temp_data.T
temp_data['deltaT'] = (temp_data.iloc[:,1]+temp_data.iloc[:,19])/2-temp_data.iloc[:,3]
thermal_conductivity = Ther_cond_equation(deltaQ,material_length_in_m,temp_data['deltaT'])
thermal_conductivity.to_csv(filepath+'thermal_conductivity.txt',sep = ' ')
mean_t_c = np.mean(thermal_conductivity)
print(mean_t_c)
#Trans_temp_data.plot()
#plt.boxplot(thermal_conductivity)
#plt.show()


