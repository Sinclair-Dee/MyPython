#pm2.5.py
#空气质量提醒
#三个地方的“：”，老是忘！！！
def main():
	pm = eval(input("what is today\'s pm 2.5："))
	#打印相应提醒
	if pm>75:
		print("不能出去")
	elif pm<35:
		print("能出去")
	else:
		print("看情况！")
main()
