# Find the factors of two number

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
def find_factors(n1, n2):
    fact1 = []
    fact2 = []

    for i in range(1, n1 + 1):
        if n1 % i == 0:
            fact1.append(i)

    for i in range(1, n2 + 1):
        if n2 % i == 0:
            fact2.append(i)

    return fact1, fact2


fact1, fact2 = find_factors(num1, num2)

print("The factors of ",num1,"are: ",fact1)
print("The factors of ",num2," are: ",fact2)