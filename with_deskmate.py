from matplotlib import pyplot as plt
from matplotlib import rc
font={"family":"MicroSoft YaHei"}
rc('font',**font)

x=[i for i in range(11,31)]
y=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]#自己
z=[1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]#同桌

#_x=x[::3]
_xtick_labels=["{}岁".format(i) for i in x]

plt.figure(figsize=(10,8),dpi=80)
plt.plot(x,y,label="自己",color='#FFB6C1',linestyle=':',linewidth=3)#label参数是添加图列,但是要添加plt.legend()对象
plt.plot(x,z,label="同桌",color='blue',linestyle='-.',linewidth=3)#linestyle参数改变线条类型,:是虚线,-.是点画线
#linewidth参数改变线条粗细

#plt.xticks(_x,_xtick_labels[::3])
plt.xticks(x,_xtick_labels)
plt.xlabel("年龄")
plt.ylabel("女朋友个数 单位(个)")
plt.yticks(range(0,9))


plt.grid(alpha=1,linestyle=':')#alpha参数是设置网格透明度,网格也有linestyle参数

plt.legend(loc=1)#添加loc参数,其中值为[0,10],可以改变添加的图例的位置

#plt.savefig('./s.png')

plt.show()
