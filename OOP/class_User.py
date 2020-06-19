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
    def __init__(self,type,model,price,millage):
        print("constructor car class")
        self._type=type
        self._model=model
        self._price=price
        self._millage=millage

    def getType(self):
        return self._type    
    def getModel(self):
        return self._model
    def getSalePrice(self):
        return self._price
    def getMillage(self):
        return self._millage
    def getCurrentPrice(self):
        return self._price - (self._millage*12)

# EXAMPLE 03 
class Bus:
    def __init__(self,**kwargs):
        print("constructor Bus class")
        self._Data=kwargs

    def getType(self):
        return self._Data["Type"]   
    def getModel(self):
        return self._Data["Model"]
    def getSalePrice(self):
        return self._Data["Price"]
    def getMillage(self):
        return self._Data["Millage"]
    def getAllData(self):
        return self._Data
#    def getCurrentPrice(self):
#        return self._price - (self._millage*12)

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
    myCar=Car("Ford","Laser",10000,12)
    currentValueOfCar =myCar.getCurrentPrice()
    print("Hey my car's current value is Rs:{}".format(currentValueOfCar))
    # example 02 end

    # example 03 starting
    myBus=Bus(Type="Tata",Model="1980",Price="20000",Millage="20")
    print(myBus.getSalePrice())
    print(myBus.getAllData())

if __name__ == '__main__':main()

# self keywork is i am in means. like own class value. like this
# self.x is mean -> in this class create a new variable x , we can assign values to it 