import numpy as np
import random

"""
a=np.array([1,2,3,4,5,])
b=np.array(range(6))
print(a,type(a))
print(b,type(b))
"""

#c=np.arange(10)#与c=np.array(range(10))相同
#print(c)

#d=np.arange(4,10,2)
#print(d)
#print(c.dtype)

#print("*"*100)
#e=np.arange(1,4,dtype=float)
#print(e)
#print(type(e))
#print(e.dtype)

#f=np.array([1,0,1,0,1,1,0],dtype=bool)
#print(f)
#print(type(f))
#print(f.dtype)

#g=f.astype("float64")
#print(g)
#print(g.dtype)

h=np.array([random.random() for i in range(10)])
print(h)
print(h.dtype)

#小数取舍
i=np.round(h,2)
print(i)