import mysql.connector as connector

class Show_train_details:
    def __init__(self):
        self.con     = connector.connect(
            host     = 'localhost',  # host, port these all are case sensitive !!
            port     = '3306',
            database = 'irctc',
            user     = 'root')

        # if self.con.is_connected():
        #     print("Database Conn succ...")
        
    def howradigha(self,date):
        query = "Select * from howradigha where Date={}".format(date)
        cur = self.con.cursor()
        cur.execute(query)
        # print(query)
        for row in cur:
            print("Train Name        : ",row[1])
            print("Train No.         : ",row[2])
            print("Available Classes : ",row[3])
            print("Fare              : ",row[4])
            print("Timings           : ",row[5])
            print("Available Seats   : ",row[6])
            print("\n")
            print("-----------------------------------")
        
    def howrapuri(self,date):
        query = "Select * from howrapuri where Date={}".format(date)
        cur = self.con.cursor()
        cur.execute(query)
        # print(query)
        for row in cur:
            print("Train Name        : ",row[1])
            print("Train No.         : ",row[2])
            print("Available Classes : ",row[3])
            print("Fare              : ",row[4])
            print("Timings           : ",row[5])
            print("Available Seats   : ",row[6])
            print("\n")
            print("-----------------------------------")

    def sealdahnewjalpaiguri(self,date):
        query = "Select * from sealdahnewjalpaiguri where Date={}".format(date)
        cur = self.con.cursor()
        cur.execute(query)
        # print(query)
        for row in cur:
            print("Train Name        : ",row[1])
            print("Train No.         : ",row[2])
            print("Available Classes : ",row[3])
            print("Fare              : ",row[4])
            print("Timings           : ",row[5])
            print("Available Seats   : ",row[6])
            print("\n")
            print("-----------------------------------")

    def sealdahrampurhat(self,date):
        query = "Select * from sealdahrampurhat where Date={}".format(date)
        cur = self.con.cursor()
        cur.execute(query)
        # print(query)
        for row in cur:
            print("Train Name        : ",row[1])
            print("Train No.         : ",row[2])
            print("Available Classes : ",row[3])
            print("Fare              : ",row[4])
            print("Timings           : ",row[5])
            print("Available Seats   : ",row[6])
            print("\n")
            print("-----------------------------------")






