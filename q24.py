a={1,2,3,4,5}
b={5,6,7,8,9}
x=a.intersection(b)
print(x)
y=a.symmetric_difference(b)
print(y)
a.intersection_update(b)
print(a)
a.symmetric_difference_update(b)
print(a)

