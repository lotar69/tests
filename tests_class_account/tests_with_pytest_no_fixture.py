from bank import Account

def test_deposit():
    account = Account(initial_balance=1000)
    account.deposit(amount=1000)
    assert account.balance == 2000

def test_withdraw():
    account = Account(initial_balance=1000)
    account.withdraw(amount=1000)
    assert account.balance == 0

r"""On lance les tests en tapant dans le terminal:

cd .\tests_class_account\ 

pytest tests_with_pytest_no_fixture.py -v
pytest tests_with_pytest_no_fixture.py -v --html==index.html
"""