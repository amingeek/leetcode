import random

class RandomizedSet:

    def __init__(self):
        self.data = []
        self.indices = {}
        
    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.data.append(val)
        self.indices[val] = len(self.data) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        index_to_remove = self.indices[val]
        last_element = self.data[-1]
        
        self.data[index_to_remove] = last_element
        self.indices[last_element] = index_to_remove
        
        self.data.pop()
        del self.indices[val]

        return True
    
    def getRandom(self) -> int:
        return random.choice(self.data)