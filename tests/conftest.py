import pytest
from home_work.atm import Account

@pytest.fixture
def account():
    acc = Account()
    assert isinstance(acc, Account) == 1
    return acc

