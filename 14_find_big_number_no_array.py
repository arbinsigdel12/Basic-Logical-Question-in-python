# Find the bigest number without using array function 

numbers_input = input("Enter numbers separated by spaces: ")
number_strings = numbers_input.split()
print(number_strings)
max_num = int(number_strings[0])

for num_str in number_strings:
    num = int(num_str)
    if num > max_num:
        max_num = num
print("The largest number is:", max_num)