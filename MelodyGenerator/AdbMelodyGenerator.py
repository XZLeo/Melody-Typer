#Target: 用python+adb点击屏幕，生成各种简易音乐
#1.获取各个简易乐曲的手机键盘谱，做成txt文件
#1.1. 每一段在txt中用换行符分隔，用空格在一行停顿x1秒，用换行符挺更长时间
#1.2. 研究一下具体节拍是一秒几次
#2.读入txt文件，视文件大小，决定读成list还是generator
#3. 解码程序，将对应字符变换成(x, y)坐标，对应手机屏
#3.1. 首先要手机连上adb，确定拨号界面每个键的

# 感觉每个都转换成按键不是很高效的样子....

import time
import os
#开头将adb加入临时环境变量,用sys.path.append无效
ADB_path = "d:/ADB/"
os.environ["PATH"] = ADB_path
# 测试有效
#os.system("adb shell input tap 250 1200")

current_path = 'd:/NewPython/MelodyGenerator/'
current_file = {"1":"HappyBirthday.txt", "2":"LittleStar.txt"}

#构建字典存储按键对应坐标
X = {'0':530, '1':250, '2':530, '3':860, '4':250, '5':530, 
    '6':860, '7':250, '8':530, '9':860, '*':250, '#':860}
Y = {'0':1800, '1':1200, '2':1200, '3':1200, '4':1400, '5':1400,
    '6':1400, '7':1600, '8':1600, '9':1600, '*':1800, '#':1800}

def filereader(path):
    #读取乐谱，返回list
    f = open(path)
    score = f.read() 
    print('type:', type(score)) #读进来是个字符串
    print(score)
    return score


def decoder(score):
    #读取list，翻译成具有等待时间的、节奏的adb命令
    for note in score:
        if note == '\n':
            #延迟0.5s
            time.sleep(0.5)
        elif note == ' ':
            #延迟0.25秒
            time.sleep(0.25)
        elif '0'<=note<='9' or note == '#' or note == '*':
            os.system("adb shell input tap {x} {y}".format(x=X[note], y=Y[note]))
        else:
            pass
    return

path = current_path + current_file
score = filereader(path)
decoder(score)

# 加入多遍循环，直到键盘按键
# 搜集更多的手机谱
# 弄个输入可以选择对应的谱子，首先需要一个字典将已有的名字放进去