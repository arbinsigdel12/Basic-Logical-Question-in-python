#find the score
# import re

score=str(input("Enter your score: "))
# x=re.findall("[0-9]*.*[0-9]",str(score))
# z=x[0]
y=float(score)
if (y >=0 and y <= 1):
    if (y >= 0.9 and y<= 1):
        print("A")
    if (y >= 0.8 and y<0.9):
        print("B")
    if (y  >= 0.7 and y<0.8):
        print("C")
    if (y  >= 0.6 and y<0.7):
        print("D")
    if (y<0.6):
        print("E")
    

else:
    print("Error")
