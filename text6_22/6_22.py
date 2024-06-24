# #面相对象
# #定义一个Foo类，包含两个方法
# class Foo:
#         def bar(self):# bar是Foo类的一个方法，不接受除 self（指向类实例本身的引用）之外的任何参数。当Bar方法调用时它会打印字符串"Cheney"
#             print("shichengfu")
#         def Hello(self,name):# Hello是Foo类的另一个方法，接受一个参数name以及隐式的self参数。该方法打印一句格式化字符串，其中包含传入的name参数
#             print("我的名字是：{}".format(name))
#
# obj = Foo()
# obj.bar()
# obj.Hello('Shichengfu')

# #封装
# #定义一个Foo类
# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# Figer1 = Foo("Shichengfu",18)
# Figer2 = Foo("Chujiahui",19)
# print("Figer1的name为%s"%Figer1.name)
# print("Figer2的age为%d"%Figer2.age)

# # 封装
# class Fool:
#     def __init__(self,name,age):    #初 始化对象属性
#         self.name = name
#         self.age = age
#     def detial(self):   #定义一个detial方法
#         print(self.name)
#         print(self.age)
# obj = Fool("Shichengfu",18)     # 实例化一个对象
# obj.detial()    # 调用detial方法

# # 继承
# class Animal:  #定义一个父类
#     def eat(self):
#         print("%s 吃"%self.name)
#     def drink(self):
#         print("%s 喝"%self.name)
#     def sleep(self):
#         print("%s 睡"%self.name)
#
# #定义一个子类
# class Dog(Animal):
#     def __init__(self,name):
#         self.name = name
#         self.breed = "王怿铭"
#     def cry(self):
#         print("汪汪汪")
# dog = Dog("王怿铭")
# dog.eat()
# dog.drink()
# dog.cry()
# class dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def speak(self):
#         print("汪汪汪")
#         print("这个dog的姓名是%s"%self.name)
#         print("这个dog的年龄是%d"%self.age)
# daoge = dog("王怿铭",18)
# daoge.speak()

