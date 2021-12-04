import random
 
class Account:
    def __init__(self, card, pin, balance = 0):
        self.card = card
        self.pin = pin
        self.balance = balance
 
    def getCard(self):
        return self.card
 
    def getPin(self):
        return self.pin
 
    def getBalance(self):
        return self.balance
 
    def withdraw(self, amount):
        self.balance -= amount

def main():
   accounts = []
   for i in range(1000, 9999):
       account = Account(i, 0)
       accounts.append(account)
