import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:

    def __init__(self):
        self.total_bill = 0
        self.chain = []
        self.create_block(nonce = 1, previous_hash = '0')