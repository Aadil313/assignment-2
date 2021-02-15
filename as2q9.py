a = ["p","q","r"]
x = map(lambda s:s[0]=="p",a)
print (list(x))
b = print(list(filter(lambda x:x[0]=="r",a)))
from functools import reduce
def add (x,y):
	return x+y

a = [1,2,3,4]
print(reduce(add,a))



