#python program to create Bankaccount class
#width both a deposit() and a widthdraw() function
class Bank_Account:
    def__init__(self) :
      self. balance=0
      print("Hello!!!  Welcome to the deposit & widthdrawl machine")

    def deposit(self):
      amount= float(input("Enter amount to be deposited: ")) 
      self. balance +=amount
      print("\n Amount deposited:",amount)

def widthdraw(self) 
    amount=float(input("Enter amount to be widthdrawn:"))
     if self. balance>=amount:
        self.balance-=amount
        print("\n you withdrew:",amount) 
     else
        print("\n insufficient balance") 

  def display(self):
      prprint("\n net available balance=",self.balance) 

#driver code

#creating an object of class
s= ￼Bank_Account() 

#calling function with that class object
s. deposit() 
s. withdraw() 
s. display() 
             
