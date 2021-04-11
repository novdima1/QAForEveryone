from home_work.atm import Account
from data import atm_data, results

class Atm(Account):

    def check_account_is_created(self):
        my_atm = Atm()
        print("\nAccount checked")
        return my_atm

    def check_money_added_to_account(self):
        expected = atm_data["value"]
        res = self.add_money(expected)
        assert res == expected
        print("Adding money checked")
        return self

    def check_money_withdrawal(self):
        res = self.withdraw(atm_data["withdraw_value"], "1234")
        assert res == results["result"]
        print("Withdrawal money checked")
        return self

    def check_pin(self):
        pin_length = self.get_pin_length()
        assert pin_length == results["pin_length"]
        print("Pin length checked")
        return self