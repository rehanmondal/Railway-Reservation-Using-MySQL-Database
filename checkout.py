import mysql.connector as connector
from IRCTC_backend import Show_train_details
std = Show_train_details()

class CheckOut:
    def __init__(self):
        self.con    = connector.connect(
            host     = 'localhost',
            port     = '3306',
            database = 'irctc',
            user     = 'root')

    def checkout(self):
        print("\n---------------- FILL THE TRAVEL INFORMATION -------------")
        try:

            nop = int(input("\nNumber of Passengers(Above 3 years) - "))

            doj     = int(input("Date of Journey(Enter Day Only) from 1 - 5 : 0_/01/2023 : "))
            frm     = input("Station From - ")
            to      = input("To Station - ")
            concat_2  = frm+to

            if doj>=1 and doj<=5:

                if concat_2.lower()=='howrapuri':
                    std.howrapuri(doj)
                elif concat_2.lower()=='howradigha':
                    std.howradigha(doj)

                elif concat_2.lower()=='sealdahrampurhat':
                    std.sealdahrampurhat(doj)

                elif concat_2.lower()=='sealdahnewjalpaiguri':
                    std.sealdahnewjalpaiguri(doj)


            tno = input("Enter Train Number - ")
            for i in range(nop):

                print(f"---------------- PASSENGER {i+1} INFORMATION -------------")
                name = input("Full Name in Block Letters - ")
                nationality = input("Nationality - ")
                gender = input("Gender - ")
                adhar = int(input("Adhar Number(optional) - "))
                address = input("Full Address - ")

            fare = nop*300
            gst = (fare * 0.18)        # FOR 18 % GST Last value , mid value trai fare
            totafare = (fare+gst)
            print(f"\nTotal Fare (incl. GST ) for {nop}: person : ",totafare)
            print("\n")
            confirm  = input("Book Tickets Confirm ? Y|N : ")
            if confirm.lower() =='y':
                print("````PAYMENT PAGE````\nNEED TO USE PAYMENT GATEWAY USING API\nAfter Succesfull Payment Booking Done\nGet SMS(TWILIO API) ")
                print("See My Integration Twilio Project to send sms")
                print("\n******** Railway Project Using Real World API DATA with Front End Coming Soon !! ********* ")
                print("\nTHANKS FOR WATCHING\nRegards Rehan")

            elif confirm.lower() =='n':
                print("Booking Canceled Sucecsfully")
            else:
                print("Invalid Input !")
        except:
            print("Invalid Input !Try Again")

