from matplotlib import pyplot as plt
from matplotlib import rc
font={"family":"MicroSoft YaHei"}
rc('font',**font)

x=[i for i in range(11,31)]
y=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
#_x=x[::3]
_xtick_labels=["{}岁".format(i) for i in x]

plt.figure(figsize=(10,8),dpi=80)
plt.plot(x,y)

#plt.xticks(_x,_xtick_labels[::3])
plt.xticks(x,_xtick_labels)
plt.xlabel("年龄")
plt.ylabel("女朋友个数 单位(个)")
plt.yticks(range(0,9))


plt.grid(alpha=0.4)#alpha参数是设置网格透明度

plt.show()