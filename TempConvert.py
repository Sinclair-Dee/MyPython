#TempConvert.py
#val=input("请输入带温度表示符号的温度值(例如32C)：")这样写会麻烦的。
val=raw_input("请输入带温度表示符号的温度值(例如32C)：")
if val[-1] in ["C","c"]:
	f=1.8*float(val[0:-1])+32
	print"转换后的温度：%.2fC"%f
elif val[-1] in ["F","f"]:
	c=(float(val[0:1])-32)/1.8
	print"转换后的温度：%.2fF"%c"
else:
	print"input error!"
i=raw_input("")
