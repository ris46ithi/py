def print_function(arg):
    print("You are executing print_function")
    print("The argument is : ", arg)


def print_function_positional_arguments(arg1, arg2):
    print("You are executing print_function_optional_argument")
    print("The argument 1 is : ", arg1)
    print("The argument 2 is : ", arg2)

print_function_positional_arguments(arg2=20, arg1=30)