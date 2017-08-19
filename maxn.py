#program:maxn.py
def maxn():
	n=eval(input("How many numbers are there?"))
	#将第一个数赋值给max
	max=eval(input("Enter a numbers>>"))
	#连续与后边N-1值比较
	for i in range(n-1):
		x=eval(input("Enter a numbers>>"))
		if x>max:
			max=x
	print("the maxnumbers is:",max)

while True:
        maxn()
