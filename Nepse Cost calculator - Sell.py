#a is buying price
#b is selling rate
#c is quantity
#d net buy
#e net sales
#f SEBON Charge
#g DP Charge
#h Total Buying Cost
#i = broker charge
#j Buying cost per unit share:
#k taxable
#l non taxable
#m profit 
#n loss
#o net profit
#p total receivable amount in profit
#q total receivable amount in loss
#Taking input from user
a = float(input("Enter Buying  Price/per share: "))
b = float(input("Enter Sellig Rate: "))
c = int(input("Quantity: "))
 
d = a*c
e = b*c
 
#Storing values for different charge ranges!
 
k = 50000
l = 500000
m = 2000000
n = 10000000
o = 1000000000
 
#Conditions for Broker charges:
 
if k >= d:
  i = c*0.004
 
elif l >= d:
  i = c*0.0037 
 
elif m >= d:
  i = c*0.0034
 
elif n >= d:
  i = c*0.003
 
elif o >= d:
  i = c*0.0027
 
f = d*0.00015
g = 25 
h = d+f+g+i
m=e-h
k=0.05*m
o=e-h-i-f-k
p=e-i-f-k
 
 
if e > h:
  
  print("Purchase cost: ",h)
  print("Net Sales: ",e)
  print("Broker Charge: ",i )
  print("SEBON COMMISION: ",f)
  print("DP Charge: ",g)
  print("Capital Gain Tax: ",k)
  print("Net Profit: ",o)
  print("Total Receivable amount: ",p)
 
 
elif e < h:
  q=e-i-f-g
  n=h-q
  print("Purchase cost: ",h)
  print("Net Sales: ",e)
  print("Broker Charge: ",i )
  print("SEBON COMMISION: ",f)
  print("DP Charge: ",g)
  print("Net Loss: ",n)
  print("Total Receivable amount: ",q)
 