
import sqlite3

class DbConnet:
    
    def __init__(self):
        db = sqlite3.connect("OOP_testing.db")
    def createTable():
        db.row_factory = sqlite3.Row
        db.execute("create table if not exists Admin(ID integer primary key autoincrement,  Name text,Age int)")
        db.commit()

    def Add(Name, Age):
        db.row_factory = sqlite3.Row
        db.execute("insert into Admin(Name,Age) values (?,?)",(Name,Age))
        db.commit()
        print("Added record")

    def listAdmins():
        data =  db.execute("select * from Admin")
        for row in data:
            print("ID {}, Name0 {}, Age {}".format(row["ID"],row["Name"],row["Age"]))

    def deleteRecord(ID):
        db.row_factory = sqlite3.Row
        db.execute("delete from Admin where ID = '{}'".format(ID))
        db.commit()
        print("deleted record")

    def updateRecord(ID,Age):
        db.row_factory = sqlite3.Row
        db.execute("update Admin set Age = ? where ID = ?",(Age,ID))
        db.commit()
        print("Updated record")

def main():
    createTable()
    while 1:
        IndexOp = int(input("Select Operation, 1-Add: \n 2-to list Admins: \n 3-to delete Admin:\n 4-to Update \n 0-to exit: "))
        if(IndexOp == 0):
            break;
        elif(IndexOp == 1):
            Name = input("Enter name:")
            Age = int(input("Enter Age"))
            Add(Name,Age)
        elif(IndexOp == 2):
            listAdmins()
        elif(IndexOp == 3):
            ID = int(input("Enter ID of Admin"))
            deleteRecord(ID)
        elif(IndexOp == 4):
            ID = input("Enter ID")
            Age = input("Enter the new Age")
            updateRecord(ID,Age)

if __name__ == '__main__':main()

