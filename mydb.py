import sqlite3

class Auth:
    def __init__(self):
        
        self.conn = sqlite3.connect("passenger.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""create table if not exists passenger (
                            Firstname varchar(20),
                            Lastname varchar(15),
                            EmailID varchar (20),
                            password varchar(8),
                            PhoneNO int(10),
                            Age int(3)

                            



        )""")

    def passenger(self, **u):
        print("Registered Sucessfull")

        self.cursor.execute(""" INSERT INTO passenger (Firstname, Lastname, EmailID, password, PhoneNO, Age)Values(?,?,?,?,?,?)""",(u["Firstname"], u["Lastname"], u["EmailID"], u["password"], u["PhoneNO"], u["Age"]))
        self.conn.commit()
        
    
        
    def loginpage(self, EmailID, password):
        self.cursor.execute("""select count(*) from passenger where EmailID = ? and password = ?""",(EmailID, password) )
        r = self.cursor.fetchone()
        if r[0]>0:
            return True
        else:
            return False 