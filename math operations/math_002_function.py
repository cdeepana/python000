def functionAndOperation(): {
print("{}".format(x and y))
}
x =  True
y = False
#functionAndOperation()    # this line for call the and operation function

def functionOROperation(): {
print(x or y)
}
#functionOROperation()

def function001(): {
    print(2<1)
}
#function001()

name = "chathura"
number = "25"
number1 = int(number)
number2 = float(number)
string1 =  str(number1)
def function002():
    print(type(name))
    #print(number1)
    #print(type(number2))
    print(number2)  # this will print 25.0 float value
# and also we do not want to use bracket in function declarion. {}
function002()

def function003():
    x = ("re","ree","wee","fdf")
    print("1st ==> {}".format(type(x)))
    print("this is original x {}".format(x))
    
    y = list(x[0:3])
    print("2nd ==> {}".format(type(y)))
    print("this is y {}".format(y))
function003()
#SO ALL THESE TYPE OF DATA TYPE CAN CONVERT LIKE THIS

# str()
# int()
# float()
# list()
# set()
# dict()
# tuple()
