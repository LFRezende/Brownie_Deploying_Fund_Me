from brownie import accounts, network, MockV3Aggregator, config
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ['mainnet-fork-dev'] # Mainnet-fork-dev is a custom development network added to brownie.
DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local2", "ganache-local3"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        account = accounts[0]
    else:
        account = accounts.add(config["wallets"]["from_key"])
    return account


def deploy_mocks():
    if len(MockV3Aggregator) <= 0:  # List of Interface MockV3Aggregator
        account = get_account()
        print(f"The active network is {network.show_active()}.")
        print("Deploying Mocks...")
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": account})
        print("Mocks Deployed!")
