#铅球飞行计算问题
#面向对象的程序设计
#IPO描述为：
#输入：铅球发射角度、初始速度(m/s)、初始高度(m)
#处理：模拟铅球飞行，时刻更新铅球在飞行中的位置
#输出：铅球飞行距离(m)
#设计参数：
 #仿真参数：投掷角度angle、
			 #初始速度velocity、
			 #初始高度height、
			 #飞行距离interval
 #位置参数：x轴坐标xpos，y轴坐标ypos
 #速度分量：x轴方向上速度xvel，
			 #y轴方向上速度yvel

#根据提示输入仿真参数
angle = eval(input("Enter the launch angle(in degress):"))
angle = eval(input("Enter the initial velocity(in meters/sec):"))
angle = eval(input("Enter the initial height (in meters):"))
angle = eval(input("Enter the time interval:"))
