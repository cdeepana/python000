import datetime
def functionIF():
 DOB =  input("Enter your DOB:")
 CurrentYear = datetime.datetime.now().year
 Age = CurrentYear -  int(DOB)
 if(Age >= 18):
  print("Your age is {}".format(Age))

#functionIF()

def functionIFELSE():
 number =  input("enter age:")
 town = input(" enter your town")
 if( int(number)>18 and "town" == str(town) ):
  print("You are old and town is ok !!!")
 elif( int(number)>18 and "town" != str(town) ):
  print("You are old and not in town")
 elif( int(number)==18 ):
  print("find a job")
 else:
  print("You are young !!!!!!!")

functionIFELSE()


