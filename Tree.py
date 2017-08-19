#Tree.py
#这是个对称的树，可以使用递归的方式来画这棵树。

form turtle import Turtle

def tree(plist,l,a,f):
	#plist is list of pens
	#l is length of branch
	#a is


def main():# main函数，画笔的初始化以及调用Tree函数。
	p=Turtle()
	p.color("green")
	p.pensize(5)
	p.hideturtle()
	# Make the turtle invisible.It'S a good idea to do this 
	# while you are in the middle of doing some complex drawing.
	# Because hiding the turtle speeds up the drawing observably 
	p.speed(10)
	p.getscreen().tracer(30,0)
	#return the turtlescreen object the turtle is drawing on.
	#TurtleScreen methods can be called for that object.
	p.left(90) #turn turtle by angle units.direction

	p.penup() # pull the pen up. -no drawing when moving
	p.goto(x,y) # move turtle to an absolute position
	# If the pen is down,draw line.Do not the turtle's orientation
	p.pendown() #pull the pen down. -drawing when moving
	#这三条语句是一个组合，相当于先把画笔收起来再移动到指定位置，再把比放下开始画。
	#否则turtle一移动就会自动把线画出来。

	t = tree([p],110,65,0.6375)

def 