# EXAMPLE 01
class User:
    def __init__(self):             # this init --constructor method
        print("this it constructor")
    def setUserName(self,userName):
        self._userName=userName
    
    def getUserName(self):
        return self._userName

# EXAMPLE 02
class Car:
    def __init__(self):
        print("constructor car class")
    def setType(self,type):
        self._type=type
    def getType(self):
        return self._type
    def setModel(self,model):
        self._model=type
    def getModel(self):
        return self._model
    def setSalePrice(self,price):
        self._price=price
    def getSalePrice(self):
        return self._price
    def setMillage(self,millage):
        self._millage=millage
    def getMillage(self):
        return self._millage
    def getCurrentPrice(self):
        return self._price - (self._millage*5)

def main():
    # exmple 01 starting
    u1=User()     #for u1
    u1.setUserName("chathurad")
    u2=User()     #for u2
    u2.setUserName("deepanah")
    print(u1.getUserName())
    print(u2.getUserName())
    # example 01 end

    # example 02 starting
    myCar=Car()
    myCar.setType("Ford")
    myCar.setModel("Laser")
    myCar.setSalePrice(10000)
    myCar.setMillage(12)

    currentValueOfCar =myCar.getCurrentPrice()
    print("Hey my car's current value is Rs:{}".format(currentValueOfCar))
    # example 02 end

if __name__ == '__main__':main()

# self keywork is i am in means. like own class value. like this
# self.x is mean -> in this class create a new variable x , we can assign values to it 