#quadratic4
import math
def main():
	print("this program find the real solutions to a quadratic \n")
	a,b,c=eval(input("please renter the coefficients(a,b,c):"))
	delta = b*b-4*a*c
	if a==0:
		x=-b/c
		print("\n there is an solutions:",x)
	elif delta < 0:
		print("\n error")
	else:
		delta=math.sqrt(delta)
		root1 = (-b+delta)/(2*a)
		root2 = (-b-delta)/(2*a)
		print("\n The solutions are:",root1,root2)

while True:
        main()
