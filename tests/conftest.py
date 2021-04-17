import pytest
from home_work.atm import Account

@pytest.fixture
def account():
    acc = Account()
    assert isinstance(acc, Account) == 1
    print("\nInitiation fixture checked")
    return acc

