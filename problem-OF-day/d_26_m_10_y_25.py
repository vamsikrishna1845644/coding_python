from typing import List
class Bank:

    def __init__(self, balance: List[int]):
        # we neeed to iniatlise balance
        self.balance = balance    

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # account number from 1 to n
        n = len(self.balance)
        if account1<=n and account2 <=n and self.balance[account1-1]>=money :
            self.balance[account1-1] -= money
            self.balance[account2-1] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        # we need to add money to the account
        n = len(self.balance)
        if account <=n:
            self.balance[account-1]+=money
            return True
        else:
            return False

        

    def withdraw(self, account: int, money: int) -> bool:
        n = len(self.balance)
        if  account<=n and self.balance[account-1]>=money :
            self.balance[account-1]-=money
            return True
        else:
            return False
