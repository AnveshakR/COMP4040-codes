# Implement dynamic tables with open addressing using a linear probing function based on myhash() given in HashTable.ipynb in Week 9. 
# When the load factor is greater than 1/2, expand to a new table that doubles the size of the old.
# When the load factor is less than 1/4, contract to a new table that halves the size of the old. 
# Run the following experiments: generate a binary string using PRNG of length 100, where 1 represents insertion and 0 deletion.
# For each 1 in the binary string, generate a 3-digit key to insert using a PRNG and 
# for each 0 in the binary string, select at random a number in the table to delete. 
# Count the number of times of table expansion and table contraction. 
# Repeat the experiments for 20 times and compute the average number of times the table is expanded and the average number of times the table is contracted.

from random import choice, randint

def myhash(key):
    hash_value = 7 
    for i in range(len(key)):
        hash_value = hash_value * 31 + ord(key[i])
        return hash_value

class HashTable:
    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.array = [0] * self.capacity
        self.expansions = 0 # counter for expansions
        self.contractions = 0 # counter for contractions
    
    def place_item(self, key_val):
        i = 0
        placed = False
        while not placed:
            index = (myhash(key_val[0]) + i) % self.capacity
            
            if self.array[index] == key_val:
                placed == True
                
            elif self.array[index] == 0:
                self.array[index] = key_val
                self.size += 1
                placed = True
                
            i+=1
                
        if placed:
            self.resize()
    
    def remove_item(self, key):
        i = 0
        removed = False
        while not removed:
            
            index = (myhash(key) + i) % self.capacity
            
            if self.array[index] == 0:
                i += 1
            elif self.array[index][0] == key:
                self.array[index] = 0
                self.size -= 1
                removed = True
            
            i += 1
    
        if removed:
            self.resize()
    
    def resize(self):
        load_factor = self.size / self.capacity
        
        if load_factor >= 0.5: # expansion

            self.capacity *= 2
            new_array = [0] * self.capacity
            
            for item in self.array:
                if item != 0 and type(item) == tuple:
                    i = 0
                    key = item[0]
                    placed = False
                    while not placed:
                        index = (myhash(key) + i) % self.capacity 
                        if new_array[index] == 0:
                            new_array[index] = item
                            placed = True
                        i += 1
                            
            self.array = new_array
            self.expansions += 1

        if load_factor <= 0.25: # contraction

            self.capacity = int(self.capacity / 2) 
            new_array = [0] * self.capacity
            
            for item in self.array:
                if item != 0 and type(item) == tuple:
                    i = 0
                    key = item[0]
                    placed = False
                    while not placed:
                        index = (myhash(key) + i) % self.capacity 
                        if new_array[index] == 0:
                            new_array[index] = item
                            placed = True
                        i += 1
                            
            self.array = new_array
            self.contractions += 1


expansion_count = []
contraction_count = []

for j in range(20):

    binary = ""
    table = HashTable() # creating hashtable object
    keys = []

    for i in range(20):
        binary += str(choice([0,1])) # binary string generator

    print("number {}: ".format(j+1), binary)

    for digit in binary:

        if digit == '1':
            num = randint(100,999)
            keys.append(str(num))
            table.place_item((str(num), num))

        if digit == '0' and len(keys) > 0:
            key_val = choice(keys)
            keys.remove(key_val)
            table.remove_item(key_val)

    
    expansion_count.append(table.expansions)
    contraction_count.append(table.contractions)

    del table # discards object


print("average expansions = ", (sum(expansion_count)/len(expansion_count))) # prints avg expansions
print("average expansions = ", (sum(contraction_count)/len(contraction_count))) # prints avg contractions