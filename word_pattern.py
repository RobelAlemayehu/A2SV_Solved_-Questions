class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        word_map = {}
        cha_map = {}

        for ch, word in zip(pattern, words):
            if ch in cha_map and cha_map[ch] != word:
                return False
            
            if word in word_map and word_map[word] != ch:
                return False


            cha_map[ch] = word
            word_map[word] = ch

        return True