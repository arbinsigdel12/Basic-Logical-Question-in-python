# draw the pattern

rows=4
for i in range(1,rows+1):
    for j in range(1,rows):
        print(i+(j-1)*rows,end="")
    print()
    
