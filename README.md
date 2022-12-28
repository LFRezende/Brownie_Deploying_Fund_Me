# Brownie Deploying Fund Me

- Disclaimer

This project was made while following the excellent Smart Contract Development Course in Python of Freebootcamp, made by Patrick Collins.
Although I have coded 100% of this, it is needed to credit his tutoring for designing this project through the course.
Here is the course I have been following through: https://www.youtube.com/watch?v=M576WGiDBdQ

# Summary 

The whole goal of this project is to effectively deploy a "Fund-Me" smart contract into any desired chain (whether development, local persistent or active blockchain) using remote method - this has been done using the python development framework Brownie.

# Fund Me 

A "Fund-Me" smart contract is a piece of code in the blockchain whose purpose is to:

- Accept donnations from different funders, who own cryptocurrencies in their respective EVM compatible wallets (such as Meta Mask, Jaxx Liberty etc.)
- Allow a single entity (the deployer of the contract) to withdraw these funds at any given time.
