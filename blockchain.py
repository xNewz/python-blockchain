import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:

    def __init__(self):
        self.total_bill = 0
        self.chain = []
        self.create_block(nonce = 1, previous_hash = '0')

    def create_block(self, nonce, previous_hash):
        block = {'index': len(self.chain) + 1,
        'total_bill': self.total_bill,
        'timestamp': str(datetime.datetime.now()),
        'nonce': nonce,
        'previous_hash': previous_hash,
        }
        self.chain.append(block) # นำไปต่อกับ block เดิมที่สร้างก่อนหน้า
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def nonce_of_work(self, previous_nonce):
        new_nonce = 1
        check_nonce = False

        while check_nonce is False:
            hash_operation = hashlib.sha256(str(new_nonce**2 - previous_nonce**1).encode()).hexdigest()
            #target
            if hash_operation[:4] == '0000':
                check_nonce = True
            else:
                new_nonce += 1
        return new_nonce

    def hash(self, block):
        encode_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encode_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_nonce = previous_block['nonce']
            nonce = block['nonce']
            hash_operation = hashlib.sha256(str(nonce**2 - previous_nonce**1).encode()).hexdigest()
            #target
            if hash_operation[:4] != '0000':
                return False

            previous_block = block
            block_index += 1
        return True