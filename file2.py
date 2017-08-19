
#下边这个函数是输出文件前五行的例子。

infile = open("file.txt","r")
for i in range(5):
	line = infile.readline()
	print(line[:-1])
	
