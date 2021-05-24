import emoji

def print_a_pattern():
    global max
    global l
   # l = list(range(1, max//2+1)) # why we have to give this max+1? coz then only we can get 10
    #l.reverse()
    for i in l:
        space = (max - i) * " "
        #print(len(space))        #space = (max - i) * (emoji.emojize(":zipper-mouth_face:"))
        if i == 1:
            space = (len(space) - (i)) * " " # for the first line : reduce 1 space, second line : reduce 2 space 
            star = (emoji.emojize(":zipper-mouth_face:"))
            #star = '*'
        else: 
            space = (len(space) - (i)) * " "
            star = (emoji.emojize(":zipper-mouth_face:")) * (i + (i - 1))
            #star = '*' * (i + (i - 1))# 2 -1 = 3 poona statement 
            ###star = '*' * (2 + (2 -1))
        print (space + star)

max = 20
l = list(range(1, max//2+1))
print_a_pattern()
l = list(range(1, max//2))
l.reverse()
print_a_pattern()

