import pytest
from data import atm_data
from dsl.atm_check_methods import Atm


@pytest.mark.sanity
def test_atm_flow():
    test = (Atm().check_account_is_created().
            check_money_added_to_account().
            check_money_withdrawal().
            check_pin())


@pytest.mark.regression
@pytest.mark.parametrize("add_value, withdraw_value, exp_result", [atm_data["pack1"],atm_data["pack2"],atm_data["pack3"]])
def test_atm_withdraw(account, add_value, withdraw_value, exp_result):
    account.add_money(add_value)
    assert account.withdraw(withdraw_value, "1234") == exp_result


@pytest.mark.contribution
def test_verify_contribution_amounts_are_correct():
    test = (Atm().
            verify_contribution_amounts_are_correct()
    )