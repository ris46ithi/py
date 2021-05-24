def addition(arg1, arg2):
    return arg1 + arg2


def addition(arg1, arg2, arg3):
    return arg1 + arg2 + arg3


def addition(*args):
    number_of_arguments = len(args)
    print ("Number of arguments are : ", number_of_arguments)
    if number_of_arguments > 0:
        result = 0
        for value in args:
            result += value
        print ("Addition result is : ", result)


addition(1, 2, 3, 4, 5, 6)

