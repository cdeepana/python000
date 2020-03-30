
y =  10
def show():
    global y
    print(y)

def main():
    x = 10 # local variable
    print("x = {}".format(x))
    show()

if __name__ == '__main__':main()
