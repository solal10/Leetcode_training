import random

class RandomizedSet(object):

    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val):
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        if val not in self.val_to_index:
            return False
        last_element = self.values[-1]
        index = self.val_to_index[val]
        self.values[index] = last_element
        self.val_to_index[last_element] = index
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self):
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()