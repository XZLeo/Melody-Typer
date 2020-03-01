import fileinput, re

file_pat = re.compile(r'\[(.+?)\]') #定义了用于匹配字段的模式

scope = {} #创建充当模板作用域的字典

def replacement(match):
    code = match.group(1) # 将组1从匹配中取出，放入code中
    try:
        return str(eval(code, scope))
    except SyntaxError:
        exec(code in scope) # exec 执行储存在字符串或文件中的 Python 语句,eg: exec('print(2)') 会返回2
        return ''

#将file输入以一个字符串形式读入
lines = [] 
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines) # 等会改成11章的方法

# 将field模式的所有匹配项都替换掉
print(file_pat.sub(replacement, text)) 
# 将text里所有和file_pat模式对象匹配的字符都替换成replacement


# 用fileinput可以使用一个文件为变量定义值，另一个文件作为插入这些值的模板
# 这样就可以用模板群发邮件

