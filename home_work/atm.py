"""
Implement an ATM (Automatic Teller Machine)
User should be able:
1. Create account with pin and balance
2. Check account balance
3. Deposit money to account
4. Withdraw money
5. Tell user that not enough money on balance in case if step 4 required more money than user had
"""

class Account:

    def __init__(self, pin='1234', balance=0, s_balance=1000):
        self.__pin = pin
        self.__balance = balance
        self.s_balance = s_balance

    def check_balance(self):
        print(self.__balance)

    def check_secret_balance(self):
        print(self.s_balance)

    def add_money(self, amount):
        if amount > 1:
            self.__balance += amount
            print(f"{amount}$ has been added to your balance")
        else:
            print("Amount should be greater than 1$")
        return self.__balance

    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if amount <= self.__balance and amount > 0:
                self.__balance -= amount
                print(f"Take your {amount}$. Rest: {self.__balance}")
                return self.__balance
            else:
                print("Not enough money")
        else:
            print("Wrong pin!")
            return None

"""
acc = Account()
acc.add_money(100)
acc.add_money(-50)
acc.withdraw(20)
acc.check_balance()

acc1 = Account('4321')
acc1.add_money(100)
acc1.add_money(-50)
acc1.withdraw(20)
acc1.check_balance()
acc1.s_balance = 2000
print(acc1.s_balance)
acc1.__balance = 3000
print(acc1.__balance)
acc1.check_balance()
acc1.check_secret_balance()
"""
