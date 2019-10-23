class Cat:
    tail = True

    def say(self):
        print('喵喵喵喵喵~')

class Ragdoll(Cat):   #创建继承类玩偶猫
    pass

Garfield=Ragdoll()
Garfield.say()