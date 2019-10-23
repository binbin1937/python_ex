#学习继承类

#定义类中国人
class Chinese:
    eye = 'black'   #定义属性 眼睛是黑色的

    #定义方法吃
    def eat(self):
        print('吃饭用筷子')

class Cantonese(Chinese) :   # 通过继承，Chinese类有的，Cantonese类也有
    pass   #跳过


xiaoming=Chinese()
print(xiaoming.eye)
xiaoming.eat()

yewen = Cantonese()
# 子类创建的实例，从子类那间接得到了父类的所有属性和方法
print(yewen.eye)
# 子类创建的实例，可调用父类的属性
yewen.eat()
# 子类创建的实例，可调用父类的方法