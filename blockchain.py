# shabbydebopbopdeshibbydayohyeah

import hashlib
import json
from time import time
from textwrap import dedent
from uuid import uuid4
from flask import Flask

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
        # 1. Get the block object as a utf-8 string
        block_json_string = json.dumps(block, sort_keys=True).encode()
        
        # 2. Hash the block object using sha256
        return hashlib.sha256(block_json_string).hexdigest()
    
    @property
    def last_block(self):
        # 1. Return the last block in the chain
        return self.chain[-1]

    # **** PROOF OF WORK ALGORITHM **** #

    def proof_of_work(self, last_proof):
        # 1. Initialise proof
        proof = 0
        
        # 2. Loop until proof a valid proof is found
        while self.validate_proof(last_proof, proof) is False:
            # 2-a. Increment proof each loop until the number satisfies the validation criteria defined in validate_proof
            proof += 1
        
        return proof
    
    @staticmethod
    def validate_proof(last_proof, proof):
        # 1. Encode the 2 proofs together in a utf-8 string
        guess = f'{last_proof}{proof}'.encode()
         
        #2. Hash the two proofs
        guess_hash = hashlib.sha256(guess).hexdigest()

        #3. Check to see if they satisfy the validation criteria and return boolean based on the outcome
        return guess_hash[:4] == "0000"


# ~~ FLASK STUFF ~~ #

#Initialise app
app = Flask(__name__)

node_id = str(uuid4()).replace('-', '')

blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    return "Mine a new block..."

@app.route('/transactions/new', methods=['POST'])
def new_transactions():
    return "Time to transact yo!.."

@app.route('/chain', methods=['GET'])
def full_chain():
    res = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(res), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
