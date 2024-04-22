# Find if the given number is armstrong or not

n=int(input("Enter a number"))
num=n
sum=0
i=0
while  n!=0:
 r=n%10
 sum=sum*10+r
 n=n//10
 i=i+1
print(sum) 
if num==sum:
  print("The given number is Armstrong number ")
else :
  print("The number is not Armstrong number")