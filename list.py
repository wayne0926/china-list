import wget
import re
import os
if os.path.exists('accelerated-domains.china.conf'):
    os.remove('accelerated-domains.china.conf')
fi = wget.download('https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf')
# 创建一个变量并存储我们要搜索的文本
search_text = "server=/"
s2 = '/114.114.114.114'

# 创建一个变量并存储我们要添加的文本
replace_text = "b"
r2 = ''

# 使用 open() 函数以只读模式打开我们的文本文件
with open(r'accelerated-domains.china.conf', 'r',encoding='UTF-8') as file:

	# 使用 read() 函数读取文件内容并将它们存储在一个新变量中
	data = file.read()

	# 使用 replace() 函数搜索和替换文本
	data = data.replace(search_text, replace_text).replace(s2, r2)

# 以只写模式打开我们的文本文件以写入替换的内容
with open(r'accelerated-domains.china.conf', 'w',encoding='UTF-8') as file:

	# 在我们的文本文件中写入替换的数据
	file.write(data)

# 打印文本已替换
print("文本已替换")
