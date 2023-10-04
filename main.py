'''
brief explanation

AHCOIN (AHC)

transactions
t1: Darlene sends 1.2 AH to Reynold
t2: Reynold sends 3.1 AH to Mike
t3: William sends 0.3 AH to Darlene

B1 ("AAA", t1, t2, t3) -> 73jh76, B2 (73jh76, T4, T5, T6)
                           HASH

'''

import hashlib

class AHCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


#TRANSACTIONS 
t1 = "Darlene sends 1.2 AH to Reynold"
t2 = "Reynold sends 3.1 AH to Mike"
t3 = "William sends 0.3 AH to Darlene"
t4 = "Julian sends 4 AH to Vanessa"
t5 = "Vanessa sends 0.9 AH to Darlene"
t6 = "Bob sends 5 AH to Darlene"

initial_block = AHCoinBlock("Initial Text", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = AHCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = AHCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)