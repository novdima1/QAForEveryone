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
    __PIN = "1234"
    __BALANCE = 0

    def check_balance(self):
        print(self.__class__.__BALANCE)
        return self.__class__.__BALANCE

    def add_money(self, amount):
        if amount > 1:
            self.__class__.__BALANCE += amount
        else:
            print("Amount should be greater than 1$")

    def withdraw(self, amount):
        i = 3
        while i > 0:
            pin = input("Enter pin: ")
            if pin == self.__class__.__PIN:
                if amount <= self.__class__.__BALANCE:
                    self.__class__.__BALANCE -= amount
                    print(f"Take your {amount}$. Rest: {self.__class__.__BALANCE}")
                    return None
                else:
                    print("Not enough money")
            else:
                print("Wrong pin!")
                i -= 1
        print("Your accout locked!")


acc = Account()
acc.add_money(100)
acc.add_money(-50)
acc.withdraw(20)
acc.check_balance()

acc1 = Account()
acc1.add_money(100)
acc1.add_money(-50)
acc1.withdraw(20)
acc1.check_balance()
