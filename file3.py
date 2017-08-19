def main():
	fname = input("enter filename:")
	#写的时候要把文件名的后缀也加上，而且如果不写文件路径的话，要确定
	#要打开的文件跟运行的.py文件在同一根目录下。
	#是当文件放在桌面上的时候，输入要写成：C:\Users\狄新凯\Desktop\addddd.py
	infile = open(fname,"r")
	data = infile.read()
	print(data)
main()