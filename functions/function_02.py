def print_a_pattern():
    max = 10

    l = list(range(1, max+1))
    for i in l:
        space = (max - i) * ' '
        if i == 1:
            star = '*'
        else:
            star = '*' * (i + (i - 1))
        print (space + star)

    l = l[:-1]
    l.reverse()
    for i in l:
        space = (max - i) * ' '
        if i == 1:
            star = '*'
        else:
            star = '*' * (i + (i - 1))
        print (space + star)

print ("Statement 1")
print ("Statement 2")
print ("Statement 3")
print_a_pattern()
print ("Statement 4")
print ("Statement 5")
print ("Statement 6")