def while_loop():
    i = 1
    while (i < 6):
        print("hello python chathura {}".format(i))
        i = i + 1  # same result from i+=1
#while_loop()
l=[1,2,3,"we",5,4]
def for_loop():
    for i in range(10):
        print(i)

    #for item in l:
    #    print(item)
    for x in range(6):
        print(l[x])
#for_loop()

def for_loop_002():
    for i in range(6):
        print("index {} = {}".format(i,l[i]))
for_loop_002()
print("app is done")