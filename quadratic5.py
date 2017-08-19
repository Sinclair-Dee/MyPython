#quadratic5
#加入了异常处理：try...except...
#try...可以捕获任何类型的错误。并提供一个稳定的出口。
import math
def main():
	print("this program find the real solutions to a quadratic \n")
	a,b,c=eval(input("please renter the coefficients(a,b,c):"))
	delta = b*b-4*a*c
	if a==0:
		x=-b/c
		print("\n there is an solutions:",x)
	else:
		try:
		#运行try,如果发生了意外找出问题，执行对应的except语句。
			delta=math.sqrt(delta)
			root1 = (-b+delta)/(2*a)
			root2 = (-b-delta)/(2*a)
			print("\n The solutions are:",root1,root2)
		except ValueError:
			print("\n No real toots")
while True:
        main()
