from matplotlib import pyplot as plt

x=range(2,26,2)
y=[15,13,14.5,17,20,25,26,26,24,22,18,15]

#fisize参数是图的长宽   dpi即dot per inch即每英寸上的像素点
fig=plt.figure(figsize=(10,8),dpi=80)

#绘制图象
plt.plot(x,y)

#设置x轴刻度
#plt.xticks(x)
plt.xticks(range(0,25))

#设置y轴刻度
plt.yticks(range(min(y),max(y)+1))

#图片保存
#plt.savefig("./s1.svg")#保存.svg矢量图格式,图片放大后不失真

#图像展示
plt.show()