num = int(input("Enter the Table Number: "))
for i in range(num, num*10+1, num):
   print(i//num, 'x', num, '=', i)