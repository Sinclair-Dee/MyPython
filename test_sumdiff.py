def sumdiff(x,y):
	sum=x+y
	diff=x-y
	return sum,diff
num1,num2=eval(input("please enter two numbers(num1,num2):"))
s,d=sumdiff(num1,num2)
print("the sum is",s,"and the difference is",d)