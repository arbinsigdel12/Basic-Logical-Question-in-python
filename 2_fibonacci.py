# Find fibonnaci series upto the given number

n=int(input("Enter you number"))
a=0
b=1
sum=0
print(a)
print(b)
while sum<n-1:
  sum=a+b
  print(sum)
  a=b
  b=sum