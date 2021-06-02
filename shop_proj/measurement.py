### measurement , ,litter,ml ,kilogram,grams, packets, count ,###

#a = input("kg")
#b= input("L")
#c = input("Pac")
#d = input("Count")
###rice 1kg 60 2kg 120
###Rice packet 25kg 1300
# oil 1 2 150 
# rice 5  300
## bill amount 450 
# card or cash or upi 
#a=10 b=10 c=10 d=10 e=10  total= 50motta
#a=25kg b=25kg c=25kg d=25kg e=25kg 
#a=1000rs b=900rs c=1200rs d=1100rs e=800rs
#sales report --
#stock report --
product=input("")
mes = str(input("kilo ? :"))
price =  int(input("price? :"))
unit = ['kg', 'L', 'ml', 'grams', 'pac']
a = {product : ( mes+unit[0], price)}
print(a)