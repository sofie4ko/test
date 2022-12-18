# Import the necessary libraries
from web3 import Web3
import json

# Set the provider for the JSON RPC API
w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

# Set the address of the contract and the ABI (Application Binary Interface)
contract_address = "0x1234567890123456789012345678901234567890"
abi = json.loads('[ABI of the contract goes here]')

# Create the contract object
contract = w3.eth.contract(address=contract_address, abi=abi)

# Set the address of the account that will receive the tokens and the amount to be claimed
to_address = "0x9876543210987654321098765432109876543210"
amount = 1000

# Unlock the account if necessary
w3.personal.unlockAccount(to_address, "password")

# Call the "transfer" function of the contract to claim the tokens
tx_hash = contract.functions.transfer(to_address, amount).transact()

# Wait for the transaction to be mined
w3.eth.waitForTransactionReceipt(tx_hash)

print("Tokens claimed successfully")
