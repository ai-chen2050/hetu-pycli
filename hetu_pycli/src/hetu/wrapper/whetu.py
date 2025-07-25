# Whetu contract class generated from [ABI](contracts/WHETU.abi)
# Do not edit this file directly, it is generated from the ABI.

from web3 import Web3

class Whetu:
    def __init__(self, address, provider, abi):
        self.web3 = Web3(provider)
        self.contract = self.web3.eth.contract(address=address, abi=abi)

    def DOMAIN_SEPARATOR(self, ):
        """
        Call DOMAIN_SEPARATOR()
        :return: [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}]
        """
        return self.contract.functions.DOMAIN_SEPARATOR().call()

    def allowance(self, owner, spender):
        """
        Call allowance(owner, spender)
        :param owner: address (solidity name: 'owner')
        :param spender: address (solidity name: 'spender')
        :return: [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}]
        """
        return self.contract.functions.allowance(owner, spender).call()

    def approve(self, spender, value):
        """
        Call approve(spender, value)
        :param spender: address (solidity name: 'spender')
        :param value: uint256 (solidity name: 'value')
        :return: [{'internalType': 'bool', 'name': '', 'type': 'bool'}]
        """
        return self.contract.functions.approve(spender, value).call()

    def balanceOf(self, account):
        """
        Call balanceOf(account)
        :param account: address (solidity name: 'account')
        :return: [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}]
        """
        return self.contract.functions.balanceOf(account).call()

    def decimals(self, ):
        """
        Call decimals()
        :return: [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}]
        """
        return self.contract.functions.decimals().call()

    def deposit(self, ):
        """
        Call deposit()
        :return: []
        """
        return self.contract.functions.deposit().call()

    def eip712Domain(self, ):
        """
        Call eip712Domain()
        :return: [{'internalType': 'bytes1', 'name': 'fields', 'type': 'bytes1'}, {'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'string', 'name': 'version', 'type': 'string'}, {'internalType': 'uint256', 'name': 'chainId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'verifyingContract', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}, {'internalType': 'uint256[]', 'name': 'extensions', 'type': 'uint256[]'}]
        """
        return self.contract.functions.eip712Domain().call()

    def name(self, ):
        """
        Call name()
        :return: [{'internalType': 'string', 'name': '', 'type': 'string'}]
        """
        return self.contract.functions.name().call()

    def nonces(self, owner):
        """
        Call nonces(owner)
        :param owner: address (solidity name: 'owner')
        :return: [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}]
        """
        return self.contract.functions.nonces(owner).call()

    def permit(self, owner, spender, value, deadline, v, r, s):
        """
        Call permit(owner, spender, value, deadline, v, r, s)
        :param owner: address (solidity name: 'owner')
        :param spender: address (solidity name: 'spender')
        :param value: uint256 (solidity name: 'value')
        :param deadline: uint256 (solidity name: 'deadline')
        :param v: uint8 (solidity name: 'v')
        :param r: bytes32 (solidity name: 'r')
        :param s: bytes32 (solidity name: 's')
        :return: []
        """
        return self.contract.functions.permit(owner, spender, value, deadline, v, r, s).call()

    def symbol(self, ):
        """
        Call symbol()
        :return: [{'internalType': 'string', 'name': '', 'type': 'string'}]
        """
        return self.contract.functions.symbol().call()

    def totalETH(self, ):
        """
        Call totalETH()
        :return: [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}]
        """
        return self.contract.functions.totalETH().call()

    def totalSupply(self, ):
        """
        Call totalSupply()
        :return: [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}]
        """
        return self.contract.functions.totalSupply().call()

    def transfer(self, to, value):
        """
        Call transfer(to, value)
        :param to: address (solidity name: 'to')
        :param value: uint256 (solidity name: 'value')
        :return: [{'internalType': 'bool', 'name': '', 'type': 'bool'}]
        """
        return self.contract.functions.transfer(to, value).call()

    def transferFrom(self, from_, to, value):
        """
        Call transferFrom(from_, to, value)
        :param from_: address (solidity name: 'from')
        :param to: address (solidity name: 'to')
        :param value: uint256 (solidity name: 'value')
        :return: [{'internalType': 'bool', 'name': '', 'type': 'bool'}]
        """
        return self.contract.functions.transferFrom(from_, to, value).call()

    def withdraw(self, amount):
        """
        Call withdraw(amount)
        :param amount: uint256 (solidity name: 'amount')
        :return: []
        """
        return self.contract.functions.withdraw(amount).call()