class my_class:
    def __init__(self):
        self.normal_variable = 100
        self.__no_modified_variable = 2

    def change_variable(self, value):
        self.__no_modified_variable = value

    def fun(self):
        print(self.normal_variable)
        print(self.__no_modified_variable)


if __name__ == '__main__':
    obj = my_class()
    obj.fun()
    obj.change_variable(10)
    obj.fun()
    obj.normal_variable = 110
    obj.__no_modified_variable = 20
    obj.fun()