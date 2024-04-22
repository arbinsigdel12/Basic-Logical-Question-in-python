#Find the hcf of the given two number

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))

def hcffunction(x, y):
    while y:
        x, y = y, x % y
    return x
hcf = hcffunction(num1, num2)
print("The HCF of ",num1," and",num2," is ",hcf)