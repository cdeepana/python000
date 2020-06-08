l = [1,45,50,80,34]
print(l[2])
print(l[1:3])

x = []
x[:] = range(6)
print(x)

# and also we can replace this defauls values with our values like this
x[0:3] = (0,0,0)
print(x)

y = []
y[0:3] = range(4)
print(y)
y[:] = range(50)
print(y)