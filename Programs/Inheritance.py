# class A:
#     def feature1(self):
#         print("feature1 is working")
#
#     def feature2(self):
#         print("feauter2 is working")
#
#
# # MULTILEVEL
# # class B(A):
# class B:
#     def feature3(self):
#         print("feauter3 is working")
#
#
# # MULTIPLE INHERITANCE
# class C(A, B):
#     def feature4(self):
#         print("feauter4 is working")
#
#
# C1 = C()
# C1.feature1()
# C1.feature2()
# C1.feature3()
# C1.feature4()

#single level inheritance
class A:
    def feature1(self):
        print("feature1 is working")

class B(A):
    def feature3(self):
        print("feauter3 is working")
        self.feature1()

B1 = B()
B1.feature3()
