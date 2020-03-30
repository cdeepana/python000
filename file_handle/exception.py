def main():
    try:
        x =  int( input("enter number"))
        print(x + 5)
    except ValueError:
        print(" Value have to be integer")

if __name__ == '__main__': main()
