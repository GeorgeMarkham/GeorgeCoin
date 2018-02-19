import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.current_transactions = []

    def create_block(self, proof, prev_hash=None):
        # 1. Create a new block
        new_block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof' proof,
            'previous_hash': prev_hash or self.generate_hash(self.chain[-1])
        }

        # 2. Set the current transactions to be empty as they've been added to a block and therefore dealt with
        self.current_transactions = []

        # 3. Add block to the chain
        self.chain.append(new_block)

        # Return the newly created block
        return new_block

    def create_transaction(self, sender, recipient, amount):
        # 1. Create a new transaction
        new_transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }

        # 2. Add transaction to transaction list
        self.current_transactions.append(new_transaction)

        # 3. Return the index of the block containing the transaction
        return self.last_block['index'] + 1
    
    @staticmethod
    def generate_hash(block):
        #Hash a block
        pass
    
    @property
    def last_block(self):
        # Return the last block in the chain
        pass

