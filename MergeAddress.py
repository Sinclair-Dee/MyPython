#利用字符串和列表通讯录文本合并为一个文本
#1.IPO模式
#输入；：电话薄文件和邮箱地址文件
#处理：将两个文件内容进行合并
#输出：合并后的包含电话和邮箱的地址薄的文件
#2.程序步骤：
#第一步：打开文件，读取文件。
#第二步：分别获取文件中的信息到两个列表2和列表2。
#第三步：建立合并后的空列表3，完成列表1和2的信息合并操作到列表3中。
#生成信息表头
#遍历列表1中的人，创立列表3的信息。
#处理列表2中剩余人信息，合并到列表3中。
#第四步：将列表3中的信息写入到新文件。
#第五步：关闭所有打开的文件。

#利用字符串和列表将两个通讯录文本合并为一个文本
def main1():
	ftele1 = open("TeleAddressBook.txt","rb")
	ftele2 = open("EmailAddressBook.txt","rb")
	ftele1.readline()
	ftele2.readline()
	line1 = ftele1.readlines()
	line2 = ftele2.readlines()

	list1_name = []
	list1_tele = []
	list2_name = []
	list2_email = []

	for line in line1:#获取第一个文本中的姓名和电话信息。
		elements = line.split()#每行都以空格为间隔，形成一个列表
		list1_name.append(str(elements[0].decode("gbk")))
		list1_tele.append(str(elements[1].decode("gbk")))

	for line in line2:#获取第一个文本中的姓名和邮箱信息。
		elements = line.split()#每行都以空格为间隔，形成一个列表
		list2_name.append(str(elements[0].decode("gbk")))
		list2_email.append(str(elements[1].decode("gbk")))

	######开始处理######
	lines = []
	#lines.append('姓名\t    电话   \t  邮箱\n')
	lines.append("\t".join(["姓名","电话","  \t邮箱\n"]))
	#按索引方式遍历姓名列表1
	for i in range(len(list1_name)):
		s = ""
		if list1_name[i] in list2_name:
			j = list2_name.index(list1_name[i])##找到list1_name[i]对应列表2中的姓名索引位置。
			s = "\t".join([list1_name[i],list1_tele[i],list2_email[j]])#里边的这个大括号的意思是把一行当做列表的一个元素。
			s += "\n"
		else:
			s = "\t".join([list1_name[i],list1_tele[i],str("   ----   ")])
			s += "\n"
		lines.append(s)
	#处理姓名列表2中剩余的姓名
	for i in range(len(list2_name)):
		s = ""
		if list2_name[i] not in list1_name:
			s = "\t".join([list2_name[i],str("   ----   "),list2_email[i]])  
			s += '\n'
		lines.append(s)

	ftele3 = open("AddressBook.txt","w")
	ftele3.writelines(lines)
	ftele1.close()
	ftele2.close()
	ftele3.close()
	print("The addressBooks are merged!")

if __name__ == '__main__':
	main1()

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

	ftele3 = open("AddressBook1.txt","w")
	ftele3.writelines(lines)

	ftele3.close()
	ftele2.close()
	ftele1.close()
	print("The AddressBook1 are merged!")

if __name__ == '__main__':#这里是两道下滑线
	main2()













		

