"""
number=1
while number< 9:
  print(number)
  number=number+1

names = ['Bill Gates', 'Steve Jobs', 'Mark Zuckerberg']
i=0
while i<len(names):
  print(names[i])
  i=i+1



cities = ["Amsterdam", "Nairobi", "Tel Aviv", "New York"]
i = 0
while i < len(cities):
  print(cities[i])
  i = i+1

numbers = [3,2,4,5,7,8]
i = 0
while i < len(numbers):
  print(numbers[i])
  i = i + 1


bars = ["Mars" , "Bounty" , "Twix","Picnic","Yorkie"]
z=0
while z<len(bars):
  print(bars[z])
  z=z+1
price=float(input("Enter price:"))
if price >=1.00:
  tax=.07
  amountWithTax=price +(price*tax)
  print("Amount is: ",amountWithTax)
else:
  tax=0
  amountWithTax=price +(price*tax)
  print("Amount is: ",amountWithTax)

#cities = ["Amsterdam", "Nairobi", "Tel Aviv", "New York"]
#for x in cities:
  #print(x)
  """
products={"Soap":"20","Milo":"40","Milk":"25"}
print(products)
products["Bread"]="10"
print(products)

names={}
names["First"]="James"
names["Second"]="Bond"
print(names)