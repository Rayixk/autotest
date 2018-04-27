# coding: utf-8
# created by yang

def f1(*args,**kwargs):
    print(args)
    print(kwargs)
    def wrapper(func):
        return func(*args,**kwargs)
    return wrapper

class My:

    def __init__(self):
        self.b = B()


    @f1
    def __getattr__(self, item,*args,**kwargs):
        print(item)
        print(args)
        print(kwargs)
        if hasattr(self.b,item):
            func = getattr(self.b,item)
            return func()

class B:
    def __init__(self):
        self.name = "yang"
    def f1(self,s):
        print(s)
        print(self.name)
        print("f1")


o = My()
o.f1("ss")