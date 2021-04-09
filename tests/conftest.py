import pytest
from home_work.atm import Account

@pytest.fixture
def create_acc():
    acc = Account()
    assert isinstance(acc, Account) == 1
    return acc

@pytest.fixture
def check_acc():
    acc = Account()
    assert isinstance(acc, Account) == 1
