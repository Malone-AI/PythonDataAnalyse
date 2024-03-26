from matplotlib import pyplot as plt
from matplotlib import rc

font={"family":"MicroSoft YaHei"}
rc("font",**font)

a=["猩球崛起3:终极之战","敦刻尔克","蜘蛛侠:英雄归来","战狼2"]
b_14=[2358,399,2358,362]
b_15=[12357,156,2045,168]
b_16=[15746,312,4497,319]

y_14=list(range(len(a)))
y_15=[i+0.3 for i in y_14]
y_16=[i+0.3 for i in y_15]

plt.figure(figsize=(18,8),dpi=80)

plt.barh(range(len(a)),b_14,height=0.3,label="9月14日")
plt.barh(y_15,b_15,height=0.3,label="9月15日")
plt.barh(y_16,b_16,height=0.3,label="9月16日")

plt.yticks(y_15,a)

plt.legend()

plt.show()