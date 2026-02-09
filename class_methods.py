class A:
    __x=10
    def __init__(self):
        pass
    @classmethod
    def incrementation(cls):
        cls.x+=1

    def display_sum(a,b):
        print(a+b)

class B(A):
    def inc(self):
        self.x+=1
        print(self.x)

class C(A):
    def inc(self):
        self.x+=1
        print(self.x)
A.display_sum(1,2)
#b=B()
#b.inc()

#c=C()
#print(c.x)