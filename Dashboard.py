from IRCTC_backend import Show_train_details
std = Show_train_details()
from booknow import Book_Now
bn  = Book_Now()

class Dashboard():
    def dashboard_method(self):
            
        print()
        print("="*70)
        print("\t\tEastern Railway Tourist Special Booking")
        print("\tAdditional Special Trains from 01/01/2023 to 05/01/2023")
        print("="*70)
        print("\t\t\t\tDeveloped By REHAN")
        print()
        print("SEALDAH  -   NEW JALPAIGURI")
        print("SEALDAH  -   RAMPURHAT")
        print("HOWRA    -   DIGHA")
        print("HOWRA    -   PURI\n")


        frm = input("From (No spaces Allow) : ")
        to = input("To (No spaces Allow): ")
        date = int(input("DD/01/2023 : "))
        # print(date)
        concat =frm+to
        # print(concat)
        if date>=1 and date<=5:

            if concat.lower()=='howrapuri':

                print(f"\n-----The Trains Available on {date}/01/2023 from {frm} to {to} are -----\n")
                std.howrapuri(date)
                bn.booknow_method()

            elif concat.lower()=='howradigha':

                print(f"\n-----The Trains Available on {date}/01/2023 from {frm} to {to} are -----\n")
                std.howradigha(date)
                bn.booknow_method()

            elif concat.lower()=='sealdahnewjalpaiguri':

                print(f"\n-----The Trains Available on {date}/01/2023 from {frm} to {to} are -----\n")
                std.sealdahnewjalpaiguri(date)
                bn.booknow_method()

            elif concat.lower()=='sealdahrampurhat':

                print(f"\n-----The Trains Available on {date}/01/2023 from {frm} to {to} are -----\n")
                std.sealdahrampurhat(date)
                bn.booknow_method()

            else:
                print("Only These 4 destinations are added for Holiday Purpose")  
                print("Choose from The List of Available Trains")
        else:
            print("Choose between 01/01/2023 to 05/01/2023")
 