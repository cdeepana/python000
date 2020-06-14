def main():
    out =  open("test.txt","a")  # a mean append(add)
    #out =  open("test.txt","w")  ==> this  w mean want to write
    #out.write("/nhi  write file")
    for i in range(5):
        inputToFile = input("enter string to write:")
        out.write("\n{}".format(inputToFile))
    out.close()

if __name__ == '__main__':main()
