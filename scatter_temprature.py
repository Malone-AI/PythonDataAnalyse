from matplotlib import pyplot as plt
from matplotlib import rc

font={"family":"MicroSoft YaHei"}
rc('font',**font)

y_3=[11,17,16,11,12,11,6,6,7,8,9,12,15,14,17,18,21,16,17,29,14,15,15,15,15,19,21,22,22,22,23]
y_10=[26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

plt.figure(figsize=(18,8),dpi=80)

x_3=range(1,32)
x_10=range(51,82)

plt.scatter(x_3,y_3,label="3月份")
plt.scatter(x_10,y_10,label="10月份")

#设置x轴
_x=list(x_3)+list(x_10)
_xticks_labels=["3月{}日".format(i) for i in range(1,32)]
_xticks_labels+=["10月{}日".format(i) for i in range(1,32)]
plt.xticks(_x[::2],_xticks_labels[::2],rotation=45)

#添加描述信息
plt.xlabel("时间")
plt.ylabel("温度 单位(℃)")
plt.title("北京3月及10月日最高温度一览")

#plt.scatter(label=)参数所需对象
plt.legend(loc=2)

plt.show()