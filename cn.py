import hashlib
class Blockchain:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash= previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256 (self.block_data.encode()).hexdigest()

t1 = "Lenevo"
t2 = "Samsung"

block1 = Blockchain('firstblock', [t1, t2])

print (f"Block 1 data: {block1.block_data}")
print (f"Block 1 hash: {block1.block_hash}")