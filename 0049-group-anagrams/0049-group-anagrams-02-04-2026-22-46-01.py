class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grouped_words = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in grouped_words:
                grouped_words[key] = []

            grouped_words[key].append(word)

        return list(grouped_words.values())

