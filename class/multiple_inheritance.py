class a():
    def __init__(self):
        print("Entering class - a")
        print("Leaving class - a")

    def a_func(self):
        print ("a_func")

    def common_func(self):
        print("a - common_func")

class b():
    def __init__(self):
        print("Entering class - b")
        print("Leaving class - b")

    def b_func(self):
        print ("b_func")

    def common_func(self):
        print("b - common_func")

class c(b, a):
    def __init__(self):
        a.__init__(self)
        b.__init__(self)


if __name__ == '__main__':
    c_obj = c()
    c_obj.a_func()
    c_obj.b_func()
    c_obj.common_func()