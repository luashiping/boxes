"""
参考链接：https://mp.weixin.qq.com/s/iZ4DZsXZA-OanvVMa8_LXw
__getattr__:
这个方法是当对象的属性不存在时调用。如果通过正常的机制能找到对象属性的话，则不会调用__getattr__方法
"""
class A:
    a = 1
    def __getattr__(self, item):
        print('__getattr__ call')
        return item

t = A()
print(t.a)
print(t.b)
print("---------------------------------------------")


"""
__getattribute__:
这个方法会被无条件调用。不管属性存不存在。
如果类中定义了__getattr__，则不会调用__getattr__方法，除非在__getattribute__方法中显示调用__getattr__()或者抛出了AttributeError
"""
class B:
    a = 1
    # def __getattribute__(self, item):
    #     print("__getattribute__ call")
    #     return AttributeError
    
    """
    一般情况下，所以为了保留__getattr__的作用，__getattribute__()方法中一般返回父类的同名方法:
    """
    def __getattribute__(self, item):
        print("__getattribute__ call")
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print("__getattr__ call")
        return item

t = B()
print("t.a is {}".format(t.a))
print("t.b is {}".format(t.b))
print("---------------------------------------------")

"""
__get__方法:
这个方法比较简单，与前面的关系并不大。
如果一个类中定义了__get__(), __set__()或__delete__()中的任何方法。则这个类的对象称为描述符。
"""
class Descri(object):
    def __get__(self, obj, type=None):
        print("call get")
    
    def __set__(self, obj, value):
        print("call set")

class C(object):
    x = Descri()

a = C()
# a.__dict__['x']
##  如果通过对象实例调用x(下面的调用方式)，则 a.x 转换为：type(a).__dict__["x"].__get__(a, type(a))
type(a).__dict__["x"].__get__(a, type(a))
a.x
## 如果类调用属性x，C.x 转换为：C.__dict__['x'].__get__(None, C)
C.__dict__['x'].__get__(None, C)
C.x
print("---------------------------------------------")

"""
__getitem__:
这个方法调用也是无条件调用，这点与__getattribute__一致。区别在于__getitem__让类实例允许[]运算，可以这样理解：
1.__getattribute__适用于所有.运算；
2.__getitem__适用于所有[]运算符。
"""
class D(object):
    a = 1

    def __getitem__(self, item):
        print("__getitem__ call")
        return item
    
    ## 如果相要对象能够通过[]获取属性的值可以用如下方法
    # def __getitem__(self, item):
    #     return object.__getattribute__(self, item)

t = D()
print(t["a"])
print(t["b"])
