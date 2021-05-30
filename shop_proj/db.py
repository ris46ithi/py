from datetime import datetime
import stock

def database():
    p = stock.sprice()
    now = datetime.now()
    d = now.strftime("%d/%m/%Y %H:%M:%S")
    f = open("stock_base.txt", 'r+')
    f.write(d+" = "+p+"\n")
    f1 = f.readlines()
    print(f1)

if __name__== "__main__":
    database()