import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('wordcount:', wordcount)
# powershell里是兼容Unix shell的命令的
#  cat ss.txt | python somescript.py | sort 
# 统计ss.txt里的单词书

