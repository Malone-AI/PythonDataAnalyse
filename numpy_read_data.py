import numpy as np
from matplotlib import pyplot as plt

#numpy读取数据
#np.loadtxt(frame,dtype=np.float,delimiter=None,skiprows=0,usecols=None,unpack=False)

#frame指文件的路径
#dtype数据类型,可选,默认np.float
#delimiter  分隔字符串,默认空格
#skiprows=x,跳过前x行
#读取指定列,索引,元组类型
#unpack是进行了矩阵转置

us_file_path=("Data_Analyse/csv_file/US_video_data_numbers.csv")
uk_file_path=("Data_Analyse/csv_file/GB_video_data_numbers.csv")

t1=np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t2=np.loadtxt(us_file_path,delimiter=",",dtype="int")

print(t2)
#print(t1)
#print("*"*20)
#print(t2)
#print("*"*20)
#print(t1.T)

#print("*"*100)
#
##取行
#print("*"*100)
#print(t2[2])
#
#print("*"*100)
#
##取连续的多行
#print("*"*100)
#print(t2[2:])
#
#print("*"*100)
#
#不连续多行
#print("*"*100)
#print(t2[[2,8,10]])

#取列
#[a,b] a表示行,b表示列
#print("*"*100)
#print(t2[1,:])
#print("*"*100)
#print(t2[2:,:])
#print("*"*100)
#print(t2[[2,10,3],:])
#print("*"*100)
#print(t2[:,0])


#取连续的多列
#print("*"*100)
#print(t2[:,2:])

#取不连续多列
#print("*"*100)
#print(t2[:,[0,2]])

#取多行多列
#print("*"*100)
#print(t2[2,3])
#print(type(t2[2,3]))
print("*"*100)
print(t2[2:5,1:3])
