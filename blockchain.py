class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.current_transactions = []
    def create_block(self):
        # 1. Create a new block
        # 2. Add block to the chain
        pass
    def create_transaction(self):
        # 1. Create a new transaction
        # 2. Add transaction to transaction list
        pass
    
    @staticmethod
    def generate_hash(block):
        #Hash a block
        pass
    
    @property
    def last_block(self):
        # Return the last block in the chain
        pass