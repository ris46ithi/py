h = eval(input("please enter diamond's height:"))
def diamond():#we only add this def for checking "eval" is working global and local
    for i in range(h):
        print("0"*(h-i), "*"*(i*2+1)) #eg:h-i = user input value 10  
    for i in range(h-2, -1, -1):
        print("1"*(h-i), "*"*(i*2+1))
diamond()