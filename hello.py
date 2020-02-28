'''
from keras import backend as K
import tensorflow as tf
#设git置两个乘数，用占位符表示
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
#设置乘积
output = tf.multiply(input1, input2)
sess = K.get_session() #tf.Session()这里两个不同
#sess是个对象
def train(sess):
    print(sess.run(fetches=output, feed_dict={input1:[8.],input2:[2.]})) #output怎么传参地？为什么？
    

#可能涉及到python的函数机制？
train(sess)
        
  #用feed_dict以字典的方式填充占位
'''

'''
run()方法接受一个参数和三个可选参数:
1.fecthes,接受数据流图中的(所有的Op和tensor),也就是希望执行的对象,tensor对象一般会返回数或数组,Op没有返回值None.
2.feed_dict参数,用于覆盖数据流图中的tensor对象,接受的参数类型为Python的字典对象
  字典的'键'为被覆盖的tensor对象的句柄,'值'可以是各种数据类型,但是必须和被覆盖tensor
  的类型相同或者能够转换为相同类型
'''

#python全局变量
a = 3
def Fuc():
    print (a,'\n')

Fuc()

'''
​ 在Python中，a=3 定义了全局变量a，作用域从定义处到代码结束，在 a=3 以下的函数中是可以引用全局变量a的，
但如果要修改函数中与全局变量同名的变量，则函数中的该变量就会变成局部变量，在修改之前对该变量的引用自然会出现未分配或未定义的错误了。
如果确定要引用并修改全局变量必须加上global关键字
'''
a = 3
def Fuc():
    global a  #子函数内必须global才能更改全局变量
    print (a)  
    a = a + 1
if __name__ == "__main__":
    print (a)  #3
    a = a + 1 
    Fuc() #4 说明主函数内不加global就能修改全局变量
    print (a) #5  

# 三个print执行的顺序为：3, 3, 4, 5 。可以看到主函数中并没有global声明变量a，仍然可以修改全局变量a。而在普通函数中，需要global声明变量a，才可以修改全局变量a。
