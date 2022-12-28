from brownie import accounts, FundMe, network, exceptions
from scripts.utils import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
import pytest


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()  # Não coloque {"from account"} dentro da função
    entrance_Fee = fund_me.getEntranceFee()
    txf = fund_me.fund({"from": account, "value": entrance_Fee})
    txf.wait(1)
    assert fund_me.addresstoAmountFunded(account.address) == entrance_Fee
    txw = fund_me.withdraw({"from": account})
    txw.wait(1)
    assert (
        fund_me.addresstoAmountFunded(account.address) == 0
    )  # ERA O FUNDERS[]!!DECLARA ANTES!


def test_only_owner():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("U no ADM, U shall not pass.")
    account = get_account()
    fund_me = deploy_fund_me()
    bad_actor = accounts[1]
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})