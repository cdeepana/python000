x=0b111
y=0b101
z=y&x
t=y|x
def f(n): print('{:08b}'.format(n))  # this 08 --> 8 define the number of value like 8 00000111   5 00111
f(0b111)  # call the function
f(t>>2)
f(t<<2)

