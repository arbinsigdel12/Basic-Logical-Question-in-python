#Find if the number is prime or not

num=int(input("Enter a number"))
n=0
i=1
while i<num+1:
    if num%i==0:
      n=n+1
    i=i+1
print(n)
if(n==2):
   print("Given number is prime")    
else:
   print("Given number is not prime")  