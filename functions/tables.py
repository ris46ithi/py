def tables(value):
    tupto= int(input("Length of The Table: "))
    for val in range(value, value*tupto+1, value):# (starting v ,v*boundries, v incressteps) s
        print (val//value, "X", value, "=", val)
table_number = int(input("Enter a table Number : "))
tables(table_number)



