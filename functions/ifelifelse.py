def compare(arg1, arg2):
    if arg1 < arg2:
        return 1
    elif arg1 > arg2:
        return 2
    else:
        return 3

def main():
    user_input_1 = input("Enter first value : ")
    user_input_1 = int(user_input_1)
    user_input_2 = input("Enter second value : ")
    user_input_2 = int(user_input_2)
    result = compare(user_input_1, user_input_2)

    if result == 1:
        print("First value is Lesser than Second value...")
    elif result == 2:
        print("First value is Greater than Second value...")
    elif result == 3:
        print ("Both the values are Equal...")


main()