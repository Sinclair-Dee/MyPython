#以下程序均是在python3.5中运行

#1字符串拼接。用户输入两个字符串，将它们组合后输出。
str1 = input("请输入一个人的名字：")
str2 = input("请输入一个国家名字：")
print("世界这么大，{}想去{}看看。".format(str1,str2))
print("")
#2整数序列求和。用户输入一个正整数N，计算从1 到N（包含1和N）相加之后的结果。
n=input("请输入整数N:")
sum=0
for i in range(int(n)):
	sum+=i+1;
print("1到N求和结果：",sum)
print("")
#3九九乘法表输出。工整打印输出常见的九九乘法表，格式不限。
for i in range(1,10):
        for j in range(1,i+1):
                print("{}*{}={:2}".format(j,i,i*j),end="")#在这里可以试一下end=""的功能。
        print("")
print("")
#4阶乘计算。计算1+2!+3!+...+10!的结果。
sum,temp = 0,1
for i in range(1,11):
	temp*=i
	sum+=temp
print("运算结果是:{}".format(sum))
print("")
#5猴子吃桃问题。
n=1
for i in range(5,0,-1):
	n=(n+1)<<1
print(n)
#6健康食谱输出
diet = ['西红柿','花椰菜', '黄瓜', '牛排', '虾仁']
for x in range(0,5):
	for y in range(0,5):
		if not(x==y):
			print("{}{}".format(diet[x],diet[y]))
print("")
#7五角星的绘制
import turtle
import time
turtle.speed("fastest")
turtle.pensize(2)
for x in range(100):
turtle.forward(2*x)
turtle.left(90)
time.sleep(3)
from turtle import * 
fillcolor("red")
begin_fill()
while True:
	forward(200)
	right(144)
	if abs(pos())<1:
		break
end_fill()
#8太阳花的绘制
from turtle import *
color("red","yellow")
begin_fill()
while True：
	forward(200)
	left(170)
	if abs(pos())<1:
		break
