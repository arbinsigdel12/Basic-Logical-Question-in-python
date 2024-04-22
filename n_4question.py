#find number is a haystack
import re

f = open('sample.txt', 'r')
content = f.read()

f = open('actual.txt', 'r')
content2 = f.read()

x=re.findall('\d+',content)
print(len(x))
add=sum(map(int,x))
print(add)

y=re.findall('\d+',content2)
print(len(y))
add2=sum(map(int,y))
print(add2)
