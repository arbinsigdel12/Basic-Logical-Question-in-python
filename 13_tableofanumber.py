# Find a table of a number

n=int(input("Enter the number"))
start=int(input("Enter the starting number"))
end=int(input("Enter the ending number"))

for i in range(start,end+1):
    z=n*i
    print(z)