#quadratic
import math
def main():
	print("this program find the real solutions to a quadratic \n")
	a,b,c=eval(input("please renter the coefficients(a,b,c):"))
	delta = b*b-4*a*c
	if delta >= 0:
		delta=math.sqrt(delta)
		root1 = (-b+delta)/(2*a)
		root2 = (-b-delta)/(2*a)
		print("\n The solutions are:",root1,root2)
main()
