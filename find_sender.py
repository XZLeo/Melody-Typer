import fileinput
import re
# 列出发件人姓名，不带邮件地址
pat = re.compile('From:(.*)<.*?>$')
for line in fileinput.input():
    m = pat.match(line)
    if m:
        print(m.group(1))
# 将头部信息中包含的email地址都列出来
pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+', re.IGNORECASE)
Addresses = set()
for line in fileinput.input():
    for address in pat.findall(line):
        Addresses.add(address)

for address in sorted(Addresses):
    print(address)



# 在powershell里这样运行文件 python find_sender.py message.eml 
# 其实就是找eml文件中的这一行From: Foo Fie <foo@bar.baz>
# 用compile函数处理正则表达式，更有效率
# (.*)是子模式，圆括号作为组，*允许通配符出现0次或多次
# $表明要匹配整行
# 用非贪婪模式对邮件地址进行匹配，只有最后一对尖括号符合要求
