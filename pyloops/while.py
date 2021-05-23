import time

print ("Executing first while loop...")
count = 1
while count <= 10:
    print ("Count is : ", count) ###id we give this to line 9 count start from 2 end with 11
    time.sleep(1) ##not ness
    count += 1 #####increment 

print ("Executing second while loop...")
count = 1
while True:
    if count > 10:
       exit() ####for main contain in while true,
    print ("Count is : ", count)
    time.sleep(1)
    count += 1