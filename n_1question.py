#find hourly rate

hrs=str(input("Enter hours: "))
rate=str(input("Enter rate: "))

hour=float(hrs)
rte=float(rate)

if(hour<=40):
    print("The pay amount is: ",hour*rte)
else:
    print("The pay amount is: ",40*rte+(hour-40)*1.5*rte)