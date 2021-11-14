from bank import Account
import pytest


@pytest.fixture
def account():
    return Account(initial_balance=1000)

def test_deposit(account):
    account.deposit(amount=1000)
    assert account.balance == 2000

def test_withdraw(account):
    account.withdraw(amount=1000)
    assert account.balance == 0

r"""On lance les tests en tapant dans le terminal:

cd .\tests_class_account\ 

pytest tests_with_pytest_with_fixture.py -v
pytest tests_with_pytest_with_fixture.py -v --html==index.html
"""