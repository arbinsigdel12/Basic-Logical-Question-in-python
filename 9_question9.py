# Draw the pattern in question 9

rows=8
for i in range(rows-1):
    for j in range(rows-i-1):
      print(j+1,end="")  
    print()
