
class A:

    def f1(self):
        print('F1 works')

    def f2(self):
        print('F2 works')


class B(A):

    def f3(self):
        print('F3 works')

    def f4(self):
        print('F4 works')

class C(B):

    def f5(self):
        print('F5 works')



obj = C()
obj.f1()
obj.f3()
obj.f5()