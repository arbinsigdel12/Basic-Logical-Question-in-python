# Draw the given pattern
rows=5
n=1
for i in range(0,rows+1):
    for j in range(1,i+n):
      print("*",end="") 
    for k in range(i):
       print(0,end="")
       n=n+1
    print()

