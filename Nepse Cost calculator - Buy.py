# a is price of unit share
#b is quantity
#c is net purchase amount
#d is sebon commision
#e is dp charge
#f broker charge when amount is less or equal to 50k
#g broker charge when amount is between 50k to 5 lakh
#h broker charge when amount is between 5 lakh to 20 lakh
#i broker charge when amount is between 20 lakh to 1 crore
#j broker charge whem amount is above 1 crore
#k = 50000  
#l = 500000
#m = 2000000
#n = 10000000
#t = Total amount
#u = Price per unit share


#Taking input from user
a = int(input("Enter Price/per share: "))
b = int(input("Quantity: "))

#Calculating net purchase amount
c = a*b

#Storing values for different charge ranges!

k = 50000
l = 500000
m = 2000000
n = 10000000
o = 1000000000


#Different Coditions for Broker Charges!

if k >= c:
  f = c*0.004
  
elif l >= c:
  f = c*0.0037 

elif m >= c:
  f = c*0.0034

elif n >= c:
  f = c*0.003

elif o >= c:
  f = c*0.0027

d = c*0.00015
e = 25 
t = c+f+d+e
u = t/b

#Displaying Final Output
print("Net Purchase Amount:",c)
print("Broker Charge:",f)
print("SEBON Commision:",d)
print("DP Charge:",e)
print("Price per unit Share:",u)
print("Total Amount:",t)


