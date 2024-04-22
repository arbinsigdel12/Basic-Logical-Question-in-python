# bubble sort 

arr=[43,56,23,78,65,12,45]
n=len(arr)
for i in range(n):
    for j in range(n-1):
        if(arr[j] > arr[j+1]):
           arr[j],arr[j+1]=arr[j+1],arr[j]
        

print("The sorted list is",arr)
    