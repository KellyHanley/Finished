# OOP ASSIGNMENT SHELL (Bank Account Manager)

#Your code here for 3 classes
class Accounts(object):
    def __init__(self,balance):
        self.balance = balance
    
class Checking(Accounts):
    def __init__(self,Checking):
        Checking >= 100
class Savings(Accounts):
    def __init__(self,Savings):
        interest = Savings*.01
        
print ("Welcome to Kelly's ATM")
accountType = int(input("What type of account? 1:Savings; 2:Checking?"))
if accountType == 1:
    accountPicked = Savings(1500)
elif accountType == 2:
    accountPicked = Checking(1000)
else:
    print ("I'm sorry. I didn't catch that. Please repeat.")

question = input("Okay. What would you like to do? 1: Check Balance 2: Deposit 3: Withdraw 4: Calculate Interest 5: Exit")
if question == "1":
    str(balance)
elif question == "2":
    input("Okay. How much would you like to deposit?")
    print ("Okay. Your money has been deposited.")
elif question == "3":
    input("Okay. How much would you like to withdraw?")
    print("Okay. Your money has been withdrawn.")
elif question == "4":
    print
elif question == "5":
    print("Okay, thank you for stoping at Kelly's ATM")
else:
    input("I'm sorry.I didn't catch that. Please repeat.")
  


    


#Your code here - loop asking the user what they want to do


    
    
