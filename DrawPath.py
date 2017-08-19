#根据数据文件在窗口中动态路径绘制。
import turtle
def main():
	#设置窗口信息
	turtle.title("数据驱动的动态路径绘制")
	turtle.setup(800,600,0,0)
	#设置画笔
	pen = turtle.Turtle()
	pen.color("red")
	pen.width(5)
	pen.shape("turtle")
	pen.speed(20)
	#读取文件
	result = []
	file = open("data.txt","r")
	#处理文件
	for line in file:
		result.append(list(map(float,line.split(','))))
		#1、line.split:把文件一行按逗号隔开的数据变成一个列表，但是每一个数据还是字符串。
		#2、map:map是映射函数，map函数用法大致如下：map(function,iterable)。
		#这里的用处是把字符串的列表变成了浮点型数据的列表。
		#3、因为map()的返回值已经不再是list，而是iterator。所以又用了一个list,将iterator转换成list。
		#4、使用append方法将列表添加到result列表中。
		#print(result)
	#动态绘制
	for i in range(len(result)):#len的值是文件data的行数。
		pen.color((result[i][3],result[i][4],result[i][5]))
		#result是个二维的列表，因为每个元素又是一个列表。
		#第i个元素的最后三个分别是R,G,B的值 
		pen.forward(result[i][0])
		if result[i][1]:
			pen.rt(result[i][2])
		else:
			pen.lt(result[i][2])
	pen.goto(0,0)


#if_name_=='_main_'
while True:
        main()	








