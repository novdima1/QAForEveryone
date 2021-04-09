import pytest


@pytest.mark.usefixtures("check_acc")
def test_atm_add(create_acc):
    acc = create_acc
    expected = 1000
    res = acc.add_money(expected)
    print(acc.check_balance())
    assert res == expected


@pytest.mark.parametrize("add_value, withdraw_value, result", [(1000,500,500),(2000,600,1400),(3000,-500,None)])
def test_atm_withdraw(create_acc,add_value,withdraw_value, result):
    acc = create_acc
    acc.add_money(add_value)
    res = acc.withdraw(withdraw_value, "1234")
    assert res == result

