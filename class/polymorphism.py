class animal:
    def walk(self):
        print("Can walk")

    def swim(self):
        print("Can swim")

    def fly(self):
        print("Can fly")

    def run(self):
        print("Can run")


class dog(animal):
    def fly(self):
        print("Can't fly")


class egret(animal):
    def run(self, arg1 = 10):
        print("Can't run : ", arg1)


if __name__ == '__main__':
    d = dog()
    e = egret()

    d.run()
    e.run()