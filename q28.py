def myFunction(b):
 return lambda a: a*b
mul=myFunction(10)
print(mul(11))