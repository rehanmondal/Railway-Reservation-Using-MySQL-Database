import mysql.connector as connector
from checkout import CheckOut

ck = CheckOut()
class Book_Now:
    def __init__(self):
        self.con    = connector.connect(
            host     = 'localhost',  # host, port these all are case sensitive in python !!
            port     = '3306',
            database = 'irctc',
            user     = 'root')

    def booknow_method(self):
        print("Want To Book Now - Y")
        print("Exit from Site - E")

        choice_ye = input("-> ")

        if choice_ye.lower()=='y':
            print("Create Account - NEW REGISTRATION -> R")
            print("Already have an Account - LOGIN -> L")
            choice_rl = input("-> ")

#=========================== NEW REGISTRATION starts ====================================
            if choice_rl.lower()=='r':
               
                r_name = input("Enter Your Name : ")
                r_pass = input("Create a Strong Password atleast 8 charater : ")
                n = len(r_pass)
                if n>=8:
                    query ="insert into userregister(userName,password) values('{}','{}')".format(r_name,r_pass)
                    cur = self.con.cursor()
                    cur.execute(query)
                    self.con.commit()
                    print("User Registration Successfully Completed ")

                    q = "select * from userregister where password='{}'".format(r_pass)
                    cur.execute(q)
                    for row in cur:
                        print("\nYour Generated ID - ",row[0])
                        print("And Your Password - ",row[2])
                        print("\n")
                else:
                    print("Passwor must contain atlease 8 characters  ! ")

                print("="*70)
                print(" Book Now")
                print("----------")
                ck.checkout()
                # pf.passengersformmethod()
            
                
#=========================== NEW REGISTRATION ends ====================================
#===========================    LOGIN starts    ====================================

            elif choice_rl.lower()=='l':
                log_id      = int(input("Enter your Login ID : "))
                log_pass    = input("Enter your password : ")
                
                q = "select * from userregister where id={} and password='{}'".format(log_id,log_pass)
                cur = self.con.cursor()
                cur.execute(q)
                cur.fetchone()
                if cur.rowcount>0:
                    # pf.passengersformmethod()
                    # print("Booking Form") #def method calling hobe passenger details page DATABASE insert
                    ck.checkout()
                else:
                    print("Invalid User ID or Password !")

            else:
                print("\nYou have not choosed any of it \n\nExited ")
               
            
        elif choice_ye.lower()=='e':
                print("Thanks For Visit Us !")
            
        else:
            print("Incorrect Input ! To Continue Press and (Y) To Exit Press (E)")
            #print("You have not choosed any of it \n Backed To Dashboard ")

# -------------- form filled --------------- now passenger details tene seat minus plus invoice confirm

# book = Book_Now()
# book.booknow_method()