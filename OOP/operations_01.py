# -------------------------------------------------------------EXAMPLE 01 ---START ----------------------------------> inheritance
class Operations:
    def sum(self,n1,n2):
        return n1+n2
    def div(self,n1,n2):
        return n1/n2

class MultiOperations(Operations):
    def mul(self,n1,n2):
        return n1*n2
# ----------------------01 END

# -------------------------------------------------------------EXAMPLE 02 ---START ----------------------------------> override method
class Operations2:
    def sum(self,n1,n2):
        return n1+n2
    def div(self,n1,n2):
        return n1/n2

class MultiOperations2(Operations2):
    def mul(self,n1,n2):
        return n1*n2
    def sum(self,n1,n2): #this sum method is override 
        return (n1+n2)*10
    def sumByParent(self,n1,n2): # want to use parent method so use keyword super()
        return super().sum(n1,n2)
# -----------------------02 END
def main():
    print("hello main")

# exmaple 01 start
    mulOP=MultiOperations()
    # print(mulOP.mul(2,3))
    print("multiply value = {}".format(mulOP.mul(2,3)))
    print("sum of values = {}".format(mulOP.sum(2,3)))
    print("sum of values = {}".format(mulOP.div(2,3)))
#example 01 end

# exmaple 02 start
    mulOP2=MultiOperations2()
    # print(mulOP.mul(2,3))
    print("multiply value = {}".format(mulOP2.mul(2,3)))
    print("sum of values = {}".format(mulOP2.sum(2,3)))
    print("sum of values by parent = {}".format(mulOP2.sumByParent(2,3)))
    print("sum of values = {}".format(mulOP2.div(2,3)))
#example 02 end
    
if __name__ == "__main__":
    main()