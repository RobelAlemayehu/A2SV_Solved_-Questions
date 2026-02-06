class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq_char = {}

        for ch in chars:
            freq_char[ch] = freq_char.get(ch, 0) + 1

        
        total_length = 0

        for word in words:

            word_count = {}
            can_form = True

            for ch in word:
                word_count[ch] = word_count.get(ch, 0) + 1


                if ch not in freq_char or word_count[ch] > freq_char[ch]:
                    can_form = False

                    break
            
            if can_form:
                total_length += len(word)


        return total_length