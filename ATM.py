def check_balance(balance):
    return f"Account Balance: {balance}\n"

def withdraw(amount, balance):
    if amount > balance:
        return "Amount too large"  
    print("Amount Withdrawn successfully\n")
    return balance - amount

def deposit(amount, balance):
    print("Amount Deposited successfully\n")
    return balance + amount

def showOption():
    print("==================")
    print("SELECT:")
    print("\t1. Check Balance")
    print("\t2. Withdraw")
    print("\t3. Deposit")
    print("\t4. Exit")
    print("==================")


def main():

    balance = 10000
    while True:

        pin = 1234

        entry_pin = input("Enter your pin here:")
        if int(entry_pin) != pin :
            print("Incorrect pin try again")
            continue

        showOption()

        choice = input("Enter your option here:")

        if choice not in ["1","2","3", "4"]:
            print("Invalid choice")

        if choice == "4":
            print("goodbye")
            break

        if choice == "1":
            print("=======loading======")
            print(check_balance(balance))
            showOption()
        if choice == "2":
            print("=======loading======")

            amount = input("Enter amount to withdraw here:")
            try:
                amount = float(amount)
            except:
                print("Invalid amount")
                continue

            balance = withdraw(amount, balance)

            showOption()

        if choice == "3":
            print("=======loading======")
        
            amount = input("Enter amount to deposit here:")

            try:
                amount = float(amount)
            except:
                print("Invalid amount")
                continue

            balance = deposit(amount, balance)
        
            showOption()

if __name__ == "__main__":
    main()
                




        




