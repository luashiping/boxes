"""
Python中的“特权种族”是什么？
特权种族：共用内存的对象
参考资料：https://mp.weixin.qq.com/s/vCs6QvJU2J6L0rIWDKQPUQ
        https://www.rogoso.info/python%E7%9A%84%E5%90%8C%E4%B8%80%E6%80%A7%E8%BF%90%E7%AE%97%E7%AC%A6is%E5%92%8C%E7%9B%B8%E7%AD%89%E8%BF%90%E7%AE%97%E7%AC%A6%E7%9A%84%E5%8C%BA%E5%88%AB/
（“>>>”表示输出结果）
"""

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)
print(l1 == l2)

print("------------------")

# 新分配内存地址的例子
ww = [1, 2]
ee = [1, 2]
print(id(ww) == id(ee))  # >>>False
a = 2018
b = 2018
print(id(a) == id(b))  # >>>True

g = 257
def foo():
    e = 257
    f = 257
    print(e is f)  # >>>True
    print(e is g)  # >>>False

foo()

print("------------------")

# 共用内存地址的例子
c = 100
d = 100
print(id(c) == id(d))  # >>>True
f1 = True
f2 = True
print(id(f1) == id(f2))  # >>>True
n1 = None
n2 = None
print(id(n1) == id(n2))  # >>>True
s = "python_cat"
t = "python_cat"
print(id(s) == id(t))  # >>>True
