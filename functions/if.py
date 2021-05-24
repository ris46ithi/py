def multiple_of(value):
    for val in range(1, 101):
        if val % value == 0:
            print (val)


def main():
    print ("OPTIONS")
    user_input = input("Enter a value between 1 to 10 : ")
    user_input = int(user_input)
    multiple_of(user_input)


main()