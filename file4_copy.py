#举例：文件拷贝

def main():
	#用户输入文件名
	f1 = input("enter a source file:").strip()
	f2 = input("enter a source file:").strip()
	#打开文件
	infile = open(f1,"r")
	outfile = open(f2,"w")

	#拷贝数据
	countlines = countchars = 0
	for line in infile:
		countlines += 1
		countchars += len(line)
		outfile.write(line)
	print(countlines,"lines and",countchars,"chars copied")

	infile.close()
	outfile.close()

main()
