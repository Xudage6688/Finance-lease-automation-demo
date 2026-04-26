
class Animal:   #定义一个父类
    eye = 2
    ear = 2
    mouth = 1

    def __init__(self): #是一个Python类的构造函数，用于初始化类的对象。当创建一个新的类实例时，这个函数会被自动调用
        print("This is Animal class")

    def make_sound(self):
        print("animal sound")

    def height(self):
        print("animal height")

    def can_walk(self):
        print("animal walk")

    def eat(self):  #父类更新方法子类全部继承
        print("need eat something")

class Dog(Animal):  #继承了父类Animal的所有方法实例
    def __init__(self):
        print("This is Dog class")

    def make_sound(self):   #函数重构 狗类的独有叫声
        print("汪汪汪")

    def run(self):  #私有方法
        print("dog can run")


class Cat(Animal):
    def __init__(self):
        print("This is Cat class")

    def make_sound(self):   #函数重构 毛类的独有叫声
        print("喵喵喵")

    def climb(self):    #私有方法
        print("cat can climb")

if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    dog.make_sound()
    cat.make_sound()