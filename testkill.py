class Cat:#创建类
    def eat(self,a,b):
        c=a+b
        print(c)
        return c
c1=Cat()#创建对象，不能够直接调用类
c2=c1.eat(1,1)