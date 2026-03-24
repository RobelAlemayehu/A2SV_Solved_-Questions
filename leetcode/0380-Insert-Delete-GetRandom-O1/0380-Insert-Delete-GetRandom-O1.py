class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.value = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False

        self.dic[val] = len(self.value)
        self.value.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        
        index = self.dic[val]
        last_element = self.value[-1]

        self.value[index] = last_element
        self.dic[last_element] = index

        self.value.pop()
        del self.dic[val]

        return True

    def getRandom(self) -> int:

        return choice(self.value)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()