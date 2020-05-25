#没有别的区别，只是将os.system从多个子进程变成一个
import sys
import time
import os

def filereader(path):
    #读取乐谱，返回list，元素是数字序列、空格和换行
    score = []
    f = open(path)
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        for i in line.split(' '):            
            score.append(i)
            score.append(' ')
        score.pop() #最后一个空格和换行重复，弃掉
        score.append('\n')
    return score
     

def decoder(score):
    #读取list，翻译成具有等待时间的、节奏的adb命令,实现分段演奏    
    for snippet in score:
        all_command = "" #空string
        if snippet == '\n':
              #延迟0.5st
            time.sleep(0.5)
        elif snippet == ' ':
            #延迟0.25秒
            time.sleep(0.25)
        else:
            for note in snippet:
                if '0'<=note<='9' or note == '#' or note == '*':
                    all_command += "adb shell input tap {x} {y} && ".format(x=X[note], y=Y[note])
            all_command = all_command.strip(" && ")  #去除最后一个命令的多余部分
            os.system(all_command)   #这么写会让上面的sleep变得毫无意义

    os.system("adb shell input swipe 1000 2000 1001 2001 1000") #删除拨号
    return


if __name__ == '__main__':
    #开头将adb加入临时环境变量,用sys.path.append无效
    ADB_path = "d:/ADB/"
    os.environ["PATH"] = ADB_path
    # 测试有效
    #os.system("adb shell input tap 250 1200")

    current_path = 'd:/NewPython/MelodyGenerator/'
    current_file = {"1":"HappyBirthday.txt", "2":"LittleStar.txt", "3":"Jasmine.txt", 
                    "4":"CaribbeanPirate.txt", "5":"taiguan.txt"}

    #构建字典存储按键对应坐标
    X = {'0':530, '1':250, '2':530, '3':860, '4':250, '5':530, 
        '6':860, '7':250, '8':530, '9':860, '*':250, '#':860}
    Y = {'0':1800, '1':1200, '2':1200, '3':1200, '4':1400, '5':1400,
        '6':1400, '7':1600, '8':1600, '9':1600, '*':1800, '#':1800}
    
    while True:
        flag = os.popen("adb devices")
        a = flag.read()
        print(a)
        if len(a) > 27:
            notification = "1:HappyBirthday, 2:LittleStar, 3:Jasmine,\n4:CaribbeanPirate 5:黑人抬棺:\n"
            music_name = input(notification)
            path = current_path + current_file[music_name]
            score = filereader(path)
            print(score)
            decoder(score)
        else:
            print("Chec your mobilephone connection")
            break

    # 如何提高按键频率
    # adb forward可以建立socket通信

    # 所以明显的停顿也是为了执行sleep！