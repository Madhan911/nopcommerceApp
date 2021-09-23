class A:

    def __init__(self):
        print(" init A class")

    def feature1(self):
        print("feature1 is working")

    def feature2(self):
        print("feauter2 is working")


# MULTILEVLE
# class B(A):
class B:

    def __init__(self):
        print("init B class")

    def feature3(self):
        print("feauter3 is working")


# MULTIPLE INHERITANCE
class C(A, B):

    def __init__(self):
        super().__init__()
        print("init c class")

    def feature4(self):
        print("feauter4 is working")

    def feat(self):
        super().feature2()


C1 = C()
C1.feat()
C1.feature1()
C1.feature2()
C1.feature3()
C1.feature4()
