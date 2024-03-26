import numpy as np

a=np.array([10,20,30,40])
b=np.arange(4)

c=a-b
d=a+b
print(a,b,c,d,sep='\n')

print(b**2)

c=10*np.sin(a)
print(c)

print(10*np.tan(a))

print(b<3)

print(b==3)

a=np.array([[1,1],[0,1]])
b=np.arange(4).reshape((2,2))

print(a)
print(b)

#*是对应位置的元素相乘
print(a*b)

#np.dot()矩阵乘法
print(np.dot(a,b))
#等价写法
print(b.dot(a))

#np.random.random创建一个元素为0~1的矩阵,接收一个矩阵行数和列数的序偶
a=np.random.random((3,4))
print(a)

a=np.arange(4).reshape((2,2))
print(a)
print(np.sum(a,axis=1))
print(np.sum(a))
print(np.min(a))
print(np.max(a))
