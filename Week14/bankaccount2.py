# bankaccount2.py

class BankAccount:
    
    # __init__ method contains a balance amount and 
    # assign it to the __balance attribute
    def __init__(self, bal):
        self.__balance = bal
        
    # deposit method makes a deposit into account
    def deposit(self, amount):
        self.__balance += amount
    
    # withdraw method withdraw money from account
    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
        else:
            print('Error: insufficient fund in the account.')
            
    # returns current account balance
    def get_balance(self):
        return self.__balance
    
    # current status of the account
    def __str__(self):
        return f'The balance is ${self.__balance:,.2f}'