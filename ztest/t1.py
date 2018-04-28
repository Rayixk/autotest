# coding: utf-8
# created by yang

class My:

    def __init__(self):
        self.b = B()


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