# Find the second highest in the array

def secondlarge(arr):
    firsthigh=arr[0]
    secondhigh=arr[1]
    for num in arr:
      if(num > firsthigh):
        secondhigh=firsthigh
        firsthigh=num
       
      elif num > secondhigh and num < firsthigh:
        num=secondhigh

    return secondhigh


num= [12,23,34,45,56,67,78]   
print (secondlarge(num))


