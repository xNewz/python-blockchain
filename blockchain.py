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