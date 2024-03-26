from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

#第一种方法更好
##第一种方法修改字体,需要matplotlib里的rc对象
###设置字体
#font={'family':'MicroSoft YaHei','weight':'bold'}
#matplotlib.rc('font',**font)

#第二种方法,需要matplotlib里的font_manager对象
my_font=font_manager.FontProperties(fname="C:/Windows/WinSxS/amd64_microsoft-windows-font-truetype-dengxian_31bf3856ad364e35_10.0.19041.3155_none_d172ec38eb2d0657/Deng.ttf")#fname参数传入电脑中字体的路径

x=[i for i in range(0,120)]
y=[random.randint(20,35) for i in range(120)]

plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y)

#修改x轴
_x=x[::3]#对x取步长,即每隔3格取一个x刻度
_xtick_labels=["10点0{}".format(i) for i in range(10)]
_xtick_labels+=["10点{}".format(i) for i in range(10,60)]
_xtick_labels+=["11点0{}".format(i) for i in range(10)]
_xtick_labels+=["11点{}".format(i) for i in range(10,60)]
#下一行语句不可执行,因为传入的两个参数长度不一样,无法一一对应
#plt.xticks(_x,_xtick_labels)
plt.xticks(_x,_xtick_labels[::3],rotation=45,fontproperties=my_font)#rotation参数用来旋转x轴上标的刻度相应的角度,逆时针旋转
#默认不显示中文字体

#添加x轴y轴描述信息
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 单位(℃)",fontproperties=my_font)
plt.title("10点到12点每分钟的气温",fontproperties=my_font)

plt.show()