def Pay(x,y):
  hour=float(x)
  rte=float(y)

  if(hour<=40):
    return hour*rte
  else:
    return 40*rte+(hour-40)*1.5*rte



hrs=str(input("Enter hours: "))
rate=str(input("Enter rate: "))

result=Pay(hrs,rate)

print("The pay amount is: ",result)