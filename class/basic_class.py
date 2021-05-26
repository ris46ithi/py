class my_class:
    var = 1
    def fun(self):
        print("Hello World")
    def run(self):
        print("delete World")
        return "dd"
#obj = my_class()
#print(type(obj))
#print(type(obj.fun))

my_class().var # if we call fun or cls we have to add ()
my_class().fun()#withput () i got error "TypeError: fun() missing 1 required positional argument: 'self'"
print(my_class().run())# we added print have to set return here i set "dd"
## i removed print from coz print need return values thats why none is come ever prints after 