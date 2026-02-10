class FrequencyTracker:

    def __init__(self):
        self.number_counts = {}
        self.freq = {}

    def add(self, number: int) -> None:
        old_freq = self.number_counts.get(number, 0)

        if old_freq in self.freq and self.freq[old_freq] > 0:
            self.freq[old_freq] -= 1

        new_freq = old_freq + 1
        self.number_counts[number] = new_freq

        self.freq[new_freq] = self.freq.get(new_freq, 0) + 1

    def deleteOne(self, number: int) -> None:
        if self.number_counts.get(number, 0) <= 0:
            return
            
        old_freq = self.number_counts[number]
        
        self.freq[old_freq] -= 1
        
        new_freq = old_freq - 1
        self.number_counts[number] = new_freq
        
        if new_freq > 0:
            self.freq[new_freq] = self.freq.get(new_freq, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq.get(frequency, 0) > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)