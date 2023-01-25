from WalletClass import Wallet
from WalletClass import Character
import pytest

def test_deposit_increases_balance_when_zero():
    # given
    test_wallet = Wallet('test wallet')
    amount = 100
    currency = 'GBP'
    # when
    test_wallet.deposit(amount,currency)
    # then
    assert test_wallet.balance.get(currency) == amount, "unexpected balance"

def test_deposit_increases_balance_with_existing_amount():
    # given
    test_wallet = Wallet('test wallet')
    amount = 100
    currency = 'GBP'
    test_wallet.deposit(amount, currency)
    # when
    amount2 = 35
    test_wallet.deposit(amount2,currency)
    # then
    assert test_wallet.balance.get(currency) == amount + amount2


def test_spend_decreases_balance():
    # given
    test_wallet = Wallet('test wallet')
    amount = 100
    currency = 'GBP'
    test_wallet.deposit(amount, currency)
    # when
    amount2 = 50
    test_wallet.spend(amount2, currency)
    # then
    assert test_wallet.show_balance(currency) == amount - amount2

def test_spend_more_than_we_have_raises_exception():
    # given
    test_wallet = Wallet('test wallet')
    amount = 100
    currency = 'GBP'
    # when, then
    with pytest.raises(ValueError,match='Not Enough Money') as err:
        test_wallet.spend(amount, currency)

# character tests - interactions passing money

def test_passing_money_between_characters():
    # given
    test_character1 = Character('szoboszlai',21)
    test_character2 = Character('dzsudzsak', 35)
    test_character1.wallet.deposit(150,'GBP')
    # when
    amount = 100
    currency = 'GBP'
    test_character1.give_money(test_character2,amount,currency)
    # then
    assert test_character2.wallet.show_balance(currency) == amount



