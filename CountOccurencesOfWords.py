#“统计词频”问题：统计文章重复词语，概要分析文章内容。搜索引擎。
#统计词频IPO模式
#输入：从文件中读取一篇英文文章
#处理: 统计文章中每个单词出现的频率
#输出：将最常出现的10个单词及出现次数，用图表的形式输出
#实现思路：
#第一步：输入英文文章
#第二步：建立用于词频计算的空字典
#第三步：对文本的每一行计算词频
#第四步：从字典中获取数据对到列表中
#第五步：对列表中的数据对交换位置，并从大到小进行排序
#第六步：输出结果
#第七步：用Turtle库绘制词频统计结果图表
import turtle
##全局变量##
#词频排列显示个数
count = 10
#单词频率数组-作为y轴数据
data = []
#单词数组-作为x轴数组
words = []
#y轴显示放大倍数-可以根据词频数量进行调节
yScale = 2
#x轴显示放大倍数-可以根据count数量进行调节
xScale = 50
##################Turtle Start##################
#t是用于绘制的turtle对象
#从点(x1,y1)到(x2,y2)绘制线段
def drawLine(t,x1,y1,x2,y2):
	t.penup()
	t.goto (x1,y1)
	t.pendown()
	t.goto (x2,y2)
#在坐标(x,y)处写文字
def drawText(t,x,y,text):
	t.penup()
	t.goto (x,y)
	t.pendown()
	t.write(text)
#绘制一个柱体
def drawRectangle(t,x,y):
	x = x*xScale
	y = y*yScale
	drawLine(t,x-5,0,x-5,y)
	drawLine(t,x-5,y,x+5,y)
	drawLine(t,x+5,y,x+5,0)
	drawLine(t,x+5,0,x-5,0)
#绘制多个柱体
def drawBar(t):
	for i in range(count):
		drawRectangle(t,i+1,data[i])
#实现drawGraph(t)函数
def drawGraph(t):
	#绘制x/y轴线
	drawLine(t,0,0,600,0)
	drawLine(t,0,300,0,0)
#xy轴：坐标及描述
	for x in range(count):
		x = x+1 #向右移一位，为了不画在原点上
		drawText(t,x*xScale-4,-20,(words[x-1]))
		drawText(t,x*xScale-4,data[x-1]*yScale+10,data[x-1])
	drawBar(t)
######################Turtle End#####################
#统计文本中每一行词频processLine()
def processLine(line,wordCounts):#line是输入的一行，wordCounts是字典
	#用空格替换标点符号
	line = replacePunctuations(line)
	#从每一行获取每个单词
	words = line.split()#以空格间隔建立列表
	for word in words:
		if word in wordCounts:
			wordCounts[word] +=1
		else:
			wordCounts[word] = 1
#符号替换函数replacePunctuations()
def replacePunctuations(line):
	for ch in line:
		if ch in "`~@#$%^&*()_+=?/,.{}[]\'""":
			line = line.replace(ch,"")
	return line

#统计词频主程序
def main():
	#输入英文文本名称
	filename = input("enter a filename:").strip()
	infile = open(filename,"r")
	#建立一个空字典
	wordCounts = {}
	#对每一行进行统计
	for line in infile:
		processLine(line.lower(),wordCounts)#lower函数将所有大写字母全部变成小写
	#词频排序
	#从字典中获取数据对
	pairs = list(wordCounts.items())#返回一个包含所有键值的列表？？？
	#列表中的数据对交换位置，数据对排序
	items = [[x,y] for [y,x] in pairs]
	items.sort()
	#输出count个数词频结果
	for i in range(len(items)-1,len(items)-count-1,-1):
		print(items[i][1]+"\t"+str(items[i][0]))
		data.append(items[i][0])
		words.append(items[i][1])
	infile.close()
	#根据词频结果绘制柱状图
	turtle.title("词频结果柱状图")
	turtle.setup(1800,1500,0,0)
	t = turtle.Turtle()
	t.hideturtle()
	t.width()
	drawGraph(t)
#调用main()函数
if __name__ == '__main__':
	main()

