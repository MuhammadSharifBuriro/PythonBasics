class bankaccount:
    def __init__(self, balance):   # Fixed
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
    
    def getBalance(self):
        return self._balance
    

acc = bankaccount(1000)
acc.deposit(500)
print(acc.getBalance())    # Fixed (no argument)
