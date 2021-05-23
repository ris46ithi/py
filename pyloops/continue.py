my_string = "This is a test string"

print ("First FOR loop...")
for character in my_string:
    if character == 'i': ## it will remove i .
        continue
    elif character == 's':## it will remove s
        continue
    print (character)
print(character) ### its print last character of the string coz we print from outloop 
print(my_string) ###string values 