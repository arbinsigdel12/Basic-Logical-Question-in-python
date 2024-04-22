import re
smaller = 0
larger = 0
flag = True
while(True):
    try:
        imp=str(input("Enter the number: "))
        if imp == "done":
            break
        else:
            num = int(imp)
            if flag:
                smaller = num
                larger = num
                flag=False
            if(num<smaller):
                smaller=num
            if(num>larger):
                larger=num

    
    except:
      print("Invalid Input")

print("Smaller Number is",smaller,"\nLarger Number is",larger)