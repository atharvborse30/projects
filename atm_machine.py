from operator import truediv

atm_balance = 1000000
account_1_balance = 100000
card_inserted = True
pin = 1234

def display_acc_bal():
    print(account_1_balance)

def display_atm_bal():
    print(atm_balance)

if card_inserted:
    print("enter your pin...")
    entered_pin = int(input())
    if entered_pin==pin:
        print("you have entered right pin",end=" ")

        transaction = input("enter what transaction you want to do....")

        match transaction:
            case "Withdrawl":
                print("so you want to withraw money")
                
                amount = int(input("enter how much money you want to withraw..."))   
                if amount < 100:
                    print("sorry please enter amount above 100",end="")
                if amount > 10000:
                    print("sorry you can't withdraw amount greater than 10000","/n")
                else:
                    if atm_balance>amount:
                        if account_1_balance>amount:
                            account_1_balance-=amount
                            print("kindly collect the money...")
                            atm_balance-=amount
                            display_acc_bal()
                            display_atm_bal()
                            print("Transaction successful")
                            print("kindly eject the card now ")
                        else:
                            print("not enought balance")
                    else:
                        print("sorry, not enough cash right now")






        
