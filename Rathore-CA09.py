import random

def myhash(key): 
    hash_value = 7; 
    for i in range(len(key)):
        hash_value = hash_value * 31 + ord(key[i]) 
        return hash_value
    
# linear probe function
def linear_probe(key, i):
    return myhash(key) + i


# Quadratic probe function
def quadratic_probe(key, i):
    return myhash(key) +  2 * (i**2) + 3 * i


class Hashtable:
    def __init__(self, elements, mode):
        self.m = 128
        self.array = [0] * self.m
        self.mode = mode # selecting quadratic or linear probe mode
        self.probes = 0 # saves the number of probes.
        self.place_element(elements)

        
    def hash(self, key, i):
        if self.mode == "linear":
            return linear_probe(key, i)
        elif self.mode == "quadratic":
            return quadratic_probe(key, i)
        else:
            raise Exception("Choose an available mode.")
    
    
    def place_element(self, elements):
        for key, value in elements:
            i = 0
            while True:
                index = self.hash(key, i) % self.m
                if self.array[index] == 0:
                    self.array[index] = (key, value)
                    self.probes += i
                    break
                i+=1
    def get_value(self, key):
        i=0
        while True:
            index = self.hash(key, i) % self.m
            val = self.array[index]
            if key != val[0]:
                i+=1
            else:
                return val[1], i
                break
            
                
    def get_probes(self):
        return self.probes
    
    def __str__(self):
        return print(self.array)

linear_probing_times = []
quadratic_probing_times = []

for k in range(100):
    test_array = [(x:=random.randint(1000, 10_000), str(x)) for i in range(128)]
    test_array = [(y, x) for x,y in test_array]

    linearHashTable = Hashtable(test_array, "linear")
  
    quadraticHashTable = Hashtable(test_array, "quadratic")
  
    linear_probing_times.append(linearHashTable.get_probes())
    quadratic_probing_times.append(quadraticHashTable.get_probes())
    

print("Linear probing average: ", (sum(linear_probing_times) / 100))
print("Quadratic probing average: ", (sum(quadratic_probing_times) / 100))
print()
print("Linear probing average for each element: ", (sum(linear_probing_times) / 12800))
print("Quadratic probing average for each element:", (sum(quadratic_probing_times) / 12800))
    

# conclusion

# quadratic probing is more than 4 times quicker than linear probing
# but finding a quadratic function that can be fitted on all the element of a hash table is difficult