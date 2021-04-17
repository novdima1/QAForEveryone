class A:
    def a(self):
        return 'a'

    def b(self):
        return 'b'

    def c(self):
        return 'c'


obj = A()
fun = [obj.a(), obj.b(), obj.c()]
print(fun)