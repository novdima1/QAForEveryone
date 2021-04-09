import pytest
from data import atm_data

@pytest.mark.usefixtures("check_acc")
def test_atm_add(create_acc):
    acc = create_acc
    expected = atm_data["value"]
    res = acc.add_money(expected)
    print(acc.check_balance())
    assert res == expected

@pytest.mark.parametrize("add_value, withdraw_value, result", [atm_data["pack1"],atm_data["pack2"],atm_data["pack3"]])
def test_atm_withdraw(create_acc,add_value,withdraw_value, result):
    acc = create_acc
    acc.add_money(add_value)
    res = acc.withdraw(withdraw_value, "1234")
    assert res == result

