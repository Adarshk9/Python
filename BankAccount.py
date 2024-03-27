Balance = 0
class BankAccount:
    x = globals()
    def deposite(self,ammount):
        global Balance
        Balance += ammount
    def withdraw(self,ammount):
        global Balance
        Balance -= ammount
        print("Success")
class SavingAccount(BankAccount):
    global Balance
    def withdraw(self, ammount):
        if(Balance-ammount<100):
            raise NotImplementedError("Account Balance less than 100")
        else:
            BankAccount.withdraw(self,ammount)
            return "success"
obj = SavingAccount()
while(True):
    ch = int(input("Press 1 to withdraw\nPress 2 to deposite\n 3 to exit"))
    if(ch==1):
        ammount = int(input("Enter ammount"))
        obj.withdraw(ammount)
    elif(ch==2):
        ammount = int(input("Enter ammount"))
        obj.deposite(ammount)
    elif(ch==3):
        print("Transaction Succesful!")
        break
    else:
        print("Invalid choice!")
        break
print("Balance = ",Balance)

