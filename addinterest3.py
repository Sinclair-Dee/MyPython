#addinterest3.py
#处理银行账户的程序

def addInterest3(balances,rate):
	for i in range(len(balances)):
                balances[i] = balances[i]*(1+rate)
def test():
	amounts = [1000,105,3500,739]
	rate = 0.05
	addinterest3(amounts,rate)
	print(amounts)
test()
