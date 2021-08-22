
import pytest
from  wallet import Wallet, InsuficientAmount

def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(100)
    assert wallet.balance == 110

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spen_cash(20)
    assert wallet.balance == 0

def test_wallet_spend_cash_raises_exception_on_insuficient_amount():
    wallet = Wallet()
    with pytest.raises(InsuficientAmount):
        wallet.spend_cash(100)