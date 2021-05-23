#######list##########
my_list = [3, 4, 5, 6]
print (type(my_list))
########set #########
my_list = {3, 4, 5, 6}
print (type(my_list))
########for loop why we are using i here (?) universel rules :-) #########
for i in my_list:
    print (i)
print(my_list)
#################
####put list using range key #####
my_list = list(range(1, 101))
print(my_list)
#################we can only get one value from list ##########
print(my_list[96])
#print(my_list[80, 96]) // if we give 2 values that through errors
#TypeError: list indices must be integers or slices, not tuple
my_list = range(1, 3) ##its give only range(1, 3)
print(my_list)
print (type(my_list)) ####<class 'range'> ## question raised to Manikandan