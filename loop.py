def while_loop():
    print('while loop function')
    i = 1
    while (i < 6):
        print("hello python chathura {}".format(i))
        i = i + 1  # same result from i+=1
    print('---------------######')
while_loop()
l=[1,2,3,"we",5,4]
def for_loop():
    print('for loop function')
    for i in range(10):
        print(i)
    print('---------------01')
    for item in l:
        print(item)
    print('---------------02')
    for x in range(6):
        print(l[x])
    print('---------------$$$$$$$$$$$$$$$')
for_loop()

def for_loop_002():
    print('for loop 02 function')
    for i in range(6):
        print("index {} = {}".format(i,l[i]))
for_loop_002()
print("app is done")