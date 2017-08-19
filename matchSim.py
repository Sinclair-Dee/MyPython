#matchSim.property
#基本思想:自顶向下的设计
#编写函数的顺序是自下而上，main函数放在本文件的最下边。
#第一阶段：隐藏函数细节对每一阶段进行抽象。
#printIntro():打印程序的介绍性信息
#probA,probB,n=getInputs():获得程序运行所需要的参数。
#winsA,winsB=simNGames(n,probA,probB):利用球员A，B的能力值模拟n次比赛。
#printSummary(winsA,winsB)：输出A和B获胜比赛的次数和频率。
#程序框架就此确定。在第一步骤不必关心细节，只考虑框架的问题。自顶向下的过程是发现功能并抽象的过程。
#第二阶段：进一步抽象第二层的函数。
#例如simNGames可以进一步分解为simOneNGames,simNGames是整个程序的核心。
#simNGames可以调用n次simOneNGames,从而获得A,B赢得次数以及平局的次数。
#printIntro()的细节在这个阶段可以写了。
#getInputs()函数的细节也可以描述。
#第三阶段：在这个阶段可以描述simOneGame(probA,probB)的具体细节。具体思路是用一个while循环来积分。
#          跟踪记录得分。还要考虑发球权和比分的问题。
#语言点：while是一种无限循环，不需要提前知道循环次数。即我们提到的当型循环也叫条件循环。
#	while <condition>: #while语句中<condition>里是布尔表达式。
#		<body>
#当<condition> 为True时，循环体重复执行。
#当<condition> 为Flase时，循环停止。
#gameOver函数用来判断程序结束，在第三阶段描述其细节。
#printSummary()函数打印竞技结果，在第三阶段描述其细节。
from random import *
def printSummary(winsA,winsB,ping):#第三阶段
	n= winsA + winsB + ping
	print("\n game simulated:%d" %n)
	print("\n wins for A:{0}({1:0.1%})".format(winsA,winsA/n))
	print("\n wins for B:{0}({1:0.1%})".format(winsB,winsB/n))
	print("\n both are not win:{0}:({1:0.1%})".format(ping,ping/n))
def gameOver(a,b): #第三阶段
	return (a==15 or b==15)  #布尔表达式。
def simOneGame(probA,probB):#第三阶段
	scoreA = 0
	scoreB = 0
	serving = "A"
	while not gameOver(scoreA,scoreB):
		if serving == "A":
			if random()<probA:
				scoreA = scoreA+1
			else:
				serving = "B"
		else:
			if random()<probB:
				scoreB = scoreB+1
			else:
				serving = "A"
	return scoreA,scoreB
def simNGames(n,probA,probB):#第二阶段，整个程序的核心。
	winsA = 0
	winsB = 0
	ping  = 0
	for i in range(n):
		scoreA,scoreB = simOneGame(probA,probB)
		if scoreA>scoreB:
			winsA = winsA + 1
		elif scoreB>scoreA:
			winsB = winsB + 1
		else:
			ping = ping+1
	return winsA,winsB,ping
def printIntro():#第二阶段
	print("This program simulates a game between two")
	print("There are two players,A and B")
	print("Probability(a number between 0 and 1) is used")
def getInputs():#第二阶段
	a=eval(input("What is the prob.player A win:"))
	b=eval(input("What is the prob.player B win:"))	
	n=eval(input("How many games to simulate:"))
	return a,b,n	
def main():#第一阶段
	printIntro()
	probA,probB,n = getInputs()
	#测试：
	#print(probA,probB,n)
	winsA,winsB,ping=simNGames(n,probA,probB)
	printSummary(winsA,winsB,ping)
main()#函数执行入口
