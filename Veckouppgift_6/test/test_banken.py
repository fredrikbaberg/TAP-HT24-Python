from Veckouppgift_6.src.banken import *

def test_banken__initial_balance():
    expected = 5.0
    account = Account(5.0)
    actual = account.balance
    assert expected == actual

def test_banken__no_initial_balance():
    expected = 0.0
    account = Account()
    actual = account.balance
    assert expected == actual

def test_banken__deposit():
    expected = 100.0
    account = Account()
    account.deposit(100)
    actual = account.balance
    assert expected == actual

def test_banken__withdraw_insufficient_balance():
    # Försök göra uttag när det finns för lite pengar på kontot.
    expected = None
    account = Account()
    actual = account.withdraw(50)
    assert expected == actual

def test_banken__withdraw_sufficient_balance():
    # Försök göra uttag när det finns tillräckligt med pengar på kontot
    expected = 10.0
    account = Account(20)
    account.withdraw(10)
    actual = account.balance
    assert expected == actual

def test_banken__apply_interest():
    account = Account()
    account.deposit(100)
    account.apply_interest(1.0)
    expected = 101
    actual = account.balance
    assert expected == actual

def test_banken__can_pay_bill():
    account = Account(10)
    actual = account.can_pay_bill(5)
    expected = True
    assert expected == actual

def test_banken__can_not_pay_bill():
    account = Account(5)
    actual = account.can_pay_bill(6)
    expected = False
    assert expected == actual
