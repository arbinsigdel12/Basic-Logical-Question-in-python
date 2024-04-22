# draw the pattern

rows=5
for i in range(1,rows+1):
    if i==1 or i==rows:
        print("*"*5)
    else:
        print("*   *")