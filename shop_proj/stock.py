##variable name date 30/05/2021
###price list and price update 1 modul : 
def sprice():
    dall = float(input(""))
    a={"dall" : 73, "rices" : 50, "sugar" : 40, "salt" : 10, "oil" : 84}
    b={"dall" : dall, "rices" : 58, "sugar" : 43, "salt" : 10, "oil" : 80}
    ab=str({**a,**b})
    return ab
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##function list
if __name__== "__main__":
    sprice()