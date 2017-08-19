#利用字典将两个通讯录文本合并为一个文本
#文本合并处理：
#1.生成新的数据表头
#2.按字典键的操作遍历姓名列表1：处理与表2中重名的信息、处理其他信息
#3.处理列表2中剩余的姓名
#gbk是用来讲中文写入文本，防止乱码
#从生成的文本结果可以看出列表和字典的一个不同，字典中元素的位置是不固定的！！
def main2():
	ftele1 = open("TeleAddressBook.txt","rb")
	ftele2 = open("EmailAddressBook.txt","rb")

	ftele1.readline()#跳过第一行
	ftele2.readline()
	line1 = ftele1.readlines()
	line2 = ftele2.readlines()

	dic1 = {}#字典方式保存
	dic2 = {}

	for line in line1:#获取第一个本文中的姓名和电话信息
		elements = line.split()
		#将文本读出来的bytes转换为str类型
		dic1[elements[0]] = str(elements[1].decode("gbk"))

	for line in line2:#获取第二个本文中的姓名和邮箱信息
		elements = line.split()
		#将文本读出来的bytes转换为str类型
		dic2[elements[0]] = str(elements[1].decode("gbk"))
	####开始处理####
	lines = []
	#lines.append("姓名\t  电话\t  邮箱\n")
	lines.append("\t".join(["姓名","电话","  \t邮箱\n"]))

	for key in dic1:
		s = ""
		if key in dic2.keys():#注意是dic2.keys()!!!
			s = "\t".join([str(key.decode("gbk")),dic1[key],dic2[key]])
			s +="\n"
		else:
			s = "\t".join([str(key.decode("gbk")),dic1[key],str("    ----    ")])
			s += "\n"
		lines.append(s)

	for key in dic2.keys():
		s = ""
		if key not in dic1.keys():
			s = "\t".join([str(key.decode("gbk")),str("    ----    "),dic2[key]])
			s += "\n"
		lines.append(s)

	ftele3 = open("AddressBook.txt","w")
	ftele3.writelines(lines)

	ftele3.close()
	ftele2.close()
	ftele1.close()
	print("The AddressBook are merged!")

if __name__ == '__main__':#这里是两道下滑线
	main2()
