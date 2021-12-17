class Atm :
 
    def _init_(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
        

    def check_balance(self):
        print("Your balance is 50000")

    def withdrawl(self,amount):
        new_amount=50000-amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))


def main():
    card_number = input("Insert your card number")
    pin_number = input("Enter your pin number")

    new_user=Atm(card_number,pin_number)

    print("Choose your activite")
    print("1.balance enquiry 2.widh drall")

    activity = int(input("Enter the activity number"))
    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2): 
        amount = int(input("enter the amount:- ")) 
        new_user.withdrawl(amount) 
    else: print("enter a valid number") 


if __name__ == "__main__": main()






