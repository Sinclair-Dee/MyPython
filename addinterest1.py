#addinterest1.py

def addInterest1(balance,rate):
	newBalance = balance*(1+rate)
	#balance = newBalance
	return newBalance
def main():
	amount = 1000
	rate = 0.05
	amount = addInterest1(amount,rate)
	print(amount)
main()
