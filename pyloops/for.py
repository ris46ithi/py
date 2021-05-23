my_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print ("Print without loop...")
print (my_list[0])
print (my_list[1])
print (my_list[2])
print (my_list[3])
print (my_list[4])
print (my_list[5])
print (my_list[6])
print (my_list[7])
print (my_list[8])
print (my_list[9])


print ("Print the values of my_list")
for value in my_list:
    print (value)


my_tuple = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print ("Print the values of my_tuple")
for content in my_tuple:
    print (content)


my_string = "Zilogic Systems"
print ("Print the values of my_string")
for character in my_string:
    print (character)


print ("Output formatting")
for val in range(1, 6):
    print (val * "*")