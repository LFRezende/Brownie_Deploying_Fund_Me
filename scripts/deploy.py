from brownie import FundMe, network, config, MockV3Aggregator
from web3 import Web3  # For Web3.toWei(x) --> add 18 decimals places.
from scripts.utils import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()
    if (
        network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS
    ):  ### CUIDADÍSSIMO!! --> NETWORK.SHOW_ACTIVE() != NETWORK.SHOW_ACTIVE !!!
        print(f">>>>>>{network.show_active()}<<<<<<<")
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    # Another way: publish_source=config["networks"][network.show_active()]["verify"]
    # ^^ Useful in case you forget to add a verify path in your .yaml.
    print(f"DEPLOYED!\n Address to Contract: {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()

