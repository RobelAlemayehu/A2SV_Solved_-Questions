class MyCircularDeque:

    def __init__(self, k: int):
        
        self.buffer = [0] * k
        self.front_index = 0
        self.current_size = 0
        self.max_capacity = k

    def insertFront(self, value: int) -> bool:
       
        if self.isFull():
            return False
      
        if not self.isEmpty():
            self.front_index = (self.front_index - 1 + self.max_capacity) % self.max_capacity
      
        self.buffer[self.front_index] = value
        self.current_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        
        if self.isFull():
            return False
      
        rear_index = (self.front_index + self.current_size) % self.max_capacity
        self.buffer[rear_index] = value
        self.current_size += 1
        return True

    def deleteFront(self) -> bool:
        
        if self.isEmpty():
            return False
      
        self.front_index = (self.front_index + 1) % self.max_capacity
        self.current_size -= 1
        return True

    def deleteLast(self) -> bool:
       
        if self.isEmpty():
            return False
      
        self.current_size -= 1
        return True

    def getFront(self) -> int:
   
        if self.isEmpty():
            return -1
      
        return self.buffer[self.front_index]

    def getRear(self) -> int:
     
        if self.isEmpty():
            return -1
      
        rear_index = (self.front_index + self.current_size - 1) % self.max_capacity
        return self.buffer[rear_index]

    def isEmpty(self) -> bool:
     
        return self.current_size == 0

    def isFull(self) -> bool:
        
        return self.current_size == self.max_capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()